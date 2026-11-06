---
name: ux-zeigarnik-effect
description: Zeigarnik Effect (Laws of UX): Unfinished tasks stay on people's minds, which can motivate completion — or nag. Use to advise up front, guide building, or strictly review progress indicators, profile and setup completion, drafts and saved work, resumable flows, to-do lists, badges and incomplete-state messaging.
---

# Zeigarnik Effect

**In one line:** Unfinished tasks stay on people's minds, which can motivate completion — or nag.

- **Category:** Memory and cognition
- **Origin:** Bluma Zeigarnik (1927), working with Kurt Lewin. Replications are mixed, so treat it as a tendency, not a law.
- **Source:** [lawsofux.com/zeigarnik-effect](https://lawsofux.com/zeigarnik-effect/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| ZE-1 | Major | interactive | An 'incomplete' indicator can't be dismissed and doesn't correspond to user value. |
| ZE-2 | Major | interactive | Unfinished work isn't preserved or resumable. |
| ZE-3 | Major | interactive | Badges or counters are inflated or never clear. |
| ZE-4 | Minor | static | A resume point lacks the context to continue (what was being done, what's left). |

Report each finding on one line:

`[SEVERITY] ZE-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Overuse creates anxiety and notification fatigue, which works against Flow and the Peak-End Rule.
- The evidence is weak; don't build a business case on this effect alone.

## Related skills

- **`ux-goal-gradient-effect`** — progress toward completion motivates ([open](../ux-goal-gradient-effect/SKILL.md))
- **`ux-working-memory`** — open loops occupy mental capacity ([open](../ux-working-memory/SKILL.md))
- **`ux-peak-end-rule`** — how incomplete endings colour memory ([open](../ux-peak-end-rule/SKILL.md))
- **`ux-flow`** — nagging open loops break focus ([open](../ux-flow/SKILL.md))
