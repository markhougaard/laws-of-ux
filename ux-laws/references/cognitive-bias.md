# Cognitive Bias

**In one line:** Systematic shortcuts in thinking shape how users decide — and how teams interpret research.

- **Category:** Memory and cognition
- **Origin:** Amos Tversky and Daniel Kahneman's heuristics-and-biases research (1974 onward).
- **Source:** [lawsofux.com/cognitive-bias](https://lawsofux.com/cognitive-bias/)
- **Code:** `CB`

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

Apply these under the review protocol in `SKILL.md` §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| CB-1 | Blocker | static, interactive | The design uses a deceptive pattern: hidden costs, pre-ticked consent, confirm-shaming, fake urgency or scarcity, a hard-to-find cancel, or asymmetric accept/reject effort. |
| CB-2 | Blocker | static | Defaults expose users to cost, risk or data sharing that a well-informed user would be unlikely to choose. |
| CB-3 | Major | static | Comparable options are framed inconsistently (different units, hidden totals, selective anchors). |
| CB-4 | Major | context | A design decision is justified by research that was interpreted without predefined criteria, or by one confirming anecdote. |
| CB-5 | Minor | context | Option order or emphasis nudges without a user-benefit rationale written down. |

## Tensions and misuse

- Nudges in the user's interest (safer defaults) are still nudges; document and justify them.
- Von Restorff and Serial Position are bias-adjacent tools and carry the same ethical duty.

## Related laws

- **`aesthetic-usability-effect`** — the halo effect in usability findings (`references/aesthetic-usability-effect.md`)
- **`serial-position-effect`** — order effects as a bias lever (`references/serial-position-effect.md`)
- **`von-restorff-effect`** — emphasis as a bias lever (`references/von-restorff-effect.md`)
- **`choice-overload`** — how option sets drive decisions (`references/choice-overload.md`)
- **`peak-end-rule`** — memory biases in how experiences are judged (`references/peak-end-rule.md`)
- **`mental-model`** — biases shape the models users form (`references/mental-model.md`)
- **`parkinsons-law`** — fake urgency and countdowns as manipulation (`references/parkinsons-law.md`)
