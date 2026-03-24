# Validation Matrix

## Objective
Provide a uniform method to prove implementation quality, report evidence, and separate introduced failures from pre-existing issues.

## Applicability Rule
Run every check that is applicable to the task and repository stack. For non-trivial/high-risk tasks, planned checks must be listed in the ExecPlan before Implementation.

## Universal Check Categories
- Unit tests
- Integration tests
- Lint
- Formatting check
- Typecheck
- Build
- Smoke test
- Manual acceptance check

If a check is not run, mark it `N/A` or `BLOCKED` with reason and impact.

## Required Reporting Format
Use a table with:
- Check
- Command
- Result (`PASS`, `FAIL`, `N/A`, `BLOCKED`)
- Notes/Evidence

Also report:
- summary outcome
- blockers and required follow-up
- distinction between pre-existing failures and introduced failures

## Example Validation Matrix
| Check | Command | Result | Notes/Evidence |
|---|---|---|---|
| Unit tests | `pytest -q` | PASS | All tests passed. |
| Integration tests | `pytest tests/integration -q` | N/A | No integration test suite exists. |
| Lint | `ruff check .` | PASS | No violations. |
| Formatting check | `ruff format --check .` | PASS | Formatting clean. |
| Typecheck | `mypy .` | N/A | Typecheck not configured. |
| Build | `npm run build` | PASS | Build succeeded. |
| Smoke test | `npm run start:smoke` | PASS | Health endpoint responded. |
| Manual acceptance check | See checklist | PASS | Acceptance checks complete. |

## Acceptance Checklist Template
- [ ] Objective and End Point achieved (or explicitly marked `Partial`/`Blocked`).
- [ ] In-scope work completed.
- [ ] Out-of-scope boundaries respected.
- [ ] Applicable checks completed and reported with evidence.
- [ ] Pre-existing failures distinguished from introduced failures.
- [ ] Security-sensitive surfaces reviewed where relevant.
- [ ] Documentation updated where required.
- [ ] Rollback/recovery notes included when relevant.

## Where to Report Validation
- ExecPlan Validation Plan: `docs/templates/execplan_template.md`
- Completion handoff: `docs/reports/completion_report_template.md`
- Pull requests: `.github/pull_request_template.md`
