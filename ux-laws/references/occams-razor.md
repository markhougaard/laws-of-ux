# Occam's Razor

**In one line:** Of two designs that work equally well, choose the one with fewer parts and fewer assumptions.

- **Category:** Decisions and complexity
- **Origin:** William of Ockham (14th century), a principle of parsimony in reasoning.
- **Source:** [lawsofux.com/occams-razor](https://lawsofux.com/occams-razor/)
- **Code:** `OCC`

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

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| OCC-1 | Major | static | An element, step or option has no identifiable user purpose. |
| OCC-2 | Major | static | Two or more paths, components or settings do essentially the same thing. |
| OCC-3 | Major | code | A new component was created where an existing one would work. |
| OCC-4 | Major | context | Simplification has removed something users need to complete a task (over-reduction). |
| OCC-5 | Minor | static | Copy is longer than needed to be clear. |

## Tensions and misuse

- Tesler's Law: some complexity is irreducible; removing it from the UI may just push it onto users.
- Aesthetic minimalism isn't the same as simplicity; a hidden necessity is a cost, not a saving.

## Related laws

- **`teslers-law`** — the limit of simplification (`references/teslers-law.md`)
- **`law-of-pragnanz`** — simplicity in visual form (`references/law-of-pragnanz.md`)
- **`pareto-principle`** — focus on the parts that matter most (`references/pareto-principle.md`)
- **`cognitive-load`** — every element costs attention (`references/cognitive-load.md`)
- **`hicks-law`** — fewer options decide faster (`references/hicks-law.md`)
