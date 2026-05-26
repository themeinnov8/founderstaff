---
title: Creating new skills
description: When (and when not) to forge a new skill. The MECE-gated hiring flow.
---

import { Aside } from '@astrojs/starlight/components';

founderstaff is **opinionated about not adding skills**. Every new skill is an asset to maintain and a surface for the operator to remember. The default answer to "should I add a new skill?" is **no**.

## The hiring flow

When you have a need that feels like "I wish there was an agent for this", invoke `@hiring-manager`:

```
> @hiring-manager
> I need someone who can do competitor pricing analysis weekly.
```

The hiring manager runs a 4-step triage:

### 1. Parse the need

Restates it in one sentence. Asks ONE clarifying question if genuinely ambiguous.

### 2. Roster scan

Reads every installed skill and scores each against the need:

| Score | Meaning |
|---|---|
| `exact-fit` | A skill already does this. Use it. |
| `partial-fit` | A skill comes close; gap is in prompt/instructions, not persona. |
| `adjacent` | Nearby but not aligned. Composition might cover it. |
| `no-fit` | Truly absent. |

### 3. MECE test (only if scan suggests a possible hire)

**Mutually exclusive (ME) check**: list every existing skill whose scope brushes against the need. For each, state the exact scope boundary and where the proposed hire would NOT overlap. If you cannot draw a clean line → fail → outcome B (adapt) or D (don't hire).

**Collectively exhaustive (CE) check**: describe the smallest composition of existing skills that comes closest. State precisely what that composition cannot do that the new role would. "Slightly better at X" fails. The gap must be **categorical**.

Both checks must pass in writing.

### 4. Pattern check

Verify ≥ 3 prior occurrences of this need in `09-meta/hires.md` / `09-meta/daily-log.md`, OR a clearly recurring workflow (named cadence, e.g., quarterly board prep). One-off needs always fail this check → outcome D.

## Outcomes

The hiring manager recommends exactly one of:

| Outcome | Meaning |
|---|---|
| **A. Invoke existing** | There's an `exact-fit`. Use it. |
| **B. Adapt existing** | A `partial-fit` exists; edit a prompt or instruction. |
| **C. Hire new** | MECE + pattern checks both passed. Proposal: `id`, `pack`, `type`, scope, value. |
| **D. Don't hire** | Failed a check, or one-off, or operator's job. |

## Confirmation gate

For outcomes B and C, the hiring manager asks:

> Confirm `{outcome}` to proceed. Reply `confirm` to continue, `revise` to discuss, or `cancel` to log as D.

It does **not** auto-proceed. On `confirm` for C → runs `/hire-skill` (which itself has another `confirm forge` gate). On `confirm` for B → produces the diff for the operator to apply.

## Why the friction is the feature

<Aside type="tip" title="Selective hiring prevents bloat">
Without the MECE + pattern + dual-confirmation gates, the platform accumulates dozens of slightly-different skills that overlap and conflict. Operators stop remembering what's available. The roster becomes noise. By making hiring expensive, founderstaff keeps the library curated and the operator's mental model intact.
</Aside>

## If you've passed the gates

`/hire-skill` writes a forge-spec to `09-meta/forge-specs/{id}.md` — a contract for `@agent-forge` to implement. The forge-spec includes:

- Skill ID, pack, type (chatmode/prompt/instructions)
- One-line description
- Tools whitelist (chatmodes only)
- Allowed write scope
- Hard rules (≤ 10)
- Cross-references (other skills it depends on)

Then `@agent-forge`:

1. Drafts the file with correct YAML frontmatter
2. Runs `/compliance-check` on the draft
3. Writes to `.claude/agents/` or `.github/chatmodes/` (per host)
4. Appends to `09-meta/hires.md`
5. (If contributing back) opens a PR to upstream `skills/{pack}/{type}/`

## Contributing a skill upstream

If your forged skill is generally useful, PR it to `themeinnov8/founderstaff`:

1. File lands in `skills/<pack>/<type>/<id>.<type>.md`
2. Add entry to `skills/index.json` (id, type, path, version, summary, tags, depends_on, requires_tokens)
3. Add ID to relevant `packs/<pack>.pack.json#skills`
4. Bump pack version (minor for additive)
5. CHANGELOG entry
6. Smoke test: `python scripts/sync.py --status` in a test workspace
