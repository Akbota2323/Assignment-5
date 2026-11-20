Assignment #05 - Expense Tracker (source export)

versions/baseline/        original code, 3 tests          (git tag: baseline)
versions/after-refactor/  after Task 03 refactoring, 8    (git tag: after-refactor)
versions/final/           final code, 20 tests, with README, AGENTS.md,
                          ACCEPTANCE.md and docs/ (risk review, risk register,
                          readiness audit, background agent safeguards,
                          release decision)                (git tag: final-docs;
                          code identical to tag: final)
git_history/expense-tracker.bundle  full git history with all tags.
                          Restore: git clone expense-tracker.bundle expense-tracker

How to run (open one version folder in VS Code, then Terminal):
  pip install pytest mypy
  python -m pytest -q
  python -m mypy expense_tracker
Use "py" instead of "python" if "python" is not found on Windows.

Expected: baseline 3 passed; after-refactor 8 passed; final 20 passed; mypy: no issues.
AI assistant used: Claude Sonnet 5.5 (Anthropic), 2026-11-20. See the report for the AI-use record.
