# Task #05: Risk register (baseline version, tag `baseline` + AGENTS.md + refactor)

Scoring: likelihood L (1-3) x impact I (1-3) = score (1-9). Only CONFIRMED findings are ranked; F5 is plausible/unverified (scored for information, not ranked). F8 was UNSUPPORTED and is not registered.
Owner for all items: Bota (sole developer). Source of evidence: docs/RISK_REVIEW.md.

| ID | Category | Cause -> Event -> Consequence | Component | Evidence | L | I | Score | Mitigation | Verification plan | Residual risk |
|----|----------|-------------------------------|-----------|----------|---|---|-------|-----------|-------------------|---------------|
| F1 | correctness | `average` divides by `len(expenses)` -> user runs `report` on empty DB -> crash, AC3 violated | calculator.average, cli | `report` in empty dir -> ZeroDivisionError | 3 | 2 | 6 | Return 0.0 (or message) for empty list | New pytest + CLI run on empty dir | Low: none expected |
| F2 | correctness | No amount validation -> negative/zero/NaN amount added -> silently wrong totals | cli.main | `-50` -> total -52.5; `nan` -> total nan | 2 | 3 | 6 | Reject non-finite and non-positive amounts | pytest + CLI run | Low: float/rounding stays (F6) |
| F3 | correctness | Category not validated -> typo -> expense silently treated as OTHER (no tax) | cli.main, calculator | `transprt` -> `[OTHER]` | 3 | 2 | 6 | Reject unknown categories (same validation as F2) | pytest + CLI run | Low |
| F4 | correctness | storage.load assumes valid JSON schema -> corrupt/edited file -> crash | storage.load | JSONDecodeError, TypeError | 2 | 2 | 4 | Not planned now | - | Medium: remains open |
| F10 | maintainability | cli.py and storage.py untested -> regressions go unnoticed | tests/ | no test imports cli/storage | 2 | 2 | 4 | Partly covered by tests added for F1/F2 | New tests run | Medium |
| F11 | agent operations | Review gates in AGENTS.md not enforced (no CI/pre-commit) -> agent or human skips tests | repo root | no .github, no pre-commit | 2 | 2 | 4 | Not planned now (documented limitation) | - | Medium |
| F6 | correctness | float money -> rounding drift in totals | calculator | 0.30000000000000004 | 3 | 1 | 3 | Not planned (output rounded to 2 places) | - | Low |
| F5 | correctness (unverified) | save truncates file first -> failed write erases data | storage.save | simulation only, real crash not reproduced | 1 | 3 | 3 | Not ranked | - | Unknown |
| F7 | maintainability | DB path relative to cwd -> data "missing" from other folder | storage.DB_FILE | `list` from subfolder: 0 lines | 2 | 1 | 2 | Document in README | - | Low |
| F9 | dependency | `pytest` unpinned, no lock -> future version can break tests | requirements.txt | file content, no lock | 2 | 1 | 2 | Not planned | - | Low |

## Ranking: top 2 confirmed risks for corrective action
Three risks tie at 6 (F1, F2, F3). Tie-break: (1) F1 breaks a stated acceptance criterion (AC3); (2) F2 is silent data corruption (worst failure type) and its fix (input validation) also covers F3.
1. **F1** empty-report crash
2. **F2** invalid amount (fix extended to also reject unknown categories, F3)

Scores will be updated after Task #07 with real test results.

## Update after Task #07 (actual results)
Checks: baseline before mitigations 8 passed, mypy clean; final 20 passed, mypy clean. Not executed: no linter available (ruff/flake8 not installed), CLI missing-argument handling not tested.

| ID | Status | New L | New I | New score | Note |
|----|--------|-------|-------|-----------|------|
| F1 | mitigated (commit 49c7818) | 1 | 2 | 2 | `report` on empty DB prints total 0, average 0.0; AC3 now holds |
| F2 | mitigated (commit 96b726d) | 1 | 3 | 3 | -50, 0, nan rejected with exit code 1 and nothing saved |
| F3 | mitigated (commit 96b726d) | 1 | 2 | 2 | unknown category rejected |
| F10 | partly reduced | 2 | 2 | 4 | cli add/list/report now have tests; storage errors (F4) still untested |
Residual: F4, F5, F6, F7, F9, F11 unchanged. `add x` with missing arguments still raises IndexError (not in scope, newly noted).
