---
name: ux-paradox-of-the-active-user
description: Paradox of the Active User (Laws of UX): Users skip manuals and tutorials and start using the product right away, even when learning first would save them time. Use to advise up front, guide building, or strictly review onboarding, tutorials, help and documentation, first-run experience, discoverability of advanced features and in-product guidance.
---

# Paradox of the Active User

**In one line:** Users skip manuals and tutorials and start using the product right away, even when learning first would save them time.

- **Category:** Interaction and conventions
- **Origin:** John Carroll and Mary Beth Rosson (1987).
- **Source:** [lawsofux.com/paradox-of-the-active-user](https://lawsofux.com/paradox-of-the-active-user/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

People are motivated to get their task done, not to learn the tool. They start immediately, learn by trial and error, and stay with the methods they discover first, even when better ones exist. It's a paradox because investing a little in learning would pay off — but they won't do it. Design has to teach in context, at the moment of need, and make good methods discoverable through use rather than through documentation.

## Mode 1 — Advise (before design)

Raise these with the team:

- What must a new user be able to do without any instruction?
- Which powerful features would users never discover by just using the product?
- Are we planning onboarding tours as a substitute for a clear interface?
- How will we learn which workarounds users settle into?

Steer the work toward:

- Make the core path self-explanatory before adding any onboarding.
- Teach advanced features in context, when users would benefit.
- Treat the need for a tutorial as a design smell to investigate.

## Mode 2 — Build (while designing or implementing)

- Empty states explain what goes here and offer the first action.
- Use inline hints and contextual tips triggered by behaviour, not front-loaded tours.
- Make tours skippable, short and replayable from help.
- Reveal shortcuts in context (show the keyboard shortcut in menus and tooltips).
- Provide safe exploration: undo, drafts, previews, non-destructive defaults.
- Keep help searchable and linked from where the question arises.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| PAU-1 | Blocker | A core task can't be completed without reading external documentation or completing a tutorial. |
| PAU-2 | Major | Onboarding is mandatory, long or unskippable. |
| PAU-3 | Major | Exploration is risky: actions are irreversible with no undo or preview. |
| PAU-4 | Major | Important capabilities are discoverable only through documentation. |
| PAU-5 | Minor | Empty states are blank or say only 'no data'. |

Report each finding on one line:

`[SEVERITY] PAU-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Some domains (safety-critical, regulated) legitimately require training; design should still not rely on it for basic operation.
- Contextual hints can become noise; limit and dismiss permanently once used.

## Related skills

- **`ux-jakobs-law`** — familiar patterns need no teaching ([open](../ux-jakobs-law/SKILL.md))
- **`ux-mental-model`** — users learn the model by doing ([open](../ux-mental-model/SKILL.md))
- **`ux-selective-attention`** — why instructions get skipped ([open](../ux-selective-attention/SKILL.md))
- **`ux-flow`** — tutorials interrupt the task users came for ([open](../ux-flow/SKILL.md))
- **`ux-cognitive-load`** — learning competes with doing ([open](../ux-cognitive-load/SKILL.md))
