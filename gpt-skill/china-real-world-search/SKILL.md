---
name: china-real-world-search
description: Use for mainland-China government, public-institution, state/public-service, and public-transport execution questions where current local facts matter, including eligibility, materials, procedures, fees, channels, outlets, opening hours, schedules, operational status, and public-transport routing. Do not use for general China research, consumer technology or device modification, shopping/products, private commercial services, company/news/finance/investment research, or ordinary technical support. For mixed requests, apply only to the public-service subtask.
license: MIT
metadata:
  author: hugeJan
  version: "1.3.0-gpt-slim"
---

# China Real-World Search

## Goal

Find the **current, locally executable path** for mainland-China public services. Do not treat an official webpage as the whole answer when the user actually needs to know what works now.

## 1. Scope gate

Use this Skill only when all three conditions pass.

### A. The provider or service is in scope

At least one must be central to the user's goal:

- government body, regulator, public-security organ, court, or government service center;
- public institution such as a public hospital, public school, examination body, or public cultural institution;
- state-owned or state-controlled operator acting as a public-service provider, such as utilities, telecommunications, postal service, or routine state-bank services;
- public-transport system or operator when the task depends on railway, flight, metro, bus, ferry, coach, station, airport, port, timetable, ticketing, or transfer operations;
- a third-party channel only when it is being evaluated as a way to complete an already in-scope public-service task.

### B. The task is in scope

Typical tasks:

- eligibility, materials, application, appointment, renewal, replacement, transfer, cancellation, status, or complaint route;
- statutory fee, public tariff, processing time, service point, service area, opening hours, or current channel;
- suspension, migration, restoration, timetable, ticketing rule, service availability, or other operational change;
- practical public-transport routing and transfer planning.

### C. Current or local execution matters

The answer must materially depend on current rules, province/city/district implementation, a real channel/outlet/station, a timetable or operational state, or the difference between written rules and what can actually be done now.

### Never activate merely because the prompt mentions China, 官方, 国企, 央企, 国产, 办理, or a government/SOE name.

Do **not** use this Skill for:

- flashing, Root, Bootloader unlocking, ROMs, firmware, hardware repair, or ordinary software troubleshooting;
- phones, appliances, vehicles, product comparison, shopping, warranty, or consumer-brand evaluation;
- private restaurants, hotels, entertainment, local-life recommendations, or ordinary private commercial services;
- company profile, management, project progress, business news, financial statements, stocks, funds, insurance, wealth products, or investment advice;
- stable general knowledge that does not require current/local execution research.

For mixed requests, use this Skill only for the separable public-service part.

## 2. Research workflow

### Step 1 — Define the exact claim

Resolve the service, requested action, jurisdiction, date/time if relevant, and the decision the user needs to make.

Prefer the exact official service/document name over colloquial shorthand.

### Step 2 — Establish the rule

Use the competent authority, current local service guide, public institution, or responsible operator for:

- eligibility and materials;
- official terminology;
- statutory fee or public tariff;
- legal/administrative processing time;
- responsible authority or operator.

A national rule does not automatically prove local execution details.

### Step 3 — Discover the path that can actually be used

For `how/where can I do this now?`, proactively search China-native execution channels, not only ordinary websites:

- provincial/city/district government-service platforms;
- official apps;
- WeChat or Alipay mini programs and public accounts;
- operator apps and service portals;
- official hotlines and service directories;
- self-service terminals;
- service halls, branches, counters, stations, airports, ports, and ticketing systems.

Name the concrete channel or service point when reasonably discoverable. Avoid vague advice such as `微信里有入口` or `去营业厅问`.

### Step 4 — Check real-world execution

When it can change the recommendation, use:

- current operator/service-hall notices;
- current map/POI data for outlets, entrances, stations, walking burden, and route topology;
- recent independent user experience for queues, transfer friction, failed entries, or channel problems;
- live transaction, inventory, timetable, or slot state only when the host can actually inspect it.

Use community evidence for practical reality, not as authority for statutory rules.

### Step 5 — Verify serious channels separately

For each serious app, mini program, branch, third party, or route, keep these propositions separate:

1. **Identity** — who operates or publishes it?
2. **Current usability** — does the relevant function appear usable now?
3. **Compatibility** — does it complete the target process?
4. **Official relationship** — self-operated, integrated, officially named/linked/recommended, or not established?
5. **Locality** — does the evidence apply to the user's city/district/service scenario?
6. **Time** — current, recent, historical only, unavailable, or unknown?

Never infer `works now` → `official`, `official in the past` → `available today`, or `provider says it works` → `target office accepts it`.

### Step 6 — Check freshness and locality

Prefer the smallest jurisdiction that controls the service:

**national/provincial rule → city/district implementation → exact channel/outlet/operator → recent operational evidence**

For changing services, distinguish event time, publication time, effective time, update time, and repost time.

When an old entry may have changed, search terms such as:

`调整` `暂停` `恢复` `搬迁` `下线` `迁移` `升级` `整合` `入口` `新版` `试运行` `正式运营` `停运` `临时`

An old official page proves historical status only unless current status is independently established.

### Step 7 — Be honest about platform access

Do not claim direct inspection of WeChat, Alipay, 12306, map apps, operator apps, hospital systems, booking slots, inventory, or in-app menus unless the host actually provides access.

If live state cannot be inspected, use accessible current evidence and state the limitation precisely.

Do not create test bookings, applications, payments, ticket purchases, accounts, or identity uploads merely to prove that a channel works.

## 3. Public-transport rule

For public-transport planning:

- resolve the exact origin, destination, date, and arrival constraint;
- verify railway/flight/metro/bus/ferry/coach schedules and disruptions with the operator or authoritative transaction surface when available;
- use maps for transfer geometry, walking, station entrances, and last-mile burden;
- compare practical door-to-door burden, transfers, fare, walking, reliability, and availability risk rather than theoretical speed alone;
- do not claim live ticket inventory unless it was directly checked.

Ordinary driving or walking directions without a public-transport/public-service dependency are out of scope.

## 4. Source rule

Choose sources by the fact they generate:

- rules/materials/fees → competent authority or current official service guide;
- local execution → local service platform, responsible office, institution, or operator;
- transport operation → operator, transport authority, airport/station/port, or authoritative transaction system;
- branch/station/route reality → current map/POI plus recent operational evidence;
- third-party compatibility → target-process acceptance evidence, not provider marketing alone.

A weak source may discover a candidate name. It should not define the official rule.

## 5. Output contract

Lead with the decision, not a source dump.

For a public-service task, normally give:

1. the best current path;
2. exact steps;
3. materials, eligibility, fee/tariff, and time when relevant;
4. concrete channel/outlet and current status;
5. why this path is preferable;
6. one fallback when useful;
7. the date and any material limitation for facts not directly verified.

For public transport, normally give:

1. primary route;
2. transfer sequence and stations;
3. time/cost range when supported;
4. critical first/last-service, station-change, walking, or availability risk;
5. one practical fallback when useful.

## 6. Routing examples

Use this Skill:

- `非本地户籍在东莞第一次办港澳通行证，需要什么材料，哪里能办？`
- `中国移动异地补卡需要什么材料，大岭山哪个营业厅能办？`
- `周一从凯里南站去东莞大岭山，给我公共交通路线。`

Do not use this Skill:

- `中国移动定制版手机能不能刷机、解锁 Bootloader？`
- `这台国产手机怎么 Root？`
- `某国有银行哪款理财收益最高？`

## Final check

Before answering, confirm:

- provider/service, task, and current/local gates all passed;
- the task is not merely consumer tech, shopping, private commerce, company research, or investment;
- rule truth and current execution were checked separately;
- China-native channels were considered when they could reduce user friction;
- third-party usability, compatibility, and official relationship were not conflated;
- locality and dates match the user's actual case;
- direct platform inspection was claimed only when it actually occurred;
- the answer leaves the user with an actionable next step.
