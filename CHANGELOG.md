# Changelog

## 1.1.2 — Capability and safety boundaries

### Changed

- Kept the project explicitly **skills-only**; no MCP server or developer-operated backend was added.
- Added a capability gate so source-routing advice never implies that the host can directly inspect WeChat, Alipay, 12306, map apps, local-life platforms, or other app-native surfaces.
- Added an untrusted-content boundary: retrieved webpages, snippets, posts, provider pages, and documents are evidence, not instructions.
- Added a consequential-action boundary so the assistant does not book, pay, register, submit applications, upload identity material, or create transactions merely to test whether a channel works.
- Replaced fixed `2-3 candidates / 3 discovery routes` completion requirements with an adaptive stop rule based on whether additional discovery can change the user's decision.
- Added explicit evidence-disclosure expectations for decisive current facts when the host supports citations/links.
- Narrowed Skill activation so pure writing/coding/translation, stable general knowledge, and tasks already fully served by a dedicated live tool do not activate the workflow unnecessarily.
- Reworked query and source-routing references around actual host capabilities rather than assumed platform access.
- Updated README and privacy documentation to describe the skills-only architecture and removed the stale `version 1.0.0` privacy wording.
- Added structured regression fixtures and expanded repository validation for stricter package consistency checks.

### Why

Version 1.1.1 improved concrete entity discovery but made candidate/search-route counts too easy to interpret as quotas. It also described valuable China-native source surfaces more strongly than a skills-only plugin can guarantee access to them.

Version 1.1.2 keeps the same research philosophy while making execution capability-aware, safer against retrieved-content prompt injection, less prone to unnecessary search, and easier to validate in CI.

## 1.1.1 — Concrete-candidate discovery hardening

### Changed

- Added a **concrete-candidate discovery gate** for practical service questions.
- Practical searches should identify named current candidates when such options are reasonably discoverable, instead of stopping at categories such as `第三方小程序`, `微信/支付宝`, `照相馆`, or `线下窗口`.
- Added an explicit fallback rule: if concrete candidates cannot be named, state the visibility/access limitation rather than pretending generic categories are a complete answer.
- Added artifact/outcome-centered query strategy so the skill searches the exact required receipt/document/service rather than only the broad surrounding task.
- Added `backend mechanism != user-facing channel`: a backend upload/inspection requirement does not by itself prove the user must use a particular provider type.
- Added official-terminology fidelity for required forms, receipts, certificates, statuses, and fees; near-synonyms must not be silently merged.
- Added regressions for `generation != acceptance`, generic-category answers, and false `must use a photo studio` inferences.
- Extended repository validation to check release-version consistency.

### Why

Version 1.1 improved recall by allowing current third-party channels into the search space, but an agent could still satisfy `discover broadly` superficially: acknowledge that online third-party services exist, then answer with generic classes instead of discovering concrete provider/platform names.

## 1.1.0 — Practical discovery without authority overclaiming

### Changed

- Reworked practical/service tasks around **discover broadly, verify narrowly**.
- Added a two-track workflow: current practical discovery + authority/relationship verification.
- Made clear that discovery-source quality and evidentiary strength are different dimensions.
- Split channel evaluation into three independent dimensions:
  - current usability;
  - target-process compatibility;
  - official relationship.
- Added explicit official-relationship distinctions between:
  - official self-operated;
  - official-platform integrated;
  - officially named/linked;
  - explicitly recommended/designated;
  - no official relationship established.
- Kept compatible third-party, practically reported, and provider self-claim states separate from official relationship.
- Added scoped handling of user firsthand evidence, including `generation != acceptance != official designation`.
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
