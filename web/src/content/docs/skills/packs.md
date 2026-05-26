---
title: Packs
description: All 10 packs with versions, sizes, and selection guidance.
---

A **pack** is a curated bundle of related skills. You opt into packs via `.platform/skills.manifest.yaml`:

```yaml
packs:
  - core         # required, always installed
  - research
  - content
  - sales
```

## All packs

| Pack | Version | Skills | Required? | Best for |
|---|---|---|---|---|
| `core` | 0.3.0 | 18 | **always** | Everyone |
| `research` | 0.2.0 | 7 | optional | Any venture making evidence-based decisions |
| `content` | 0.2.0 | 12 | optional | Anyone publishing externally |
| `sales` | 0.2.0 | 9 | optional | Anyone in deal-led GTM |
| `marketing` | 0.2.0 | 6 | optional | Anyone running channels / launches |
| `operations` | 0.2.0 | 6 | optional | Anyone with recurring operational hygiene |
| `delivery` | 0.2.0 | 7 | optional | Anyone running client engagements |
| `compliance` | 0.2.0 | 2 | optional but recommended | Anyone with a day job, regulated industry, or partner conflicts |
| `finance` | 0.2.0 | 4 | optional | Anyone managing P&L / pricing |
| `product` | 0.2.0 | 4 | optional | Anyone building software / digital products |

## Pack selection by persona

| Persona | Recommended packs |
|---|---|
| **Solo AI consultant** (day-job constraint) | `core + research + content + sales + delivery + compliance + finance` |
| **Indie SaaS dev** | `core + product + research + content + marketing + finance` |
| **Content creator** | `core + content + research + marketing` |
| **Local service business** | `core + sales + marketing + operations + finance` |
| **Open-source maintainer** | `core + content + research + product` |

See [examples](/examples/) for full end-to-end walkthroughs of each.

## How packs depend on each other

All packs depend on `core`. Some skills additionally depend on other-pack skills (declared in `skills/index.json#depends_on`). `relearn.py` resolves the dep graph transitively — installing one pack pulls all its dependencies automatically.

Example: installing `delivery` pulls in `content-voice` and `public-publishing` (from `content`) and `fact-check` (from `research`), because the `case-study` prompt depends on them.

## Adding / removing packs

Add:

```bash
python .platform/relearn.py --pack marketing
```

Remove: edit `.platform/skills.manifest.yaml` and remove the pack from the list, then `relearn.py`. The sync engine prunes skills no longer in any installed pack (unless they're in `extra_skills`).

Disable a single skill without removing the pack:

```yaml
packs:
  - content
disabled_skills:
  - youtube-script
```

Add one skill from a pack you haven't installed:

```yaml
packs:
  - core
extra_skills:
  - cold-email   # from sales pack
```
