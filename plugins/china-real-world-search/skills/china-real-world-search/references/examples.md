# Execution Examples

These examples demonstrate method. Never reuse their factual details without fresh verification.

## Example 1: Photo-receipt search must produce named candidates

User asks where to obtain a digital photo receipt required for a travel document and says online mini programs may exist.

Correct pattern:
1. Verify the current requirement and preserve the competent authority's **exact official artifact name**.
2. Search the artifact/outcome directly, not only the surrounding task:
   - exact artifact name + `在线`;
   - exact artifact name + `小程序`;
   - locality + artifact + current year;
   - WeChat/Alipay/platform-native search where available.
3. Extract **specific mini-program/provider names** even from weak SEO/provider/community pages.
4. If multiple options plausibly exist, form a small named candidate set (normally 2-3) before ranking.
5. For each serious candidate, separately verify:
   - current usability;
   - provider/operator identity;
   - generation vs actual target-process acceptance;
   - official relationship.
6. If an older government notice shows an official platform previously exposed the service, treat that as historical evidence and search for migration/replacement/current state.
7. Recommend a concrete current option plus a low-ambiguity fallback when useful.

Failure modes:
- answering only `微信/支付宝有第三方服务` without naming any current candidate;
- answering only `去有资质的照相馆` when online/self-service front ends may exist;
- calling a working third-party `officially designated` without evidence;
- using an old official integration notice as proof of current availability;
- changing the official artifact name from `采集回执` to `检测回执` (or vice versa) without evidence.

## Example 2: Backend system requirement does not define the user-facing provider

A source says a photo/data artifact must be uploaded to or pass backend system X.

Correct reasoning:
1. Record the backend acceptance requirement exactly.
2. Ask what user-facing channels can satisfy it today.
3. Search official platform, third-party mini program, self-service device, counter, and traditional provider paths as appropriate.
4. Only say `must use provider type Y` if a competent source explicitly restricts the user-facing channel.

Failure to avoid:

`必须进入检测系统` -> `所以必须去照相馆`

The second proposition does not follow from the first by itself.

## Example 3: Current third-party channel vs historical official platform

Search finds:
- one or more current third-party mini programs that claim to generate a required artifact;
- an older government notice showing that an official government platform previously exposed an online service;
- the old official entry is no longer visible today.

Pattern:
1. Keep current third-party candidates in the search space even if they are not officially named.
2. Classify separately:
   - current usability;
   - operator/issuer identity;
   - compatibility/acceptance evidence;
   - official relationship.
3. Treat the old government notice as proof of **historical official integration only** unless current availability is independently verified.
4. Search for migration, replacement, withdrawal, or new official entry points.
5. If the user personally reports successful use of a current mini program, accept that as scoped evidence and research the remaining uncertainty instead.

Failure modes:
- ignoring the current third-party channel because it is non-official;
- calling the third-party `officially designated` because it works;
- claiming the historical official platform still works because an old government article exists;
- claiming the historical platform never offered the service because the current entry disappeared;
- assuming `not listed by government today` means `cannot be accepted`.

## Example 4: Local government document / requirement

User asks whether a particular document or receipt is required.

Pattern:
1. Convert to exact claim: document type, first-time/renewal, locality, current date.
2. Find the competent authority defining the requirement.
3. Preserve the exact official title/wording.
4. Verify provincial/city implementation where local execution matters.
5. Separate `what is required` from `how the user can satisfy it`.
6. Only then compare current channels, costs, and convenience.

Failure to avoid: letting a service provider's marketing page define the statutory requirement.

## Example 5: Neighborhood -> major rail station

Pattern:
1. Resolve exact origin and destination POIs.
2. Use current route/transit systems.
3. Compare plausible multimodal options: taxi to strategic hub, bus+metro, intercity rail, direct taxi.
4. Check first/last service or disruptions when time-sensitive.
5. Rank by total burden, not only in-vehicle time.
6. Recommend one route and a fallback.

Failure to avoid: expensive end-to-end taxi as the automatic default.

## Example 6: Train trip with no direct seats

Pattern:
1. Query authoritative railway inventory for the date.
2. If direct seats are unavailable, discover official-transfer or alternative-hub options.
3. Compare fare, transfer buffer, station change, arrival time, and availability risk.
4. Verify final seats in the authoritative system before calling the itinerary `available`.

Failure to avoid: treating an aggregator's cached itinerary as proof of live availability.

## Example 7: Hospital registration

Pattern:
1. Identify exact hospital and campus.
2. Broadly discover **named** current registration channels: official account/mini program, local health platform, Alipay/WeChat entry, or third-party integration.
3. Verify which channel the hospital currently names or integrates when possible.
4. Verify department, opening rules, identity/payment requirements.
5. Use map data for the correct campus/entrance.
6. Use community content for queueing/navigation and practical experience.

Failure to avoid: saying only `use the hospital's WeChat/mini program` when multiple named channels are discoverable, or assuming a third-party registration tool is hospital-operated merely because booking succeeds.

## Example 8: Known mini program not visible on open web

Pattern:
1. Treat the user's claim as a discovery lead.
2. Search the exact platform name + institution/service on official pages and platform-native search.
3. Verify operator/主体 when possible.
4. If an official source documents the mini program but the current in-app screen is inaccessible, report:
   - channel existence: verified/credibly documented;
   - official relationship: state only what the source proves;
   - current menu/slot state: not directly inspected.
5. If the user says the mini program currently opens, accept that as scoped current evidence instead of concluding the channel does not exist.

Failure to avoid: `web search cannot find it, therefore it does not exist`.

## Example 9: Provider name appears on a government page

User finds a `.gov.cn` page containing the name of a third-party service and asks whether this proves official recognition.

Pattern:
1. Read the exact passage carrying the provider name.
2. Determine authorship/context:
   - government-authored recommendation/listing;
   - citizen question;
   - reposted content;
   - incidental mention.
3. Read the official response itself and identify what proposition it actually answers.
4. Do not infer endorsement from government-domain hosting alone.
5. Search for an independent current official source that explicitly names/recommends the provider if official status matters.

Failure to avoid: `provider name on government website = officially designated provider`.

## Example 10: Local restaurant / place recommendation

Pattern:
1. Build a geographically coherent **named** candidate set with map/local-business data.
2. Check branch identity, hours, distance, and price level.
3. Read recent independent reviews when the choice is subjective.
4. Account for actual visit time and transport.
5. Recommend a small shortlist with clear tradeoffs.

## Example 11: Did a factory/project actually start operating?

User asks whether Project X `has already gone into production`.

Pattern:
1. Rewrite as: `Entity X + commercial production state + place Y + date T`.
2. Search lifecycle states separately: filing -> permits -> construction -> completion -> trial production -> production -> deliveries/capacity.
3. Reject old `预计/计划投产` articles as proof of actual production.
4. Find the closest origin record for actual production: company filing/announcement or responsible local authority.
5. Add an independently generated reality trace when useful: recruitment/logistics/onsite/physical observation.
6. State exactly what milestone is confirmed and what remains unproven.

Failure to avoid: project-name search returning an old forecast that looks like a completed fact.

## Example 12: Conflicting railway/metro opening-length figures

Pattern:
1. Separate `full planned line` from `initial operating section`.
2. Find official opening date and initial operational scope.
3. Find operator timetable/fare/current-service evidence.
4. Treat different km/station counts as potentially different scopes before calling them contradictory.

Failure to avoid: choosing one number by majority vote.

## Example 13: Physical event / disaster verification

Pattern:
1. Use official event records for timing and administrative status.
2. Add independent physical evidence such as remote sensing, map change, or onsite imagery.
3. Use the physical evidence only for what it directly observes.
4. Do not infer cause, legal liability, or ownership from imagery alone.

## Example 14: Historical webpage or deleted notice

Pattern:
1. Search exact title/document number on the official site and gazette.
2. Find original PDF or contemporary references.
3. Use recognized web archives when current URLs fail.
4. Separate original publication/event time from archive-capture time.
5. For an old service entry, separately test current availability/migration.
6. Never conclude `never existed` solely because an archive has no copy or the current page is gone.
