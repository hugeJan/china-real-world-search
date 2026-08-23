#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "china-real-world-search"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
SKILLS_DIR = PLUGIN / "skills"
PUBLISHING = ROOT / "PUBLISHING.md"
CHANGELOG = ROOT / "CHANGELOG.md"
PRIVACY = ROOT / "PRIVACY.md"
GITIGNORE = ROOT / ".gitignore"
EVALS = ROOT / "evals" / "skill-regressions.json"
RUBRICS = ROOT / "evals" / "rubrics.json"
EVAL_README = ROOT / "evals" / "README.md"
EVAL_BUILDER = ROOT / "scripts" / "build_eval_packets.py"

SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)

MARKDOWN_SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "node_modules",
    "dist",
    "build",
}
VALID_RUBRIC_SCOPES = {"response", "trace", "response_or_trace"}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {rel(path)}")
    except UnicodeDecodeError as exc:
        fail(f"file is not valid UTF-8: {rel(path)}: {exc}")
    return None


def load_json(path: Path) -> Any | None:
    text = read_text(path)
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {rel(path)}: {exc}")
        return None


def is_semver(value: object) -> bool:
    return isinstance(value, str) and SEMVER_RE.fullmatch(value) is not None


def resolve_plugin_path(value: object, field: str) -> Path | None:
    if not isinstance(value, str) or not value.startswith("./"):
        fail(f"manifest {field} must be a ./-relative path")
        return None
    resolved = (PLUGIN / value[2:]).resolve()
    try:
        resolved.relative_to(PLUGIN.resolve())
    except ValueError:
        fail(f"manifest {field} escapes plugin root")
        return None
    return resolved


def parse_simple_frontmatter(text: str, path: Path) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        fail(f"{rel(path)} has no YAML frontmatter")
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{rel(path)} has malformed frontmatter")
        return None

    fields: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith((" ", "\t")):
            fail(f"{rel(path)} uses multiline/nested frontmatter unsupported by repo validator")
            return None
        if ":" not in raw_line:
            fail(f"{rel(path)} has malformed frontmatter line: {raw_line!r}")
            return None
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            fail(f"{rel(path)} has empty frontmatter field: {raw_line!r}")
            return None
        if key in fields:
            fail(f"{rel(path)} repeats frontmatter field: {key}")
            return None
        fields[key] = value
    return fields


def validate_markdown_links(root: Path) -> None:
    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    uri_scheme_re = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")

    for md in root.rglob("*.md"):
        try:
            parts = md.relative_to(root).parts
        except ValueError:
            parts = ()
        if any(part in MARKDOWN_SKIP_DIRS for part in parts[:-1]):
            continue

        text = read_text(md)
        if text is None:
            continue
        for target in link_re.findall(text):
            target = target.strip()
            if not target or target.startswith(("#", "//")) or uri_scheme_re.match(target):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (md.parent / path_part).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"markdown link escapes repository: {rel(md)} -> {target}")
                continue
            if not resolved.exists():
                fail(f"broken markdown link: {rel(md)} -> {target}")


manifest = load_json(MANIFEST)
marketplace = load_json(MARKETPLACE)

version = ""
if manifest is not None:
    if not isinstance(manifest, dict):
        fail("manifest must be a JSON object")
    else:
        for field in ("name", "version", "description"):
            value = manifest.get(field)
            if not isinstance(value, str) or not value.strip():
                fail(f"manifest missing/invalid required field: {field}")

        name = manifest.get("name", "")
        version = manifest.get("version", "")

        if isinstance(name, str) and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail("manifest name must be kebab-case")
        if not is_semver(version):
            fail("manifest version must be strict SemVer")

        plugin_manifest_dir = PLUGIN / ".codex-plugin"
        if plugin_manifest_dir.exists():
            extras = [p.name for p in plugin_manifest_dir.iterdir() if p.name != "plugin.json"]
            if extras:
                fail(f".codex-plugin may only contain plugin.json; found: {', '.join(sorted(extras))}")

        skills_path = resolve_plugin_path(manifest.get("skills", ""), "skills")
        if skills_path and not skills_path.is_dir():
            fail("manifest skills path does not exist")

        interface = manifest.get("interface", {})
        if not isinstance(interface, dict):
            fail("manifest interface must be an object")
            interface = {}

        prompts = interface.get("defaultPrompt", [])
        if isinstance(prompts, str):
            prompts = [prompts]
        if not isinstance(prompts, list) or any(not isinstance(p, str) for p in prompts):
            fail("interface.defaultPrompt must be a string or list of strings")
            prompts = []
        if len(prompts) > 3:
            fail("interface.defaultPrompt should contain at most 3 prompts")
        for prompt in prompts:
            if len(prompt) > 128:
                fail("interface.defaultPrompt entry exceeds 128 characters")

        for field in ("composerIcon", "logo"):
            if field in interface:
                path = resolve_plugin_path(interface[field], f"interface.{field}")
                if path and not path.is_file():
                    fail(f"interface.{field} points to a missing file")

        for field in ("homepage", "repository"):
            value = manifest.get(field)
            if value is not None and (not isinstance(value, str) or not value.startswith("https://")):
                fail(f"manifest {field} must be an https:// URL when present")

        publishing_text = read_text(PUBLISHING)
        if publishing_text is not None and version:
            match = re.search(r"Current plugin version:\s*\*\*(\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?)\*\*", publishing_text)
            if not match:
                fail("PUBLISHING.md missing parseable Current plugin version")
            elif match.group(1) != version:
                fail(f"version mismatch: manifest={version}, PUBLISHING={match.group(1)}")

        changelog_text = read_text(CHANGELOG)
        if changelog_text is not None and version:
            match = re.search(r"(?m)^##\s+(\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?)\b", changelog_text)
            if not match:
                fail("CHANGELOG.md missing a version heading")
            elif match.group(1) != version:
                fail(f"version mismatch: manifest={version}, CHANGELOG={match.group(1)}")

        privacy_text = read_text(PRIVACY)
        if privacy_text is not None and version:
            for old_version in re.findall(r"\bversion\s+(\d+\.\d+\.\d+)\b", privacy_text, flags=re.IGNORECASE):
                if old_version != version:
                    fail(f"PRIVACY.md contains stale explicit release version: {old_version} (current {version})")

if SKILLS_DIR.exists():
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        fail("plugin has no bundled skills")
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        text = read_text(skill_file)
        if text is None:
            continue
        fields = parse_simple_frontmatter(text, skill_file)
        if fields is None:
            continue

        name = fields.get("name")
        description = fields.get("description")
        compatibility = fields.get("compatibility")

        if name is None:
            fail(f"{rel(skill_file)} frontmatter missing name")
        elif name != skill_dir.name:
            fail(f"skill folder/name mismatch: {skill_dir.name} != {name}")
        elif len(name) > 64:
            fail(f"{rel(skill_file)} frontmatter name exceeds 64 characters")

        if not description:
            fail(f"{rel(skill_file)} frontmatter missing description")
        elif len(description) > 1024:
            fail(f"{rel(skill_file)} frontmatter description exceeds 1024 characters")

        if compatibility is not None and len(compatibility) > 500:
            fail(f"{rel(skill_file)} frontmatter compatibility exceeds 500 characters")
else:
    fail("missing skills directory")

# Check relative links across all repository Markdown, not only the Skill bundle.
validate_markdown_links(ROOT)

if marketplace is not None:
    if not isinstance(marketplace, dict):
        fail("marketplace must be a JSON object")
    else:
        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list) or not plugins:
            fail("marketplace.plugins must contain at least one entry")
        else:
            matches = [p for p in plugins if isinstance(p, dict) and p.get("name") == "china-real-world-search"]
            if len(matches) != 1:
                fail("marketplace must contain exactly one china-real-world-search entry")
            else:
                entry = matches[0]
                source = entry.get("source", {})
                if not isinstance(source, dict) or source.get("source") != "local":
                    fail("repo marketplace source must be local")
                else:
                    path = source.get("path")
                    if not isinstance(path, str) or not path.startswith("./"):
                        fail("marketplace source.path must be ./-relative")
                    else:
                        resolved = (ROOT / path[2:]).resolve()
                        try:
                            resolved.relative_to(ROOT.resolve())
                        except ValueError:
                            fail("marketplace source.path escapes repository root")
                        if not resolved.is_dir():
                            fail("marketplace source.path does not exist")

                policy = entry.get("policy", {})
                if not isinstance(policy, dict):
                    fail("marketplace policy must be an object")
                else:
                    if policy.get("installation") not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
                        fail("invalid marketplace policy.installation")
                    if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                        fail("invalid marketplace policy.authentication")
                if not entry.get("category"):
                    fail("marketplace entry missing category")

# Structured regression fixtures are schema-validated here. Behavior execution belongs
# to a host/agent eval harness or the manual release gate documented in PUBLISHING.md.
evals = load_json(EVALS)
rubrics = load_json(RUBRICS)
referenced_invariants: set[str] = set()

if evals is not None:
    if not isinstance(evals, list) or not evals:
        fail("evals/skill-regressions.json must be a non-empty JSON array")
    else:
        seen_ids: set[str] = set()
        categories: set[str] = set()
        for index, case in enumerate(evals):
            prefix = f"eval case #{index + 1}"
            if not isinstance(case, dict):
                fail(f"{prefix} must be an object")
                continue
            case_id = case.get("id")
            category = case.get("category")
            prompt = case.get("prompt")
            must = case.get("must")
            must_not = case.get("must_not")

            if not isinstance(case_id, str) or not case_id:
                fail(f"{prefix} missing id")
            elif case_id in seen_ids:
                fail(f"duplicate eval id: {case_id}")
            else:
                seen_ids.add(case_id)

            if not isinstance(category, str) or not category:
                fail(f"{prefix} missing category")
            else:
                categories.add(category)

            if not isinstance(prompt, str) or not prompt.strip():
                fail(f"{prefix} missing prompt")

            for field_name, values in (("must", must), ("must_not", must_not)):
                if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v for v in values):
                    fail(f"{prefix} {field_name} must be a non-empty list of strings")
                else:
                    referenced_invariants.update(values)

        required_categories = {"routing", "capability", "security", "action", "discovery", "verification"}
        missing = sorted(required_categories - categories)
        if missing:
            fail(f"eval fixtures missing required categories: {', '.join(missing)}")

if rubrics is not None:
    if not isinstance(rubrics, dict) or not rubrics:
        fail("evals/rubrics.json must be a non-empty JSON object")
    else:
        for rubric_id, rubric in rubrics.items():
            if not isinstance(rubric_id, str) or not rubric_id:
                fail("rubric IDs must be non-empty strings")
                continue
            if not isinstance(rubric, dict):
                fail(f"rubric {rubric_id} must be an object")
                continue
            for field in ("description", "judge", "scope"):
                value = rubric.get(field)
                if not isinstance(value, str) or not value.strip():
                    fail(f"rubric {rubric_id} missing/invalid {field}")
            scope = rubric.get("scope")
            if scope not in VALID_RUBRIC_SCOPES:
                fail(f"rubric {rubric_id} has invalid scope: {scope!r}")

        missing_rubrics = sorted(referenced_invariants - set(rubrics))
        if missing_rubrics:
            fail("eval fixtures reference undefined rubrics: " + ", ".join(missing_rubrics))

# Keep generated/local development artifacts out of the repository by default.
gitignore_text = read_text(GITIGNORE)
if gitignore_text is not None:
    ignored = {line.strip() for line in gitignore_text.splitlines() if line.strip() and not line.lstrip().startswith("#")}
    for required_pattern in {".DS_Store", "__pycache__/", "*.py[cod]", "*.zip"}:
        if required_pattern not in ignored:
            fail(f".gitignore missing expected development artifact pattern: {required_pattern}")

for release_file in (
    "LICENSE",
    "PRIVACY.md",
    "TERMS.md",
    "PUBLISHING.md",
    "CHANGELOG.md",
    "README.md",
    "evals/README.md",
    "evals/rubrics.json",
    "scripts/build_eval_packets.py",
):
    if not (ROOT / release_file).is_file():
        fail(f"missing release/support file: {release_file}")

if errors:
    print("Plugin validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print("Plugin validation passed")
print(f" - manifest: {rel(MANIFEST)}")
print(f" - marketplace: {rel(MARKETPLACE)}")
print(f" - bundled skill: {rel(SKILLS_DIR / 'china-real-world-search' / 'SKILL.md')}")
print(f" - markdown links: repository-wide")
print(f" - regression fixtures: {rel(EVALS)}")
print(f" - eval rubrics: {rel(RUBRICS)}")
if version:
    print(f" - release version: {version}")
