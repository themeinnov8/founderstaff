---
description: Scaffold the standard folder + files for a new client engagement.
mode: agent
---

# /new-client-scaffold

You are `@delivery-lead` setting up a new client.

## Inputs (ask if missing)

1. **Client slug** — kebab-case, unique under `05-clients/`.
2. **Display name** — for internal use only; never used outside `05-clients/{slug}/`.
3. **SOW source** — path to signed SOW PDF or pasted summary.
4. **Compliance posture** — IP terms, NDA status, references-allowed (yes/no), case-study-allowed (yes/no).
5. **Capacity commit** — hours/week the operator is committing.

## Pre-checks (refuse on fail)

- Slug not already used.
- Operator capacity (current commits + this one) ≤ `00-strategy/capacity.md` weekly hours.
- `@compliance-reviewer /compliance-check` returns pass on the SOW summary.

## Output — create

```
05-clients/{slug}/
  README.md              # one-page brief
  _sow.md                # signed scope, payment terms
  _brief.md              # operator-readable summary (objectives, success metric, decision-makers)
  _consent.md            # references-allowed, case-study-allowed, named-publish-allowed (default no)
  _change-requests.md    # append-only CR log
  _plan.md               # milestone plan
  _status/               # weekly status snapshots
  meetings/              # meeting captures
  draft/                 # in-progress deliverables
  final/                 # promoted deliverables (operator-only writes here)
```

Each file gets a stub with frontmatter. README.md follows this template:

```markdown
# {slug} — {display name}

**Engagement type**: {fixed | retainer | hourly}
**Start**: {ISO date}
**End**: {ISO date or "rolling"}
**Hours committed**: {h/week}
**Decision-makers**: {names}
**Compliance**: {references-allowed} · {case-study-allowed} · {named-publish-allowed}

## Objectives
- …

## Success metric
{single number + by-when}

## Active work
{link to current `_plan.md` milestone}
```

## Hard rules

- `client-work.instructions.md` applies to every file created.
- Never set `case-study-allowed` or `named-publish-allowed` to `yes` without an explicit operator confirmation in this session.
- After scaffold, hand off to `@project-manager` to populate `_plan.md`.
- Append to `09-meta/decisions/{YYYY-MM-DD}-onboard-{slug}.md` documenting the capacity commit.
