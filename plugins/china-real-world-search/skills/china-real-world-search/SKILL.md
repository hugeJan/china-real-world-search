---
name: china-real-world-search
description: Research and verify mainland-China real-world questions by locating the system that actually generates the relevant fact, then combining China-native service surfaces, official records, platform-native search, and independent evidence. Use for 中国大陆现实场景 involving 政务办理、证件、出行、铁路/航班、本地商家、医院挂号、微信/支付宝小程序、公众号、App、政策执行、企业/项目状态、营业/运营状态、费用/余票/库存、地图POI、历史版本、事实核查 or any task where open-web-only search may miss the actual service or record.
---

# China Real-World Search

## Objective

Find the answer that corresponds to how reality in mainland China is actually **recorded and operated**, not merely the answer easiest to retrieve from the open web.

Use this mental model:

> **Find the system that naturally generates the fact -> retrieve the closest available original record -> verify what it proves -> add an independent execution/reality check when needed.**

Open web search is a discovery layer, not a complete model of the Chinese information environment.

## Core principles

- **Source by data-generating process, not prestige.** Ask which workflow/system naturally creates the decisive record.
- **Rule truth != operational truth.** Verify legal/official rules and the actual local execution path separately.
- **Not found != nonexistent.** App-only, mini-program-only, login-gated, unindexed, migrated, removed, paywalled, rate-limited, or badly queried information may still exist.
- **Independent evidence means independent generation.** Reposts derived from one upstream notice count as one source family.
- **Time/state semantics matter.** `计划/预计` cannot prove `已发生`; lifecycle states must not be collapsed.
- **Official authority is claim-bounded.** Official sources dominate for their own rules/records, not automatically for user experience or physical reality.
- **Never invent inaccessible platform state.** Verify that a channel exists; label current in-app state unverified if it cannot be inspected.

## 1. Choose research intensity

### Practical mode
Use for routes, opening hours, nearby places, booking paths, live availability, ordinary local-life questions.

Minimum:
- the live/operational source controlling the current state;
- an authority/operator source if rules, identity, or disruption matters.

### Standard verification mode
Use for government services, eligibility, documents, fees, hospital registration, local implementation, service authenticity.

Minimum:
- one first-party/competent source for the rule/status;
- one execution source showing the usable channel;
- a recent reality check when the path is time-sensitive or locally variable.

### Investigation mode
Use for `核实/调查/深挖/研究`, conflicting claims, companies/projects/legal/historical events, or “did this actually happen?” questions.

Target:
- one origin/first-party/legal record;
- one independently generated source;
- when applicable, one different modality such as transaction data, map/POI,现场影像, or遥感.

Read [verification-protocol.md](references/verification-protocol.md) for investigation mode.

## 2. Normalize the claim before searching

Extract only what materially changes the answer:

- **entity/subject**;
- **action or state**;
- **place/jurisdiction**;
- **time/window**;
- **user constraints** such as eligibility, documents, budget, transport, account access;
- **decision needed**: learn, execute, compare, verify, or reconstruct history.

For ambiguous lifecycle questions, split the state first. Examples:

- `签约 != 立项/备案 != 施工许可 != 开工 != 竣工 != 试生产 != 投产 != 量产 != 达产`
- `计划开通 != 试运行 != 初期运营 != 正式运营`
- `地图有POI != 企业依法登记 != 门店今天营业 != 建筑具有某法定用途`

Never let an earlier plan silently answer a later actual-state question.

## 3. Identify the fact-generating system

For every decisive claim ask:

> **Which real-world workflow naturally creates the closest-to-origin record for this fact?**

Examples:
- policy/eligibility -> competent authority / gazette / official service guide;
- company registration -> GSXT / market-regulation record;
- listed-company disclosure -> exchange / CNINFO filing;
- procurement -> official procurement system;
- actual government-service workflow -> local政务平台 / app / mini program / service hall;
- rail schedule/inventory -> 12306;
- route/traffic/POI -> map + transport operator systems;
- hospital appointment -> hospital / officially integrated health system;
- current store operation -> merchant/operator + map/local-life + recent reality evidence;
- physical change -> map/remote sensing/field imagery;
- old wording/page -> gazette/original PDF/archive.

Read [source-routing.md](references/source-routing.md) for the full routing map.

## 4. Build the required evidence tracks

Use only the tracks the task needs.

### Origin / authority
Find the original rule, record, filing, registry entry, notice, or transaction system.

### Execution
Find how the user actually acts in mainland China: 政务 App, WeChat/Alipay, operator app, booking system, map/local platform, service hall, or official hotline.

### Reality
Use current transaction state, maps, recent independent experience, onsite imagery, or physical evidence when actual conditions matter.

### History/version
Use gazettes, original PDFs, libraries/network archives, and web archives when reconstructing old/removed/migrated information.

## 5. Search China-native surfaces deliberately

When relevant, consider:

- central/provincial/municipal/district official sites and databases;
- national/local 政务平台 and specialized official systems;
- 微信搜一搜、公众号、小程序、视频号;
- 支付宝小程序、市民中心、生活号;
- official apps and app-store identity pages;
- 高德/百度地图 and transport operator channels;
- 12306, airline/airport/operator systems;
- 美团/大众点评 and other local-life platforms;
- 微博、小红书、抖音/快手、Bilibili、知乎、贴吧/vertical forums;
- GSXT, CNINFO/exchanges, court/enforcement/procurement/statistics systems;
- academic/professional databases, geospatial/remote-sensing systems, and archives for research tasks.

Do not let open-web accessibility decide whether a source category exists.

## 6. Search in three passes

### Discovery
Use broad Chinese queries to discover exact terminology, platform name, item name, department, entity alias, project name, or old name.

### Verification
After finding a candidate, narrow to the original/first-party source using exact titles, document numbers, entity IDs, official domains, or native system search.

### Current reality
For time-sensitive tasks, finish with the system controlling the live state: transaction inventory, appointment system, map/traffic, operator notice, or current platform screen.

Read [query-playbook.md](references/query-playbook.md) when results are stale, noisy, repetitive, or empty.

## 7. Apply locality and freshness

For locally implemented services, move from:

`national -> province -> city/county -> exact hall/operator/branch -> recent local operational evidence`

Do not substitute another city's workflow because it is easier to find.

For current questions:
- distinguish event date, publication date, effective date, update date, and repost date;
- search recent change terms such as `调整` `暂停` `恢复` `搬迁` `试运行` `正式运营` `升级` `停运` `施工` `临时` `预约`;
- use live systems for live claims whenever possible.

## 8. Diagnose empty results before concluding “no”

Check whether the information is:

- not proactively public;
- app/mini-program only;
- login/real-name gated;
- paywalled/professional-database only;
- moved, revised, deleted, or archived;
- unindexed;
- blocked by rate limits/CAPTCHA;
- hidden by wrong entity name, old name, jurisdiction, time window, or terminology;
- account/region visibility dependent.

Only then treat nonexistence as the leading hypothesis.

## 9. Check source independence and conflicts

Trace origins, not link counts.

When sources disagree ask:

1. Which system directly generated the fact?
2. Which is closest to the event time?
3. Are definitions/lifecycle states different?
4. Are geographic/statistical scopes different?
5. Is one a plan and the other an actual outcome?
6. Is there a later correction or superseding notice?

Do not use “official wins” or “majority wins” mechanically.

For deeper provenance, time-triangle, spatial/physical, negative-evidence, or archive handling, read [verification-protocol.md](references/verification-protocol.md).

## 10. Respect platform identity and access boundaries

For unfamiliar apps, mini programs, QR codes, payments, or identity flows:

- verify the issuer/responsible organization when possible;
- avoid unofficial APK mirrors, random QR codes, and unofficial payment links;
- do not bypass login, CAPTCHA, permissions, or platform controls;
- do not collect unnecessary personal/private data.

If an in-app screen cannot be inspected:
1. verify the channel itself;
2. provide only documented search terms/menu paths;
3. state that the live in-app state was not directly verified;
4. never invent slots, prices, labels, or availability.

## 11. Optimize for the user's real objective

For actionable tasks compare realistic options on:
- total cost;
- total time;
- transfers/steps;
- walking/taxi burden;
- timing/availability risk;
- reliability/officialness;
- prerequisites the user can satisfy.

Return one primary recommendation, not a source dump.

## 12. Confidence states

Use precise states when uncertainty matters:

- **Confirmed** — current origin/first-party evidence directly supports the claim.
- **Confirmed rule / live state not inspected** — rule verified; current platform state may differ.
- **Cross-verified** — independent generation mechanisms agree.
- **Credibly documented platform-only channel** — channel verified; current in-app state inaccessible.
- **Lead only** — useful clue, not yet verified.
- **Unknown** — evidence insufficient.

## 13. Output contract

### Practical / service tasks
1. recommendation/conclusion first;
2. exact action path;
3. critical numbers: fee/time/distance/hours/transfers/availability;
4. why this beats the main alternative;
5. fallback or uncertainty only when material.

### Investigation / verification tasks
1. verdict + confidence;
2. what is actually established;
3. evidence chain by generation mechanism;
4. time/definition conflicts resolved;
5. what remains unproven;
6. best next source if more certainty is warranted.

## Final quality gate

Before answering, check:

- Did I define the actual entity + state/action + place + time claim?
- Did I identify the system that naturally generates each decisive fact?
- Did I separate rule truth from execution truth?
- Did I use China-native/platform-native surfaces where open Web is structurally incomplete?
- Did I separate event time from publication/effective/update time?
- Did I avoid turning plans/forecasts into accomplished facts?
- Did I count independent generation rather than reposts?
- Did I diagnose “not found” before “does not exist”?
- Did I verify locality/current state where actionability depends on them?
- Can the user act on the recommendation without another round of basic research?

## References

- [Source routing](references/source-routing.md)
- [Query playbook](references/query-playbook.md)
- [Verification protocol](references/verification-protocol.md)
- [Execution examples](references/examples.md)
