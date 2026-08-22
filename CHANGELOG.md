# Changelog

## 1.1.0 — Practical discovery without authority overclaiming

### Changed

- Reworked practical/service tasks around **discover broadly, verify narrowly**.
- Added a two-track workflow: current practical discovery + authority/relationship verification.
- Made clear that discovery-source quality and evidentiary strength are different dimensions.
- Added explicit distinctions between:
  - official self-operated;
  - official-platform integrated;
  - officially named/recommended;
  - compatible third-party;
  - practically reported;
  - provider self-claim only.
- Separated **current usability** from **official relationship**.
- Added scoped handling of user firsthand evidence.
- Added migration/downline checks for historical official service entries.
- Added government-domain authorship checks so citizen questions/reposts are not mistaken for official endorsement.
- Expanded query strategy so practical channel discovery does not begin with `site:gov.cn` filtering.
- Added regression examples/tests for current third-party channels vs historical official platforms.

### Why

The v1.0 workflow was strong at fact provenance but could still narrow too early toward authoritative sources during practical service discovery. In mainland-China service ecosystems, the channel that works today may first surface through platform-native search, service-provider pages, local-life platforms, or recent user experience, while official material may only define the requirement or document an older entry.

Version 1.1 keeps strict claim verification while improving recall of real executable options.

## 1.0.0 — Initial Plugin release

- Converted the project from a loose Skill into a ChatGPT/Codex skills-only Plugin.
- Added `.codex-plugin/plugin.json`, repo marketplace support, package validation, publishing metadata, and the initial China real-world search workflow.
