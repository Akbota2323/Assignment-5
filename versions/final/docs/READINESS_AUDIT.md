# Task #06: Agent-readiness audit (version tagged `final` + risk register update)

| Area | Observation (evidence) | Result |
|------|------------------------|--------|
| Readable structure | 4 small modules, one responsibility each, architecture described in AGENTS.md; category rules in one table | OK |
| README accuracy | Run/test commands work. Missing: list of valid categories, validation behavior, Python version, setup/venv steps, mypy | Partial |
| Reproducible setup | Fresh `git clone` + venv + `pip install -r requirements.txt` + `pytest` -> 20 passed | OK |
| Pinned dependencies | `requirements.txt` = `pytest` (no version), no lock file | Missing |
| Tests | 20 tests; cover calculator, validation, CLI add/list/report. NOT covered: storage errors (corrupt JSON), CLI missing arguments | Partial |
| Type check | mypy clean locally, BUT mypy is not in requirements.txt: `python -m mypy` fails in a fresh env ("No module named mypy") although AGENTS.md lists it as a safe command | Gap (found in this audit) |
| Lint | No linter configured or installed | Missing |
| Build | No build step / pyproject.toml (CLI runs directly) | N/A / missing packaging |
| Logging | None (`grep logging` -> no matches) | Missing |
| Security safeguards | No secrets (grep clean), no eval/subprocess, `expenses.json` in .gitignore; input validation added (M2). No dependency scanning | Partial |
| AGENTS.md | Has purpose, architecture, setup, safe commands, commands needing approval, forbidden actions, conventions, test expectations, review gates | OK |
| Enforcement of AGENTS.md rules | No CI, no pre-commit; gates rely on human discipline. Whether a given tool auto-loads AGENTS.md was not verified | Missing |

## Readiness level: 2 (Documented)
Justification: the repo is understandable, has accurate-enough run/test commands, working tests and a complete AGENTS.md with permissions and prohibitions. It is not level 3 (Agent-ready) because an agent cannot verify its own work end to end without extra setup: mypy is not installed by the documented setup, there is no linter, dependencies are unpinned, and nothing (CI/pre-commit) enforces the review gates.

## Missing evidence / needed for level 3
1. Add mypy (and a linter) to a pinned dev requirements file; confirm fresh-env run of every command listed in AGENTS.md.
2. Pin dependency versions.
3. CI or pre-commit running pytest + mypy + lint.
4. Tests for storage errors and CLI missing arguments (F4 and the IndexError).
5. Confirm the chosen agent tool actually loads AGENTS.md (otherwise paste the instructions and disclose it).
