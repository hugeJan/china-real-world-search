#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "china-real-world-search"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
SKILLS_DIR = PLUGIN / "skills"
PUBLISHING = ROOT / "PUBLISHING.md"
CHANGELOG = ROOT / "CHANGELOG.md"

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return None


def resolve_plugin_path(value: str, field: str) -> Path | None:
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


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing file: {path.relative_to(ROOT)}")
        return None


manifest = load_json(MANIFEST)
marketplace = load_json(MARKETPLACE)

if manifest:
    for field in ("name", "version", "description"):
        if not manifest.get(field):
            fail(f"manifest missing required field: {field}")

    name = manifest.get("name", "")
    version = manifest.get("version", "")

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("manifest name must be kebab-case")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
        fail("manifest version must be semantic-version shaped")

    plugin_manifest_dir = PLUGIN / ".codex-plugin"
    extras = [p.name for p in plugin_manifest_dir.iterdir() if p.name != "plugin.json"] if plugin_manifest_dir.exists() else []
    if extras:
        fail(f".codex-plugin may only contain plugin.json; found: {', '.join(extras)}")

    skills_path = resolve_plugin_path(manifest.get("skills", ""), "skills")
    if skills_path and not skills_path.is_dir():
        fail("manifest skills path does not exist")

    interface = manifest.get("interface", {})
    prompts = interface.get("defaultPrompt", [])
    if isinstance(prompts, str):
        prompts = [prompts]
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

    publishing_text = read_text(PUBLISHING)
    if publishing_text is not None:
        match = re.search(r"Current plugin version:\s*\*\*(\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?)\*\*", publishing_text)
        if not match:
            fail("PUBLISHING.md missing parseable Current plugin version")
        elif match.group(1) != version:
            fail(f"version mismatch: manifest={version}, PUBLISHING={match.group(1)}")

    changelog_text = read_text(CHANGELOG)
    if changelog_text is not None:
        match = re.search(r"(?m)^##\s+(\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?)\b", changelog_text)
        if not match:
            fail("CHANGELOG.md missing a version heading")
        elif match.group(1) != version:
            fail(f"version mismatch: manifest={version}, CHANGELOG={match.group(1)}")

if SKILLS_DIR.exists():
    skill_dirs = [p for p in SKILLS_DIR.iterdir() if p.is_dir()]
    if not skill_dirs:
        fail("plugin has no bundled skills")
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            fail(f"missing {skill_file.relative_to(ROOT)}")
            continue
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"{skill_file.relative_to(ROOT)} has no YAML frontmatter")
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            fail(f"{skill_file.relative_to(ROOT)} has malformed frontmatter")
            continue
        frontmatter = parts[1]
        match = re.search(r"(?m)^name:\s*([^\n]+)$", frontmatter)
        if not match:
            fail(f"{skill_file.relative_to(ROOT)} frontmatter missing name")
        elif match.group(1).strip() != skill_dir.name:
            fail(f"skill folder/name mismatch: {skill_dir.name} != {match.group(1).strip()}")
        if not re.search(r"(?m)^description:\s*\S", frontmatter):
            fail(f"{skill_file.relative_to(ROOT)} frontmatter missing description")

        for link in re.findall(r"\]\((references/[^)]+)\)", text):
            if not (skill_dir / link).is_file():
                fail(f"broken SKILL.md reference: {link}")
else:
    fail("missing skills directory")

if marketplace:
    if not isinstance(marketplace.get("plugins"), list) or not marketplace["plugins"]:
        fail("marketplace.plugins must contain at least one entry")
    else:
        matches = [p for p in marketplace["plugins"] if p.get("name") == "china-real-world-search"]
        if len(matches) != 1:
            fail("marketplace must contain exactly one china-real-world-search entry")
        else:
            entry = matches[0]
            source = entry.get("source", {})
            if source.get("source") != "local":
                fail("repo marketplace source must be local")
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
            if policy.get("installation") not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
                fail("invalid marketplace policy.installation")
            if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                fail("invalid marketplace policy.authentication")
            if not entry.get("category"):
                fail("marketplace entry missing category")

for release_file in ("LICENSE", "PRIVACY.md", "TERMS.md", "PUBLISHING.md", "CHANGELOG.md"):
    if not (ROOT / release_file).is_file():
        fail(f"missing release file: {release_file}")

if errors:
    print("Plugin validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

print("Plugin validation passed")
print(f" - manifest: {MANIFEST.relative_to(ROOT)}")
print(f" - marketplace: {MARKETPLACE.relative_to(ROOT)}")
print(f" - bundled skill: {SKILLS_DIR / 'china-real-world-search' / 'SKILL.md'}")
if manifest:
    print(f" - release version: {manifest.get('version')}")
