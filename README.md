# China Real-World Search

A real ChatGPT/Codex **Plugin** for researching mainland-China real-world questions through the systems that actually generate and operate the relevant facts.

This repository is no longer packaged as a loose root-level Skill. It follows the OpenAI Plugin layout with a required `.codex-plugin/plugin.json`, a bundled Agent Skill, and a repo marketplace for local installation and testing.

## What it does

China Real-World Search helps the assistant avoid the common failure mode of treating open-Web search as the whole Chinese internet. It routes each important claim toward the system that naturally generates it, then verifies current execution when needed.

Typical use cases include:

- government services, eligibility, materials, fees, and local execution paths;
- transport schedules, availability, disruptions, and route planning;
- hospitals, appointments, local businesses, and current operating status;
- WeChat/Alipay mini programs, public accounts, local apps, and platform-native service entry points;
- companies, projects, policies, filings, and lifecycle-state verification;
- historical pages, migrated records, conflicting claims, and fact checking.

## Plugin structure

```text
.
├── .agents/plugins/marketplace.json
├── plugins/
│   └── china-real-world-search/
│       ├── .codex-plugin/plugin.json
│       ├── assets/
│       └── skills/
│           └── china-real-world-search/
│               ├── SKILL.md
│               └── references/
├── scripts/validate_plugin.py
├── PUBLISHING.md
├── PRIVACY.md
├── TERMS.md
└── LICENSE
```

## Install as a personal/repo Plugin

The repository includes an OpenAI marketplace manifest. Add the Git-backed marketplace from Codex:

```bash
codex plugin marketplace add hugeJan/china-real-world-search --ref main
```

Then use the ChatGPT desktop app:

1. Open ChatGPT and switch to **Work**, or open **Codex**.
2. Open **Plugins**.
3. Select the **hugeJan Plugins** marketplace/source.
4. Open **China Real-World Search** and install it.
5. Start a fresh conversation and invoke `@China Real-World Search` when you want to force the workflow.

Local/repo marketplaces are an authoring and testing path. Public distribution uses the universal Plugin Directory after OpenAI review.

## Validate the package

```bash
python3 scripts/validate_plugin.py
```

The same validator runs in GitHub Actions on pushes and pull requests.

## Publish to the universal ChatGPT/Codex Plugin Directory

This is a **skills-only Plugin**; it does not need an MCP server merely to qualify as a Plugin. Public submission is done through the OpenAI Platform plugin submission portal.

See [`PUBLISHING.md`](PUBLISHING.md) for the exact submission checklist, listing copy, and the required five positive plus three negative review tests.

## Design principle

> Find the system that naturally generates the fact → retrieve the closest available original record → verify what it proves → add an independent execution/reality check when needed.

Open Web is a discovery layer, not a complete model of the mainland-China information environment.
