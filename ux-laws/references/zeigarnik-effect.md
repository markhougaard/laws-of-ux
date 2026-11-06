# Zeigarnik Effect

**In one line:** Unfinished tasks stay on people's minds, which can motivate completion — or nag.

- **Category:** Memory and cognition
- **Origin:** Bluma Zeigarnik (1927), working with Kurt Lewin. Replications are mixed, so treat it as a tendency, not a law.
- **Source:** [lawsofux.com/zeigarnik-effect](https://lawsofux.com/zeigarnik-effect/)
- **Code:** `ZE`

## The principle

An open loop tends to stay active in memory and create a mild pull toward closing it. Products use this with visible progress, setup checklists and saved drafts. Used well, it helps people pick up where they left off. Used badly, it manufactures obligation: endless badges, unclosable checklists and 'your profile is 80% complete' nags that serve the product rather than the user. The effect is modest and inconsistently replicated, so it's a design consideration rather than a guaranteed lever.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which tasks will users realistically leave unfinished and come back to?
- Is completion of the 'incomplete' thing actually valuable to the user, or only to us?
- How will users dismiss or close a loop they don't want to finish?

Steer the work toward:

- Make resumption easy and indicators honest.
- Only create open loops for tasks that benefit the user.

## Mode 2 — Build (while designing or implementing)

- Save drafts automatically and show 'continue where you left off' with enough context to resume.
- Setup checklists: show progress, and let users dismiss or permanently hide them.
- Badge counts must reflect real, actionable items and clear when handled.
- Show what remains, not only what's done.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| ZE-1 | Major | interactive | An 'incomplete' indicator can't be dismissed and doesn't correspond to user value. |
| ZE-2 | Major | interactive | Unfinished work isn't preserved or resumable. |
| ZE-3 | Major | interactive | Badges or counters are inflated or never clear. |
| ZE-4 | Minor | static | A resume point lacks the context to continue (what was being done, what's left). |

## Tensions and misuse

- Overuse creates anxiety and notification fatigue, which works against Flow and the Peak-End Rule.
- The evidence is weak; don't build a business case on this effect alone.

## Related laws

- **`goal-gradient-effect`** — progress toward completion motivates ([open](goal-gradient-effect.md))
- **`working-memory`** — open loops occupy mental capacity ([open](working-memory.md))
- **`peak-end-rule`** — how incomplete endings colour memory ([open](peak-end-rule.md))
- **`flow`** — nagging open loops break focus ([open](flow.md))
