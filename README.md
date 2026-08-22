# China Real-World Search

A Codex and ChatGPT skill for researching and verifying mainland-China real-world questions through the systems that actually generate and operate the relevant facts.

It combines authoritative records with China-native execution channels such as government apps, WeChat and Alipay mini programs, operator systems, maps, local platforms, transaction systems, and recent independent evidence.

## What it helps with

- Government services, eligibility, materials, fees, and local execution paths
- Transport schedules, availability, disruptions, and route planning
- Hospitals, appointments, local businesses, and current operating status
- Companies, projects, policies, filings, and lifecycle-state verification
- Historical pages, migrated records, conflicting claims, and fact-checking

## Install in Codex

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/hugeJan/china-real-world-search.git \
  ~/.codex/skills/china-real-world-search
```

Start a new Codex task after installation and invoke the skill with:

```text
$china-real-world-search
```

## Install in ChatGPT Web

Download the repository as a ZIP file, open **Plugins → Skills → Create → Upload from computer**, and upload the ZIP.

## Structure

- [`SKILL.md`](SKILL.md) — main workflow and quality gate
- [`references/source-routing.md`](references/source-routing.md) — fact-generating system routing
- [`references/query-playbook.md`](references/query-playbook.md) — China-native query strategy
- [`references/verification-protocol.md`](references/verification-protocol.md) — investigation and conflict-resolution method
- [`references/examples.md`](references/examples.md) — execution examples

