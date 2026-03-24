# Coding Rules

## Readability
- Prefer clear naming and straightforward control flow.
- Optimize for maintainers who are new to the code area.
- Keep functions/modules focused on one responsibility.

## Minimal Diffs
- Make the smallest change set that satisfies the objective.
- Avoid unrelated formatting or refactors in the same change.

## Architecture Consistency
- Follow existing repository patterns unless an explicit design change is in scope.
- Preserve interface contracts unless migration is part of the task.

## File Discipline
- Place new files in appropriate directories with consistent naming.
- Do not duplicate logic when existing abstractions are suitable.

## Error Handling
- Handle failure paths explicitly and predictably.
- Return actionable error messages without leaking sensitive data.

## Maintainability
- Prefer composable, testable units.
- Keep edge cases and invariants visible in code and docs.

## Dependency Discipline
- Avoid adding dependencies without clear value.
- Reuse standard library or existing project tooling first.
- Document rationale for any new dependency.

## Security-Aware Behavior
- Treat external input as untrusted.
- Avoid unsafe shell/file/network operations unless required and validated.
- Never hardcode credentials, tokens, or private keys.
