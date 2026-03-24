# Failure and Recovery

## Purpose
Define actionable stop, blocker, partial completion, rollback, and recovery behavior so risk is controlled and reporting is honest.

## Immediate Stop Conditions
Stop work and report immediately when:
- continuing would violate scope or explicit constraints
- required access, dependencies, files, or environment capabilities are unavailable
- unresolved security, privacy, or data-loss risk is discovered
- a destructive or irreversible operation is required but not explicitly approved
- safe Validation cannot be executed

## Blocker Handling Workflow
1. Record the blocker: what failed, where, and impact on objective.
2. Preserve safe state: avoid speculative or unrelated edits.
3. Attempt only in-scope, low-risk fallback paths.
4. If still blocked, report external action needed and mark status `Blocked`.

## Partial Completion Standard
`Partial` means some in-scope deliverables are complete, but objective end point is not fully met.

When reporting `Partial`:
- list completed items and remaining items explicitly
- include current Validation status and known gaps
- state shipping risk of current state
- provide minimal safe next steps

## Rollback Notes Requirements
If changes touch config, schema, deployment behavior, data movement, or destructive operations, include:
- changed surfaces (files/components/behaviors)
- rollback trigger conditions
- exact rollback steps
- post-rollback verification commands/checks

## Safe Recovery Guidance
Recovery notes should be:
- specific (concrete commands/actions)
- minimal (fewest steps to safe state)
- testable (verification included)
- honest about residual risk or unknowns

## Completion Status Labels
Use exactly one in handoff and PR context:
- `Complete`: Objective and end point achieved.
- `Partial`: Work delivered but end point not fully achieved.
- `Blocked`: Work cannot proceed safely without external input/action.
