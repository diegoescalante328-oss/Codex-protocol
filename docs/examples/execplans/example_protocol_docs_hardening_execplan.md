# Execution Plan (ExecPlan): Example Protocol Documentation Hardening

## Task
Clarify validation and handoff routing by aligning protocol, validation matrix, and completion report template.

## Why This Task Exists
Reviewers reported that completion quality is inconsistent because planning and reporting linkage is not explicit enough.

## Objective
Strengthen documentation so non-trivial tasks have clear traceability from plan to validation evidence to handoff.

## Start Point
- Existing protocol stages are defined.
- Validation matrix exists.
- Completion report template lacks explicit plan linkage.

## End Point
- Plan/report linkage is explicit in templates.
- Vocabulary is aligned (`ExecPlan`, `Done Definition`, `Completion Report`).
- No contradictory routing remains.

## Task Class
- `non-trivial`

## Scope
### In Scope
- `PLANS.md`, validation matrix, completion report template, and related routing docs.

### Out of Scope
- CI workflow behavior changes.
- Non-protocol repository areas.

## Constraints
- Keep AGENTS concise; route detail to docs.
- Preserve stage sequence and status labels.

## Target Files
- `PLANS.md`
- `docs/standards/validation_matrix.md`
- `docs/reports/completion_report_template.md`
- `README.md`
- `AGENTS.md`

## Discovery Notes
- Current state: planning/reporting relationship is implied, not explicit.
- Desired state: clear artifact chain and reviewable output shape.
- Dependencies: protocol docs, standards docs, PR template.
- Assumptions requiring verification: all referenced files exist and are reachable.
- Risks discovered during Discovery: wording duplication causing drift.

## Risks and Mitigations
- Risk: introducing repetitive policy text.
  - Mitigation: centralize detail in one file and cross-reference.
- Risk: tightening language could over-burden small tasks.
  - Mitigation: preserve task-class gating in stage definitions.

## Design Contract
- Planned files/components/interfaces: docs-only protocol layer.
- Invariants to preserve: stage order, status labels, honest validation reporting.
- Non-goals: adding build/test tooling.
- Compatibility/migration considerations: maintain existing paths; additive changes preferred.

## Implementation Plan
1. Add planning guide and route from README/AGENTS/protocol docs.
2. Update templates so Completion Report references ExecPlan where used.
3. Run consistency sweep for vocabulary and routing.
4. Produce completion report with validation evidence.

## Validation Plan
| Check | Command | Expected Result | Notes |
|---|---|---|---|
| Markdown heading sanity | `find . -type f -name '*.md' -not -path './.git/*' -print0 \| xargs -0 -I{} sh -c 'head -n 1 "{}" \| grep -Eq "^(#|---)" || { echo "bad heading: {}"; exit 1; }'` | PASS | Ensures template/doc parse hygiene |
| Routing existence | `test -f PLANS.md && test -f docs/reports/completion_report_template.md` | PASS | Core references resolve |
| Vocabulary alignment | `rg -n "ExecPlan|Done Definition|Completion Report" AGENTS.md README.md docs` | PASS | Terms present and aligned |
| Manual review | Manual read of changed files | PASS | No conflicting directives |

## Rollback / Recovery
- Rollback trigger(s): protocol docs become contradictory.
- Rollback steps: revert hardening commit.
- Post-rollback verification: rerun heading/routing checks.

## Done Definition
- Planning and handoff linkage is explicit across docs.
- Vocabulary is consistent across AGENTS, README, protocols, standards, and templates.
- Example artifacts demonstrate expected usage quality.

## Final Report Requirements
- Summary and objective status (`Complete`, `Partial`, `Blocked`)
- Plan vs actual summary
- Files changed
- Commands run
- Validation results
- Documentation updates
- Known risks
- Follow-up recommendations
