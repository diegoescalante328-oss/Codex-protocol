# Example Issue: Bugfix Request

## Bug Summary
`completion_report_template.md` does not require a plan reference, causing weak traceability between planned and delivered work for non-trivial tasks.

## Expected Behavior
Completion reports for plan-driven work include explicit ExecPlan path and note deviations from plan.

## Actual Behavior
Template has no dedicated section for plan linkage; reviewers must infer whether planning was followed.

## Reproduction Steps
1. Open `docs/reports/completion_report_template.md`.
2. Confirm sections present for status/files/validation.
3. Observe missing explicit plan reference field.

## Suspected Files or Areas
- `docs/reports/completion_report_template.md`
- `docs/templates/execplan_template.md`
- `PLANS.md`

## Constraints
- Maintain compatibility with existing completion reporting workflow.
- Keep template concise and scan-friendly.

## Success Criteria
- Completion report template includes ExecPlan reference field.
- Template includes plan deviation note.
- Routing between plans and reports is explicit.

## Failure Criteria
- Plan linkage remains implicit.
- Added fields duplicate existing sections without improving clarity.

## Validation Requirements
- Required checks:
  - Template headings are valid markdown.
  - Cross-referenced plan/report files exist.
- Regression checks:
  - Existing status and validation sections remain intact.
- Suggested commands:
  - `rg -n "Plan Reference|deviation" docs/reports/completion_report_template.md`
  - `test -f PLANS.md && test -f docs/templates/execplan_template.md`
