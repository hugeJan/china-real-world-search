# Skill Regression Evals

This directory contains provider-neutral regression fixtures for China Real-World Search.

The project remains a **skills-only Plugin**. These eval files are development/release tooling; they do not add a runtime service, MCP server, API dependency, or model-provider dependency to the Plugin.

## Files

- `skill-regressions.json` — prompts plus `must` / `must_not` invariant IDs.
- `rubrics.json` — the canonical meaning and judging rule for every invariant ID.
- `../scripts/build_eval_packets.py` — converts the fixtures and rubrics into JSONL packets that any agent/eval harness can consume.

## Evaluation semantics

Each case has two sets of invariants:

- `must`: every listed behavior must be satisfied.
- `must_not`: every listed prohibited behavior must be absent.

Rubrics have a `scope`:

- `response` — can normally be judged from the assistant's final answer.
- `trace` — requires tool/action/routing trace evidence.
- `response_or_trace` — either surface may establish the behavior.

A judge should return `pass`, `fail`, or `indeterminate` for each invariant. Use `indeterminate` when the required evidence surface is unavailable; do **not** silently convert missing trace evidence into a pass.

For a release-level case to pass:

1. every `must` invariant must be `pass`;
2. every `must_not` invariant must be judged absent/pass;
3. no required invariant may remain `indeterminate` unless the release process explicitly treats that case as manual-only and records the manual result.

## Validate the eval definitions

The repository validator checks the fixture schema, required categories, rubric schema, and that every invariant referenced by a case exists in `rubrics.json`:

```bash
python3 scripts/validate_plugin.py
```

You can also check/build eval packets without invoking any model API:

```bash
python3 scripts/build_eval_packets.py --check
python3 scripts/build_eval_packets.py > /tmp/china-real-world-search-evals.jsonl
```

## Using an external target runner

Run each packet's `target_prompt` against a fresh conversation with the Plugin installed. Capture:

- the assistant final response;
- tool/routing/action trace when the host exposes it.

Store target outputs as JSON or JSONL, one object per case:

```json
{"id":"capability-no-wechat-access","response":"...","trace":"optional host trace"}
```

Then attach the captured outputs to the judge packets:

```bash
python3 scripts/build_eval_packets.py \
  --responses path/to/responses.jsonl \
  > /tmp/china-real-world-search-judge-packets.jsonl
```

Each generated object contains a `judge_prompt` with the case-specific positive and prohibited criteria. Send that prompt to whichever LLM-as-a-judge or evaluation framework you already use.

The repository intentionally does **not** hard-code OpenAI Evals, promptfoo, or another provider/runtime. This keeps the eval source of truth portable and avoids requiring API keys or third-party packages merely to validate the Plugin repository.

## Recommended judge output

Use a structured result such as:

```json
{
  "id": "capability-no-wechat-access",
  "verdict": "pass",
  "checks": [
    {
      "invariant": "state_in_app_state_not_directly_inspected",
      "result": "pass",
      "reason": "The answer explicitly says the live WeChat screen was not inspected."
    }
  ]
}
```

A case-level `pass` requires all required behaviors and no prohibited behaviors. Keep the reason short and tied to observable response/trace evidence.

## Adding a regression

When adding a new case:

1. choose one of the existing categories unless a genuinely new behavior class is needed;
2. reuse an existing invariant when its meaning already matches;
3. if a new invariant is necessary, add it to `rubrics.json` with an observable judge criterion and scope;
4. avoid rubric names that encode one exact wording — judge behavior, not phrasing;
5. run both validation commands before opening a release PR.
