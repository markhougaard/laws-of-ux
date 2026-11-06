# Serial Position Effect

**In one line:** People remember and notice the first and last items in a sequence best; the middle gets lost.

- **Category:** Memory and cognition
- **Origin:** Hermann Ebbinghaus (1885); primacy and recency described by Bennet Murdock (1962).
- **Source:** [lawsofux.com/serial-position-effect](https://lawsofux.com/serial-position-effect/)
- **Code:** `SPE`

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

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| SPE-1 | Major | static | The most important item in a list or navigation is buried in the middle. |
| SPE-2 | Major | interactive | Item order changes between sessions or screens without user control (except deliberate, explained personalisation). |
| SPE-3 | Major | static | Order is used to push an option against user interest without a clear label. |
| SPE-4 | Minor | static | A long sequence users must remember has no summary at the end. |

## Tensions and misuse

- Alphabetical or chronological ordering may beat importance where users look up known items.
- Ordering is a bias lever; see Cognitive Bias for the ethics.

## Related laws

- **`von-restorff-effect`** — the other way to make an item memorable ([open](von-restorff-effect.md))
- **`working-memory`** — why the middle fades ([open](working-memory.md))
- **`peak-end-rule`** — the experiential version of primacy and recency ([open](peak-end-rule.md))
- **`cognitive-bias`** — order effects as influence ([open](cognitive-bias.md))
- **`jakobs-law`** — conventional positions for common items ([open](jakobs-law.md))
