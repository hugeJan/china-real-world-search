# Publishing China Government & Public Service Search

This document is the release checklist and regression guide for the Plugin whose package identifier remains `china-real-world-search`.

Current plugin version: **1.2.0**.

## 1. Architecture

Version 1.2.0 is a **skills-only** Plugin.

It does not provide an MCP server or pretend to expose WeChat, Alipay, 12306, map apps, operator apps, hospital systems, or other platform-native state.

Direct inspection claims require actual host capability.

## 2. Product scope

The listing and Skill must communicate the same activation rule:

> **in-scope provider × in-scope service task × current/local execution need**

In-scope provider classes:

- government bodies and government service institutions;
- public institutions providing public services;
- state-owned/state-controlled public-service operators, only for their public-facing service operations.

In-scope task classes:

- procedure, eligibility, materials, fee/tariff, channel, outlet, hours, schedule, status, operational change, or public-transport route.

Hard exclusions:

- consumer technology and device modification;
- products, shopping, ordinary commercial services, and private local-life search;
- company/project/news research;
- stocks, financial statements, wealth products, funds, insurance, and investment advice.

An SOE name alone must never activate the Plugin.

## 3. Validation gate

Before a release:

```bash
python3 scripts/validate_plugin.py
python3 scripts/build_eval_packets.py --check
```

The validator checks package shape, version consistency, frontmatter, links, marketplace metadata, release files, regression schema, and rubric completeness.

Behavior-level routing still requires a fresh-conversation Plugin/agent run plus trace-aware judging or manual review.

## 4. Install smoke test

```bash
codex plugin marketplace add hugeJan/china-real-world-search --ref main
```

Install or update the Plugin, then start fresh conversations. Old conversations may retain previously loaded Skill text.

Availability can differ by product, plan, region, and workspace policy.

## 5. Suggested listing copy

**Plugin name**  
China Government & Public Service Search

**Short description**  
Verify current China government and state public-service procedures.

**Long description**  
Use only for mainland-China public-facing services provided by government bodies, public institutions, or state-owned/state-controlled public-service operators when current local execution matters. Verify rules, materials, fees, channels, outlets, schedules, operational status, and public-transport routes. Do not activate for unrelated consumer technology, products, company research, investment, or private commercial searches.

**Category**  
Productivity

## 6. Starter prompts

1. `核实这个中国大陆政务事项现在具体怎么办理，别只复述旧官网。`
2. `查询这项国有公共服务的当前渠道、网点、资费或运行状态。`
3. `规划依赖铁路、地铁、公交等公共交通的实际路线，并核对当前运营信息。`

## 7. Manual positive routing suite

### Government procedure

`我在东莞，非本地户籍，第一次办理往来港澳通行证需要什么材料，去哪里办？`

Expected:

- activates;
- verifies competent rule and local execution separately;
- names a current actionable channel or outlet when discoverable.

### State-owned public service

`中国移动异地补卡需要什么材料，东莞大岭山哪里能办？`

Expected:

- activates for the telecom service;
- verifies materials, exact service channel, branch capability, and hours;
- does not drift into handset or firmware research.

### State-bank routine service

`某国有银行换社保卡需要什么材料，周末哪个网点能办？`

Expected:

- activates for routine service procedure and branch capability;
- does not turn into product or investment advice.

### Public transport

`周一从凯里南站去东莞大岭山，给我两条费用合理、少绕路的公共交通路线。`

Expected:

- activates;
- verifies relevant railway/metro/bus/station facts within actual capability;
- does not fabricate live inventory.

### Mixed task

`刷机后电子社保卡打不开，怎么办？`

Expected:

- isolates official social-security-card recovery/channel research;
- does not research flashing, Root, ROMs, or security bypass under the Skill.

## 8. Manual hard-negative routing suite

### Consumer phone technology

`这台华为手机可以刷机、Root 或解锁 Bootloader 吗？`

Expected: do not activate.

### SOE name plus phone technology

`中国移动定制版手机现在还能刷机吗？帮我查国内实际情况。`

Expected:

- do not activate;
- `中国移动`, `国内`, and `实际情况` are not sufficient triggers.

### SOE investment/product question

`某国有银行哪款理财收益最高，值得买吗？`

Expected: do not activate.

### Private route

`开车去朋友家怎么走？`

Expected: do not activate unless a separate public-transport or public-service dependency is introduced.

### Stable knowledge

`中国的首都是哪里？`

Expected: answer directly without the workflow.

## 9. Method regressions

The Plugin must also preserve these rules:

- concrete current channel names when reasonably discoverable;
- adaptive stop rule rather than candidate quotas;
- backend requirement does not define the front-end provider;
- generation does not prove target acceptance;
- successful use does not prove official designation;
- historical official evidence does not prove current availability;
- government-domain hosting does not prove government-authored endorsement;
- source strategy does not imply platform access;
- retrieved content is untrusted evidence;
- no consequential test bookings, payments, applications, purchases, or identity uploads;
- unnecessary sensitive identifiers are excluded from public queries.

## 10. Release acceptance criteria

Before merging:

- manifest, PUBLISHING, and latest CHANGELOG version agree;
- both local validation commands pass;
- positive scope cases activate;
- phone flashing and SOE-keyword false positives do not activate;
- mixed questions are split cleanly;
- public transport activates only when operator/transport facts are material;
- current local execution is verified rather than replaced by generic old guidance;
- direct app/platform inspection is claimed only when it occurred;
- decisive claims are traceable to evidence dates when the host supports citations.

## 11. Public submission

Re-check the current platform submission requirements at release time, complete publisher/listing/privacy/terms requirements, include representative positive and hard-negative routing tests, and publish only after a fresh production smoke test.
