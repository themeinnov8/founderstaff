---
description: Regenerate the rich HTML dashboard at 09-meta/dashboard/index.html from current markdown state.
mode: agent
---

# /refresh-dashboard

You are the **dashboard-generator**. Your job: produce a single, self-contained HTML file at `09-meta/dashboard/index.html` that visualizes the current operational state of the {{BRAND}} Business OS.

## Hard rules

1. **Idempotent.** Running this twice with no state change produces byte-identical output (except the `generated:` timestamp).
2. **Self-contained.** No build step. Inline CSS (Tailwind CDN OK). Inline JS (Chart.js CDN OK). Must work when opened directly from disk.
3. **Archive first, then write.** Before overwriting `index.html`, copy current contents to `09-meta/dashboard/history/YYYY-MM-DD-HHMM.html`. Never delete history.
4. **Read-only on sources.** Never modify source files. Write ONLY to `09-meta/dashboard/`.
5. **Compliance gate.** Run `/compliance-check` over the rendered HTML string before writing. If any operator name or employer name leaks, fail closed with a clear error — do NOT write the file.
6. **Cite sources.** Every widget has a small `source:` footer linking to the markdown file it was derived from.
7. **No invention.** If a source file is missing or empty, render the widget as "Not yet tracked — create `path/to/file.md`" instead of fabricating data.

## Data sources (scan in this order)

| Widget | Source file(s) | Render as |
|---|---|---|
| Header (date, week #, phase) | `00-strategy/milestones.md` (current phase) + system date | top bar |
| Action queue | `09-meta/action-queue.md` (top section "## Now") | numbered list, top 3 highlighted |
| Time budget gauge | `09-meta/time-log.md` (this week) | progress bar (used / 7h) + month rollup |
| Milestone progress | `00-strategy/milestones.md` | progress bars, next 3 milestones |
| Pipeline kanban | `04-pipeline/_pipeline.md` (table with `stage` column) | 5 columns: Lead → Discovery → Proposal → Closed-Won → Closed-Lost |
| Client list | `05-clients/*/README.md` frontmatter (name, stage, MRR, next_step, last_contact) | sortable table |
| Revenue YTD | `07-finance/revenue.md` (monthly table) | bar chart + YTD total + % of annual target |
| Passive product health | `07-products/_health.md` | table: product · launched · MRR · health (green/amber/red based on ₹5K/60d rule) |
| Compliance flags | `09-meta/compliance-log.md` (last entry) | green check or red flags with count |
| MSFT firewall status | `09-meta/compliance-log.md` (last `/compliance-check` run) | timestamp + pass/fail |

## Output structure (sections, top to bottom)

1. **Top bar**: brand logo, "Live Dashboard · generated {ts}", current phase pill, week-of-year badge
2. **Action queue** (full width, amber accent) — what to do *right now*
3. **Two-column row**: Time budget gauge | Milestone progress
4. **Pipeline kanban** (full width)
5. **Client list table**
6. **Two-column row**: Revenue chart | Passive product health
7. **Footer**: compliance status, last dashboard refresh, link to `plan.html`

## Visual conventions

- Dark mode (`<html class="dark">`), zinc palette to match `plan.html`
- Brand gradient header (same as plan.html)
- Tailwind via CDN: `https://cdn.tailwindcss.com`
- Chart.js via CDN: `https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js`
- Status colors: emerald (on track), amber (watch), rose (off track)
- Money: ₹ for INR, $ for USD. Never auto-convert except in the YTD chart (note exchange rate ₹83/$).

## Process

1. Check `09-meta/dashboard/index.html` exists. If yes → copy to `history/{timestamp}.html`.
2. Read each source file from the table above. For missing files, queue a "not tracked" placeholder.
3. Build the HTML in memory. Use one `<template>` per widget for readability.
4. Run compliance check on the rendered string. Halt on failure.
5. Write to `09-meta/dashboard/index.html`.
6. Print a 3-line summary: widgets rendered, sources missing, compliance status. Suggest the next `/refresh-dashboard` trigger (typically: after `/daily-log` or `/weekly-review`).

## When to invoke

- After `/daily-log` (auto-chain optional)
- Start of every Saturday weekly review
- Before sharing screenshots with anyone
- After any pipeline stage change
- After any client onboard/offboard
