# Contributing to founderstaff

Thanks for the interest. This platform grows through real use — every generated OS that ships an improvement back here makes the next clone better.

## What's in scope for contributions

| Welcomed | Out of scope |
|---|---|
| New standard agents (chatmodes, prompts, instructions) that generalize beyond one venture | Venture-specific agents — those belong in your generated OS as `agent-forge` outputs |
| Improvements to the planner templates (proposal, clarifying questions, plan) | Removing safety guardrails (firewall, research-quality, compliance) |
| New scaffolding folders or per-folder READMEs | Adding folders without a clear lifecycle owner |
| Documentation, prompt-writing examples, case studies | Generic AI hype content |
| Bug fixes, typo fixes, broken-link fixes | Style-only changes without a maintenance rationale |

## Adding a new standard agent

Standard agents are bundled into every generated OS by default. The bar is high. Before opening a PR:

### 1. Justify against the existing library

Run this checklist:

- [ ] No existing chatmode/prompt can be extended to cover this with ≤1 new section or arg.
- [ ] The use case is recurring (not one-off) and applies across ≥3 different venture types.
- [ ] The agent has clearly scoped read/write boundaries.
- [ ] Hard rules are explicit. No empty-rules submissions.

### 2. Use `/forge-agent` to generate the candidate

The platform's own meta-skill is the authoritative way to draft a new agent. From a workspace that has `founderstaff/skills/` available, invoke `/forge-agent` and follow its self-check. Paste the output into your PR.

### 3. Write a justification doc

Add a brief at `docs/proposals/{date}-{agent-name}.md`:

```markdown
# Proposal: {agent-name}
- **Why now:** what triggered this need?
- **Existing coverage gap:** which existing agent could NOT be extended? Why?
- **Across-venture utility:** name ≥3 hypothetical ventures that benefit
- **Maintenance owner:** GitHub handle willing to triage issues for this agent
- **Versioning:** does this break compat with existing generated OSes?
```

### 4. Open the PR

PR title: `feat(skills): add {agent-name} {chatmode|prompt|instructions}`

Maintainers review for:
- Convention alignment (frontmatter, scope declarations, hard rules)
- Cross-references actually exist
- No `{{TOKEN}}` leaks
- Justification is real

## Improving the planner

Planner changes affect every future clone. Process:

1. Open an issue first describing the problem you hit during a real planning session.
2. If accepted, PR the template change *plus* an example showing the before/after on a real proposal (anonymize).
3. Bump `planner` version in `version.json` per SemVer:
   - **Patch:** wording fixes
   - **Minor:** new optional fields/questions
   - **Major:** changing the stage shape, removing fields, renaming files

## Versioning policy

| Layer | Bump on |
|---|---|
| `planner` | template structure changes |
| `skills` | new/removed standard agents |
| `scaffolding` | folder-tree changes |
| top-level `version` | any of the above (highest of the three) |

Generated OSes pin to a planner version. Major bumps require migration notes.

## Style

- Markdown only. No HTML in agent files (except `plan.html`-style visualizations under `scaffolding/09-meta/dashboard/`).
- ATX headings (`#`, not `===`).
- Tables for any structured 2D content. Lists for sequences.
- No emoji in agent file content. Emoji OK in README and docs.

## Code of conduct

Be useful. Disagree with the artifact, not the contributor. Cite your sources.
