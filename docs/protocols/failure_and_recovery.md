# Failure and Recovery

## Purpose
Define safe behavior when work cannot proceed, validation fails, or delivery is partial.

## Stop Immediately When
- Continuing would violate explicit scope or constraints.
- Required permissions, dependencies, or critical inputs are unavailable.
- A security risk, data-loss risk, or destructive side effect is detected and unresolved.
- Validation reveals a high-severity regression with no safe mitigation.

## What To Do When Blocked
1. Record the blocker clearly (what, where, impact).
2. Preserve current state and avoid speculative changes.
3. Attempt safe fallback paths only if they stay in-scope.
4. If unresolved, mark task as blocked and report required external action.

## Partial Completion Rules
- Deliver only coherent, reviewable partial work.
- Explicitly mark incomplete sections.
- Do not claim objective success when end point is unmet.
- Include next actions and ownership assumptions.

## Rollback Notes Requirements
Rollback guidance must include:
- What changed (files/components/behaviors).
- Trigger for rollback (failure symptoms or thresholds).
- Exact rollback actions (revert commit, restore config/state, disable feature path, etc.).
- Post-rollback verification steps.

## Safe Reporting for Incomplete Work
When incomplete, the handoff must include:
- Objective status: `Complete`, `Partial`, or `Blocked`.
- Completed scope vs remaining scope.
- Validation status and known failing checks.
- Risks of shipping current state.
- Minimal path to finish safely.
