# Paradox of the Active User

**In one line:** Users skip manuals and tutorials and start using the product right away, even when learning first would save them time.

- **Category:** Interaction and conventions
- **Origin:** John Carroll and Mary Beth Rosson (1987).
- **Source:** [lawsofux.com/paradox-of-the-active-user](https://lawsofux.com/paradox-of-the-active-user/)
- **Code:** `PAU`

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

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| PAU-1 | Blocker | interactive | A core task can't be completed without reading external documentation or completing a tutorial. |
| PAU-2 | Major | interactive | Onboarding is mandatory, long or unskippable. |
| PAU-3 | Major | interactive | Exploration is risky: actions are irreversible with no undo or preview. |
| PAU-4 | Major | static, context | Important capabilities are discoverable only through documentation. |
| PAU-5 | Minor | static | Empty states are blank or say only 'no data'. |

## Tensions and misuse

- Some domains (safety-critical, regulated) legitimately require training; design should still not rely on it for basic operation.
- Contextual hints can become noise; limit and dismiss permanently once used.

## Related laws

- **`jakobs-law`** — familiar patterns need no teaching ([open](jakobs-law.md))
- **`mental-model`** — users learn the model by doing ([open](mental-model.md))
- **`selective-attention`** — why instructions get skipped ([open](selective-attention.md))
- **`flow`** — tutorials interrupt the task users came for ([open](flow.md))
- **`cognitive-load`** — learning competes with doing ([open](cognitive-load.md))
