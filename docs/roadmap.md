# Roadmap

## v0.1.0 — Alpha scaffold (2026-05-22) — SHIPPED

- [x] Platform repo + license + README
- [x] `skills/` registry with 12 skills migrated from vcc
- [x] `packs/`: `core`, `research` active; `content`, `sales`, `delivery`, `compliance`, `n8n`, `video` stubs
- [x] `planner/` — 4-stage idea→OS pipeline
- [x] `scripts/sync.py` — Python stdlib sync engine
- [x] `scaffolding/.platform/` — workspace control plane template
- [x] `scaffolding/.platform/relearn.py` — one-command wrapper
- [x] `docs/`: architecture, skill-distribution, AGENTS.md, copilot-instructions.md

## v0.2.0 — Content / Sales / Compliance packs

- [ ] Author `content` pack skills: `linkedin-post`, `linkedin-carousel`, `youtube-script`, `newsletter-issue`, `lead-magnet`, `content-voice` instructions, `content-creator` chatmode
- [ ] Author `sales` pack skills: `outreach`, `cold-email`, `discovery-call-prep`, `discovery-call-recap`, `proposal-sow`, `pricing-quote`, `senior-leader-pitch`, `sales-coach` chatmode
- [ ] Author `compliance` pack skills: `firewall` instructions, `public-publishing` prompt, `progress-logging` instructions, `compliance-check` prompt, `compliance-reviewer` chatmode
- [ ] Author `delivery` pack skills: `new-client-scaffold`, `client-brief`, `case-study`, `delivery` chatmode, `client-work` instructions
- [ ] Author `n8n` pack: `n8n-generate-flow`, `n8n-troubleshoot`, `n8n-best-practices` instructions, `n8n-workflow-builder` chatmode
- [ ] `aliases` field in `skills/index.json` for renames
- [ ] Auto-generate `skills/index.json` from frontmatter (tool: `scripts/build_index.py`)
- [ ] Telemetry opt-in (which packs installed; anonymous; just a ping)

## v0.3.0 — Video pack + UX polish

- [ ] Author `video` pack: `video-script`, `video-storyboard`, `voiceover-brief`, `broll-plan`, `shorts-extract`, `video-creator` chatmode
- [ ] `python .platform/relearn.py --init` to bootstrap a fresh workspace
- [ ] Diff view: show before/after of a skill update before applying

## v0.4.0 — Public launch

- [ ] Site at founderstaff.com (lands on README + quickstart video)
- [ ] `pipx install founderstaff` packaging (so `founderstaff relearn` works globally)
- [ ] At least 3 public example OSes (anonymized)
- [ ] Contributor guide for community-submitted packs

## Backlog (no version yet)

- [ ] Private upstream auth (PAT-based) for paid packs
- [ ] Version pinning per skill in pack
- [ ] Bisect tool for "which sync broke my OS"
- [ ] Migration helpers when a major skill version ships
- [ ] Web-based pack browser
