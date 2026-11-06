---
name: ux-working-memory
description: Working Memory (Laws of UX): People can hold and manipulate only a few things in mind at once, and only briefly. Use to advise up front, guide building, or strictly review multi-step flows, comparisons, codes and IDs, re-entering information, authentication, navigation context and anything users must remember between moments.
---

# Working Memory

**In one line:** People can hold and manipulate only a few things in mind at once, and only briefly.

- **Category:** Memory and cognition
- **Origin:** Alan Baddeley and Graham Hitch's model (1974).
- **Source:** [lawsofux.com/working-memory](https://lawsofux.com/working-memory/)
- **Index and review protocol:** `ux-laws` ([open](../ux-laws/SKILL.md))

## Pick the mode

- **Advise** — only a goal, brief, problem or early concept exists. Use Mode 1 and shape the direction before anything is drawn or built.
- **Build** — a design or implementation is in progress. Use Mode 2 as the working reference.
- **Review** — a finished design, prototype, screenshot set or diff is about to be committed. Use Mode 3 and be strict.

If the request doesn't say, infer it from what you were given: a goal means Advise, work in progress means Build, a finished artifact means Review.

## The principle

Working memory is the mental scratchpad used to hold and juggle information during a task. It's small — about four meaningful chunks for most people — and fades within seconds without rehearsal. Interruptions wipe it. Interfaces that rely on recall (remember this code, remember what you chose two screens ago, compare these from memory) fail exactly when people are busy or distracted. Recognition beats recall: show things rather than asking people to remember them.

## Mode 1 — Advise (before design)

Raise these with the team:

- Where in the planned flows would a user need to remember something from one moment to the next?
- Will users compare options? Can they see them side by side?
- Are there codes, IDs or values users must carry from one place to another (including another app)?
- How often will users be interrupted mid-task, and what do they need to resume?

Steer the work toward:

- Design for recognition, not recall.
- Plan side-by-side comparison wherever users choose between items.
- Make every flow resumable with its context visible.

## Mode 2 — Build (while designing or implementing)

- Show previous choices in context (breadcrumbs, step summaries, selected filters as chips).
- Never ask for information already provided in the same process; carry it forward or let users select it (WCAG 3.3.7 Redundant Entry).
- Allow copy-paste and autofill for codes, passwords and one-time codes; don't block paste (supports WCAG 3.3.8 Accessible Authentication).
- Provide comparison views that keep attributes aligned across items.
- Keep instructions visible while the user acts on them, rather than on a previous screen.
- Save drafts automatically so interruptions don't cost work.

## Mode 3 — Review (strict gate before commit)

Run every check. A check passes only on positive evidence in the artifact — never by default. The **Evidence** column says what kind of input can settle each check (`static`, `interactive`, `code`, `runtime`, `context` — defined in `ux-laws`). If none of those kinds was supplied, list the check as *out of scope* with the evidence it needs. If the right kind was supplied but the relevant state or element is missing, mark it `UNVERIFIED` and name what you would need. Don't soften findings and don't award points for intent.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| WM-1 | Blocker | interactive, code | A login or verification step requires transcribing or remembering a value with no paste, autofill or alternative (WCAG 3.3.8). |
| WM-2 | Blocker | static | Information entered earlier in the same process must be re-entered (WCAG 3.3.7), outside the allowed exceptions. |
| WM-3 | Major | static | Users must compare options across separate screens or modals without a side-by-side view. |
| WM-4 | Major | static | Instructions or reference data needed for a step are shown only before that step. |
| WM-5 | Major | interactive | An interruption (navigating away, a timeout) loses entered data with no recovery. |
| WM-6 | Minor | static | Current context (selection, filters, location in a flow) isn't visible on screen. |

Report each finding on one line:

`[SEVERITY] WM-n · <screen / component / file:line> — <what you observed> → <specific fix>`

Verdict: any **Blocker** → *Do not commit*. An in-scope Blocker-level check left `UNVERIFIED` → *Blocked pending evidence*. Any **Major** → *Commit only with each Major fixed or explicitly accepted by a named owner*. Only **Minor** or none → *Pass*. Every verdict states its evidence scope and lists out-of-scope Blocker checks. Severity definitions and the full verdict rule are in `ux-laws`.

## Tensions and misuse

- Showing everything to avoid recall can increase visual load; show what's relevant to the current step.
- Security requirements can conflict; prefer methods (passkeys, password managers) that remove the memory burden instead of adding it.

## Related skills

- **`ux-millers-law`** — the classic capacity claim, and its limits ([open](../ux-millers-law/SKILL.md))
- **`ux-chunking`** — how to fit more into the same capacity ([open](../ux-chunking/SKILL.md))
- **`ux-cognitive-load`** — the broader budget working memory belongs to ([open](../ux-cognitive-load/SKILL.md))
- **`ux-zeigarnik-effect`** — unfinished tasks occupy the mind ([open](../ux-zeigarnik-effect/SKILL.md))
- **`ux-serial-position-effect`** — which items in a sequence survive ([open](../ux-serial-position-effect/SKILL.md))
