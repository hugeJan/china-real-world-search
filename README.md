# China Real-World Search

A ChatGPT/Codex **Plugin** for researching mainland-China real-world questions through the systems that actually generate and operate the relevant facts — while still discovering the channels people can actually use today.

This repository follows the OpenAI Plugin layout with `.codex-plugin/plugin.json`, a bundled Agent Skill, and a repo marketplace for personal/local installation and testing.

## What it does

China Real-World Search is designed around a common failure mode in China-local research: **the most authoritative source is often not the best place to discover the current executable channel**.

Version 1.1 therefore uses two complementary workflows:

### Practical/actionable questions

> **Discover current options broadly → verify each option narrowly → classify what it is → confirm current usability → recommend the best path.**

This allows the assistant to discover real third-party mini programs, platform-native services, current local-life channels, and recent user-practice signals without incorrectly calling them official.

### Investigation/fact-verification questions

> **Find the system that naturally generates the fact → retrieve the closest original record → verify what it proves → add independent evidence when needed.**

Typical use cases include:

- government services, eligibility, materials, fees, and local execution paths;
- WeChat/Alipay mini programs, public accounts, local apps, and third-party service channels;
- distinguishing `official`, `official-platform integrated`, `officially named`, and `compatible third-party`;
- transport schedules, availability, disruptions, and route planning;
- hospitals, appointments, local businesses, and current operating status;
- companies, projects, policies, filings, and lifecycle-state verification;
- historical pages, migrated/removed service entries, conflicting claims, and fact checking.

## Why v1.1 changed the search order

A weak source can be a strong **lead generator** while still being weak evidence for authority claims.

For example, a recent SEO article or community post may surface the mini program that actually works today. The plugin keeps that candidate, then separately verifies:

- who operates it;
- whether the relevant function works now;
- whether its output is compatible with the target business process;
- whether a competent authority actually names/recommends it;
- whether an older official channel is only historically documented rather than currently available.

This avoids both bad extremes:

- `Only trust official pages, therefore miss the real usable channel.`
- `The channel works, therefore it must be official.`

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
│                   ├── channel-verification.md
│                   ├── examples.md
│                   ├── query-playbook.md
│                   ├── source-routing.md
│                   └── verification-protocol.md
├── scripts/validate_plugin.py
├── CHANGELOG.md
├── PUBLISHING.md
├── PRIVACY.md
├── TERMS.md
└── LICENSE
```

## Install as a personal/repo Plugin

Add the Git-backed marketplace from Codex:

```bash
codex plugin marketplace add hugeJan/china-real-world-search --ref main
```

Then use the ChatGPT desktop app:

1. Open ChatGPT and switch to **Work**, or open **Codex**.
2. Open **Plugins**.
3. Select the **hugeJan Plugins** marketplace/source.
4. Open **China Real-World Search** and install/update it.
5. Start a fresh conversation and invoke `@China Real-World Search` when you want to force the workflow.

Local/repo marketplaces are an authoring/testing path; availability can differ across ChatGPT surfaces.

## Validate the package

```bash
python3 scripts/validate_plugin.py
```

The same validator is configured in GitHub Actions on pushes and pull requests.

## Publish to the universal ChatGPT/Codex Plugin Directory

This is a **skills-only Plugin**; it does not need an MCP server merely to qualify as a Plugin.

See [`PUBLISHING.md`](PUBLISHING.md) for the submission checklist and regression tests.

## Design principles

> **For practical tasks: discover broadly, verify narrowly.**

> **For decisive facts: source by the system that actually generates the record.**

Open Web is a discovery layer, not a complete model of the mainland-China information environment.
