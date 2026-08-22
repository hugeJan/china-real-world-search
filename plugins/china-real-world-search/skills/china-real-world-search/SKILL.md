---
name: china-real-world-search
description: Research and solve mainland-China real-world questions by discovering concrete current practical channels, then verifying decisive claims against the systems that actually generate them. Use for 中国大陆现实场景 involving 政务办理、证件、出行、铁路/航班、本地商家、医院挂号、微信/支付宝小程序、公众号、App、政策执行、企业/项目状态、营业/运营状态、费用/余票/库存、地图POI、历史版本、事实核查 or any task where open-web-only search may miss the actual service or record.
---

# China Real-World Search

## Objective

Find answers that match how reality in mainland China is **actually operated, recorded, and accessed**, not merely what is easiest to retrieve from the open web.

Use two complementary models:

### Practical/actionable service questions

> **Discover concrete current options broadly -> verify serious candidates narrowly -> classify what each candidate actually is -> confirm current usability/compatibility -> recommend the best path.**

### Investigation/fact-verification questions

> **Find the system that naturally generates the fact -> retrieve the closest original record -> verify what it proves -> add independent evidence when needed.**

Open-web search is a discovery layer, not a complete model of the Chinese information environment.

## Core principles

- **Discover concrete options, not only categories.** `微信小程序/第三方平台/照相馆/线下窗口` are source/channel classes, not satisfactory discoveries when named candidates are reasonably discoverable.
- **Discover broadly, verify narrowly.** Do not begin practical-channel discovery with filters that destroy recall.
- **Discovery strength != evidentiary strength.** Weak sources can be strong lead generators.
- **Source decisive facts by data-generating process, not prestige.** Ask which workflow naturally creates the relevant record.
- **Rule truth != operational truth.** Verify requirements and current execution separately.
- **Backend mechanism != user-facing channel.** A rule saying data must enter system X does not prove the user must visit provider type Y unless a competent source explicitly imposes that restriction.
- **Preserve official terminology.** For required forms, receipts, certificates, licenses, statuses, or fees, use the exact current official name/wording when material; do not silently normalize near-synonyms.
- **Usable != official.** A working channel need not be officially operated, named, or designated.
- **Generation != acceptance != official designation.** Successfully producing an artifact does not prove the target process accepts it; successful acceptance still does not prove official designation.
- **Historically official != currently available.** Old official evidence is time-scoped.
- **Not officially listed != unusable.** Silence in a current guide does not prove a compatible third-party cannot work.
- **User firsthand evidence is scoped evidence.** Use it for exactly what the user observed, not broader claims.
- **Not found != nonexistent.** App-only, mini-program-only, login-gated, unindexed, migrated, removed, paywalled, rate-limited, or badly queried information may still exist.
- **Independent evidence means independent generation.** Reposts from one upstream source count as one source family.
- **Time/state semantics matter.** `计划/预计` cannot prove `已发生`.
- **Official authority is claim-bounded.** Official sources dominate for their own rules/records, not automatically for user experience or physical reality.
- **Never invent inaccessible platform state.** If the current screen cannot be inspected, say so.

## 1. Choose research intensity

### Practical mode

Use for routes, opening hours, nearby places, booking paths, live availability, current channel discovery, and ordinary local-life questions.

Minimum:
- discover concrete plausible current options when the user asks `where/how can I do this now?`;
- verify the live/operational state that materially affects the choice;
- verify authority/operator claims only where rules, identity, official relationship, or disruption matter.

### Standard verification mode

Use for government services, eligibility, documents, fees, hospital registration, local implementation, service authenticity, or any practical task where a wrong channel could waste meaningful time/money.

Minimum:
- one competent source for the rule/status;
- concrete current execution candidates when official guides may be incomplete;
- identity/relationship verification for the recommended option;
- current usability/compatibility evidence to the degree needed for the decision;
- exact official terminology for required documents/artifacts when wording matters.

### Investigation mode

Use for `核实/调查/深挖/研究`, conflicting claims, companies/projects/legal/historical events, or `did this actually happen?` questions.

Target:
- one origin/first-party/legal record;
- one independently generated source;
- when applicable, one different modality such as transaction data, map/POI, 现场影像, or 遥感.

Read [verification-protocol.md](references/verification-protocol.md) for investigation mode.

## 2. Normalize the question

Extract only what materially changes the answer:

- **entity/subject**;
- **action or state**;
- **place/jurisdiction**;
- **time/window**;
- **user constraints**: eligibility, documents, budget, transport, account access;
- **decision needed**: learn, execute, compare, verify, or reconstruct history.

Split ambiguous lifecycle states before searching:

- `签约 != 立项/备案 != 施工许可 != 开工 != 竣工 != 试生产 != 投产 != 量产 != 达产`
- `计划开通 != 试运行 != 初期运营 != 正式运营`
- `地图有POI != 企业依法登记 != 门店今天营业 != 建筑具有某法定用途`

Never let an earlier plan silently answer a later actual-state question.

## 3. Concrete-candidate discovery gate

For a practical question asking **where / which app / which mini program / which provider / how to do this now**, discovery is not complete merely because channel categories were identified.

### Pass condition

Before finalizing, do one of the following:

**A. Concrete candidate set formed**
- identify **2-3 named current candidates** when multiple options are plausibly discoverable; or
- identify the only serious named candidate found after broad discovery and say why alternatives did not survive verification.

**B. Concrete discovery genuinely blocked**
- attempt at least **3 materially different discovery routes** (for example ordinary web, platform-native/service search, local/community/provider discovery);
- state the visibility/access limitation;
- do not replace missing names with vague phrases as though the search succeeded.

### Failure condition

Treat the practical search as incomplete if the answer only says things like:
- `可以找第三方小程序`;
- `微信/支付宝上有线上服务`;
- `去能上传系统的照相馆`;
- `可以在线办理`;

while concrete names are reasonably discoverable.

The goal of the first pass is **entity discovery**: collect exact platform/provider/service names first, then verify them.

## 4. For service/channel questions, run two tracks

When the user asks **where/how can I do this now?**, do not require every candidate to be official before it enters the search space.

### Track A — Current practical discovery

Search broadly for plausible **named** current channels:

- WeChat / Alipay native search;
- current third-party mini programs/service providers;
- maps and local-life platforms;
- current transaction/platform surfaces;
- recent community/social reports;
- ordinary web results, including SEO-heavy pages when useful for extracting candidate names.

Treat these as **candidate generators**, not automatic proof.

Do not use `site:gov.cn` or equivalent official-domain filtering as the first pass for current-channel discovery.

When results are generic, pivot from topic queries to **artifact/outcome queries** and extract names:
- exact required document/artifact name + `在线/小程序/微信/支付宝`;
- locality + artifact name + current year;
- candidate name + exact service/outcome.

### Track B — Narrow verification

For each serious candidate, separately determine:

- what the competent authority actually requires;
- the exact current official name of the required artifact/status when material;
- who operates/publishes the candidate;
- whether a current competent source merely **names/links** it;
- whether a current competent source explicitly **recommends/designates** it;
- whether it is integrated into an official platform;
- whether its output/action is accepted by the target business process;
- whether evidence only shows practical use or provider self-claims.

Do not discard a useful Track-A candidate solely because no official endorsement is established. Label the uncertainty precisely.

If the user names a channel they already used or saw, keep it as a candidate and verify only the unresolved claims.

Read [channel-verification.md](references/channel-verification.md) for the detailed model.

## 5. Keep channel dimensions separate

For any important channel, track three independent dimensions.

### Current usability

`confirmed now / recently evidenced / historical only / currently unavailable / unknown`

### Official relationship

Use only what is actually supported:
- official self-operated;
- official-platform integrated;
- officially named/linked;
- explicitly recommended/designated;
- no official relationship established.

These relationship labels may coexist. Do not upgrade naming/linking into recommendation/designation.

### Compatibility / practical evidence

`accepted/compatible / practically reported / provider self-claim only / unknown`

Do not infer one dimension from another.

Examples:
- `works now` does not prove `official`;
- `officially integrated in 2023` does not prove `works now`;
- `generated the receipt` does not prove `receipt was accepted`;
- `receipt was accepted` does not prove `provider was officially designated`.

## 6. Do not infer user-channel restrictions from backend requirements

When a competent source says an artifact/data must pass a backend system, inspection, upload, validation, or database process:

1. record what the backend requirement actually proves;
2. separately search how users can satisfy it today;
3. do not infer `must use a photo studio / must use a government app / must visit a counter` unless the source explicitly restricts the user-facing provider/channel.

Example pattern:

`照片/数据必须进入检测系统`  
**does not by itself prove**  
`用户必须去照相馆`.

A third-party mini program, official-platform integration, self-service device, or counter may all be front ends to the same backend process.

## 7. Preserve official names and semantic boundaries

For documents, receipts, certificates, permits, status labels, fees, or service items:

- copy the exact current official title from the competent source when possible;
- distinguish official title from colloquial shorthand;
- if official sources use different names, investigate whether they are versions, regional variants, or genuinely different artifacts;
- do not invent a hybrid name from near-synonyms.

This matters especially for terms such as `采集回执`, `检测回执`, `受理回执`, `电子回执`, `照片回执`.

## 8. Identify the fact-generating system for decisive claims

For claims that materially affect the recommendation ask:

> **Which real-world workflow naturally creates the closest-to-origin record for this fact?**

Examples:
- policy/eligibility -> competent authority / gazette / official service guide;
- company registration -> GSXT / market-regulation record;
- listed-company disclosure -> exchange / CNINFO filing;
- procurement -> official procurement system;
- government-service workflow -> local 政务 platform / app / mini program / service hall;
- rail schedule/inventory -> 12306;
- route/traffic/POI -> map + transport operator systems;
- hospital appointment -> hospital / integrated health system;
- current store operation -> merchant/operator + map/local-life + recent reality evidence;
- physical change -> map/remote sensing/field imagery;
- old wording/page -> gazette/original PDF/archive.

Read [source-routing.md](references/source-routing.md) for the full routing map.

## 9. Build only the evidence tracks the task needs

### Discovery
Find named candidates, terminology, aliases, platform names, and current practical paths.

### Origin / authority
Find the rule, record, filing, registry entry, notice, transaction system, or competent authority statement.

### Execution
Find how the user actually acts: 政务 App, WeChat/Alipay, operator app, third-party service, booking system, map/local platform, service hall, or official hotline.

### Reality
Use current transaction state, maps, recent independent experience, user firsthand evidence, onsite imagery, or physical evidence when actual conditions matter.

### History/version
Use gazettes, original PDFs, libraries/network archives, and web archives for old/removed/migrated information.

## 10. Search China-native surfaces deliberately

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

Do not let open-web accessibility or source prestige decide whether a source category is allowed into discovery.

## 11. Use the right search order

### Practical/service task

1. **Discover named current candidates** broadly.
2. **Verify candidate identity and relationship** for serious options.
3. **Verify the underlying rule/requirement and exact terminology** when relevant.
4. **Check current usability and target-process compatibility** as directly as possible.
5. **Compare and recommend** one primary option plus fallback when useful.

### Investigation task

1. **Normalize the proposition**.
2. **Find the fact-generating system/origin record**.
3. **Trace provenance and source independence**.
4. **Add current/physical/independent evidence** when warranted.
5. **Resolve time, lifecycle, definition, and version conflicts**.

Read [query-playbook.md](references/query-playbook.md) when results are stale, noisy, repetitive, overly official, overly commercial, generic, or empty.

## 12. Apply locality and freshness

For locally implemented services, move across both rule and execution layers:

`national/provincial rule -> city/county implementation -> exact hall/operator/provider -> recent local operational evidence`

Do not substitute another city's workflow because it is easier to find.

For current questions:
- distinguish event date, publication date, effective date, update date, and repost date;
- search recent change terms such as `调整` `暂停` `恢复` `搬迁` `下线` `迁移` `升级` `整合` `入口`;
- when an old official channel is found, test whether it still exists, moved, was withdrawn, or was replaced;
- use live systems for live claims whenever possible.

## 13. Diagnose empty or generic results before concluding

Check whether information is:

- not proactively public;
- app/mini-program only;
- login/real-name gated;
- paywalled/professional-database only;
- moved, revised, deleted, or archived;
- unindexed;
- blocked by rate limits/CAPTCHA;
- hidden by wrong artifact name, provider name, entity name, old name, jurisdiction, time window, or terminology;
- account/region visibility dependent;
- absent from official guides while a compatible third-party service still exists.

If results are only generic categories, **change the query objective from explanation to entity extraction** before stopping.

Only after plausible alternatives are exhausted should nonexistence or `no concrete candidate found` become the leading conclusion.

## 14. Resolve conflicts by proposition, not prestige

When sources disagree ask:

1. Which system directly generated the fact?
2. Which is closest to the event time?
3. Are definitions/lifecycle states different?
4. Are geographic/statistical scopes different?
5. Is one a plan and the other an actual outcome?
6. Is one about channel existence/usability while another is about official relationship?
7. Is there a later correction, migration, withdrawal, or replacement?

Do not use `official wins` or `majority wins` mechanically.

Read [verification-protocol.md](references/verification-protocol.md) for deeper provenance/conflict handling.

## 15. Respect identity and access boundaries

For unfamiliar apps, mini programs, QR codes, payments, or identity flows:

- verify exact provider/issuer identity when possible;
- distinguish platform host from underlying provider;
- prefer native search or verified institution entry over random QR codes;
- avoid unofficial APK mirrors and unofficial payment links;
- do not bypass login, CAPTCHA, permissions, or platform controls;
- do not collect unnecessary personal/private data.

If an in-app screen cannot be inspected:
1. verify the channel itself where possible;
2. provide only documented or clearly qualified paths;
3. say the live state was not directly inspected;
4. never invent slots, prices, labels, availability, compatibility, or official endorsement.

## 16. Use user firsthand evidence precisely

Examples:

`I opened mini program X today.`
- supports current access for that user/account;
- does not prove the target function works.

`I generated the required receipt in X today.`
- supports current generation/usability for that user/context;
- does not prove the target authority accepted it.

`Office Y accepted the receipt.`
- supports compatibility for that process/place/time;
- does not prove official designation.

Do not waste time re-proving what the user directly observed. Research the remaining uncertainty.

## 17. Optimize for the user's actual objective

For actionable tasks compare realistic options on:
- current usability;
- compatibility confidence;
- official relationship / issuer identity;
- total cost;
- total time;
- steps/transfers;
- walking/taxi burden;
- timing/availability risk;
- prerequisites the user can satisfy.

Return one primary recommendation, not a source dump.

A compatible third-party may be best for speed/convenience. An official self-operated/integrated path may be the better fallback when the user prioritizes minimum ambiguity.

## 18. Output contract

### Practical / service tasks

1. recommendation/conclusion first;
2. **named** primary channel/provider/route, not only a category;
3. exact action path;
4. current usability + compatibility + official relationship when material;
5. critical numbers: fee/time/distance/hours/transfers/availability;
6. why this beats the main alternative;
7. fallback or uncertainty only when material.

If concrete discovery was blocked, say what was searched and what visibility limitation prevented naming a candidate.

Do not dump the full taxonomy when one concise qualification is enough.

### Investigation / verification tasks

1. verdict + confidence;
2. what is actually established;
3. evidence chain by generation mechanism;
4. time/definition conflicts resolved;
5. what remains unproven;
6. best next source if more certainty is warranted.

## Final quality gate

Before answering, check:

- Did I define the actual entity + action/state + place + time claim?
- For a practical task, did I discover **concrete names** rather than stop at channel categories?
- If multiple options plausibly exist, did I form a small named candidate set or explain why concrete discovery was blocked?
- Did I avoid inferring a user-facing provider restriction from a backend technical requirement?
- Did I preserve the competent source's exact name for required documents/artifacts when material?
- Did I keep useful third-party candidates even when they were not officially named?
- Did I separate current usability, compatibility, and official relationship?
- Did I distinguish official naming/linking from explicit recommendation/designation?
- Did I avoid treating successful generation as successful acceptance?
- Did I avoid treating successful acceptance as official designation?
- Did I identify the system that naturally generates each decisive fact?
- Did I separate rule truth from execution truth?
- Did I use China-native/platform-native surfaces where open Web is incomplete?
- Did I separate event time from publication/effective/update time?
- Did I avoid turning historical official support into current availability?
- Did I count independent generation rather than reposts?
- Did I diagnose `not found` before `does not exist`?
- Did I verify locality/current state where actionability depends on them?
- Can the user act on the recommendation without another round of basic research?

## References

- [Source routing](references/source-routing.md)
- [Query playbook](references/query-playbook.md)
- [Channel verification](references/channel-verification.md)
- [Verification protocol](references/verification-protocol.md)
- [Execution examples](references/examples.md)
