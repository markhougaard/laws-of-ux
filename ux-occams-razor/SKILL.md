---
name: ux-occams-razor
description: Occam's Razor (Laws of UX): Of two designs that work equally well, choose the one with fewer parts and fewer assumptions. Use to advise up front, guide building, or strictly review scope decisions, feature creep, design simplification, solution choice, and any element whose purpose is unclear.
---

# Occam's Razor

**In one line:** Of two designs that work equally well, choose the one with fewer parts and fewer assumptions.

- **Category:** Decisions and complexity
- **Origin:** William of Ockham (14th century), a principle of parsimony in reasoning.
- **Source:** [lawsofux.com/occams-razor](https://lawsofux.com/occams-razor/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Every element, option, step and concept carries a cost — to build, maintain, learn and look past. When two solutions meet the need equally well, the simpler one is better. In design this works as a discipline: remove elements one by one and keep only those whose absence would hurt. The key qualifier is 'equally well': simplicity that drops necessary capability is not parsimony, it's loss.

## Mode 1 — Advise (before design)

Raise these with the team:

- What is the smallest solution that fully solves the user's problem?
- Which planned features, settings or steps are hedges against hypothetical needs?
- What assumptions does each proposed solution depend on, and which has the fewest?

Steer the work toward:

- Start from the minimum and add only on evidence.
- Prefer one flexible pattern over several special cases.
- Kill options that exist only because nobody decided.

## Mode 2 — Build (while designing or implementing)

- For each element ask: what breaks if this is removed? If nothing, remove it.
- Combine duplicate paths to the same result.
- Prefer existing components to new ones.
- Remove settings by making a good decision for the user.
- Write the simplest copy that's still specific.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| OCC-1 | Major | An element, step or option has no identifiable user purpose. |
| OCC-2 | Major | Two or more paths, components or settings do essentially the same thing. |
| OCC-3 | Major | A new component was created where an existing one would work. |
| OCC-4 | Major | Simplification has removed something users need to complete a task (over-reduction). |
| OCC-5 | Minor | Copy is longer than needed to be clear. |

Report each finding on one line:

`[SEVERITY] OCC-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Tesler's Law: some complexity is irreducible; removing it from the UI may just push it onto users.
- Aesthetic minimalism isn't the same as simplicity; a hidden necessity is a cost, not a saving.

## Related skills

- **`ux-teslers-law`** — the limit of simplification ([open](../ux-teslers-law/SKILL.md))
- **`ux-law-of-pragnanz`** — simplicity in visual form ([open](../ux-law-of-pragnanz/SKILL.md))
- **`ux-pareto-principle`** — focus on the parts that matter most ([open](../ux-pareto-principle/SKILL.md))
- **`ux-cognitive-load`** — every element costs attention ([open](../ux-cognitive-load/SKILL.md))
- **`ux-hicks-law`** — fewer options decide faster ([open](../ux-hicks-law/SKILL.md))
