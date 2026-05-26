# Testing

## 1. Current coverage

### Manual smoke tests (passing as of 2026-05-22)

| # | Scenario | Status |
|---|---|---|
| S1 | Fresh workspace + sync installs 13 skills | ✅ |
| S2 | Second sync is silent (idempotent) | ✅ |
| S3 | `--status` lists resolved skills without writing | ✅ |
| S4 | Lockfile records post-substitution sha256 | ✅ |
| S5 | Cache directory created at `~/.founderstaff/cache/<slug>/` | ✅ |
| S6 | `git pull origin main` works against local file:// upstream | ✅ |
| S7 | Bytes-mode write avoids CRLF hash mismatch on Windows | ✅ |

### Automated tests

**None yet.** This is the most important v0.2 deliverable.

## 2. Test plan — v0.2 priority order

### T1 — Resolver: transitive dependency closure
- **Given:** manifest with pack `research`
- **When:** `resolve_skills()` runs
- **Then:** result includes `research-quality` (a `depends_on` of `market-research`) even though it's not listed directly.

### T2 — Resolver: disabled_skills wins over pack inclusion
- **Given:** pack `core` includes `chief-of-staff`; manifest's `disabled_skills` contains `chief-of-staff`
- **When:** resolve
- **Then:** result does NOT include `chief-of-staff`.

### T3 — Resolver: missing pack prints warning, continues
- **Given:** manifest's `packs` includes a nonexistent pack id
- **When:** resolve
- **Then:** stderr warns, return list still contains skills from valid packs.

### T4 — Resolver: cyclic deps don't infinite-loop
- **Given:** skill A `depends_on: [B]`, skill B `depends_on: [A]`
- **When:** resolve from pack containing A
- **Then:** terminates, both A and B included exactly once.

### T5 — Apply: idempotent
- **Given:** lockfile in sync with on-disk state
- **When:** apply runs
- **Then:** zero `install`/`update` lines; lockfile bytes-identical pre and post.

### T6 — Apply: local edit detection
- **Given:** synced file modified after last lockfile write
- **When:** apply runs
- **Then:** prints `! local edit detected ... skipping`; file untouched; lockfile unchanged for that id.

### T7 — Apply: deletion pruning
- **Given:** lockfile contains skill `X`; current resolved skills do not contain `X`; on-disk file matches lockfile hash
- **When:** apply runs
- **Then:** file removed from `.github/`; entry removed from lockfile.

### T8 — Apply: deletion respects local edits
- **Given:** lockfile contains skill `X`; current resolved skills do not contain `X`; on-disk file's hash differs from lockfile hash
- **When:** apply runs (dry-run)
- **Then:** file NOT removed (decision: protect local edits even on prune). *Requires implementation update.*

### T9 — Token substitution: missing tokens left literal
- **Given:** skill body contains `{{UNDEFINED_TOKEN}}`; `platform.config.json` lacks that key
- **When:** substitute
- **Then:** output contains literal `{{UNDEFINED_TOKEN}}`; warning printed.

### T10 — find_workspace walks parents
- **Given:** cwd is `<ws>/02-research/competitors/`; `<ws>/.platform/skills.manifest.yaml` exists
- **When:** `find_workspace()`
- **Then:** returns `<ws>`.

## 3. Suggested test harness

### Layout
```
tests/
├── conftest.py           ← pytest fixtures (tmp_workspace, fake_upstream)
├── test_resolver.py      ← T1–T4
├── test_apply.py         ← T5–T8
├── test_tokens.py        ← T9
├── test_workspace.py     ← T10
└── fixtures/
    ├── mini-upstream/    ← minimal repo with 3 fake skills, 2 fake packs
    └── manifests/
```

### Fixture idea: `fake_upstream`
- A `tmp_path`-rooted git repo with hand-crafted `skills/index.json` and `packs/*.pack.json`.
- `git init -b main; git add .; git commit -m "fixture"` so `git clone` works.
- Tests point manifest at `file://{path}`.

### Fixture idea: `tmp_workspace`
- `tmp_path / "ws"` with `.platform/` populated from a parameterizable manifest.
- Yields the path; cleanup automatic.

### Why pytest
- Stdlib `unittest` would work too, but pytest's fixtures + parametrization fit this style better. **Tests can use pytest as a dev dependency** even though runtime is stdlib-only.

### Adding pytest
1. Create `pyproject.toml` with `[project.optional-dependencies] dev = ["pytest>=8"]`.
2. Run `python -m pip install -e ".[dev]"` (developer-only step).
3. `pytest tests/` becomes the local validation gate.

## 4. CI plan (v0.2+)

GitHub Actions workflow `.github/workflows/test.yml`:
- Trigger: push, PR.
- Matrix: `ubuntu-latest`, `windows-latest`, `macos-latest` × Python 3.10, 3.11, 3.12.
- Steps: checkout → setup-python → `pip install -e ".[dev]"` → `pytest -v`.

## 5. Bigger validation we want eventually

- **Snapshot tests** — synced output for a fixed manifest + fixed upstream commit must be byte-identical across runs and platforms.
- **Fuzz test** the YAML mini-parser against arbitrary inputs.
- **Integration test** the planner: run all 4 stages on a sample idea and validate the output structure.
