# AGENTS.md

## Purpose
Expense Tracker: small Python CLI to record expenses and report totals with a per-category tax. Educational project (Assignment #05); contains no real or personal data.

## Architecture
- `expense_tracker/cli.py`: entry point, parses argv, calls storage and calculator.
- `expense_tracker/calculator.py`: tax per category, labels, total, average.
- `expense_tracker/storage.py`: load/save `expenses.json` in the current directory.
- `expense_tracker/models.py`: `Expense` dataclass.
- `tests/`: pytest tests. Keep business logic out of `cli.py`.

## Setup
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt

## Safe commands (run freely)
    python3 -m pytest -q
    python3 -m mypy expense_tracker
    git status / git diff / git log
    python3 -m expense_tracker.cli list | report   (run in a temp dir, not the repo root)

## Commands needing human approval
- `git commit`, `git push`, branch/merge operations
- `pip install` of any new package or version change in `requirements.txt`
- Any command that writes outside this repository

## Forbidden
- No secrets, tokens, or real personal/financial data in code, tests, or logs.
- No production deployment or publishing.
- No destructive commands (`rm -rf`, `git reset --hard`, `git push --force`, deleting `.git` or the `baseline` tag).
- No unreviewed dependency changes.
- Do not edit or delete existing tests to make them pass.
- Do not fabricate test results; report actual command output.

## Coding conventions
- Python 3.13, type hints on all functions, mypy must stay clean.
- Small functions, no duplicated category conditionals (add new categories in one place).
- Handle bad input with clear errors, not tracebacks.

## Test expectations
- Every behavior change comes with a test. Run `pytest` and `mypy` before and after changes and record both outputs.
- Acceptance criteria in `ACCEPTANCE.md` must hold after every change.

## Review gates
- One focused change per commit; a human reviews each diff before it is accepted.
- AI-generated findings are unverified until reproduced by a command or a code reference.
