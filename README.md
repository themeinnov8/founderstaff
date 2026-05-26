# founderstaff

> **An operating system for founders.** Clone, answer 12 questions, get an executable business plan + a complete agent-powered workspace to run it. Self-evolving — new agents and skills check in here.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: alpha](https://img.shields.io/badge/status-alpha-orange.svg)](#)
[![Version: 0.1.0](https://img.shields.io/badge/version-0.1.0-blue.svg)](version.json)

🌐 [founderstaff.com](https://founderstaff.com) *(coming soon)*

---

## Why this exists

Most founders fail at execution, not ideas. They lose to:

- **Decision fatigue** — too many small choices, not enough budget for them.
- **Scattered state** — plan in Notion, leads in a spreadsheet, content in drafts folder, decisions in their head.
- **Solo blind spots** — no chief of staff, no red-teamer, no research analyst.
- **Compliance drift** — especially when running a venture alongside a day job.

`founderstaff` turns a half-formed idea into a working business OS in a few hours:

1. **Intake** — proposal template, ~45 min
2. **Brainstorm** — 12 clarifying questions, 60–90 min call
3. **Plan** — structured plan + visual dashboard, ~90 min
4. **Generate** — agent scaffolds the full workspace (folders, guardrails, 10 chatmodes, 30+ prompts), 2–3 hours
5. **Run** — founder operates with `chief-of-staff`, `red-team`, `research-analyst`, `dashboard-generator`, `agent-forge` and more, with all guardrails on
6. **Evolve** — when a gap shows up, `agent-forge` creates new chatmodes/prompts safely. Learnings flow back here via PR.

---

## What's in this repo

```
founderstaff/
├── planner/         4-stage flow: intake → brainstorm → plan → generate (+ 04-evolve)
├── skills/          standard agent library (instructions, prompts, chatmodes)
├── scaffolding/     numbered folder skeleton (00-strategy … 09-meta) + READMEs
├── docs/            architecture, prompt-writing guide, self-evolution
├── examples/        reference clones (e.g., outcome-stack — link to public case study)
└── version.json     semver pin
```

Standard agent library bundled:

| Type | Agents |
|---|---|
| Chatmodes | `chief-of-staff` · `dashboard-generator` · `research-analyst` · `red-team` · `agent-forge` *(+ generated per venture: `strategist`, `content-creator`, `sales-coach`, `delivery`, `compliance-reviewer`)* |
| Prompts | `/next-best-action` · `/refresh-dashboard` · `/market-research` · `/customer-interview` · `/fact-check` · `/red-team` · `/forge-agent` *(+ generated content, sales, delivery, ops, compliance factories)* |
| Instructions | `research-quality` *(+ generated per venture: `firewall`, `content-voice`, `outreach`, `client-work`, `public-publishing`, `progress-logging`)* |

> Some standard agents are *generated* for a new OS rather than copy-pasted, because they need parametric values (e.g., the firewall instructions get strictness level and employer name from the plan).

---

## Two workflows

founderstaff is used in two ways:

| Workflow | Audience | What it does |
|---|---|---|
| **A. Install skills** (`relearn`) | Anyone running a business | Pulls curated AI skills into `.github/` of your workspace so Copilot uses them |
| **B. Generate a new OS** (planner) | Someone starting a new venture | 4-stage idea→OS pipeline: intake → brainstorm → plan → generate |

Most users start with A. Use B when you want a venture-tailored OS from scratch.

---

## Workflow A — Install skills into an existing workspace

**Use this if** you already have a project folder and just want Copilot to gain `@chief-of-staff`, `/next-best-action`, etc.

### Prerequisites

founderstaff has **no package dependencies** — `sync.py` and `relearn.py` use only the Python standard library (hard constraint, see [AGENTS.md](AGENTS.md)). There is no `requirements.txt`, no `pip install` step, no virtualenv to manage.

What you do need on a clean machine:

| Tool | Min version | Why | Verify |
|---|---|---|---|
| **Python** | 3.10+ | Runs `relearn.py` / `sync.py` | `python --version` |
| **Git** | 2.30+ | Sync engine uses `git pull` against a cache clone | `git --version` |
| **VS Code** | 1.90+ | Host for the generated `.github/` skills | `code --version` |
| **GitHub Copilot** extension | latest | Auto-discovers chatmodes/prompts/instructions | Sign in inside VS Code |

#### Install on a fresh machine

**Windows** (PowerShell, requires [winget](https://learn.microsoft.com/windows/package-manager/winget/)):
```powershell
winget install --id Python.Python.3.12 -e
winget install --id Git.Git -e
winget install --id Microsoft.VisualStudioCode -e
# Then in VS Code: install the "GitHub Copilot" + "GitHub Copilot Chat" extensions and sign in.
```

**macOS** (requires [Homebrew](https://brew.sh)):
```bash
brew install python git
brew install --cask visual-studio-code
# Then in VS Code: install "GitHub Copilot" + "GitHub Copilot Chat" and sign in.
```

**Linux** (Debian/Ubuntu):
```bash
sudo apt update
sudo apt install -y python3 python3-venv git
# VS Code: see https://code.visualstudio.com/docs/setup/linux
# Then install "GitHub Copilot" + "GitHub Copilot Chat" extensions and sign in.
```

> On Windows, the `python` command may be aliased to a Microsoft Store stub. If `python --version` opens the Store, run `py --version` instead, or disable the alias under **Settings → Apps → App execution aliases**.

That's it — no founderstaff-specific dependencies to install.

### Steps

```bash
# 1. From inside your project folder, create .platform/
mkdir .platform

# 2. Copy the four scaffolding files (one-time)
#    (Replace <fs> with the path to a local clone, or download raw from GitHub.)
cp <fs>/scaffolding/.platform/skills.manifest.yaml         .platform/
cp <fs>/scaffolding/.platform/platform.config.json.template .platform/platform.config.json
cp <fs>/scaffolding/.platform/relearn.py                    .platform/
cp <fs>/scaffolding/.platform/README.md                     .platform/

# 3. Fill in your tokens
#    (edit .platform/platform.config.json — BRAND, OPERATOR, etc.)

# 4. Install skills
python .platform/relearn.py
```

You'll see something like:

```
[relearn] cloning https://github.com/themeinnov8/founderstaff.git
[founderstaff] syncing 13 skills into <your-workspace>
  install: chief-of-staff v0.1.0 -> .github/chatmodes/chief-of-staff.chatmode.md
  install: next-best-action v0.1.0 -> .github/prompts/next-best-action.prompt.md
  ...
[founderstaff] lockfile updated
[founderstaff] done.
```

Open VS Code in this workspace and Copilot will auto-discover the skills.

### Day-2 commands

| Command | What it does |
|---|---|
| `python .platform/relearn.py` | Pull latest, re-sync |
| `python .platform/relearn.py --status` | List installed skills + versions |
| `python .platform/relearn.py --dry-run` | Show what would change |
| `python .platform/relearn.py --pack n8n` | Add a pack to manifest, then sync |

To **disable** a skill: add its id to `.platform/skills.manifest.yaml` under `disabled_skills:` and re-sync.

To **protect a local edit**: just edit the file. The sync engine hash-checks and skips locally-modified files with a warning. To accept an upstream update later, delete the file and re-sync.

See [spec/examples.md](spec/examples.md) for six end-to-end walkthroughs (fresh install, adding packs, local-edit protection, contributor flow, etc.).

---

## Workflow B — Generate a brand-new business OS from an idea

**Use this if** you're starting a new venture and want a venture-tailored folder structure, dashboard, and agent roster generated end-to-end.

```bash
# 1. Clone the platform
git clone https://github.com/themeinnov8/founderstaff.git my-venture-planning
cd my-venture-planning

# 2. Fill out the proposal (00-intake)
cp planner/00-intake/proposal-template.md planner/00-intake/proposal.md
# open it, fill 10 sections — see planner/README.md

# 3. Brainstorm (01-brainstorm) — 12 clarifying questions, 4 blocks
# Capture answers in planner/01-brainstorm/transcript.md

# 4. Write the plan (02-plan)
cp planner/02-plan/plan-template.md planner/02-plan/plan.md
# fill all 10 sections, especially §7 custom agents and §10 generation params

# 5. Generate the OS in a fresh sibling directory
mkdir ../my-venture-os
# Open ../my-venture-os in VS Code with a Copilot agent session,
# paste the contents of planner/03-generate/seed-prompt.md as the first message.
```

Full walkthrough: [docs/architecture.md](docs/architecture.md).

---

## Design principles

1. **Time-first, revenue-second.** Default config assumes 5–10 hours/week. Guardrails refuse to recommend over-budget work.
2. **Cheap markdown, rich HTML.** Working state lives in MD files. Anything that benefits from "see at a glance" is regenerated as HTML on demand.
3. **Scoped agents.** Every chatmode declares minimum read/write scope. `agent-forge` rejects requests for unrestricted access.
4. **Compliance baseline.** Every generated OS gets a firewall instructions file. Especially important for operators with day jobs.
5. **Never invent.** Research-quality guardrails enforce citation, confidence levels, recency. No fabricated statistics.
6. **Self-evolution as code.** New agents check in as PRs. The platform improves through use.
7. **One next action.** `chief-of-staff` always returns ONE action with reasoning, never a buffet.

---

## For contributors and AI coding agents

If you (human or AI) are picking up work on founderstaff itself:

1. Read [AGENTS.md](AGENTS.md) first — mental model, repo map, hard constraints.
2. Read [spec/](spec/) cover to cover — requirements, design, implementation map, examples, tests.
3. Check [docs/roadmap.md](docs/roadmap.md) for the current sprint.
4. From a Copilot chat in this repo, invoke `/continue-building` (see [.github/prompts/continue-building.prompt.md](.github/prompts/continue-building.prompt.md)) for a guided resume.

The `spec/` folder is the **contract**. When code and `spec/` disagree, the spec wins until explicitly updated.

---

## Roadmap

- [x] **v0.1** — planner (4 stages), 5 platform chatmodes + 5 generated, 30+ prompts, dashboard generator, scaffolding skeleton
- [ ] **v0.2** — example OS gallery; automated validation script; OpenAI API automation kit (`08-automation/`); operating manual generator
- [ ] **v0.3** — webapp at founderstaff.com (paid intake → managed planning sessions)
- [ ] **v0.4** — multi-venture mode (operator running 2+ generated OSes in parallel)

See [CHANGELOG.md](CHANGELOG.md) for releases.

---

## Contributing

This platform improves when generated OSes feed learnings back. See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- How to propose a new standard agent
- The "agent justification" template (why does this belong in the standard library vs. as a per-venture custom?)
- How `agent-forge` validates contributions
- Versioning policy

---

## License

MIT — see [LICENSE](LICENSE). Use this for any venture, commercial or otherwise. Attribution appreciated but not required.

---

## Acknowledgements

Born out of *outcome-stack* — one operator's attempt to build an AI consultancy alongside a day job. The platform exists because the first operator couldn't keep the plan, agents, clients, and content in their head simultaneously. Now nobody has to.
