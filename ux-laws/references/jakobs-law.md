# Jakob's Law

**In one line:** Users spend most of their time in other products, so they expect yours to work like the ones they already know.

- **Category:** Interaction and conventions
- **Origin:** Jakob Nielsen (2000).
- **Source:** [lawsofux.com/jakobs-law](https://lawsofux.com/jakobs-law/)
- **Code:** `JAK`

## The principle

People carry expectations from every other app and site they use. Conventions — where navigation lives, how a cart works, what a hamburger or a gear icon means, how forms behave — let users transfer what they know and act without thinking. Breaking conventions makes people relearn, and the cost lands on every user every time. Innovation is welcome where it creates real value, not where it just looks different. Redesigns deserve the same care: your existing users' expectations are now a convention too.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which products and platforms do our users spend most time in, and what conventions do they set?
- Where are we planning to deviate from convention, and what's the measurable benefit?
- For redesigns or migrations: what do current users rely on, and how will we transition them?

Steer the work toward:

- Default to platform and industry conventions; innovate on the problem, not the controls.
- Require a stated benefit for any deviation and test it.
- Plan transitions for redesigns (preview, opt-in period, what changed).

## Mode 2 — Build (while designing or implementing)

- Follow platform guidelines (Apple HIG, Material, Fluent, web conventions) for core controls and navigation.
- Use standard placements: logo top-left links home, search top or top-right, account top-right, primary navigation consistent across pages.
- Use native or standard components before custom ones; custom ones must match native keyboard and screen-reader behaviour.
- Keep navigation consistent across pages (WCAG 3.2.3) and identify the same functions consistently (WCAG 3.2.4).
- Use familiar icons with labels; don't redefine established icons.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| JAK-1 | Blocker | interactive, code | A custom control replaces a standard one but lacks its expected keyboard or assistive-technology behaviour. |
| JAK-2 | Major | static | A core interaction deviates from platform or industry convention without a documented and tested benefit. |
| JAK-3 | Major | static | Navigation or component placement is inconsistent across screens (WCAG 3.2.3, 3.2.4). |
| JAK-4 | Major | static | An established icon is used with a different meaning. |
| JAK-5 | Minor | context | A redesign changes learned locations or behaviours with no transition support. |

## Tensions and misuse

- Conventions can perpetuate bad patterns; deviate when the benefit is clear and you can teach it.
- Domain conventions (for example professional analysis or GIS tools) may outweigh consumer-web conventions for your users.

## Related laws

- **`mental-model`** — conventions are shared mental models (`references/mental-model.md`)
- **`paradox-of-the-active-user`** — users won't read how a novel pattern works (`references/paradox-of-the-active-user.md`)
- **`law-of-similarity`** — consistency within your product (`references/law-of-similarity.md`)
- **`cognitive-load`** — familiarity reduces effort (`references/cognitive-load.md`)
- **`aesthetic-usability-effect`** — distinctive style without breaking conventions (`references/aesthetic-usability-effect.md`)
