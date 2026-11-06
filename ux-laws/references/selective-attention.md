# Selective Attention

**In one line:** People attend to the parts of a screen that match their current goal and filter out the rest.

- **Category:** Perception and attention
- **Origin:** Colin Cherry's cocktail-party studies (1953); later inattentional blindness (Simons and Chabris, 1999) and banner blindness (Benway and Lane, 1998).
- **Source:** [lawsofux.com/selective-attention](https://lawsofux.com/selective-attention/)
- **Code:** `SA`

## The principle

Attention is narrow and goal-driven. People focused on a task stop seeing things outside it — including changes in plain view, and anything that looks like advertising. So 'we showed a message' is not the same as 'the user saw it'. Information that matters must be placed in the path of the task, at the moment it matters, in a form that doesn't resemble the things users have learned to ignore.

## Mode 1 — Advise (before design)

Raise these with the team:

- What must users notice even when they're focused on something else (errors, security, data loss, status changes)?
- Where will their attention actually be at that moment?
- How many notifications and interruptions will the product generate, and who decides what interrupts?

Steer the work toward:

- Put critical information where the user is already looking — at the point of action.
- Create a notification priority model: what interrupts, what waits, what's ambient.
- Assume promotional-looking areas are invisible.

## Mode 2 — Build (while designing or implementing)

- Show validation errors next to the field, and on submit move focus to the first error or an error summary.
- Announce dynamic status changes to assistive tech with live regions (aria-live='polite' for status, assertive only for urgent issues).
- Avoid banner-shaped, ad-coloured or carousel placements for anything essential.
- For changes far from the focus point (a badge updating, a row added), add a brief transition or highlight so the change is noticed.
- Moving, blinking or auto-updating content that lasts more than 5 seconds needs a way to pause, stop or hide it (WCAG 2.2.2).
- Don't rely on users reading a toast for anything they must act on; toasts disappear while attention is elsewhere.

## Mode 3 — Review (strict gate before commit)

Apply these under the review protocol in [`SKILL.md`](../SKILL.md) §5: evidence scope, severities, finding format and verdict.

| ID | Severity | Evidence | Check |
|---|---|---|---|
| SA-1 | Blocker | static | Information required to avoid an error, data loss or security risk appears only outside the user's focus area, or only in a transient toast. |
| SA-2 | Blocker | interactive, code | Errors are displayed but focus isn't moved and they aren't announced, so keyboard and screen-reader users miss them. |
| SA-3 | Major | static | Essential content uses banner, ad-like or carousel styling. |
| SA-4 | Major | static | Several simultaneous notifications compete with no priority order. |
| SA-5 | Major | interactive, code | A significant state change happens without any visible or announced cue. |
| SA-6 | Minor | interactive | Ambient animation or auto-updating content draws attention away from the primary task. |

## Tensions and misuse

- Von Restorff emphasis helps only if it doesn't look like noise users already filter.
- Adding more alerts to fix missed alerts accelerates alert fatigue.

## Related laws

- **`von-restorff-effect`** — how to stand out without being filtered as noise ([open](von-restorff-effect.md))
- **`cognitive-load`** — attention is a finite resource ([open](cognitive-load.md))
- **`flow`** — interruptions break focused work ([open](flow.md))
- **`working-memory`** — what users miss can't be held for later ([open](working-memory.md))
- **`paradox-of-the-active-user`** — users skip instructions for the same reason ([open](paradox-of-the-active-user.md))
