# Coding Rules

## Readability and Maintainability
- Use clear naming and direct control flow.
- Keep units focused and composable.
- Optimize for future maintainers unfamiliar with the area.

## Minimal Diff Policy
- Make the smallest coherent change that satisfies objective and Success Criteria.
- Avoid unrelated refactors or formatting-only edits in the same change.

## Architecture Consistency
- Follow existing repository patterns unless an explicit architecture change is in scope.
- Preserve contracts unless contract migration is part of the Design Contract.

## File Discipline
- Place files in the correct domain location.
- Avoid duplicate logic when existing abstractions can be reused.
- Keep changed files tightly tied to task scope.

## Dependency Discipline
- Do not add dependencies casually.
- Prefer standard library and existing tooling first.
- If adding a dependency, document rationale and operational impact.

## Error Handling
- Handle expected failure paths explicitly.
- Provide actionable errors without exposing sensitive internals.
- Fail safely when assumptions are violated.

## Security-Aware Coding
- Treat all external input as untrusted.
- Validate/sanitize data at boundaries.
- Avoid unsafe shell/file/network patterns.
- Never commit credentials, secrets, or private keys.
