# Project Profile

## Repository Identity
Codex Project Kit is a governance scaffold for running scoped, staged, validated Codex execution with auditable handoff.

## Primary Users
- Engineers and technical leads delegating delivery tasks to Codex.
- Maintainers who review task quality, scope discipline, and handoff evidence.

## Work Types Expected
- Feature delivery planning and execution.
- Bugfix planning and validation.
- Refactor design and risk-managed rollout.
- Protocol/standards hardening for repository operations.

## Operational Conventions
- Follow stage order: Discovery → Plan → Design Contract → Implementation → Validation → Hardening → Documentation → Handoff.
- Use `Success Criteria`, `Failure Criteria`, `Done Definition`, and `Stop Conditions` consistently.
- Keep diffs minimal and tightly scoped to declared target files.

## Planning Expectations
- Non-trivial/high-risk tasks require an ExecPlan before Implementation.
- Planning rules and quality bar live in `PLANS.md`.
- Active plans live in `plans/active/`.

## Validation Expectations
- Use `docs/standards/validation_matrix.md` as authoritative check/report format.
- Do not claim checks that were not run.
- Mark non-run checks as `N/A` or `BLOCKED` with explicit reason and impact.

## Documentation Expectations
- Update docs in the same change set when behavior, constraints, interfaces, or operations change.
- Keep `AGENTS.md` concise; route detail to protocol/standards/templates.

## Dependency and Artifact Discipline
- Avoid adding dependencies without explicit rationale.
- Keep large generated artifacts and datasets out of the repository when possible.
- Never commit secrets.

## Key Locations
- Protocol: `docs/protocols/`
- Standards: `docs/standards/`
- Templates: `docs/templates/`
- Completion reporting: `docs/reports/`
- Examples: `docs/examples/`
- Active ExecPlans: `plans/active/`

## Review Expectations
Reviewers should verify:
1. Scope boundaries were respected.
2. Plan (when required) existed before implementation.
3. Validation evidence is complete and honest.
4. Completion Report and PR summary align with the Done Definition.
