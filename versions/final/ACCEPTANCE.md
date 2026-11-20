# Acceptance criteria

| ID | Criterion | How verified |
|----|-----------|--------------|
| AC1 | Category tax rates stay: food +5%, transport +12%, entertainment +20%, other 0% | `pytest` (tests/test_calculator.py) |
| AC2 | `add` stores an expense and `list` shows it after restart | manual CLI run in a temp dir |
| AC3 | `report` prints total and average; on an empty database it does not crash | manual CLI run in a temp dir |
| AC4 | The 3 baseline tests keep passing and mypy stays clean | `pytest -q`, `mypy expense_tracker` |
