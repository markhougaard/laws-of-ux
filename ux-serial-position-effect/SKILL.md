---
name: ux-serial-position-effect
description: Serial Position Effect (Laws of UX): People remember and notice the first and last items in a sequence best; the middle gets lost. Use to advise up front, guide building, or strictly review navigation order, list and menu ordering, tab bars, onboarding sequences, presentation of options, and long content.
---

# Serial Position Effect

**In one line:** People remember and notice the first and last items in a sequence best; the middle gets lost.

- **Category:** Memory and cognition
- **Origin:** Hermann Ebbinghaus (1885); primacy and recency described by Bennet Murdock (1962).
- **Source:** [lawsofux.com/serial-position-effect](https://lawsofux.com/serial-position-effect/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

In a list or sequence, items at the start benefit from primacy (more attention, better encoding) and items at the end from recency (still fresh in memory). The middle is weakest. In interfaces this shows up in navigation bars, option lists, search results and onboarding: put what matters most at the ends and expect the middle to be skimmed. It's also an influence lever, which means order is never neutral.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which items in each list, menu or sequence matter most to users?
- Which items are we putting first or last for business reasons, and is that honest?
- Are there long sequences (onboarding, tours, forms) where the middle would be lost?

Steer the work toward:

- Order navigation by importance and frequency, with key items at the ends.
- Keep sequences users must remember short.

## Mode 2 — Build (while designing or implementing)

- Bottom tab bars and top navigation: most important destinations at the start; a strong, distinct destination (or account/settings) at the end.
- In onboarding, open and close with the most important message.
- Put the most important information at the start and end of long pages and emails.
- Present the key point of an error or confirmation first.
- Keep the position of navigation items stable — reordering destroys learned positions.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| SPE-1 | Major | The most important item in a list or navigation is buried in the middle. |
| SPE-2 | Major | Item order changes between sessions or screens without user control (except deliberate, explained personalisation). |
| SPE-3 | Major | Order is used to push an option against user interest without a clear label. |
| SPE-4 | Minor | A long sequence users must remember has no summary at the end. |

Report each finding on one line:

`[SEVERITY] SPE-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Alphabetical or chronological ordering may beat importance where users look up known items.
- Ordering is a bias lever; see Cognitive Bias for the ethics.

## Related skills

- **`ux-von-restorff-effect`** — the other way to make an item memorable ([open](../ux-von-restorff-effect/SKILL.md))
- **`ux-working-memory`** — why the middle fades ([open](../ux-working-memory/SKILL.md))
- **`ux-peak-end-rule`** — the experiential version of primacy and recency ([open](../ux-peak-end-rule/SKILL.md))
- **`ux-cognitive-bias`** — order effects as influence ([open](../ux-cognitive-bias/SKILL.md))
- **`ux-jakobs-law`** — conventional positions for common items ([open](../ux-jakobs-law/SKILL.md))
