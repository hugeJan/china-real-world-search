# China Real-World Search

A ChatGPT/Codex **skills-only Plugin** for researching mainland-China real-world questions through the systems that actually generate and operate the relevant facts — while still discovering the channels people can actually use today.

This repository follows the Plugin layout with `.codex-plugin/plugin.json`, a bundled Agent Skill, and a repo marketplace for personal/local installation and testing.

## What it does

China Real-World Search is designed around a common failure mode in China-local research: **the most authoritative source is often not the best place to discover the current executable channel**.

The plugin therefore uses two complementary workflows.

### Practical/actionable questions

> **Discover current options broadly → verify serious candidates narrowly → classify what each option is → confirm current usability/compatibility → recommend the best path.**

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

## Skills-only by design

This project does **not** require an MCP server or developer-operated backend.

The Skill provides research instructions and reference material. It uses whatever search/browser/apps/tools the host environment already makes available.

That distinction matters:

- a source category such as WeChat, Alipay, 12306, maps, local-life platforms, or an app may be the ideal place to verify a fact;
- the Skill must only claim direct inspection when the current host actually exposes access to that surface;
- otherwise it should use accessible official/web/secondary evidence and clearly state that the in-app/live state was not directly inspected.

The project intentionally does not add an MCP server merely to simulate access that the host does not have.

## Security and evidence boundaries

Retrieved webpages, snippets, posts, provider pages, PDFs, and other search results are treated as **untrusted evidence**, not instructions. Content found during research must not override the user's task, privacy boundaries, tool permissions, or action scope.

The Skill also separates:

- `current usability`;
- `target-process compatibility`;
- `official relationship`;
- `historical status`;
- `user firsthand evidence`.

A channel working today does not prove it is official. An old official integration does not prove it still works today.

## Practical discovery without quota chasing

The plugin prefers concrete provider/platform names when they are reasonably discoverable, but it no longer treats a fixed number of candidates or search routes as a mandatory completion target.

Discovery stops when the user's decision is sufficiently answered, an exclusive route is established, additional alternatives are unlikely to change the recommendation, or access limitations make further direct verification impossible.

When the user has a real choice and alternatives could change the recommendation, a small named candidate set is still useful.

## No consequential actions just for verification

The Skill must not create bookings, submit applications, make payments, register accounts, buy tickets, upload identity documents, or perform other consequential actions merely to test whether a channel works.

Already-completed user transactions may be evidence. New consequential actions require an explicit user request and the host's normal confirmation/approval flow.

## Plugin structure

```text
.
├── .agents/plugins/marketplace.json
├── evals/
│   └── skill-regressions.json
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

Then install the plugin from the available Plugins surface in ChatGPT/Codex for your plan/workspace.

Local/repo marketplace availability can differ across products, plans, regions, and workspace policies.

## Validate the package

```bash
python3 scripts/validate_plugin.py
```

The same validator runs in GitHub Actions on pushes and pull requests.

The repository also contains structured regression fixtures in `evals/skill-regressions.json`. The validator checks their schema and coverage; behavior-level execution still requires an Agent/Plugin eval harness or manual release testing.

## Publish

This remains a **skills-only Plugin**. It does not need an MCP server merely to qualify as a Plugin.

See [`PUBLISHING.md`](PUBLISHING.md) for the release checklist and regression suite.

## Design principles

> **For practical tasks: discover broadly, verify narrowly, stop when the decision is answered.**

> **For decisive facts: source by the system that actually generates the record.**

> **Source strategy never implies tool availability.**

Open Web is a discovery layer, not a complete model of the mainland-China information environment.
