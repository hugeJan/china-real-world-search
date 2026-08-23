#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "evals" / "skill-regressions.json"
RUBRICS_PATH = ROOT / "evals" / "rubrics.json"

VALID_SCOPES = {"response", "trace", "response_or_trace"}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_definitions(cases: Any, rubrics: Any) -> None:
    errors: list[str] = []

    if not isinstance(cases, list) or not cases:
        errors.append("skill-regressions.json must be a non-empty array")
        cases = []
    if not isinstance(rubrics, dict) or not rubrics:
        errors.append("rubrics.json must be a non-empty object")
        rubrics = {}

    seen_ids: set[str] = set()
    referenced: set[str] = set()

    for index, case in enumerate(cases):
        prefix = f"case #{index + 1}"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object")
            continue

        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{prefix} missing id")
        elif case_id in seen_ids:
            errors.append(f"duplicate case id: {case_id}")
        else:
            seen_ids.add(case_id)

        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"{prefix} missing prompt")

        for field in ("must", "must_not"):
            values = case.get(field)
            if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v for v in values):
                errors.append(f"{prefix} {field} must be a non-empty list of invariant IDs")
                continue
            referenced.update(values)

    for invariant_id, rubric in rubrics.items():
        if not isinstance(invariant_id, str) or not invariant_id:
            errors.append("rubric IDs must be non-empty strings")
            continue
        if not isinstance(rubric, dict):
            errors.append(f"rubric {invariant_id} must be an object")
            continue
        for field in ("description", "judge", "scope"):
            if not isinstance(rubric.get(field), str) or not rubric[field].strip():
                errors.append(f"rubric {invariant_id} missing/invalid {field}")
        if rubric.get("scope") not in VALID_SCOPES:
            errors.append(f"rubric {invariant_id} has invalid scope: {rubric.get('scope')!r}")

    missing = sorted(referenced - set(rubrics))
    if missing:
        errors.append("missing rubric definitions: " + ", ".join(missing))

    if errors:
        print("Eval definition validation failed:", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        raise SystemExit(1)


def load_responses(path: Path) -> dict[str, dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    stripped = text.lstrip()
    if not stripped:
        return {}

    if stripped.startswith("["):
        data = json.loads(text)
        if not isinstance(data, list):
            raise SystemExit("responses JSON must be an array")
        rows = data
    else:
        rows = []
        for line_no, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSONL at line {line_no}: {exc}")

    responses: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise SystemExit(f"response row #{index + 1} must be an object")
        case_id = row.get("id")
        response = row.get("response")
        if not isinstance(case_id, str) or not case_id:
            raise SystemExit(f"response row #{index + 1} missing id")
        if not isinstance(response, str):
            raise SystemExit(f"response row {case_id} missing string response")
        if case_id in responses:
            raise SystemExit(f"duplicate response id: {case_id}")
        responses[case_id] = row
    return responses


def criterion(invariant_id: str, rubrics: dict[str, Any], expectation: str) -> dict[str, str]:
    rubric = rubrics[invariant_id]
    return {
        "id": invariant_id,
        "expectation": expectation,
        "scope": rubric["scope"],
        "description": rubric["description"],
        "judge": rubric["judge"],
    }


def build_judge_prompt(packet: dict[str, Any]) -> str:
    response = packet.get("response")
    trace = packet.get("trace")

    lines = [
        "You are grading one China Real-World Search regression case.",
        "Judge observable behavior, not exact wording.",
        "For each required criterion, decide pass/fail/indeterminate.",
        "For each prohibited criterion, pass means the prohibited behavior is absent; fail means it is present.",
        "Use indeterminate when the rubric requires a trace/evidence surface that is not provided. Do not silently pass missing evidence.",
        "Return JSON with: id, verdict(pass|fail|indeterminate), checks[{invariant,result,reason}].",
        "A case verdict is pass only when every required criterion passes and every prohibited behavior is absent.",
        "",
        f"CASE ID: {packet['id']}",
        f"CATEGORY: {packet['category']}",
        "TARGET PROMPT:",
        packet["target_prompt"],
        "",
        "REQUIRED CRITERIA:",
    ]

    for item in packet["must"]:
        lines.append(
            f"- {item['id']} [scope={item['scope']}]: {item['description']} Judge rule: {item['judge']}"
        )

    lines.append("")
    lines.append("PROHIBITED CRITERIA:")
    for item in packet["must_not"]:
        lines.append(
            f"- {item['id']} [scope={item['scope']}]: {item['description']} Detection rule: {item['judge']}"
        )

    if response is not None:
        lines.extend(["", "ASSISTANT RESPONSE:", response])
    else:
        lines.extend(["", "ASSISTANT RESPONSE: <not supplied>"])

    if trace is not None:
        if isinstance(trace, str):
            trace_text = trace
        else:
            trace_text = json.dumps(trace, ensure_ascii=False)
        lines.extend(["", "HOST/TOOL TRACE:", trace_text])
    else:
        lines.extend(["", "HOST/TOOL TRACE: <not supplied>"])

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build provider-neutral target/judge packets from the Skill regression fixtures."
    )
    parser.add_argument(
        "--responses",
        type=Path,
        help="Optional JSON/JSONL file containing {id, response, trace?} target outputs.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write JSONL packets to this file instead of stdout.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate definitions (and response IDs when supplied) without emitting packets.",
    )
    args = parser.parse_args()

    cases = load_json(CASES_PATH)
    rubrics = load_json(RUBRICS_PATH)
    validate_definitions(cases, rubrics)

    responses: dict[str, dict[str, Any]] = {}
    if args.responses:
        responses = load_responses(args.responses)
        case_ids = {case["id"] for case in cases}
        unknown = sorted(set(responses) - case_ids)
        if unknown:
            raise SystemExit("responses contain unknown case IDs: " + ", ".join(unknown))

    if args.check:
        suffix = f", {len(responses)} responses" if responses else ""
        print(f"Eval definitions passed: {len(cases)} cases, {len(rubrics)} rubrics{suffix}")
        return

    packets: list[dict[str, Any]] = []
    for case in cases:
        packet: dict[str, Any] = {
            "id": case["id"],
            "category": case["category"],
            "target_prompt": case["prompt"],
            "must": [criterion(i, rubrics, "present") for i in case["must"]],
            "must_not": [criterion(i, rubrics, "absent") for i in case["must_not"]],
        }

        captured = responses.get(case["id"])
        if captured is not None:
            packet["response"] = captured["response"]
            if "trace" in captured:
                packet["trace"] = captured["trace"]

        packet["judge_prompt"] = build_judge_prompt(packet)
        packets.append(packet)

    output_text = "".join(json.dumps(packet, ensure_ascii=False) + "\n" for packet in packets)
    if args.output:
        args.output.write_text(output_text, encoding="utf-8")
    else:
        sys.stdout.write(output_text)


if __name__ == "__main__":
    main()
