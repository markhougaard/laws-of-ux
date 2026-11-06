---
name: ux-doherty-threshold
description: Doherty Threshold (Laws of UX): Keep responses under about 400 ms so neither the user nor the system waits on the other. Use to advise up front, guide building, or strictly review performance budgets, latency, loading states, optimistic UI, progress indicators, animation timing and perceived speed.
---

# Doherty Threshold

**In one line:** Keep responses under about 400 ms so neither the user nor the system waits on the other.

- **Category:** Interaction and conventions
- **Origin:** Walter Doherty and Ahrvind Thadani (IBM, 1982), who found productivity rose sharply when system response time dropped below about 400 ms.
- **Source:** [lawsofux.com/doherty-threshold](https://lawsofux.com/doherty-threshold/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

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

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| DOH-1 | Blocker | A user action produces no visible feedback for more than about 1 s, so users may repeat it (double submissions, duplicate payments). |
| DOH-2 | Major | Common interactions exceed about 400 ms on target hardware with no perceived-performance mitigation. |
| DOH-3 | Major | Operations over about 10 s block the interface with no progress, estimate or background option. |
| DOH-4 | Major | No performance measurement was done on realistic devices or networks. |
| DOH-5 | Minor | Animations or transitions lengthen the time to result. |
| DOH-6 | Minor | Layout shifts during loading move targets under the user's pointer. |

Report each finding on one line:

`[SEVERITY] DOH-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Optimistic UI can mislead if failures are frequent or silent.
- Artificial delays (to 'feel thorough') are occasionally justified for trust but should be rare and short.

## Related skills

- **`ux-flow`** — speed preserves focused work ([open](../ux-flow/SKILL.md))
- **`ux-peak-end-rule`** — slow moments can become the remembered peak ([open](../ux-peak-end-rule/SKILL.md))
- **`ux-selective-attention`** — attention drifts while waiting ([open](../ux-selective-attention/SKILL.md))
- **`ux-goal-gradient-effect`** — progress indicators sustain motivation ([open](../ux-goal-gradient-effect/SKILL.md))
- **`ux-fitts-law`** — fast acquisition needs fast feedback ([open](../ux-fitts-law/SKILL.md))
- **`ux-parkinsons-law`** — task time is the human half of speed ([open](../ux-parkinsons-law/SKILL.md))
