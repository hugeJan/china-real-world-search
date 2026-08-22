# China Search Query Playbook

Use this when generic web queries return stale guides, SEO aggregators, repeated reposts, or nothing useful.

## 1. Search the action/state, not only the topic

Weak:

`港澳通行证 东莞`

Better:

- `东莞 往来港澳通行证 首次申领 办事指南`
- `东莞 出入境 预约 微信小程序`
- `东莞 港澳通行证 相片回执`
- `东莞 大岭山 出入境 受理点`

Useful action terms:

`办事指南` `首次申领` `续签` `预约` `在线办理` `办理地点` `材料清单` `收费标准` `办理时限` `咨询电话` `小程序` `公众号` `支付宝` `App` `自助机` `网点` `营业时间`

## 2. Build entity/alias matrices

For companies/projects, search:

```text
"公司全称"
"公司简称"
"旧公司名"
"统一社会信用代码"
"品牌名"
"法定代表人"
"项目公司名称"
```

For places/events:

```text
"正式地名"
"旧地名"
"行政区新名称"
"附近乡镇/道路/河流/设施"
"正式事件名称"
```

Entity mismatch is a major cause of false negative search results.

## 3. Search lifecycle verbs explicitly

For projects:

```text
"项目全称" 立项
"项目全称" 备案
"项目全称" 环评
"项目全称" 施工许可
"项目全称" 开工
"项目全称" 封顶
"项目全称" 竣工
"项目全称" 验收
"项目全称" 试生产
"项目全称" 投产
"项目全称" 首件 下线
"项目全称" 达产
```

Do not search only the project name and accept whichever lifecycle word appears in the top result.

## 4. Add locality explicitly

Use the smallest jurisdiction likely to control implementation:

`省 + 市 + 区/镇 + 事项`

Examples:
- `广东 东莞 大岭山 居住证 预约`
- `深圳 福田 口岸 地铁 末班车`

If a village/neighborhood is too small for indexing, move up to town/street and add the nearest transport/service hub.

## 5. Separate event time from publication time

For historical or changing facts, search by the event window and state verb:

```text
"项目全称" 2025年2月 投产
"线路名称" 2024年12月 初期运营
"机构名称" 2026年8月 搬迁 通知
```

When results contain `预计` `计划` `拟` `将` `力争`, treat them as planned states until later actual-state evidence is found.

## 6. Search for change notices

For current operations append:

`最新` `2026` `通知` `通告` `调整` `暂停` `恢复` `搬迁` `升级` `试运行` `初期运营` `正式运营` `停运` `施工` `临时` `预约优先` `延时服务`

Verify publication and effective dates; the word `最新` is not enough.

## 7. Search mobile/service channels directly

Try:

- `事项 + 微信小程序`
- `事项 + 微信公众号`
- `事项 + 支付宝小程序`
- `事项 + 市民中心`
- `机构名 + 小程序`
- `机构名 + App`
- `机构名 + 预约办理`

After discovering a platform name, verify it on the responsible organization's official pages or issuer identity surface.

## 8. Separate discovery queries from verification queries

Discovery:

`东莞 办港澳通行证 微信 小程序`

Verification after finding a candidate:

`site:dg.gov.cn i莞家 出入境 预约`

Do not constrain every query to official domains from the start; that can prevent discovery of the actual execution channel.

## 9. Use exact-title/document-number search

For policies, approvals, judicial/procurement/filing records:

```text
site:gov.cn "文件精确标题"
site:*.gov.cn "项目全称" "批复"
site:*.gov.cn "项目全称" "环境影响评价"
site:*.gov.cn "企业全称" "行政处罚"
"文件文号"
"统一社会信用代码"
"证券代码" "项目名称"
```

Document numbers and entity IDs reduce same-name errors.

## 10. Search platform-natively

### WeChat

In 搜一搜 try:
- exact document title;
- `主管部门 + 事项`;
- `医院/学校/景区全名 + 通知`;
- `项目全称 + 状态动词`.

Inspect account/mini-program identity and recency.

### Maps

Search exact branch/POI and compare:
- address;
- phone;
- hours;
- route;
- recent place updates.

### Local-life / community

Search:
- `广州南站 换乘 10分钟`
- `东莞 出入境 周六 办证`
- `医院全名 停车 挂号`
- `门店全名 2026年8月 营业`

Use as experience/field evidence unless the account is official.

## 11. Build a query pack

For a complex task, run a compact pack rather than repeating one query:

1. origin/official record;
2. local implementation;
3. mobile/platform channel;
4. current operational state;
5. independent recent evidence;
6. historical/version search if needed.

Skeleton:

- `[authority] [formal item] 办事指南/批复/公告`
- `[city] [service] 微信 小程序 预约`
- `[exact hall/operator] 地址 营业时间`
- `[live system] [date] [origin] [destination]`
- `[platform/community] [entity] [state] [date]`
- `[exact title/document no.] 历史/原文`

## 12. Diagnose weak-result symptoms

Switch strategy when:
- results are SEO aggregators;
- every result repeats the same wording;
- results are old for a current service;
- only national rules appear for a local execution question;
- the user knows an in-app channel exists but open web cannot find it;
- map and official page disagree;
- every article cites the same announcement;
- search keeps returning planned future dates for a question about actual completion.

Response:
- change vocabulary/state verb;
- change jurisdiction;
- search exact platform/entity identifier;
- move to platform-native search;
- search recent change notices;
- trace reposts to origin;
- use an independent modality;
- use official hotline/formal request only when the remaining uncertainty materially matters.
