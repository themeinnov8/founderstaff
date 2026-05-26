# Spec — founderstaff

This folder is the **single source of truth** for what founderstaff must do, how it's designed, and how it's currently implemented. A new agent (or human) reading this folder cover-to-cover can resume any in-flight work.

## Read order

1. [requirements.md](requirements.md) — *what* and *why*. Functional + non-functional contract.
2. [design.md](design.md) — *how (architecturally)*. Components, data flow, schemas, invariants.
3. [implementation.md](implementation.md) — *how (in code)*. File-by-file map, key functions, gotchas.
4. [examples.md](examples.md) — six walkthroughs covering common and edge-case flows.
5. [testing.md](testing.md) — current test coverage + the next 10 test cases to write.

## When to update

| Change | Update |
|---|---|
| New functional requirement | `requirements.md` first, then code |
| New component / data structure | `design.md` first, then code |
| Code change | `implementation.md` (file-map) |
| New flow worth showing | `examples.md` |
| New test | `testing.md` (move from "pending" → "shipped") |

## Relationship to other docs

| Doc | Lives in | Audience |
|---|---|---|
| Marketing / quickstart | [../README.md](../README.md) | end users |
| Agent context | [../AGENTS.md](../AGENTS.md) | AI coding agents |
| Decision log + diagrams | [../docs/architecture.md](../docs/architecture.md) | contributors |
| Authoritative protocol | [../docs/skill-distribution.md](../docs/skill-distribution.md) | sync engine maintainers |
| Roadmap | [../docs/roadmap.md](../docs/roadmap.md) | release manager |
| **THIS spec/** | here | anyone resuming work |

When `spec/` disagrees with `docs/`, **`spec/` wins** — it's the contract.
