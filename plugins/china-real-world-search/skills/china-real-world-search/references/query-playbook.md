# China Search Query Playbook

Use this when generic web queries return stale guides, SEO aggregators, repeated reposts, only official pages, or nothing useful.

The key distinction is:

> **Discovery queries maximize recall. Verification queries maximize precision. Do not confuse the two.**

## 1. Practical service discovery pack

When the user asks `where/how can I do this now?`, start broad enough to discover real current channels.

### Current-channel discovery

Try combinations such as:

- `[事项] 在线办理`
- `[事项] 微信 小程序`
- `[事项] 支付宝 小程序`
- `[事项] 公众号`
- `[事项] App`
- `[事项] 线上 回执/预约/办理`
- `[事项] [城市] 小程序`
- `[事项] [current year]`
- `[事项] 最新 入口`
- `[事项] 手机办理`

Also search platform-natively when possible:
- 微信搜一搜;
- 支付宝;
- maps/local-life platforms;
- relevant operator/transaction apps;
- recent community/social content.

At this stage, the goal is to **collect candidate names**, not to prove that each candidate is official.

Do not start with `site:gov.cn` or another official-domain filter unless the user explicitly asks only for official channels. Early authority filtering improves precision but can destroy recall.

## 2. Verify a discovered candidate separately

After finding candidate X, run a compact verification pack:

```text
"X" [事项]
"X" [主管部门/机构]
"X" site:*.gov.cn
"X" 官方
"X" 小程序 主体
"X" 回执/接口/受理/预约
"X" [城市/省份]
```

Then ask:
- who operates it?
- is it currently usable?
- is it official, officially integrated, officially named, compatible third-party, or only self-claimed?
- is the evidence current or historical?

Do not require the discovery source itself to answer these questions.

## 3. Search the action/state, not only the topic

Weak:

`港澳通行证 东莞`

Better:

- `东莞 往来港澳通行证 首次申领 办事指南`
- `东莞 出入境 预约 微信小程序`
- `东莞 港澳通行证 相片回执 在线办理`
- `东莞 大岭山 出入境 受理点`

Useful action terms:

`办事指南` `首次申领` `续签` `预约` `在线办理` `办理地点` `材料清单` `收费标准` `办理时限` `咨询电话` `小程序` `公众号` `支付宝` `App` `自助机` `网点` `营业时间`

## 4. Build entity/alias matrices

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

For apps/mini programs/services:

```text
"完整服务名"
"旧服务名"
"开发者/运营主体"
"公众号名"
"小程序名"
"官方平台入口名"
```

Entity mismatch is a major cause of false negative search results.

## 5. Search lifecycle verbs explicitly

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

## 6. Add locality explicitly

Use the smallest jurisdiction likely to control implementation:

`省 + 市 + 区/镇 + 事项`

Examples:
- `广东 东莞 大岭山 居住证 预约`
- `深圳 福田 口岸 地铁 末班车`

If a village/neighborhood is too small for indexing, move up to town/street and add the nearest transport/service hub.

## 7. Separate event time from publication time

For historical or changing facts, search by the event window and state verb:

```text
"项目全称" [year-month] 投产
"线路名称" [year-month] 初期运营
"机构名称" [current year] 搬迁 通知
```

When results contain `预计` `计划` `拟` `将` `力争`, treat them as planned states until later actual-state evidence is found.

## 8. Search for change/migration notices

For current operations append:

`最新` `通知` `通告` `调整` `暂停` `恢复` `搬迁` `升级` `下线` `迁移` `整合` `入口` `新版` `服务迁移` `试运行` `初期运营` `正式运营` `停运` `临时`

This is especially important when an old official notice proves that a service once existed.

Verify publication and effective dates; the word `最新` is not enough.

## 9. Handle historical official channels explicitly

If an old official page says Platform A offered Service S:

1. search the current Platform A for S;
2. search `A + S + 下线/迁移/调整/升级/入口`;
3. search current official guides for replacement language;
4. search current platform-native channels for S without assuming A is still the entry;
5. record `historically official/integrated` separately from `currently usable`.

Do not use an old official page as current operational proof.

Do not let the disappearance of A make you conclude that no current third-party channel exists.

## 10. Search mobile/service channels directly

Try:

- `事项 + 微信小程序`
- `事项 + 微信公众号`
- `事项 + 支付宝小程序`
- `事项 + 市民中心`
- `机构名 + 小程序`
- `机构名 + App`
- `机构名 + 预约办理`
- `事项 + 第三方 服务`

After discovering a platform name, verify its issuer/relationship separately.

## 11. Separate discovery queries from verification queries

Discovery:

`东莞 办港澳通行证 微信 小程序`

Verification after finding candidate `X`:

`"X" 东莞 出入境`

`"X" site:dg.gov.cn`

`"X" 运营主体`

The discovery phase may use low-authority sources. The verification phase should tighten the claim and source type.

## 12. Use exact-title/document-number search

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

## 13. Search platform-natively

### WeChat

In 搜一搜 try:
- exact service name;
- `主管部门 + 事项`;
- `医院/学校/景区全名 + 通知`;
- `项目全称 + 状态动词`;
- third-party candidate name + exact service.

Inspect account/mini-program identity and recency.

### Alipay

Try the same service/agency name inside Alipay, especially for government, city, transport, utility, healthcare, and payment workflows.

### Maps

Search exact branch/POI and compare:
- address;
- phone;
- hours;
- route;
- recent place updates.

### Local-life / community

Search recent phrases such as:
- `[station] 换乘 [minutes]`
- `[city] 出入境 周六 办证`
- `[hospital] 停车 挂号`
- `[store] [current month/year] 营业`
- `[mini-program] 成功 回执/预约/办理`

Use as experience/field evidence unless the account is official.

## 14. Treat provider marketing as a claim, not proof

When a provider page says:

`官方认可` `官方指定` `政府认证` `政务打通` `100%合规` `官方合作`

search the exact phrase/provider name against:
- competent official sources;
- current official service directories;
- issuer identity pages;
- independent successful-use evidence.

If no independent support appears, classify the statement as provider self-claim only.

## 15. Test government-domain mentions for authorship

If a provider name appears on a `.gov.cn` page, inspect **who actually says it**.

Possible cases:
- official body itself names/recommends provider -> can support official naming;
- citizen question includes provider name, official reply answers something else -> does not prove endorsement;
- page republishes third-party content -> trace authorship;
- old official page -> historical only unless current status is verified.

Do not use `government domain = government endorsement` as a shortcut.

## 16. Use the user's firsthand evidence efficiently

If the user says:
- `I used X today and it generated the receipt.`

Do not spend the whole search trying to prove X opens.

Instead verify the remaining uncertain claims:
- official relationship;
- jurisdictional scope;
- whether the output is accepted by the target process;
- whether a safer/cheaper official fallback exists.

User evidence is scoped, not universal.

## 17. Build a query pack for complex tasks

For a practical service task:

1. broad current-channel discovery;
2. candidate identity/relationship verification;
3. competent rule/requirement source;
4. current operational/live state;
5. recent independent success evidence;
6. historical/migration search if an old official channel appears.

Skeleton:

- `[service] [city] 微信/支付宝/在线/小程序`
- `[candidate] [service] [city]`
- `[candidate] site:*.gov.cn`
- `[authority] [formal item] 办事指南/公告`
- `[candidate] 成功/可用 [current year]`
- `[old platform] [service] 下线/迁移/调整`

For an investigation task, keep the origin-record-first workflow from the verification protocol.

## 18. Diagnose weak-result symptoms

Switch strategy when:
- results are SEO aggregators;
- every result repeats the same wording;
- results are old for a current service;
- only national rules appear for a local execution question;
- only official pages appear but none gives a usable current channel;
- only commercial pages appear and none establishes authority relationship;
- the user knows an in-app channel exists but open web cannot find it;
- a historical official entry is documented but no longer visible;
- map and official page disagree;
- every article cites the same announcement;
- search keeps returning planned future dates for a question about actual completion.

Response options:
- widen discovery before narrowing;
- change vocabulary/state verb;
- change jurisdiction;
- search exact platform/entity identifier;
- move to platform-native search;
- search recent change/migration notices;
- trace provider claims to independent evidence;
- trace reposts to origin;
- use an independent modality;
- use official hotline/formal request only when the remaining uncertainty materially matters.
