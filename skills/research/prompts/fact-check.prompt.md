---
description: Verify every factual claim in a draft (content, proposal, SOW). Outputs claim-by-claim verdict.
mode: agent
---

# /fact-check

Scan a draft file and verify every factual claim. Output a table of claims with verdicts. Block publish if any `false` or `unverified-load-bearing` claim remains.

## Inputs

- `artifact_path`: file to fact-check
- `strictness`: standard (block on false) | aggressive (block on any unverified)

## Process

1. Extract every factual claim from the artifact. A "claim" = any statement a reader could in principle check (numbers, dates, names, attributions, comparative statements like "fastest growing", causal claims).
2. For each claim, classify: `verified` | `unverified` | `false` | `opinion` (not a fact, skip) | `outdated`.
3. For each `verified` and `false`, cite the source.
4. For each `unverified`, propose how to verify (which source to consult) and time estimate.
5. Score the artifact's overall trust grade: A (all verified), B (some unverified non-load-bearing), C (load-bearing unverified), F (any false).

## Output schema

```
## Fact-check — {artifact} — {trust grade}

| # | Claim (verbatim) | Verdict | Source / how to verify | Load-bearing? |
|---|------------------|---------|------------------------|---------------|
| 1 | "AI adoption grew 40% YoY" | unverified | Need McKinsey 2026 State of AI | yes |
| 2 | "I worked at Microsoft" | true | LinkedIn profile | n/a — anonymity rule, REMOVE |

### Verdict
- [ ] Pass — publish
- [ ] Block — fix items: {list of #}
- [ ] Pass with redactions — remove items: {list of #}

### Time to fully verify open items
{N} minutes
```

## Hard rules

- Numbers always need a source. "Roughly" / "about" doesn't excuse a missing citation.
- Personal anecdotes don't need citation but DO trigger the firewall check (anonymity, employer mention).
- If artifact cites a source you cannot reach, mark it `unverified` and ask for the original document.
- Opinion claims pass — but flag them as opinions if presented as facts.
- Never auto-edit the artifact. Output is read-only; operator edits.
