# Task #04: Read-only risk review (baseline code, no files modified during review)
Reviewer: AI assistant (Claude). Every finding below was checked by running a command; status reflects the result.

| ID | Category | Candidate finding | Status | Evidence |
|----|----------|-------------------|--------|----------|
| F1 | correctness | `report` crashes on empty database | CONFIRMED | `cli report` in empty dir -> `ZeroDivisionError` (calculator.average) |
| F2 | correctness | Negative, zero and NaN amounts accepted | CONFIRMED | `add refund -50 food` accepted; `add nan nan food` made `total: nan` |
| F3 | correctness | Mistyped category silently becomes OTHER | CONFIRMED | `add taxi 10 transprt` -> `[OTHER] taxi` |
| F4 | correctness | Corrupt or unexpected JSON crashes the app | CONFIRMED | `{bad` -> `JSONDecodeError`; extra key -> `TypeError` (storage.load) |
| F5 | correctness (data loss) | `save` truncates file before writing, so a failed write erases data | PLAUSIBLE/UNVERIFIED | Simulated `json.dump` failure left `expenses.json` at 0 bytes; a real crash or disk-full was not reproduced |
| F6 | correctness | Money stored as float | CONFIRMED (low impact) | 3 x 0.1 = `0.30000000000000004`; output is rounded to 2 places |
| F7 | maintainability | DB path is relative to cwd, so data "disappears" from another folder | CONFIRMED (low) | `list` from a subfolder printed 0 lines |
| F8 | security | Code injection or hardcoded secrets | UNSUPPORTED | grep for eval/exec/subprocess/os.system/pickle and password/secret/token/api_key: no matches |
| F9 | dependency | Unpinned dependency, no lock file | CONFIRMED | `requirements.txt` = `pytest` (installed 9.1.1), no lock file |
| F10 | maintainability | No tests for cli.py and storage.py | CONFIRMED | no test file imports cli or storage |
| F11 | agent operations | AGENTS.md review gates are not enforced | CONFIRMED (absence) / consequence PLAUSIBLE | no `.github/`, no `.pre-commit-config.yaml`, no linter installed |

Not verified: whether a specific coding tool auto-loads AGENTS.md.
