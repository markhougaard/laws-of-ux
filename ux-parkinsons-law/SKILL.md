---
name: ux-parkinsons-law
description: Parkinson's Law (Laws of UX): Work expands to fill the time available, so make tasks take less time than users expect. Use to advise up front, guide building, or strictly review task duration, form length, autofill and defaults, checkout and sign-up speed, time limits and timeouts, and expected-effort messaging.
---

# Parkinson's Law

**In one line:** Work expands to fill the time available, so make tasks take less time than users expect.

- **Category:** Motivation and experience
- **Origin:** C. Northcote Parkinson, essay in The Economist (1955).
- **Source:** [lawsofux.com/parkinsons-law](https://lawsofux.com/parkinsons-law/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Originally an observation about bureaucracy, the law applies to users too: given an open-ended task, people spend more time and effort than needed. Design can compress tasks below expectations — autofill, sensible defaults, fewer fields, one-tap actions — and set clear expectations of how long things take. It isn't a reason to impose time pressure: artificial deadlines and timeouts harm accessibility and trust.

## Mode 1 — Advise (before design)

Raise these with the team:

- How long do users expect each key task to take, and how long does it take now?
- Which inputs can the system fill or skip?
- Do any flows have time limits, and are they genuinely necessary?

Steer the work toward:

- Set target task durations and measure against them.
- Cut fields and steps that don't change the outcome.
- Communicate expected effort upfront for longer tasks.

## Mode 2 — Build (while designing or implementing)

- Use autocomplete attributes and device autofill for personal data.
- Pre-fill from known data and previous entries.
- Ask only for what's needed now; defer optional data.
- Tell users how long a task will take ('about 3 minutes') and keep the promise.
- If a time limit is essential, warn before it expires and let users extend it at least ten times or turn it off, unless an exception applies (WCAG 2.2.1).

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. If you can't verify a check from what you were given, mark it `UNVERIFIED` and name what you would need (a state, a measurement, real content, a device). Don't soften findings and don't award points for intent.

| ID | Severity | Check |
|---|---|---|
| PKL-1 | Blocker | A time limit expires without warning or a way to extend it, outside WCAG 2.2.1 exceptions. |
| PKL-2 | Major | A form asks for information the system already has or doesn't need for the current purpose. |
| PKL-3 | Major | Autofill or autocomplete is missing or broken on personal-data fields (WCAG 1.3.5). |
| PKL-4 | Major | Artificial urgency (countdowns, 'only today') is used without a real deadline. |
| PKL-5 | Minor | Expected duration isn't communicated for tasks longer than a few minutes. |

Report each finding on one line:

`[SEVERITY] PKL-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. A Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Severity definitions are in `ux-laws`.

## Tensions and misuse

- Speed can conflict with care in consequential decisions; don't rush users through irreversible choices.
- Fake time pressure is a deceptive pattern; see Cognitive Bias.

## Related skills

- **`ux-doherty-threshold`** — system speed, the other half of task speed ([open](../ux-doherty-threshold/SKILL.md))
- **`ux-teslers-law`** — the system does the work so users don't ([open](../ux-teslers-law/SKILL.md))
- **`ux-goal-gradient-effect`** — shorter remaining effort motivates ([open](../ux-goal-gradient-effect/SKILL.md))
- **`ux-cognitive-bias`** — urgency as manipulation ([open](../ux-cognitive-bias/SKILL.md))
- **`ux-occams-razor`** — remove unnecessary steps ([open](../ux-occams-razor/SKILL.md))
