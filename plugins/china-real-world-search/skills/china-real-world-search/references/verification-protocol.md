# Verification Protocol

Use this reference for investigation mode, conflicting sources, historical reconstruction, or any claim where a false positive would materially mislead the user.

For current apps/mini programs/service providers, also read [channel-verification.md](channel-verification.md). Channel **current usability**, **compatibility**, and **official relationship** are separate propositions.

## 1. Start from a falsifiable proposition

Rewrite vague questions into:

> **Entity X + action/state Z + place Y + time T**

Bad:
- `这个项目到底怎么样？`
- `这家工厂是不是已经搞好了？`

Better:
- `公司 X 是否在地点 Y 于 2026-08-01 前开始商业生产？`
- `线路 X 是否在日期 T 开始载客运营？`

If the state is ambiguous, split it into lifecycle checkpoints before searching.

For a service channel, split the question too:
- does the channel exist now?
- who operates it?
- does the required function work now?
- is its output accepted by the target process?
- is it official/integrated/named, or merely compatible?

## 2. Minimal provenance record

For every decisive piece of evidence, track as many of these as applicable:

- original data-generating entity/system;
- publisher/host;
- original URL or system name;
- document/file number;
- entity identifier (统一社会信用代码, securities code, standard place name, etc.);
- event time;
- publication time;
- effective date;
- retrieval time;
- version/revision status;
- repost/source relationship;
- spatial identifier/address/coordinates when relevant.

For service channels also track, when relevant:
- provider/operator identity;
- host platform vs underlying provider;
- evidence of current usability;
- evidence of compatibility/acceptance;
- evidence of official relationship;
- evidence date and locality.

The purpose is not bureaucracy. It prevents a search result snippet, repost, provider claim, or later summary from masquerading as the original event/business record.

## 3. Source independence test

Ask whether two sources could both exist because of the same upstream record.

If yes, they are not fully independent.

Common dependency chains:

- official press release -> news syndication -> public-account repost -> search summary;
- company filing -> financial database -> company-data aggregator -> finance article;
- user video -> repost account -> screenshot -> forum discussion;
- provider marketing copy -> SEO article -> self-media repost -> search snippet.

Prefer a second source with a different data-generating mechanism.

## 4. Time triangle

For important events, seek three temporal perspectives when available:

1. **Before** — plan, permit, schedule, forecast.
2. **At the event** — opening, approval, transaction, onsite record.
3. **After** — operation, follow-up, delivery, later status.

If only `before` exists, the strongest supported claim may be `planned`, not `happened`.

For historical service channels, a similar rule applies:
- old official integration proves historical availability;
- current availability requires current evidence;
- disappearance should trigger migration/replacement search, not retroactive denial of the old fact.

## 5. Time fields are not interchangeable

Distinguish:

- event time;
- document signature date;
- publication date;
- effective date;
- statistics reference period;
- ingestion/update time;
- page last-modified date;
- repost date.

When a query asks `when did it happen?`, use event time unless the user explicitly asks for publication/effective time.

## 6. Chinese lifecycle semantics

Never collapse these without proof:

`签约 -> 立项/备案 -> 核准/审批 -> 施工许可 -> 开工 -> 封顶 -> 竣工 -> 验收 -> 试生产/试运行 -> 投产/开通 -> 量产/稳定运营 -> 达产`

Likewise:

- `预计/计划/拟/将/力争` are future or intended states;
- `首发/首件下线` may prove production began, not that design capacity was reached;
- `试运行/初期运营` may not mean the same thing as full formal operation.

Search the **state verb**, not only the project name.

## 7. Spatial / physical verification

For location-sensitive claims, choose the modality that actually observes the physical fact:

- map POI and road topology;
- official geospatial/public works information;
- recent onsite images/videos;
- weather context when it helps validate timing;
- remote sensing for large-scale visible changes.

Use remote sensing for propositions like:
- a large facility appeared;
- construction footprint expanded;
- flooding/water extent changed;
- a large road/bridge structure formed.

Do not use remote sensing alone to infer:
- legal ownership;
- corporate responsibility;
- motive;
- contract relationship;
- precise indoor operations.

## 8. Negative-evidence diagnosis

Before saying `there is no record/service/event`, test:

- was it never public?
- is it app/mini-program only?
- is login/real-name verification required?
- is it in a paid/professional database?
- was the page deleted, migrated, revised, or archived?
- was it not indexed?
- did rate limits/CAPTCHA block retrieval?
- are entity aliases/old names missing?
- is the jurisdiction or time window wrong?
- is visibility account/region dependent?
- is the official guide silent while a compatible third-party channel still exists?

Only after plausible alternatives are exhausted should `probably does not exist` become the leading interpretation.

## 9. Conflict resolution

When sources conflict, compare:

1. generation mechanism;
2. event proximity;
3. definitions;
4. scope/geography/population;
5. plan vs actual;
6. original vs repost;
7. current availability vs historical status;
8. practical compatibility vs official relationship;
9. revision/correction chronology.

A conflict can be semantic rather than factual. Example pattern:

- `全线 68.6 km`
- `首期开通 59 km`

Both can be true because scope differs.

Likewise:
- `third-party channel works`;
- `no current official source names that provider`.

These can also both be true.

## 10. Historical reconstruction

For old/deleted/migrated information:

1. look for official gazette, original PDF, formal document number;
2. search the current official site using exact title/number;
3. inspect recognized web archives when necessary;
4. search for contemporary citations to the original page;
5. record the archive timestamp separately from the original event/publication time;
6. if it was a service entry, search current platform-native surfaces and migration/change notices.

Absence from an archive never proves a page never existed.

A current missing service entry never disproves a well-supported historical official entry.

## 11. Government-domain authorship check

A claim gains authority from **who actually makes it**, not merely from the domain hosting the page.

When a provider/service name appears on a government site, distinguish:
- government-authored naming/recommendation;
- citizen-submitted question containing the name;
- reposted/quoted third-party content;
- official response that answers a different part of the question.

Only the relevant government-authored statement can establish official naming/recommendation.

## 12. Government-information request as fallback

When public evidence is insufficient and the task genuinely warrants deeper research, consider whether a lawful government-information disclosure request or formal data request could retrieve an **existing record**.

Frame requests around records that already exist, not a request for the agency to create new analysis.

Do not imply guaranteed disclosure: privacy, trade secrets, security, internal/process records, and other statutory limits may apply.

## 13. Confidence language

Use:

- **Confirmed** — direct current origin/first-party evidence.
- **Cross-verified** — independent mechanisms support the same proposition.
- **Highly likely** — strong but missing one decisive origin record.
- **Lead only** — unverified social/community/secondary clue.
- **Unknown** — evidence gap remains.

For practical channels, do not use these claim-confidence labels as substitutes for the channel relationship/usability labels in [channel-verification.md](channel-verification.md).

Never write low-confidence clues as settled facts.
