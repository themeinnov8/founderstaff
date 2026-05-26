---
description: Generate 09-meta/dashboard/roster.html — a visualization of the active roster and rhythm schedule.
mode: agent
---

# /roster-dashboard

Produce a self-contained HTML page that visualizes the {{BRAND}} active staff and their rhythms.

## Hard rules

1. **Idempotent.** Same input → byte-identical output except `generated:` timestamp.
2. **Self-contained.** Inline CSS (Tailwind CDN OK). No build step. Opens directly from disk.
3. **Read-only on sources.** Read `roster.json`, `rhythms.json`, `rhythms/runs.md`. Write ONLY to `09-meta/dashboard/roster.html`.
4. **Archive first.** Before overwriting, copy current file to `09-meta/dashboard/history/roster-{YYYY-MM-DD-HHMM}.html`.
5. **No invention.** If a roster entry has no rhythm, render `—` not a fake schedule.
6. **Cite sources.** Footer: links to `roster.json` and `rhythms.json`.

## Sections (top to bottom)

### 1. Header
- Title: `{{BRAND}} · Active Staff`
- Counts: `{N agents} active · {M rhythms} scheduled · {K} due today`
- `generated: {ISO timestamp}`

### 2. Roster grid
One card per agent. Card layout:
- Top: agent ID (kebab-case, monospace) + role
- Body: activated date · notes · rhythms attached (list of rhythm IDs)
- Footer: `last_run` (most recent across attached rhythms) · `next_due` (earliest across attached rhythms)
- Status pill:
  - **green** — has at least one active rhythm, all rhythms last ran within 1.5× cadence
  - **amber** — has rhythms but at least one is overdue
  - **gray** — on roster, no rhythms attached (manual-use only)

### 3. Rhythm timeline
Horizontal timeline (next 14 days). Each rhythm gets a row; due dates marked with a dot. Council rhythms shown with multiple agent initials stacked.

Render as a simple table if a timeline is too complex:

```
rhythm-id              | kind    | cadence    | agents                    | next_due   | status
-----------------------|---------|------------|---------------------------|------------|--------
daily-nba              | solo    | daily      | chief-of-staff            | 2026-05-24 | DUE
weekly-research-scan   | solo    | weekly mon | research-analyst          | 2026-05-25 | upcoming
monday-pipeline-review | council | weekly mon | sales-coach, delivery-lead| 2026-05-25 | upcoming
```

### 4. Recent runs
Last 10 entries from `rhythms/runs.md`, rendered as a clean table: `when · rhythm · outcome`.

### 5. Council index
If `09-meta/rhythms/councils/` exists, list the most recent 5 council transcripts as links.

### 6. Footer
- `Source files: roster.json · rhythms.json · runs.md`
- `Refresh: /roster-dashboard`
- `Owner: @roster-manager`

## Visual conventions

- Dark mode (`<html class="dark">`), zinc palette, matches `index.html`.
- Tailwind via CDN: `https://cdn.tailwindcss.com`.
- Status pills: emerald (green), amber, zinc (gray).
- Monospace for IDs (`font-mono`).

## Process

1. Archive existing `roster.html` if present.
2. Read `roster.json`, `rhythms.json`, `rhythms/runs.md`.
3. Compute `next_due` for every rhythm (use the `/schedule` algorithm).
4. Build HTML in memory.
5. Write atomically.
6. Print path + summary counts.

## Output

- Path to `09-meta/dashboard/roster.html`
- One-line summary: `Wrote roster dashboard: {N} agents · {M} rhythms · {K} due today`
