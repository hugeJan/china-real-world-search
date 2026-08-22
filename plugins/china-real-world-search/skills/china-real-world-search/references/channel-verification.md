# Channel Verification Protocol

Use this reference when the user needs a **current service channel**: a mini program, app, public account, booking path, payment/registration surface, service provider, self-service terminal, or offline counter.

The central rule is:

> **Discover broadly; verify narrowly. Current usability and official relationship are separate dimensions.**

A channel can be useful without being official. A channel can also be historically official but no longer usable.

## 1. Do not force discovery sources to prove authority claims

Different source types have different jobs.

### Good lead generators

These can be excellent for finding candidate channels:
- ordinary web search;
- SEO-heavy articles;
- service-provider pages;
- WeChat/Alipay native search;
- app-store search;
- maps/local-life platforms;
- Xiaohongshu/Douyin/Weibo/forums;
- recent user reports.

They may have weak evidentiary value for claims such as `官方指定` or `政府认可`.

### Good relationship/proof sources

Use these to establish official status, rules, or system relationships:
- competent authority notices/guides;
- official government or operator platforms;
- current institution pages/accounts;
- official service directories;
- formal technical/service documentation when publicly available;
- direct platform issuer/developer identity surfaces.

The correct pattern is:

`weak/ broad source discovers candidate -> stronger/narrow source verifies the claim the user actually needs`

Do not discard the candidate just because the first source is weak.

## 2. Decompose every important channel into separate claims

For channel X, ask separately:

1. **Existence** — does X exist?
2. **Identity** — who operates/publishes X?
3. **Current usability** — can the relevant function be used now?
4. **Output/compatibility** — does X produce the artifact/action needed by the target business system?
5. **Official relationship** — is X official, integrated, named, recommended, or merely third-party?
6. **Local scope** — does this hold in the user's province/city/service scenario?
7. **Time scope** — is the evidence current, recent, or historical only?

Never let evidence for one proposition silently prove the others.

Example:

- a government article from 2023 can prove that an official platform exposed a service in 2023;
- it cannot by itself prove the entry still exists today;
- a user successfully using a third-party mini program today can prove current usability in that context;
- it cannot by itself prove the mini program is an officially designated provider.

## 3. Authority-relationship classes

These labels are not a simple quality ranking. Use the most precise supported class.

### A. Official self-operated

The responsible government agency, public institution, operator, or its clearly identified official technical entity operates the channel itself.

Evidence target:
- current official ownership/issuer identity;
- official platform or institution documentation.

### B. Official-platform integrated

The service is exposed inside an official platform, but the underlying capability may be supplied or operated by another provider.

Examples of the pattern:
- an official government super-app exposes a service entry;
- an official hospital mini program embeds a third-party payment/registration service.

Do not automatically describe the underlying provider as `官方自营`.

Always attach a time qualifier when the integration evidence is old:
- `currently integrated`;
- `historically integrated as of YYYY-MM`.

### C. Officially named / recommended

A current competent official source explicitly names, links, lists, or recommends the specific provider/channel for the relevant task.

This is stronger than merely finding the provider mentioned inside a citizen question, repost, comment, or unrelated government page.

Require that the **official response/content itself** performs the naming or recommendation.

### D. Compatible third-party

Evidence indicates that the third-party channel can produce an output/action accepted by the relevant business process, but no current official designation has been established.

Compatibility evidence can include:
- current successful use verified firsthand;
- multiple independent recent success reports;
- a transaction/business-system acceptance result;
- credible technical/service documentation tied to the target process.

Do not translate `compatible` into `officially designated`, `government-certified`, or `official channel` without separate evidence.

### E. Practically reported

Recent users or current service surfaces report that the channel works, but compatibility has not been independently established strongly enough.

Useful as a candidate or fallback; label uncertainty when recommending it.

### F. Provider self-claim only

The provider claims `官方认可`, `政务打通`, `指定`, `认证`, `100%可用`, etc., but no independent evidence has verified the claim.

Treat these phrases as claims to investigate, not facts.

### G. Unknown

Evidence is insufficient to classify the official relationship.

Unknown does not mean unofficial, fraudulent, or unusable.

## 4. Current-usability states

Track usability independently from authority relationship.

### Confirmed usable now

Strong current evidence supports the relevant function in the user's context.

Examples:
- live platform state inspected;
- current transaction/booking completed;
- user reports direct successful use today/recently and the observation is internally consistent.

When based on user firsthand evidence, qualify the scope: `confirmed for the user's current context`.

### Recently evidenced usable

Recent independent evidence shows successful use, but the exact live state was not inspected.

### Historical only

A reliable old source proves the function existed, but no current evidence establishes continued availability.

### Currently unavailable

Current evidence shows the specific entry/function is missing, disabled, suspended, or no longer offered.

Do not infer that every equivalent service has disappeared.

### Unknown

No adequate current evidence.

## 5. Build a two-axis channel matrix

For each serious candidate, maintain an internal matrix:

| Candidate | Current usability | Authority relationship | Compatibility confidence | Evidence date |
|---|---|---|---|---|
| X | confirmed/recent/historical/unavailable/unknown | A-G above | high/medium/low/unknown | date/window |

This prevents common category errors:

- `works now -> must be official`;
- `official once -> must still work`;
- `not in current guide -> cannot work`;
- `government page mentions the name -> government recommends it`.

## 6. Historical official channel handling

When an old official source documents a channel/service:

1. record the exact date;
2. record exactly what function the source proves;
3. test the current entry directly if possible;
4. search `调整` `迁移` `下线` `暂停` `恢复` `升级` `整合` `入口` `新版` `服务迁移`;
5. search current official documentation for a replacement;
6. search current platform-native discovery for the same service;
7. report historical official status and current usability separately.

Correct language:
- `A government notice confirms that this service was integrated into Platform X in 2023; I have not established that the entry still exists today.`

Incorrect language:
- `The government once documented it, therefore Platform X can still do it now.`

Also incorrect:
- `The current entry is gone, therefore Platform X never offered the service.`

## 7. User-provided firsthand evidence

Treat direct user observations as evidence for the narrow observed proposition.

Examples:

`I opened mini program X today.`
- supports current existence/access for that user/account;
- does not prove the target transaction works.

`I generated the required receipt successfully in X today.`
- strongly supports current usability for that user/context;
- does not prove official designation;
- does not automatically prove every jurisdiction accepts the output.

`I used the receipt at office Y and it was accepted.`
- supports practical compatibility for that office/process at that time;
- still does not prove official recommendation unless separately documented.

Use external research to fill only the remaining uncertainty.

## 8. Government-page mention test

A provider name appearing on a government domain is not automatically official endorsement.

Distinguish:

1. **Government-authored recommendation/listing** — may establish official naming.
2. **Government reproduces a citizen's question containing the provider name** — does not establish endorsement by itself.
3. **Archived third-party material hosted or linked incidentally** — inspect authorship and context.
4. **Government response answers another part of the question but remains silent on the provider** — do not treat silence as confirmation.

Read the actual sentence that carries the claim.

## 9. Compatibility verification ladder

When the user cares about `will this work?`, prefer evidence in this order when available:

1. current successful transaction/acceptance in the target business system;
2. competent current official documentation explicitly accepting/naming the channel/output;
3. current official-platform integration showing the relevant function;
4. user's firsthand successful use in the same context;
5. multiple independent recent successful-use reports;
6. credible provider technical documentation;
7. provider marketing claim alone.

This ladder evaluates **compatibility**, not officialness.

## 10. Security and issuer identity

Before sending the user into an unfamiliar mini program/app/payment flow:

- confirm the exact platform name;
- inspect publisher/developer/主体 information when available;
- prefer entry through native search or a verified institution page over random QR codes;
- do not recommend unofficial APK mirrors;
- do not ask for unnecessary ID numbers, passwords, payment credentials, or screenshots containing sensitive data;
- if two services share similar names, resolve the exact entity before recommending one.

## 11. Recommendation rule

Optimize for the user's objective without overstating provenance.

If the user prioritizes **speed/convenience**:
- a confirmed compatible third-party can be the primary recommendation;
- clearly say that no current official designation was established if that matters.

If the user prioritizes **minimum ambiguity / official certainty**:
- prefer an official self-operated/integrated channel or the responsible service counter;
- mention the more convenient third-party as an alternative when useful.

A good concise answer often looks like:

> `For doing it now, X is the most practical option I found and current evidence supports that it works. I did not find a current competent source naming X as an official designated provider, so I would describe it as a compatible third-party rather than an official channel. Platform Y has historical official evidence, but that old evidence does not establish that its entry is still available today.`

## 12. Failure modes to reject

- Searching only official domains and missing the current usable channel.
- Treating SEO/community results as final proof of official status.
- Calling a provider `officially recognized` because its own marketing says so.
- Treating a provider name inside a citizen question on a government page as government endorsement.
- Treating old official integration as current availability.
- Treating the disappearance of an old official entry as proof that online service no longer exists.
- Treating lack of official naming as proof that a third-party service cannot work.
- Treating a user's successful use as proof of universal or permanent compatibility.
