# Validation Matrix

## Objective
Provide a consistent, explicit standard for proving task correctness and readiness.

## Universal Checks
Run all checks that apply to the task and repository stack:
- Unit tests
- Integration tests
- Lint
- Formatting check
- Typecheck
- Build
- Smoke test
- Manual acceptance check

If a check is not applicable, mark it `N/A` with a brief reason.

## Required Reporting Format
Report validation in a matrix table:
- Check name
- Command
- Result (`PASS`, `FAIL`, `N/A`, `BLOCKED`)
- Notes/evidence

Also include:
- Summary pass rate
- Any blocked checks and required follow-up

## Example Validation Matrix
| Check | Command | Result | Notes |
|---|---|---|---|
| Unit tests | `pytest -q` | PASS | All tests passed. |
| Integration tests | `pytest tests/integration -q` | N/A | No integration suite exists. |
| Lint | `ruff check .` | PASS | No violations. |
| Formatting | `ruff format --check .` | PASS | Formatting clean. |
| Typecheck | `mypy .` | N/A | Typecheck not configured. |
| Build | `npm run build` | PASS | Build artifact produced. |
| Smoke test | `npm run start:smoke` | PASS | App starts and health endpoint is OK. |
| Manual acceptance | See checklist | PASS | Required acceptance items verified. |

## Acceptance Checklist Template
- [ ] Objective met at defined end point.
- [ ] In-scope items completed.
- [ ] Out-of-scope boundaries respected.
- [ ] Required validation checks passed or explicitly marked N/A/BLOCKED.
- [ ] Security-sensitive changes reviewed.
- [ ] Documentation updated.
- [ ] Rollback notes captured.
