# Execution Examples

These examples demonstrate method. Never reuse their factual details without fresh verification.

## Example 1: Local government document / photo receipt

User asks where to get a photo receipt required for a travel document.

Pattern:
1. Convert to exact claim: which document, first-time/renewal, locality, current date.
2. Find the authority that defines the photo requirement.
3. Verify provincial/city implementation.
4. Discover the actual mobile/service channel (政务平台, WeChat/Alipay, service hall, compliant photo service).
5. Use maps/local platforms only after the requirement is known.
6. Distinguish `required by rule` from `convenient way to obtain it`.

Failure to avoid: “must go to a photo studio” when online/self-service paths may exist.

## Example 2: Neighborhood -> major rail station

Pattern:
1. Resolve exact origin and destination POIs.
2. Use current route/transit systems.
3. Compare plausible multimodal options: taxi to strategic hub, bus+metro, intercity rail, direct taxi.
4. Check first/last service or disruptions when time-sensitive.
5. Rank by total burden, not only in-vehicle time.
6. Recommend one route and a fallback.

Failure to avoid: expensive end-to-end taxi as the automatic default.

## Example 3: Train trip with no direct seats

Pattern:
1. Query authoritative railway inventory for the date.
2. If direct seats are unavailable, discover official-transfer or alternative-hub options.
3. Compare fare, transfer buffer, station change, arrival time, and availability risk.
4. Verify final seats in the authoritative system before calling the itinerary “available.”

Failure to avoid: treating an aggregator's cached itinerary as proof of live availability.

## Example 4: Hospital registration

Pattern:
1. Identify exact hospital and campus.
2. Find the hospital's official site/account/mini program and integrated health platform.
3. Verify department, opening rules, identity/payment requirements.
4. Use map data for the correct campus/entrance.
5. Use community content only for queueing, navigation, and practical experience.

## Example 5: Known mini program not visible on open web

Pattern:
1. Treat the user's claim as a discovery lead.
2. Search `platform name + institution + service` in official notices and native platform search.
3. If an official source documents the mini program but the current in-app screen is inaccessible, report:
   - channel existence: verified/credibly documented;
   - current menu/slot state: not directly inspected.
4. Give exact documented search terms/path only when supported.

Failure to avoid: “web search cannot find it, therefore it does not exist.”

## Example 6: Local restaurant / place recommendation

Pattern:
1. Build a geographically coherent candidate set with map/local-business data.
2. Check branch identity, hours, distance, and price level.
3. Read recent independent reviews when the choice is subjective.
4. Account for actual visit time and transport.
5. Recommend a small shortlist with clear tradeoffs.

## Example 7: Did a factory/project actually start operating?

User asks whether Project X “has already gone into production.”

Pattern:
1. Rewrite as: `Entity X + commercial production state + place Y + date T`.
2. Search lifecycle states separately: filing -> permits -> construction -> completion -> trial production -> production -> deliveries/capacity.
3. Reject old `预计/计划投产` articles as proof of actual production.
4. Find the closest origin record for actual production: company filing/announcement or responsible local authority.
5. Add an independently generated reality trace when useful: recruitment/logistics/onsite/physical observation.
6. State exactly what milestone is confirmed and what remains unproven.

Failure to avoid: project-name search returning an old forecast that looks like a completed fact.

## Example 8: Conflicting railway/metro opening-length figures

Pattern:
1. Separate `full planned line` from `initial operating section`.
2. Find official opening date and initial operational scope.
3. Find operator timetable/fare/current-service evidence.
4. Treat different km/station counts as potentially different scopes before calling them contradictory.

Failure to avoid: choosing one number by majority vote.

## Example 9: Physical event / disaster verification

Pattern:
1. Use official event records for timing and administrative status.
2. Add independent physical evidence such as remote sensing, map change, or onsite imagery.
3. Use the physical evidence only for what it directly observes.
4. Do not infer cause, legal liability, or ownership from imagery alone.

## Example 10: Historical webpage or deleted notice

Pattern:
1. Search exact title/document number on the official site and gazette.
2. Find original PDF or contemporary references.
3. Use recognized web archives when current URLs fail.
4. Separate original publication/event time from archive-capture time.
5. Never conclude “never existed” solely because an archive has no copy.
