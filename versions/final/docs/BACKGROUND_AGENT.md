# Task #08: Background agent safeguards (hypothetical; no real background agent was run)

## Hypothetical task
"Handle a corrupt or unexpected `expenses.json` in `storage.load` (risk F4) and handle missing CLI arguments in `add` (IndexError), with tests."
Chosen because both are open residual risks and small enough to review in one sitting.

## Isolation
- Fresh git worktree on a new branch from `final`: `git worktree add ../agent-f4 -b agent/f4-storage-errors final`
- No access to `main`, no push rights, no network except package index if a dependency is explicitly approved.
- Runs in a throw-away environment (venv created from `requirements.txt`); no real data, no secrets mounted.

## Allowed
| Item | Allowed |
|------|---------|
| Files to edit | `expense_tracker/storage.py`, `expense_tracker/cli.py`, `tests/test_storage.py` (new), `tests/test_validation.py` |
| Files read-only | everything else, including `AGENTS.md`, `ACCEPTANCE.md`, `docs/` |
| Commands | `python3 -m pytest -q`, `python3 -m mypy expense_tracker`, `git status/diff/log/add/commit` on the agent branch |
| Time limit | 30 minutes wall-clock, max 5 test runs; stop and report when exceeded |
| Size limit | max 80 changed lines outside tests; larger diff means stop and ask |

## Prohibited
- Editing/deleting existing tests, `AGENTS.md`, `ACCEPTANCE.md` or docs
- Changing `requirements.txt` or installing packages
- `git push`, merge to main, rebase/force operations, deleting tags (`baseline`, `final`)
- `rm -rf`, writing outside the worktree, touching real `expenses.json`
- Reading or printing secrets / environment variables; any deployment

## Required artifacts (all attached to the branch/PR)
1. Change summary: what and why, linked to risk IDs
2. `git diff main..agent/f4-storage-errors`
3. Test logs: pytest output before and after (pass/fail counts)
4. mypy result (and lint result if a linter exists)
5. Acceptance check: AC1-AC4 from `ACCEPTANCE.md`, each marked pass/fail
6. Risk notes: new assumptions, anything not executed, updated scores

## Human review and approval
- Nothing merges or deploys without a human reading the full diff and re-running `pytest` and `mypy` locally.
- Reviewer checks: only allowed files changed; no test weakened; new tests fail on the old code; AC1-AC4 pass.
- The agent's own "all tests pass" claim is not accepted without the reviewer's own run.

## Failure and rollback handling
- Time/size limit hit, tests failing, or prohibited action attempted: agent stops, commits nothing further, and writes a failure report (what was tried, last command output).
- Rejected or failed work: delete the branch/worktree (`git worktree remove`, `git branch -D agent/f4-storage-errors`); `main` and tag `final` are untouched, so there is nothing to revert.
- If a bad change was merged by mistake: `git revert <merge-commit>`, rerun checks, and record it in the risk register.
