---
description: Guardrails for client deliverables, briefs, and any artifact under 05-clients/**.
applyTo: "05-clients/**"
---

# client-work

Applies to every artifact written for or about a paying client.

## Confidentiality

- Never reference a client by real name in any file outside `05-clients/{slug}/`. Use the slug elsewhere.
- Never use one client's data, prompts, or outputs as examples for another without written consent logged in `05-clients/{slug}/_consent.md`.
- Screenshots of client systems are forbidden in `03-content/**` and `06-marketing/**`.

## Scope discipline

- Every client folder must contain `_sow.md` (signed scope) and `_brief.md` (operator-readable summary).
- New work requests outside the SOW go to `05-clients/{slug}/_change-requests.md`, not silently absorbed.
- Hour-tracking lives in `09-meta/time-log.md` tagged `client:{slug}` — non-negotiable for invoicing accuracy.

## Deliverable rules

- Every deliverable has a single canonical file. No "_v3_final_final.md".
- Drafts use `draft/` subfolder; only `final/` artifacts are billable / shareable.
- Every shared deliverable carries a footer: "Prepared by {{BRAND}} · {{date}} · For {client} only".

## Hard refusals

- Refuse to produce work that violates the client's stated compliance posture (logged in `_brief.md`).
- Refuse to write client-attributable opinions outside what the SOW authorizes.
- If a deliverable touches {{EMPLOYER}} or a competitor of {{EMPLOYER}}, route through `/compliance-check`.
