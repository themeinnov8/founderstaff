---
description: Structured market research scan for a topic, audience, competitor set, or pricing question. Outputs a citation-disciplined research note.
mode: agent
---

# /market-research

Run a structured market research scan and write the result as a new file under `02-research/` following `research-quality.instructions.md`.

## Inputs (ask the operator if missing)

- `topic`: 1-line research question (e.g., "Pricing for PM bootcamps in India 2026")
- `type`: market | competitor | audience | pricing | trend | benchmark
- `decision`: what OS decision this informs (e.g., "Set B2 PM Bootcamp price tier")
- `time_budget_min`: 30 | 60 | 90 (default 60)
- `freshness_required`: ≤ {N} months old

## Process

1. **Frame** — restate the question in 1 sentence. List 3–5 sub-questions that must be answered to decide.
2. **Search plan** — list 5–10 search queries you will run, ordered by expected information value.
3. **Collect** — for each query, capture: source URL, key data point, date published, confidence.
4. **Triangulate** — every numeric claim needs ≥2 independent sources. Surface disagreements explicitly.
5. **Synthesize** — write the file using the standard structure in `research-quality.instructions.md`.
6. **Decide** — close with 1–3 *Implications for the OS* — specific, actionable, tied to the named decision.

## Output

Write to: `02-research/{type}/{YYYY-MM-DD}-{slug}.md`

After write, append a 1-line entry to `09-meta/progress-log.md`:
`{date} · research · {topic} · {decision} · confidence:{level}`

## Hard rules

- If you cannot find ≥2 sources for any key claim within the time budget, ship the file with `confidence: low` and flag what's missing — do NOT pad with weaker sources.
- Never invent statistics. If a number is unknown, write "unknown — needs primary research".
- If the topic touches Microsoft or current employer, route through `/compliance-check` before write.
- Suggest 1 follow-up research task if a critical sub-question remained open.
