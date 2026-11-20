# Task #09: Release decision

Reviewed version: git tag `final` (commit 96b726d) plus docs up to 81eac40. Code identical to `final`.

## Decision: CONDITIONAL

## Evidence
| Source | Result |
|--------|--------|
| Tests | `pytest -q`: 20 passed (baseline was 8 passed); mypy clean |
| Acceptance criteria | AC1-AC4 all pass (AC3 failed at baseline, fixed by M1) |
| Risk register | Top 2 risks (F1, F2) mitigated and re-scored 2 and 3; F3 also mitigated. No open confirmed risk scores above 4 |
| Readiness audit | Level 2 (Documented); not level 3 |
| Not executed | Lint (no linter), storage-error and missing-argument tests, real crash test for F5 |

## Why not GO
Critical checks pass, but "no unacceptable unresolved risks" is not fully demonstrated: F4 (corrupt JSON crashes) and the missing-argument IndexError are still open, F5 (data loss on failed write) is unverified, and nothing enforces the checks automatically (no CI, no linter, unpinned dependencies).

## Why not NO-GO
No risk scores above 4 remains open. The tool is a small local CLI with no network, no secrets and no real personal data. All critical verification that exists passes and was run, not assumed.

## Conditions (owner: Bota)
| # | Condition | Controls the risk | Verification |
|---|-----------|-------------------|--------------|
| 1 | Use only with a local, non-critical `expenses.json`; keep a manual backup | F4, F5 | file backed up before use |
| 2 | Fix F4 and the missing-argument IndexError with tests (see BACKGROUND_AGENT.md plan) | F4 | new tests fail on old code, pass on new |
| 3 | Add mypy and a linter to a pinned dev requirements file and run them in a fresh env | F11, readiness gap | fresh clone runs all AGENTS.md commands |
| 4 | Reproduce or rule out F5 with a real interrupted write; if confirmed, write via temp file + rename | F5 | test or documented experiment |

Release stays CONDITIONAL until 1 is in place; it can move to GO when 2-4 are done and checks are re-run.
