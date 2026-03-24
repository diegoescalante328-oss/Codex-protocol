# Failure and Recovery

## Purpose
Define stop, blocker, partial completion, rollback, and recovery behavior so risk is controlled and reporting remains honest.

## Immediate Stop Conditions
Stop and report immediately when:
- continuing would violate scope or explicit constraints
- required access, dependencies, files, or environment capabilities are unavailable
- unresolved security, privacy, or data-loss risk is discovered
- destructive/irreversible operations are required without explicit approval
- safe Validation cannot be executed

## Blocker Handling Workflow
1. Record blocker details (what failed, where, impact on objective).
2. Preserve safe state (avoid speculative or unrelated edits).
3. Attempt only in-scope, low-risk fallback paths.
4. If still blocked, report required external action and set status `Blocked`.

## Partial Completion Standard
Use `Partial` only when some in-scope deliverables are complete but objective end point is not fully achieved.

When reporting `Partial`:
- list completed vs remaining items explicitly
- include Validation status and known gaps
- state shipping risk of current state
- provide minimal safe next steps

## Rollback Notes Requirements
If changes touch config, schema, deployment behavior, data movement, or destructive operations, include:
- changed surfaces (files/components/behaviors)
- rollback trigger conditions
- exact rollback steps
- post-rollback verification checks

## Safe Recovery Guidance
Recovery notes must be:
- specific (concrete commands/actions)
- minimal (fewest steps to safe state)
- testable (verification included)
- honest about residual risk/unknowns

## Completion Status Labels
Use exactly one status in Completion Report and PR context:
- `Complete`: objective and end point achieved.
- `Partial`: work delivered but end point not fully achieved.
- `Blocked`: work cannot proceed safely without external input/action.
