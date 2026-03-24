# AGENTS.md

## Purpose
This repository is a reusable **Codex Project Kit** for running work with clear scope, staged execution, explicit validation, and auditable handoff.

## Instruction Priority
1. Direct system/developer/user instructions
2. This `AGENTS.md`
3. Protocol docs under `docs/protocols/`
4. Standards under `docs/standards/`
5. Templates under `docs/templates/`

## Required Workflow Stages
Follow these stages in order for all non-trivial tasks:
1. Discovery
2. Plan
3. Design Contract
4. Implementation
5. Validation
6. Hardening
7. Documentation
8. Handoff

## Discovery Requirements
- Read task intake and confirm start point, end point, constraints, and success/failure criteria.
- Identify impacted files/systems and risks.
- Confirm assumptions explicitly.

## Planning Requirements
- Produce a concise execution plan before coding.
- For non-trivial tasks, create/update an ExecPlan in `plans/active/` using `docs/templates/execplan_template.md`.
- Define validation gates and rollback approach before implementation.

## Implementation Rules
- Stay within declared scope.
- Prefer minimal, readable diffs and architecture-consistent changes.
- Avoid speculative refactors unless explicitly in scope.

## Validation Rules
- Use `docs/standards/validation_matrix.md`.
- Run all applicable checks (tests/lint/build/typecheck/format/smoke/manual as relevant).
- Report commands and outcomes clearly.

## Documentation Rules
- Update affected docs in the same change set.
- Follow `docs/standards/documentation_rules.md`.
- Ensure examples and operational instructions match implemented behavior.

## Stop Conditions
Stop and report immediately if:
- Task violates constraints or requested scope.
- Required access, files, or environment dependencies are missing.
- A change introduces unresolved security or data-loss risk.

## Handoff Format
Provide a completion summary with:
- Objective status
- Files changed
- Commands run and validation results
- Risks, rollback notes, and follow-ups
Use `docs/reports/completion_report_template.md`.

## Required Supporting Docs
Read before significant work:
- `docs/protocols/project_execution_protocol.md`
- `docs/protocols/stage_definitions.md`
- `docs/protocols/failure_and_recovery.md`
- `docs/standards/validation_matrix.md`
- `docs/standards/coding_rules.md`
- `docs/standards/documentation_rules.md`
- `docs/standards/security_rules.md`

## ExecPlan Rule
If a task is non-trivial or high-risk, an ExecPlan in `plans/active/` is mandatory before implementation.

## Scope Discipline
- Respect explicit in-scope/out-of-scope boundaries.
- Record deferred items instead of implementing them silently.
- Do not expand deliverables without updating scope and criteria first.
