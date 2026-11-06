---
name: ux-jakobs-law
description: Jakob's Law (Laws of UX): Users spend most of their time in other products, so they expect yours to work like the ones they already know. Use to advise up front, guide building, or strictly review use of conventions and platform patterns, navigation, standard components, redesigns, migrations from legacy tools and any novel interaction pattern.
---

# Jakob's Law

**In one line:** Users spend most of their time in other products, so they expect yours to work like the ones they already know.

- **Category:** Interaction and conventions
- **Origin:** Jakob Nielsen (2000).
- **Source:** [lawsofux.com/jakobs-law](https://lawsofux.com/jakobs-law/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| JAK-1 | Blocker | interactive, code | A custom control replaces a standard one but lacks its expected keyboard or assistive-technology behaviour. |
| JAK-2 | Major | static | A core interaction deviates from platform or industry convention without a documented and tested benefit. |
| JAK-3 | Major | static | Navigation or component placement is inconsistent across screens (WCAG 3.2.3, 3.2.4). |
| JAK-4 | Major | static | An established icon is used with a different meaning. |
| JAK-5 | Minor | context | A redesign changes learned locations or behaviours with no transition support. |

Report each finding on one line:

`[SEVERITY] JAK-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Conventions can perpetuate bad patterns; deviate when the benefit is clear and you can teach it.
- Domain conventions (for example professional analysis or GIS tools) may outweigh consumer-web conventions for your users.

## Related skills

- **`ux-mental-model`** — conventions are shared mental models ([open](../ux-mental-model/SKILL.md))
- **`ux-paradox-of-the-active-user`** — users won't read how a novel pattern works ([open](../ux-paradox-of-the-active-user/SKILL.md))
- **`ux-law-of-similarity`** — consistency within your product ([open](../ux-law-of-similarity/SKILL.md))
- **`ux-cognitive-load`** — familiarity reduces effort ([open](../ux-cognitive-load/SKILL.md))
- **`ux-aesthetic-usability-effect`** — distinctive style without breaking conventions ([open](../ux-aesthetic-usability-effect/SKILL.md))
