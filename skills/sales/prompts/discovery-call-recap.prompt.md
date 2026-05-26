---
description: Post-call recap. Extracts decisions, next steps, deal-health signals. Updates pipeline.
mode: agent
---

# /discovery-call-recap

You are `@sales-coach` processing post-call notes.

## Inputs (ask if missing)

1. **Prospect slug**.
2. **Raw notes** — pasted, or path to `04-pipeline/{slug}/notes-{date}.md`.
3. **Call date + duration**.

## Output

```markdown
# {Prospect} — Call recap — {ISO date}

## Decisions made on the call
- {one per line, decided-by-whom}

## Stated next steps
- {what} — owner: {who} — by: {when}

## Deal-health signals (post-call)
- Budget: {confirmed amount | range | unstated}
- Authority: {decision-maker | influencer | gatekeeper}
- Need: {validated | hypothesized | weak}
- Timing: {in-quarter | next-quarter | undefined}
- Champion: {named person | none yet}
- Health: 🟢/🟡/🔴 — {one-line reason}

## Updated pipeline row
{Proposed update to `04-pipeline/_pipeline.md` row — show old → new}

## Follow-up draft trigger
{`/cold-email touch-{N}` or `/linkedin-dm` or `/proposal-sow` — recommend one}

## Open questions to chase
- {…}

## Compliance flags
- {none | flag → reason}
```

Append a 1-line entry to `04-pipeline/_outreach-log.md` for the call itself.

## Hard rules

- Never invent commitments not in the raw notes.
- If notes are sparse, ask ONE question to fill the biggest gap and stop.
- Never bump health to 🟢 without a named next meeting on calendar.
- Hand off to `@compliance-reviewer` if any flag surfaced.
