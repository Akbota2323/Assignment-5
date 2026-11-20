# Expense Tracker

Small command-line tool to record expenses and show totals. A per-category tax is applied to every expense.

## Requirements
- Python 3.13 (earlier 3.x versions were not tested)
- `pytest` (listed in `requirements.txt`); `mypy` is optional, for type checks

## Setup
    python3 -m venv .venv
    source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\activate
    pip install -r requirements.txt
    pip install mypy                   # only for the type check

## Usage
    python -m expense_tracker.cli add <description> <amount> <category>
    python -m expense_tracker.cli list
    python -m expense_tracker.cli report

Data is stored in `expenses.json` in the **current folder**; running from another folder uses another file.

### Categories and tax
| Category | Tax |
| --- | --- |
| food | +5% |
| transport | +12% |
| entertainment | +20% |
| other | 0% |

### Input validation
`add` rejects (with an `error:` message and exit code 1, nothing saved): an amount that is not a positive number (zero, negative, NaN, infinity), a category not in the table above, and an empty description. `report` on an empty database prints total 0 and average 0.0.

## Checks
    python -m pytest -q
    python -m mypy expense_tracker

## Agent instructions
See `AGENTS.md` (rules for coding agents) and `ACCEPTANCE.md` (criteria that must stay true).

## Known limitations
A corrupt `expenses.json` and `add` with missing arguments still raise errors. There is no linter or CI. See `docs/` for the risk register and release decision.
