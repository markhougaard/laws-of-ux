# Miller's Law

**In one line:** Short-term memory holds only a handful of items, so organise information into manageable chunks — don't use '7' as a hard rule.

- **Category:** Memory and cognition
- **Origin:** George A. Miller (1956), 'The Magical Number Seven, Plus or Minus Two'. Later research (Cowan, 2001) puts the limit nearer four chunks.
- **Source:** [lawsofux.com/millers-law](https://lawsofux.com/millers-law/)
- **Code:** `MIL`

## The principle

Miller's paper showed that short-term memory capacity is limited and that grouping information into chunks extends what people can handle. The number seven is widely misused: it's an average from recall experiments, not a cap on menu items. People don't memorise a visible menu — they scan it. The useful lesson is about memory load, not item counts: anything users must hold in their head should be small and well chunked, while visible, scannable content can be longer if it's well organised.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which information must users hold in memory (not just see) to complete the task?
- Is anyone using 'seven plus or minus two' as a rule for navigation or menus? Redirect the debate to scannability and structure.
- Where are codes, numbers or sequences that would benefit from chunking?

Steer the work toward:

- Apply capacity limits to what must be remembered, not to what is visible.
- Plan to chunk long strings and long lists.

## Mode 2 — Build (while designing or implementing)

- Format long identifiers in groups (for example 4-4-4 for card numbers, grouped phone numbers, IBAN in blocks of four) while accepting input with or without separators.
- Group long lists into labelled sections instead of truncating them to an arbitrary count.
- Present at most a few new concepts per onboarding step.
- For anything memorised, aim for about four chunks or fewer.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| MIL-1 | Major | static | Users must memorise more than about four unchunked items to finish a task. |
| MIL-2 | Major | static | Long codes or numbers are displayed as unbroken strings. |
| MIL-3 | Major | context | Useful options were removed or hidden purely to meet a 'seven items' rule. |
| MIL-4 | Minor | static | A long visible list has no grouping or ordering to aid scanning. |

## Tensions and misuse

- Misapplied, it leads to arbitrary limits that hurt findability; Hick's Law and good structure are better guides for menus.
- Display formatting must not leak into input validation; see Postel's Law.

## Related laws

- **`chunking`** — the actionable technique behind this law ([open](chunking.md))
- **`working-memory`** — the more current model of the same limit ([open](working-memory.md))
- **`hicks-law`** — a better guide for number of choices ([open](hicks-law.md))
- **`postels-law`** — accept chunked and unchunked input alike ([open](postels-law.md))
- **`cognitive-load`** — memory demand is one source of load ([open](cognitive-load.md))
