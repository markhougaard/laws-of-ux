# Doherty Threshold

**In one line:** Keep responses under about 400 ms so neither the user nor the system waits on the other.

- **Category:** Interaction and conventions
- **Origin:** Walter Doherty and Ahrvind Thadani (IBM, 1982), who found productivity rose sharply when system response time dropped below about 400 ms.
- **Source:** [lawsofux.com/doherty-threshold](https://lawsofux.com/doherty-threshold/)
- **Code:** `DOH`

## The principle

When a system responds quickly, people stay in the rhythm of their work; once responses slow past a few hundred milliseconds, they start waiting, lose focus and work less effectively. The commonly used tiers are about 0.1 s to feel instant, about 1 s to keep the flow of thought, and about 10 s before attention wanders. Where real work takes longer, perceived performance — immediate feedback, progress and optimistic updates — keeps the interaction feeling responsive.

## Mode 1 — Advise (before design)

Raise these with the team:

- What are the performance budgets for key interactions, and on what devices and networks will they be measured?
- Which operations are inherently slow (search, analysis, sync, uploads) and how will we keep users informed?
- Is performance in the definition of done, or an afterthought?

Steer the work toward:

- Set explicit budgets: feedback within 100 ms, results within about 400 ms for common actions, and progress for anything over 1 s.
- Measure on realistic hardware and networks, not developer machines.
- Design loading, progress and background states as first-class screens.

## Mode 2 — Build (while designing or implementing)

- Acknowledge every input visually within 100 ms (pressed state, spinner on the button, optimistic change).
- For web, target the Core Web Vitals 'good' thresholds: INP at or under 200 ms, LCP at or under 2.5 s, CLS at or under 0.1.
- Use skeleton screens for content loads; use determinate progress with an estimate for operations over a few seconds.
- Apply optimistic UI for low-risk actions, with clear rollback on failure.
- Let long operations run in the background with a notification on completion.
- Keep UI transitions short (roughly 150–300 ms); don't add animation that delays the result.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| DOH-1 | Blocker | interactive, code, runtime | A user action produces no visible feedback for more than about 1 s, so users may repeat it (double submissions, duplicate payments). |
| DOH-2 | Major | runtime | Common interactions exceed about 400 ms on target hardware with no perceived-performance mitigation. |
| DOH-3 | Major | interactive | Operations over about 10 s block the interface with no progress, estimate or background option. |
| DOH-4 | Major | context | No performance measurement was done on realistic devices or networks. |
| DOH-5 | Minor | interactive | Animations or transitions lengthen the time to result. |
| DOH-6 | Minor | interactive, runtime | Layout shifts during loading move targets under the user's pointer. |

## Tensions and misuse

- Optimistic UI can mislead if failures are frequent or silent.
- Artificial delays (to 'feel thorough') are occasionally justified for trust but should be rare and short.

## Related laws

- **`flow`** — speed preserves focused work ([open](flow.md))
- **`peak-end-rule`** — slow moments can become the remembered peak ([open](peak-end-rule.md))
- **`selective-attention`** — attention drifts while waiting ([open](selective-attention.md))
- **`goal-gradient-effect`** — progress indicators sustain motivation ([open](goal-gradient-effect.md))
- **`fitts-law`** — fast acquisition needs fast feedback ([open](fitts-law.md))
- **`parkinsons-law`** — task time is the human half of speed ([open](parkinsons-law.md))
