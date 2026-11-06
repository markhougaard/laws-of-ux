---
name: ux-millers-law
description: Miller's Law (Laws of UX): Short-term memory holds only a handful of items, so organise information into manageable chunks — don't use '7' as a hard rule. Use to advise up front, guide building, or strictly review how much information to present at once, chunking of lists and codes, menu and navigation size debates, and dashboard density.
---

# Miller's Law

**In one line:** Short-term memory holds only a handful of items, so organise information into manageable chunks — don't use '7' as a hard rule.

- **Category:** Memory and cognition
- **Origin:** George A. Miller (1956), 'The Magical Number Seven, Plus or Minus Two'. Later research (Cowan, 2001) puts the limit nearer four chunks.
- **Source:** [lawsofux.com/millers-law](https://lawsofux.com/millers-law/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| MIL-1 | Major | static | Users must memorise more than about four unchunked items to finish a task. |
| MIL-2 | Major | static | Long codes or numbers are displayed as unbroken strings. |
| MIL-3 | Major | context | Useful options were removed or hidden purely to meet a 'seven items' rule. |
| MIL-4 | Minor | static | A long visible list has no grouping or ordering to aid scanning. |

Report each finding on one line:

`[SEVERITY] MIL-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Misapplied, it leads to arbitrary limits that hurt findability; Hick's Law and good structure are better guides for menus.
- Display formatting must not leak into input validation; see Postel's Law.

## Related skills

- **`ux-chunking`** — the actionable technique behind this law ([open](../ux-chunking/SKILL.md))
- **`ux-working-memory`** — the more current model of the same limit ([open](../ux-working-memory/SKILL.md))
- **`ux-hicks-law`** — a better guide for number of choices ([open](../ux-hicks-law/SKILL.md))
- **`ux-postels-law`** — accept chunked and unchunked input alike ([open](../ux-postels-law/SKILL.md))
- **`ux-cognitive-load`** — memory demand is one source of load ([open](../ux-cognitive-load/SKILL.md))
