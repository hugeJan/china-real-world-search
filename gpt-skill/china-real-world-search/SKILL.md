---
name: china-real-world-search
description: Use for mainland-China government, public-institution, state/public-service, and public-transport execution questions where current local facts matter, including eligibility, materials, procedures, fees, channels, outlets, opening hours, schedules, operational status, and public-transport routing. Do not use for general China research, consumer technology or device modification, shopping/products, private commercial services, company/news/finance/investment research, or ordinary technical support. For mixed requests, apply only to the public-service subtask.
license: MIT
metadata:
  author: hugeJan
  version: "1.3.1-gpt-slim"
---

# China Real-World Search

## Goal

Find the **current, locally executable path** for mainland-China public services. An official webpage may establish a rule without proving what channel actually works now.

## 1. Scope gate

Activate only when all three pass:

1. **Provider/service** — government body or service center; public institution; state-owned/state-controlled operator acting as a public-service provider; or public transport whose operation is material to the task.
2. **Task** — eligibility, materials, procedure, appointment, fee/tariff, processing time, channel, outlet, opening hours, status, suspension/migration, timetable, ticketing rule, complaint route, or public-transport routing.
3. **Current/local need** — the answer depends on current rules/state, province/city/district implementation, a concrete channel/outlet/station, timetable, disruption, or other real execution detail.

A third-party app/mini program may be researched only as a channel for an already in-scope task.

Do **not** activate merely because the prompt mentions China, 官方, 国企, 央企, 国产, 办理, or an SOE/government name.

Do **not** use for:

- flashing, Root, Bootloader, ROMs, firmware, device repair, or ordinary software troubleshooting;
- product comparison, shopping, phones, appliances, vehicles, warranty, or brand evaluation;
- restaurants, hotels, entertainment, private local-life recommendations, or ordinary private commercial services;
- company/profile/project/news research, financial statements, stocks, funds, insurance, wealth products, or investment advice;
- stable general knowledge that does not require current/local execution research.

For mixed requests, apply only to the separable public-service part.

## 2. Research workflow

### Step 1 — Resolve the exact task

Identify the service, requested action, jurisdiction, relevant date/time, and the decision the user needs. Preserve the exact current official service/document name when possible.

### Step 2 — Establish rule truth

Use the competent authority, current local service guide, public institution, or responsible operator for eligibility, materials, official terminology, statutory fee/public tariff, formal processing time, and responsibility.

Do not assume a national rule proves local execution details.

### Step 3 — Find the executable channel

For `how/where can I do this now?`, proactively search China-native channels instead of stopping at ordinary webpages:

- provincial/city/district government-service platforms;
- official apps;
- WeChat/Alipay mini programs and public accounts;
- operator apps/portals and official hotlines;
- self-service terminals;
- service halls, branches, counters, stations, airports, ports, and ticketing systems.

Name the concrete channel or service point when discoverable. Avoid vague advice like `微信里有入口` or `去营业厅问`.

### Step 4 — Check real execution

When it can change the recommendation, use current operational notices, map/POI data, and recent user experience.

- maps/POI → location, entrance, route topology, walking burden;
- recent user reports → queueing, transfer friction, failed entries, or practical channel problems;
- live transaction/inventory/slot state → only when the host can actually inspect it.

Community evidence can describe practical reality, but should not define statutory rules.

### Step 5 — Verify serious channels without conflating claims

For each serious app, mini program, branch, third party, or route, separately verify:

- **identity** — who operates/publishes it;
- **usability** — whether the relevant function appears usable now;
- **compatibility** — whether it completes the target process;
- **official relationship** — self-operated, integrated, officially named/linked/recommended, or not established;
- **locality/time** — whether the evidence matches the user's place and current period.

Never infer `works now` → `official`, `official before` → `works today`, or `provider claims compatibility` → `target office accepts it`.

### Step 6 — Check freshness and capability

Prefer:

**national/provincial rule → city/district implementation → exact channel/outlet/operator → recent operational evidence**

For old or changing services, search terms such as `调整` `暂停` `恢复` `搬迁` `下线` `迁移` `升级` `整合` `入口` `新版` `试运行` `正式运营` `停运` `临时`.

Treat old official evidence as historical unless current status is independently established.

Do not claim direct inspection of WeChat, Alipay, 12306, map apps, operator apps, hospital systems, booking slots, inventory, or in-app menus unless the host actually has that access. Do not create test bookings, payments, applications, ticket purchases, accounts, or identity uploads merely to verify usability.

## 3. Public transport

For public-transport planning:

- resolve exact origin, destination, date, and arrival constraint;
- verify schedules/disruptions with operators, authorities, stations/airports/ports, or authoritative transaction systems when available;
- use maps for transfer geometry, walking, entrances, and last-mile burden;
- compare door-to-door time, cost, transfers, walking, reliability, and availability risk rather than theoretical speed alone;
- never claim live ticket inventory unless it was directly checked.

Ordinary driving/walking directions without a public-transport or public-service dependency are out of scope.

## 4. Output

Lead with the decision, not a source dump.

For a service task, normally provide: **best current path → exact steps → materials/fee/time → concrete channel/outlet → why it is preferable → one useful fallback → material verification limitation**.

For public transport, normally provide: **primary route → transfer sequence → supported time/cost → critical risk → one practical fallback**.

## Routing examples

Use:

- `非本地户籍在东莞第一次办港澳通行证，需要什么材料，哪里能办？`
- `中国移动异地补卡需要什么材料，大岭山哪个营业厅能办？`
- `周一从凯里南站去东莞大岭山，给我公共交通路线。`

Do not use:

- `中国移动定制版手机能不能刷机、解锁 Bootloader？`
- `这台国产手机怎么 Root？`
- `某国有银行哪款理财收益最高？`

## Final check

Before answering, confirm that the scope gate passed, rule truth and execution truth were separated, China-native channels were considered where useful, locality/freshness match the user's case, and no unsupported claim of direct platform inspection was made.
