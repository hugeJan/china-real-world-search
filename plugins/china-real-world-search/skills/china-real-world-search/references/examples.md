# Execution Examples

These examples define routing and method. Never reuse their factual details without fresh verification.

## 1. Government service: activate

User asks:

`我在东莞，非本地户籍，第一次办理往来港澳通行证，需要什么材料，哪个点能办？`

Correct:

1. The provider and task gates pass.
2. Verify the competent rule and exact service-item/document names.
3. Check the current local implementation, appointment channel, service point, hours, and jurisdiction.
4. Recommend one practical path with a fallback only when useful.

## 2. SOE name plus device modification: do not activate

User asks:

`中国移动定制版手机能不能刷机、解锁 Bootloader？`

Correct:

- Do not activate this Skill.
- The entity may be state-owned, but the requested task is device modification.
- Use ordinary technical/device research instead.

Failure:

- treating `中国移动`, `官方`, or `国内实际还能不能` as sufficient activation signals.

## 3. State-owned telecom service: activate

User asks:

`中国移动异地补卡需要什么材料，东莞大岭山哪里能办？`

Correct:

- Verify current identity/material requirements.
- Identify a concrete branch/channel and whether it handles the requested service.
- Check hours and locality.
- Do not drift into handset, firmware, or Root research.

## 4. State-bank service vs investment

In scope:

`某国有银行换社保卡需要什么材料，周末哪个网点能办？`

Out of scope:

`某国有银行哪款理财收益最高？`

The provider name is the same. The requested task determines routing.

## 5. Public-transport route: activate

User asks:

`周一从凯里南站去东莞大岭山，给我两条费用合理、少绕路的公共交通路线。`

Correct:

1. Resolve date, origin, and destination.
2. Use railway, metro, bus, station, and map evidence according to actual host capability.
3. Compare total journey burden, transfers, walking, fare, and availability risk.
4. Do not claim live 12306 inventory without direct access.

## 6. Ordinary private-place route: do not activate

User asks:

`开车去朋友家怎么走？`

With no public-transport or public-service dependency, do not activate this Skill merely because the route is in China.

## 7. Mixed technology and public service

User asks:

`刷机后电子社保卡打不开，怎么办？`

Correct:

- Use the Skill only to verify official electronic-social-security-card login/recovery, identity verification, or service-counter paths.
- Do not research flashing, Root, bypassing security controls, or ROM installation under this Skill.
- Ask one concise clarification if the user's actual objective cannot be separated.

## 8. Historical official channel

User finds a 2023 government notice showing Platform A offered a service, but the entry is missing now.

Correct:

- Treat the old notice as historical official evidence.
- Search for current migration, replacement, suspension, or new entry.
- Do not claim either `still available` or `never existed` without current evidence.

## 9. Public institution channel

User asks how to register at a public hospital.

Correct:

- Verify exact hospital/campus and current official registration route.
- Discover named channels when accessible.
- Verify department/opening rules without making a test booking.
- Use maps for campus/entrance, not as authority for medical or administrative rules.

A private clinic recommendation alone is not enough to activate this Skill.

## 10. Utility service

User asks:

`租房后怎么把国家电网户号过户到自己名下？`

Correct:

- Verify whether transfer is supported, required materials, account/property prerequisites, current app/counter channel, fee, and local service rule.
- Separate the formal rule from the current executable channel.

## 11. Third-party channel

A third-party mini program claims it can generate an official required receipt.

Correct:

- Keep it as a candidate for an already in-scope government service.
- Verify current usability, operator identity, target-process compatibility, and official relationship separately.
- Provider self-claims do not prove official designation.
- Do not create a paid test transaction merely to verify it.

## 12. Capability limitation

The ideal source is WeChat, Alipay, 12306, an operator app, or a map app, but the host cannot directly inspect it.

Correct:

- Use accessible official/web/secondary evidence.
- State that live in-app state was not directly inspected.
- Never fabricate menus, slots, inventory, or current app status.
