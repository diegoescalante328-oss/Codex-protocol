# PLANS.md

## Purpose
`PLANS.md` defines how ExecPlans are used to keep non-trivial and high-risk work tightly scoped, reviewable, and reproducible.

## When an ExecPlan Is Required
Create or update an ExecPlan **before Implementation** when any of these are true:
- Task class is `non-trivial` or `high-risk` (per `docs/protocols/stage_definitions.md`).
- Work touches multiple areas/files with meaningful coupling.
- Requirements contain ambiguity that could cause scope drift.
- Rollback/recovery planning is likely needed.

For small tasks, ExecPlan is optional but recommended when uncertainty appears during Discovery.

## Where Plans Live
- Active plans: `plans/active/`
- Template source: `docs/templates/execplan_template.md`
- Example plan: `docs/examples/execplans/example_protocol_docs_hardening_execplan.md`

Use one plan file per active task. Keep file names stable and scannable:
`YYYY-MM-DD_<short-task-name>_execplan.md`

## Minimum ExecPlan Quality Bar
A valid ExecPlan must include all of the following:
1. Objective, Start Point, End Point.
2. Scope boundaries (`In Scope`, `Out of Scope`) and Constraints.
3. Target Files list specific enough to prevent opportunistic edits.
4. Discovery notes that capture assumptions and dependencies.
5. Risk notes with at least one mitigation or containment action.
6. Design Contract with invariants and non-goals.
7. Ordered Implementation Plan.
8. Validation Plan mapped to `docs/standards/validation_matrix.md`.
9. Rollback/Recovery notes when operational risk warrants it.
10. Done Definition and explicit Completion Report expectations.

## How ExecPlans Constrain Execution
- Implementation must stay within declared Scope, Constraints, and Target Files unless the plan is updated first.
- Validation must execute the planned checks or record `N/A`/`BLOCKED` with reason.
- Handoff must report against the plan's Done Definition and objective status (`Complete`, `Partial`, `Blocked`).

## Required Stage Linkage
ExecPlans are the backbone artifact for these stages:
- **Discovery**: assumptions, risks, and dependencies are captured.
- **Plan**: execution order and validation gates are committed.
- **Design Contract**: invariants and non-goals are locked.
- **Validation**: evidence traces to planned checks.
- **Handoff**: Completion Report references outcomes versus plan.

## Relationship to AGENTS.md and Reports
- `AGENTS.md` defines trigger discipline and routing.
- `PLANS.md` defines operational planning rules.
- `docs/reports/completion_report_template.md` defines final reporting structure.

If implementation deviates from plan, record the reason in the ExecPlan and reflect it in the Completion Report.
