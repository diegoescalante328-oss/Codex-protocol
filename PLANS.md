# PLANS.md

## Purpose
Define the repository’s authoritative planning rules for when an ExecPlan is required, where it lives, what quality it must meet, and how planning connects to protocol stages, validation, and Completion Report handoff.

## Authority and Routing
- `AGENTS.md` sets top-level operating rules and instruction priority.
- `PLANS.md` is the **authoritative planning policy** for ExecPlan trigger rules, lifecycle rules, and quality bar.
- `docs/templates/execplan_template.md` defines ExecPlan structure.
- `plans/active/` is the working location for active ExecPlans.
- `plans/completed/` stores closed historical ExecPlans.
- `docs/protocols/project_execution_protocol.md` defines stage behavior that planning must support.

If planning guidance conflicts across documents, follow `AGENTS.md` first, then this file, then protocol/standards/templates.

## When an ExecPlan Is Required
Create or update an ExecPlan **before Implementation** when any of the following is true:
1. The task is classified `non-trivial` or `high-risk`.
2. The work is likely to touch multiple files or multiple components/areas.
3. The work changes structure, interfaces/contracts, configuration, or migration behavior.
4. The work needs explicit rollback/recovery planning or has material operational/security/data risk.

For `small` tasks, ExecPlan is optional unless Discovery reveals ambiguity or upward reclassification risk.

## ExecPlan Lifecycle Policy
`plans/active/` is reserved for currently active work only.

### Active
An ExecPlan is active when implementation/hardening/documentation/handoff for that task is still in progress.

Rules:
- Store active ExecPlans in `plans/active/`.
- Keep one active ExecPlan per active task.
- Use naming: `YYYY-MM-DD_<short-task-name>_execplan.md`.

### Completed
When task status is `Complete` or `Partial` and handoff is finished:
- Move the ExecPlan from `plans/active/` to `plans/completed/`.
- Do not delete closed plans; preserve historical traceability.
- Link the Completion Report to the final plan path.

### Cancelled / Superseded
When work stops or is replaced before completion:
- Move the ExecPlan to `plans/completed/`.
- Keep the original filename.
- Add `Cancelled` or `Superseded by <new-plan-path>` note near the top of the moved plan.

## ExecPlan Quality Bar
An ExecPlan must be specific enough to constrain implementation, not merely describe intent.

Minimum required content:
- Objective and scope boundaries (`In Scope` / `Out of Scope`)
- Target files and assumptions/dependencies
- Risks and mitigations
- Validation Plan (planned checks with expected outcomes)
- Done Definition
- Final Report Requirements

For high-risk work, include explicit rollback/recovery notes and post-rollback verification.

## Relationship to Protocol Stages
- Planning authority is exercised in **Stage 2: Plan** (`docs/protocols/project_execution_protocol.md`).
- Design decisions are locked in **Stage 3: Design Contract** and must remain aligned with the ExecPlan.
- Scope-critical deviations discovered during implementation require updating the ExecPlan before continuing.

## Relationship to Validation and Completion Reporting
- Validation checks listed in the ExecPlan must align with `docs/standards/validation_matrix.md`.
- Handoff must use `docs/reports/completion_report_template.md` and report plan-vs-actual status.
- Completion reporting should state whether Done Definition was met and disclose any deviations.

## Fast Usage Flow
1. Classify task (`small`, `non-trivial`, `high-risk`) via `docs/protocols/stage_definitions.md`.
2. Apply trigger rules above to decide if ExecPlan is mandatory.
3. Create/update plan in `plans/active/` from template.
4. Implement only after plan satisfies the quality bar.
5. Move closed plan to `plans/completed/` during handoff.
6. Validate and hand off with explicit plan linkage.
