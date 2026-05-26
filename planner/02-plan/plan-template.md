# Plan — {brand} Business OS

> **Status:** DRAFT | UNDER REVIEW | APPROVED — {YYYY-MM-DD}
> **Approved by:** {prospect signature/handle} + {operator}
> **Generated OS will be created at:** `../{brand-slug}-business-os/`

This file is the contract for `03-generate/`. Once both parties approve, the generation step is mechanical — no more negotiation. If something feels wrong during generation, stop and amend this file first.

---

## 1. Identity

| Field | Value |
|---|---|
| Brand name | {final, not a token} |
| Brand short | {≤8 chars} |
| Domain | {brand.com — verify available before approval} |
| Primary handle | {@brand} |
| Operator handle | {anonymized if employer firewall applies} |
| Tagline (≤12 words) | {…} |
| One-paragraph positioning | {…} |

## 2. Audience(s)

| ID | Audience | Size estimate | Where they live | Currency |
|---|---|---|---|---|
| A1 | {primary} | {N} | {LI / Slack / …} | {INR/USD} |
| A2 | {secondary, optional} | {N} | … | … |

## 3. Offerings (SKU ladder)

> Follow the 4-tier shape unless a strong reason not to. Token any "later" tiers as locked.

| Tier | ID | Name | Price | Launch month | Audience | Deliverable |
|---|---|---|---|---|---|---|
| A | A1 | {micro-SKU} | {₹/$} | M+1 | … | … |
| A | A2 | … | … | M+2 | … | … |
| B | B1 | {cohort} | … | M+6 | … | … |
| C | C1 | {high-ticket sprint} | $… | M+12 | … | … |
| D | D1 | {maturity-gated} | … | LOCKED | … | unlock criteria: {…} |

## 4. Constraints & firewall

- **Employer:** {name or "none"} — firewall strictness: {MAX / standard / none}
- **Anonymity:** {required / preferred / not required}
- **Do-not-contact:** {seed entries — colleagues, ex-employer customers, etc.}
- **IP boundaries:** {what they cannot use from prior employment}
- **Geography & tax:** {who they're paid as, where invoices originate}

## 5. Time & timeline

- **Operator hours/week:** {N} (hard cap, not aspirational)
- **Timeline:** {start date} → {end date} = {N} months
- **Buffer cadence:** {every Nth week off}
- **Phase count & names:** P0 … P{n}
- **Milestones (≥4):**
  | ID | Milestone | Target date | Definition of done |
  | M01 | First ₹ | {…} | {…} |
  | M02 | First {SKU} launched | {…} | {…} |
  | … | … | … | … |

## 6. Revenue plan

- **Endpoint goal:** {₹/$ per month}, of which {N}% passive
- **Currency split:** {INR for X / USD for Y}
- **Passive product roadmap:** {3–4 products, each with launch month + price}
- **Pricing posture:** {layoff-friendly? premium? mixed?}

## 7. Custom skills/agents needed beyond the standard set

> Standard set = `strategist`, `content-creator`, `sales-coach`, `delivery`, `compliance-reviewer`, `chief-of-staff`, `dashboard-generator`, `research-analyst`, `red-team`, `agent-forge` + the standard prompt library.
>
> List anything **domain-specific** this venture needs. The `agent-forge` will generate these in stage 03.

| Type | Name | Purpose | Why standard set isn't enough |
|---|---|---|---|
| chatmode | {…} | {…} | {…} |
| prompt | {/…} | {…} | {…} |
| instructions | {…} | {…} | {…} |

Example for a fitness coaching OS: chatmode `program-designer`, prompt `/workout-week`, instructions `medical-disclaimer.instructions.md` (applyTo: all client-facing content).

## 8. Content strategy

- **Channels:** {LI / YT / newsletter / podcast — pick ≤2 to start}
- **Cadence:** {N posts/week, sustainable for given hours}
- **Content pillars (3–5):** {…}
- **30% rule applied?** {what % is enterprise/high-ticket-bait vs tactical?}

## 9. Compliance & quality gates

- **Required guardrail instructions to enable:**
  - [ ] `msft-firewall` / employer-firewall
  - [ ] `content-voice`
  - [ ] `outreach` (do-not-contact)
  - [ ] `client-work` (IP + CoI)
  - [ ] `public-publishing` (compliance-check before publish)
  - [ ] `progress-logging`
  - [ ] `research-quality`
  - [ ] {custom from §7}

## 10. Generation parameters (read by stage 03 seed prompt)

```yaml
brand: "{…}"
brand_short: "{…}"
brand_domain: "{…}"
brand_handle: "{…}"
operator_handle: "{…}"
home_currency: "INR | USD"
hours_per_week: 7
timeline_months: 16
employer_firewall: "max | standard | none"
employer_name: "{…}"
generated_repo_path: "../{brand-slug}-business-os"
standard_chatmodes: ["strategist","content-creator","sales-coach","delivery","compliance-reviewer","chief-of-staff","dashboard-generator","research-analyst","red-team","agent-forge"]
custom_chatmodes: [{see §7}]
custom_prompts: [{see §7}]
custom_instructions: [{see §7}]
```

---

## Approval

- [ ] Prospect has read this plan end-to-end
- [ ] All §7 custom agents have been justified (red-teamed)
- [ ] §10 generation parameters are filled and valid
- [ ] Domain availability checked (§1)
- [ ] Compliance gates in §9 reviewed by `compliance-reviewer`

When all boxes ticked → run `03-generate/seed-prompt.md`.
