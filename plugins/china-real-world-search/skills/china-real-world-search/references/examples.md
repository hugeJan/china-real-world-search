# Execution Examples

These examples demonstrate method. Never reuse their factual details without fresh verification.

## Example 1: Current third-party channel vs historical official platform

User asks where to obtain a digital photo receipt required for a travel document.

Search finds:
- one or more current third-party mini programs that claim to generate the receipt;
- an older government notice showing that an official government platform previously exposed an online photo/receipt service;
- the old official entry is no longer visible today.

Pattern:
1. Verify the current statutory/administrative photo requirement with the competent authority.
2. Run broad current-channel discovery without restricting the first pass to government domains.
3. Keep current third-party candidates in the search space even if they are not officially named.
4. For each serious candidate, classify separately:
   - current usability;
   - operator/issuer identity;
   - compatibility evidence;
   - official relationship.
5. Treat the old government notice as proof of **historical official integration only** unless current availability is independently verified.
6. Search for migration, replacement, withdrawal, or new official entry points.
7. If the user personally reports successful use of a current mini program, accept that as scoped evidence of current usability and spend research effort on the remaining uncertainty instead.
8. Recommend the most practical option while accurately labeling its status; offer an official counter/self-operated path as fallback if minimum ambiguity matters.

Failure modes to avoid:
- ignoring the current third-party channel because it is non-official;
- calling the third-party `officially designated` because it works;
- claiming the historical official platform still works because an old government article exists;
- claiming the historical platform never offered the service because the current entry disappeared;
- assuming `not listed by government today` means `cannot be accepted`.

## Example 2: Local government document / photo requirement

User asks whether a particular document or receipt is required.

Pattern:
1. Convert to exact claim: document type, first-time/renewal, locality, current date.
2. Find the competent authority defining the requirement.
3. Verify provincial/city implementation where local execution matters.
4. Separate `what is required` from `how the user can satisfy it`.
5. Only then compare current channels, costs, and convenience.

Failure to avoid: letting a service provider's marketing page define the statutory requirement.

## Example 3: Neighborhood -> major rail station

Pattern:
1. Resolve exact origin and destination POIs.
2. Use current route/transit systems.
3. Compare plausible multimodal options: taxi to strategic hub, bus+metro, intercity rail, direct taxi.
4. Check first/last service or disruptions when time-sensitive.
5. Rank by total burden, not only in-vehicle time.
6. Recommend one route and a fallback.

Failure to avoid: expensive end-to-end taxi as the automatic default.

## Example 4: Train trip with no direct seats

Pattern:
1. Query authoritative railway inventory for the date.
2. If direct seats are unavailable, discover official-transfer or alternative-hub options.
3. Compare fare, transfer buffer, station change, arrival time, and availability risk.
4. Verify final seats in the authoritative system before calling the itinerary `available`.

Failure to avoid: treating an aggregator's cached itinerary as proof of live availability.

## Example 5: Hospital registration

Pattern:
1. Identify exact hospital and campus.
2. Broadly discover current registration channels: official account/mini program, local health platform, Alipay/WeChat entry, or third-party integration.
3. Verify which channel the hospital currently names or integrates when possible.
4. Verify department, opening rules, identity/payment requirements.
5. Use map data for the correct campus/entrance.
6. Use community content for queueing/navigation and practical experience.

Failure to avoid: assuming a third-party registration mini program is hospital-operated merely because it successfully books appointments.

## Example 6: Known mini program not visible on open web

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

## Example 7: Provider name appears on a government page

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

## Example 8: Local restaurant / place recommendation

Pattern:
1. Build a geographically coherent candidate set with map/local-business data.
2. Check branch identity, hours, distance, and price level.
3. Read recent independent reviews when the choice is subjective.
4. Account for actual visit time and transport.
5. Recommend a small shortlist with clear tradeoffs.

## Example 9: Did a factory/project actually start operating?

User asks whether Project X `has already gone into production`.

Pattern:
1. Rewrite as: `Entity X + commercial production state + place Y + date T`.
2. Search lifecycle states separately: filing -> permits -> construction -> completion -> trial production -> production -> deliveries/capacity.
3. Reject old `预计/计划投产` articles as proof of actual production.
4. Find the closest origin record for actual production: company filing/announcement or responsible local authority.
5. Add an independently generated reality trace when useful: recruitment/logistics/onsite/physical observation.
6. State exactly what milestone is confirmed and what remains unproven.

Failure to avoid: project-name search returning an old forecast that looks like a completed fact.

## Example 10: Conflicting railway/metro opening-length figures

Pattern:
1. Separate `full planned line` from `initial operating section`.
2. Find official opening date and initial operational scope.
3. Find operator timetable/fare/current-service evidence.
4. Treat different km/station counts as potentially different scopes before calling them contradictory.

Failure to avoid: choosing one number by majority vote.

## Example 11: Physical event / disaster verification

Pattern:
1. Use official event records for timing and administrative status.
2. Add independent physical evidence such as remote sensing, map change, or onsite imagery.
3. Use the physical evidence only for what it directly observes.
4. Do not infer cause, legal liability, or ownership from imagery alone.

## Example 12: Historical webpage or deleted notice

Pattern:
1. Search exact title/document number on the official site and gazette.
2. Find original PDF or contemporary references.
3. Use recognized web archives when current URLs fail.
4. Separate original publication/event time from archive-capture time.
5. For an old service entry, separately test current availability/migration.
6. Never conclude `never existed` solely because an archive has no copy or the current page is gone.
