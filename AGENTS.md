# AGENTS.md

## Purpose
Operate this repository as a disciplined execution system for scoped, staged, validated Codex work with auditable handoff.

## Instruction Priority
1. Direct system/developer/user instructions
2. `AGENTS.md`
3. `docs/project_profile.md`
4. `PLANS.md`
5. `docs/protocols/`
6. `docs/standards/`
7. `docs/templates/` and repository conventions

## Required Workflow
Use this stage order (lightweight for small tasks, full rigor for non-trivial/high-risk):
1. Discovery
2. Plan
3. Design Contract
4. Implementation
5. Validation
6. Hardening
7. Documentation
8. Handoff

## Core Operating Rules
- Confirm objective, start/end points, scope boundaries, constraints, assumptions, and validation path before editing.
- Keep diffs minimal and within declared scope; do not perform unrelated refactors.
- Use stable vocabulary: `Success Criteria`, `Failure Criteria`, `Done Definition`, `Stop Conditions`, `ExecPlan`, `Completion Report`.
- Stop immediately if safe validation cannot be performed, required dependencies are missing, or unresolved security/data-loss risk appears.

## Planning Discipline
- Use `PLANS.md` as the authoritative planning policy.
- Create/update an ExecPlan before Implementation whenever `PLANS.md` trigger rules require it.
- Keep active ExecPlans in `plans/active/` using `docs/templates/execplan_template.md`.

## Validation and Reporting Discipline
- Follow `docs/standards/validation_matrix.md`.
- Run all applicable checks; mark non-run checks as `N/A` or `BLOCKED` with reason/impact.
- Distinguish pre-existing failures from introduced failures.
- Produce handoff with `docs/reports/completion_report_template.md`.

## Required Reading for Major Work
- `docs/project_profile.md`
- `PLANS.md`
- `docs/protocols/project_execution_protocol.md`
- `docs/protocols/stage_definitions.md`
- `docs/protocols/failure_and_recovery.md`
- `docs/standards/validation_matrix.md`
- `docs/standards/documentation_rules.md`
- `docs/standards/security_rules.md`

## Scope Discipline
- Stay within explicit in-scope boundaries.
- Record deferred work explicitly instead of silently expanding scope.
- Optional cleanup is out of scope unless required for correctness or risk reduction.
