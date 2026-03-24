# AGENTS.md

## Repository Purpose
This repository is **Codex Project Kit**: a reusable operating system for scoped, staged, validated project execution with auditable handoff.

## Instruction Priority
1. Direct system/developer/user instructions
2. This `AGENTS.md`
3. Protocols in `docs/protocols/`
4. Standards in `docs/standards/`
5. Templates, repository conventions, and local patterns

## Required Workflow
Use these stages in order for all non-trivial and high-risk tasks (and in lightweight form for small tasks):
1. Discovery
2. Plan
3. Design Contract
4. Implementation
5. Validation
6. Hardening
7. Documentation
8. Handoff

## Discovery Requirements
Before editing, confirm:
- objective
- current state and desired end state
- likely target files and dependencies
- risks and constraints
- validation path
- explicit in-scope/out-of-scope boundaries
- assumptions requiring verification

## Planning Requirements
Create a concise plan before implementation that includes:
- proposed file changes
- ordered execution steps
- key risks
- validation approach
- rollback/recovery considerations when relevant

## ExecPlan Rule
If work is non-trivial or high-risk, create or update an ExecPlan in `plans/active/` using `docs/templates/execplan_template.md` **before** Implementation.

## Implementation Rules
- Keep diffs minimal, readable, and reviewable.
- Follow existing architecture and repository patterns.
- Do not add dependencies casually.
- Do not refactor unrelated areas.
- Avoid speculative edits.

## Validation Rules
- Use `docs/standards/validation_matrix.md`.
- Run all applicable checks.
- If a check cannot run, report the exact reason and impact.
- Distinguish pre-existing failures from failures introduced by your change.

## Documentation Rules
When behavior, setup, interfaces, config, limitations, or operations change, update docs in the same change set using `docs/standards/documentation_rules.md`.

## Stop Conditions
Stop and report immediately if:
- requirements conflict or scope is unclear in a way that risks incorrect implementation
- required access/dependencies are missing
- unresolved security or data-loss risk appears
- safe validation cannot be performed

## Handoff Requirements
Final handoff must include:
- summary and objective status
- files changed
- commands run
- validation results
- known risks
- rollback/recovery notes when relevant
- follow-up recommendations

Use `docs/reports/completion_report_template.md`.

## Required Supporting Docs (read before major work)
- `docs/protocols/project_execution_protocol.md`
- `docs/protocols/stage_definitions.md`
- `docs/protocols/failure_and_recovery.md`
- `docs/standards/validation_matrix.md`
- `docs/standards/coding_rules.md`
- `docs/standards/documentation_rules.md`
- `docs/standards/security_rules.md`

## Scope Discipline
- Stay within explicit scope boundaries.
- Capture deferred items explicitly instead of silently expanding scope.
- Optional cleanup is out of scope unless required for correctness or risk reduction.

## Repeated-Use Optimization Rules
- Keep recurring operational guidance in this file; move details to `docs/`.
- Use stable terminology across protocol, standards, templates, issues, and PRs.
- Prefer concise directives over long narrative.
- Optimize for future tasks that only say: “Follow `AGENTS.md` and implement this.”
