---
name: china-real-world-search
description: Research and solve mainland-China real-world questions by broadly discovering current practical channels, then verifying decisive claims against the systems that actually generate them. Use for 中国大陆现实场景 involving 政务办理、证件、出行、铁路/航班、本地商家、医院挂号、微信/支付宝小程序、公众号、App、政策执行、企业/项目状态、营业/运营状态、费用/余票/库存、地图POI、历史版本、事实核查 or any task where open-web-only search may miss the actual service or record.
---

# China Real-World Search

## Objective

Find answers that correspond to how reality in mainland China is **actually operated, recorded, and accessed**, not merely what is easiest to retrieve from the open web.

Use two complementary mental models:

### For practical/actionable service questions

> **Discover current options broadly -> verify each option narrowly -> classify what it is -> confirm the live state -> recommend the best usable path.**

### For investigation/fact-verification questions

> **Find the system that naturally generates the fact -> retrieve the closest available original record -> verify what it proves -> add independent evidence when needed.**

Open-web search is a discovery layer, not a complete model of the Chinese information environment.

## Core principles

- **Discover broadly, verify narrowly.** Do not begin practical-channel discovery with filters that destroy recall.
- **Discovery strength != evidentiary strength.** A weak source may be an excellent lead generator even when it cannot prove the final claim.
- **Source by data-generating process, not prestige.** For decisive facts, ask which workflow/system naturally creates the relevant record.
- **Rule truth != operational truth.** Verify legal/official rules and the actual local execution path separately.
- **Usable != official.** A channel may work in practice without being official or officially designated.
- **Historically official != currently available.** An old official notice proves what existed then, not that the entry still works today.
- **Not officially listed != unusable.** Silence in a current guide does not prove that a compatible third-party service cannot work.
- **User firsthand evidence is scoped evidence.** A user's current successful use can establish that observed behavior in that context, but not official endorsement or universal compatibility.
- **Not found != nonexistent.** App-only, mini-program-only, login-gated, unindexed, migrated, removed, paywalled, rate-limited, or badly queried information may still exist.
- **Independent evidence means independent generation.** Reposts derived from one upstream notice count as one source family.
- **Time/state semantics matter.** `计划/预计` cannot prove `已发生`; lifecycle states must not be collapsed.
- **Official authority is claim-bounded.** Official sources dominate for their own rules/records, not automatically for user experience or physical reality.
- **Never invent inaccessible platform state.** Verify that a channel exists; label current in-app state unverified if it cannot be inspected.

## 1. Choose research intensity

### Practical mode

Use for routes, opening hours, nearby places, booking paths, live availability, current service-channel discovery, and ordinary local-life questions.

Minimum:
- broad discovery of plausible current options when more than one channel may exist;
- verification of the live/operational state that matters to the user;
- authority/operator verification only for claims about rules, identity, official relationship, or disruption.

### Standard verification mode

Use for government services, eligibility, documents, fees, hospital registration, local implementation, service authenticity, or any practical task where choosing the wrong channel could waste meaningful time/money.

Minimum:
- one first-party/competent source for the rule/status;
- broad discovery of current execution options when the official guide may be incomplete;
- relationship/identity verification for the recommended channel;
- a recent reality check when the path is time-sensitive or locally variable.

### Investigation mode

Use for `核实/调查/深挖/研究`, conflicting claims, companies/projects/legal/historical events, or “did this actually happen?” questions.

Target:
- one origin/first-party/legal record;
- one independently generated source;
- when applicable, one different modality such as transaction data, map/POI, 现场影像, or 遥感.

Read [verification-protocol.md](references/verification-protocol.md) for investigation mode.

## 2. Normalize the question before searching

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

## 3. For service/channel questions, run two tracks

When the user asks **where/how can I do this now?**, do not force every candidate to be official before it is allowed into the search space.

### Track A — Current practical discovery

Search broadly for channels people can plausibly use now:

- WeChat / Alipay native search;
- current third-party mini programs and service providers;
- maps and local-life platforms;
- current platform pages and transaction surfaces;
- recent community/social reports;
- ordinary web results, including SEO-heavy pages when useful for lead discovery.

Treat these as **candidate generators**, not automatic proof.

Do not use `site:gov.cn` or equivalent official-domain filtering as the first pass for current-channel discovery.

### Track B — Authority / relationship verification

For each serious candidate, separately determine:

- what the competent authority actually requires;
- who operates or issues the channel;
- whether a competent current source explicitly names/recommends it;
- whether it is integrated into an official platform;
- whether evidence only shows practical/technical compatibility;
- whether the provider is merely making a self-claim.

Do not discard a useful Track-A candidate solely because Track B cannot establish official endorsement. Instead, label its relationship accurately.

If the user names a channel they have already used or seen, include it as a candidate and verify only the claims that remain uncertain.

Read [channel-verification.md](references/channel-verification.md) for the channel relationship/usability model.

## 4. Identify the fact-generating system for decisive claims

For every claim that materially affects the recommendation ask:

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

## 5. Build only the evidence tracks the task needs

### Discovery

Find candidate channels, terminology, platform names, aliases, and current practical paths. Discovery sources can be weak evidence but strong lead generators.

### Origin / authority

Find the original rule, record, filing, registry entry, notice, transaction system, or competent authority statement.

### Execution

Find how the user actually acts in mainland China: 政务 App, WeChat/Alipay, operator app, booking system, third-party service, map/local platform, service hall, or official hotline.

### Reality

Use current transaction state, maps, recent independent experience, user firsthand evidence, onsite imagery, or physical evidence when actual conditions matter.

### History/version

Use gazettes, original PDFs, libraries/network archives, and web archives when reconstructing old/removed/migrated information.

## 6. Search China-native surfaces deliberately

When relevant, consider:

- central/provincial/municipal/district official sites and databases;
- national/local 政务平台 and specialized official systems;
- 微信搜一搜、公众号、小程序、视频号;
- 支付宝小程序、市民中心、生活号;
- official apps and app-store identity pages;
- third-party mini programs/service providers discovered through current search;
- 高德/百度地图 and transport operator channels;
- 12306, airline/airport/operator systems;
- 美团/大众点评 and other local-life platforms;
- 微博、小红书、抖音/快手、Bilibili、知乎、贴吧/vertical forums;
- GSXT, CNINFO/exchanges, court/enforcement/procurement/statistics systems;
- academic/professional databases, geospatial/remote-sensing systems, and archives for research tasks.

Do not let open-web accessibility or source prestige decide whether a candidate source category is allowed into discovery.

## 7. Use the right search order for the task

### Practical/service task

1. **Discover** current candidates broadly.
2. **Verify candidate identity/relationship** for the options that may be recommended.
3. **Verify the underlying rule/requirement** with the competent source when relevant.
4. **Check current usability/live state** as close to the actual platform/transaction system as possible.
5. **Compare and recommend** one primary option plus fallback when useful.

### Investigation task

1. **Normalize the proposition**.
2. **Find the fact-generating system/origin record**.
3. **Trace provenance and source independence**.
4. **Add current/physical/independent evidence** when the proposition warrants it.
5. **Resolve time, lifecycle, definition, and version conflicts**.

Read [query-playbook.md](references/query-playbook.md) when results are stale, noisy, repetitive, overly official, overly commercial, or empty.

## 8. Apply locality and freshness

For locally implemented services, move across both rule and execution layers:

`national/provincial rule -> city/county implementation -> exact hall/operator/provider -> recent local operational evidence`

Do not substitute another city's workflow because it is easier to find.

For current questions:
- distinguish event date, publication date, effective date, update date, and repost date;
- search recent change terms such as `调整` `暂停` `恢复` `搬迁` `试运行` `正式运营` `升级` `停运` `施工` `临时` `预约`;
- when an old official channel is found, explicitly test whether it still exists, moved, was withdrawn, or was replaced;
- use live systems for live claims whenever possible.

## 9. Diagnose empty results before concluding “no”

Check whether the information is:

- not proactively public;
- app/mini-program only;
- login/real-name gated;
- paywalled/professional-database only;
- moved, revised, deleted, or archived;
- unindexed;
- blocked by rate limits/CAPTCHA;
- hidden by wrong entity name, old name, jurisdiction, time window, or terminology;
- account/region visibility dependent;
- absent from official guides but present as a third-party compatible service.

Only then treat nonexistence as the leading hypothesis.

## 10. Check source independence and conflicts

Trace origins, not link counts.

When sources disagree ask:

1. Which system directly generated the fact?
2. Which is closest to the event time?
3. Are definitions/lifecycle states different?
4. Are geographic/statistical scopes different?
5. Is one a plan and the other an actual outcome?
6. Is one describing channel existence while another describes official endorsement?
7. Is there a later correction, migration, withdrawal, or superseding notice?

Do not use “official wins” or “majority wins” mechanically.

For deeper provenance, time-triangle, spatial/physical, negative-evidence, or archive handling, read [verification-protocol.md](references/verification-protocol.md).

## 11. Respect platform identity and access boundaries

For unfamiliar apps, mini programs, QR codes, payments, or identity flows:

- verify the issuer/responsible organization when possible;
- distinguish platform host from underlying service provider;
- avoid unofficial APK mirrors, random QR codes, and unofficial payment links;
- do not bypass login, CAPTCHA, permissions, or platform controls;
- do not collect unnecessary personal/private data.

If an in-app screen cannot be inspected:
1. verify the channel itself where possible;
2. provide only documented or clearly qualified search terms/menu paths;
3. state that the live in-app state was not directly verified;
4. never invent slots, prices, labels, availability, or official endorsement.

## 12. Treat user firsthand evidence precisely

When the user reports a direct current observation, use it for the narrow fact actually observed.

Example:
- `I opened mini program X today and successfully generated the receipt.`

This can support **current usability for that user/context**.

It does not by itself establish:
- official designation;
- universal acceptance across jurisdictions;
- availability to every account;
- future availability.

Do not waste time re-proving the user's observed fact unless it conflicts with the task or materially affects safety/reliability. Verify the remaining claims instead.

## 13. Optimize for the user's real objective

For actionable tasks compare realistic options on:
- current usability;
- total cost;
- total time;
- steps/transfers;
- walking/taxi burden;
- timing/availability risk;
- compatibility confidence;
- official relationship / issuer identity;
- prerequisites the user can satisfy.

Return one primary recommendation, not a source dump.

A compatible third-party option may be the best recommendation when the user's objective is speed/convenience. An official self-operated path may be the better fallback when the user prioritizes minimum ambiguity.

## 14. Keep claim confidence and channel status separate

### Claim confidence

Use precise states when uncertainty matters:

- **Confirmed** — direct current origin/first-party evidence directly supports the claim.
- **Cross-verified** — independent generation mechanisms support the same proposition.
- **Highly likely** — strong evidence but one decisive origin record is missing.
- **Lead only** — useful clue, not yet verified.
- **Unknown** — evidence insufficient.

### Channel status

When material, separately state:
- **current usability**: confirmed / recently reported / historical only / unavailable / unknown;
- **authority relationship**: official self-operated / official-platform integrated / officially named / compatible third-party / practically reported / provider self-claim only / unknown.

Do not infer either dimension from the other.

## 15. Output contract

### Practical / service tasks

1. recommendation/conclusion first;
2. exact action path;
3. current usability + channel relationship when material;
4. critical numbers: fee/time/distance/hours/transfers/availability;
5. why this beats the main alternative;
6. fallback or uncertainty only when material.

Do not dump the full evidence taxonomy when a short qualification is enough.

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
- For a practical service task, did I discover broadly before narrowing to authoritative proof?
- Did I keep useful third-party candidates even when they were not officially named?
- Did I classify current usability separately from official relationship?
- Did I distinguish official self-operation, official-platform integration, official naming, compatibility, and self-claim?
- Did I identify the system that naturally generates each decisive fact?
- Did I separate rule truth from execution truth?
- Did I use China-native/platform-native surfaces where open Web is structurally incomplete?
- Did I separate event time from publication/effective/update time?
- Did I avoid turning historical official support into a claim of current availability?
- Did I avoid turning practical success into a claim of official endorsement?
- Did I count independent generation rather than reposts?
- Did I diagnose “not found” before “does not exist”?
- Did I verify locality/current state where actionability depends on them?
- Can the user act on the recommendation without another round of basic research?

## References

- [Source routing](references/source-routing.md)
- [Query playbook](references/query-playbook.md)
- [Channel verification](references/channel-verification.md)
- [Verification protocol](references/verification-protocol.md)
- [Execution examples](references/examples.md)
