---
name: ux-cognitive-bias
description: Cognitive Bias (Laws of UX): Systematic shortcuts in thinking shape how users decide — and how teams interpret research. Use to advise up front, guide building, or strictly review defaults, framing, pricing and plan choice, consent and privacy choices, nudges, dark-pattern risk, research interpretation and design decision-making.
---

# Cognitive Bias

**In one line:** Systematic shortcuts in thinking shape how users decide — and how teams interpret research.

- **Category:** Memory and cognition
- **Origin:** Amos Tversky and Daniel Kahneman's heuristics-and-biases research (1974 onward).
- **Source:** [lawsofux.com/cognitive-bias](https://lawsofux.com/cognitive-bias/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

People rely on mental shortcuts that are fast and usually good enough, but that err in predictable directions: anchoring on the first number seen, sticking with defaults, weighing losses more than gains, seeking confirming evidence. Interfaces inevitably trigger these biases through defaults, order and framing, so neutral design is a myth. The responsibility is to use them in the user's interest, never against it — and to recognise that designers, product managers and stakeholders are just as biased when they read research and make decisions.

## Mode 1 — Advise (before design)

Raise these with the team:

- Which decisions in this product will users make, and which biases (default, anchoring, framing, loss aversion, social proof) will influence them?
- Would we be comfortable showing users exactly how we've set the defaults and framing?
- Are we looking for evidence that our solution works, or testing whether it doesn't?
- Who on the team is anchored on an early idea, and how will we challenge it?

Steer the work toward:

- Set defaults that a well-informed user would choose for themselves.
- Pre-register success criteria for research before seeing results.
- Treat dark patterns as defects with legal exposure (consumer protection and privacy law in the EU and elsewhere).

## Mode 2 — Build (while designing or implementing)

- Defaults: choose the safest and most common good option; for consent, default to off for non-essential processing.
- Present options with symmetrical effort: 'reject' must be as easy as 'accept', 'cancel' as easy as 'subscribe'.
- Frame information honestly and comparably (same units, same baselines); don't hide totals.
- Use real social proof only; never fabricate counts, urgency or scarcity.
- Order options deliberately and know that the first one anchors.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| CB-1 | Blocker | The design uses a deceptive pattern: hidden costs, pre-ticked consent, confirm-shaming, fake urgency or scarcity, a hard-to-find cancel, or asymmetric accept/reject effort. |
| CB-2 | Blocker | Defaults expose users to cost, risk or data sharing that a well-informed user would be unlikely to choose. |
| CB-3 | Major | Comparable options are framed inconsistently (different units, hidden totals, selective anchors). |
| CB-4 | Major | A design decision is justified by research that was interpreted without predefined criteria, or by one confirming anecdote. |
| CB-5 | Minor | Option order or emphasis nudges without a user-benefit rationale written down. |

Report each finding on one line:

`[SEVERITY] CB-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Nudges in the user's interest (safer defaults) are still nudges; document and justify them.
- Von Restorff and Serial Position are bias-adjacent tools and carry the same ethical duty.

## Related skills

- **`ux-aesthetic-usability-effect`** — the halo effect in usability findings ([open](../ux-aesthetic-usability-effect/SKILL.md))
- **`ux-serial-position-effect`** — order effects as a bias lever ([open](../ux-serial-position-effect/SKILL.md))
- **`ux-von-restorff-effect`** — emphasis as a bias lever ([open](../ux-von-restorff-effect/SKILL.md))
- **`ux-choice-overload`** — how option sets drive decisions ([open](../ux-choice-overload/SKILL.md))
- **`ux-peak-end-rule`** — memory biases in how experiences are judged ([open](../ux-peak-end-rule/SKILL.md))
- **`ux-mental-model`** — biases shape the models users form ([open](../ux-mental-model/SKILL.md))
- **`ux-parkinsons-law`** — fake urgency and countdowns as manipulation ([open](../ux-parkinsons-law/SKILL.md))
