# Project Execution Protocol

## Objective
Define the authoritative lifecycle for Codex Project Kit tasks so work is scoped, staged, validated, hardened, and handed off with clear evidence.

## Stage 0: Intake / Readiness
**Purpose**
- Confirm task intent and boundaries before Discovery.

**Required inputs/actions**
- Capture intake with `docs/templates/project_intake_template.md`.
- Confirm objective, start point, end point, in-scope/out-of-scope boundaries, constraints, Success Criteria, and Failure Criteria.
- Classify task size/risk using `docs/protocols/stage_definitions.md`.

**Required outputs**
- Completed intake record.
- Task class decision: `small`, `non-trivial`, or `high-risk`.

**Exit criteria**
- Intake is complete and unambiguous.

## Stage 1: Discovery
**Purpose**
- Build accurate understanding of current state, dependencies, and risks.

**Required inputs/actions**
- Read repository guidance (`AGENTS.md`, `docs/project_profile.md`, applicable protocol/standards docs).
- Identify target files, assumptions, constraints, and validation path.

**Required outputs**
- Discovery notes that identify assumptions, dependencies, and risk highlights.

**Exit criteria**
- Current state is clear enough to plan safely.

## Stage 2: Plan
**Purpose**
- Commit execution order, scope controls, and validation strategy.

**Required inputs/actions**
- Draft ordered implementation steps with explicit target files.
- Define planned checks from `docs/standards/validation_matrix.md`.
- If task is non-trivial/high-risk, create or update ExecPlan in `plans/active/` using `docs/templates/execplan_template.md`.
- Apply planning rules in `PLANS.md`.

**Required outputs**
- Plan artifact with scope boundaries, risks, validation plan, Done Definition, and reporting expectations.

**Exit criteria**
- Plan is actionable and constrains implementation.

## Stage 3: Design Contract
**Purpose**
- Lock design intent and non-goals before editing.

**Required inputs/actions**
- Define touched files/components/interfaces.
- Record invariants, non-goals, and compatibility considerations.

**Required outputs**
- Design Contract section in plan/task record.

**Exit criteria**
- No unresolved architecture ambiguity.

## Stage 4: Implementation
**Purpose**
- Apply minimal, reviewable, in-scope changes.

**Required inputs/actions**
- Follow plan scope and target files.
- Update plan if scope-critical deviations are required.

**Required outputs**
- In-scope changes ready for validation.

**Exit criteria**
- Implementation satisfies Design Contract and scope boundaries.

## Stage 5: Validation
**Purpose**
- Demonstrate correctness with explicit, reproducible evidence.

**Required inputs/actions**
- Run all applicable planned checks.
- Capture exact commands and results.
- Mark skipped checks as `N/A` or `BLOCKED` with reason/impact.
- Distinguish pre-existing failures from introduced failures.

**Required outputs**
- Validation evidence table and summary.

**Exit criteria**
- Required checks pass or exceptions are disclosed and risk-assessed.

## Stage 6: Hardening
**Purpose**
- Reduce operational and security risk before handoff.

**Required inputs/actions**
- Review failure paths, rollback triggers, and sensitive surfaces.
- Remove temporary/debug-only artifacts.

**Required outputs**
- Hardened changes and residual risk notes.

**Exit criteria**
- No unresolved high-severity risk without explicit escalation.

## Stage 7: Documentation
**Purpose**
- Keep repository docs aligned with implemented behavior and process.

**Required inputs/actions**
- Update docs per `docs/standards/documentation_rules.md`.
- Ensure vocabulary consistency across protocol/templates/reports.

**Required outputs**
- Updated docs with valid cross-references.

**Exit criteria**
- Documentation is accurate and implementation-aligned.

## Stage 8: Handoff
**Purpose**
- Deliver an auditable closeout tied to plan and validation evidence.

**Required inputs/actions**
- Produce Completion Report using `docs/reports/completion_report_template.md`.
- Include objective status (`Complete`, `Partial`, `Blocked`), files changed, commands run, Validation results, known risks, rollback/recovery notes when relevant, and follow-up recommendations.
- Confirm outcome against plan Done Definition.

**Required outputs**
- Completion Report and PR-ready summary.

**Exit criteria**
- Reviewers can verify objective status, evidence, and operating safety.

## Global Success Criteria
- Objective/end point achieved within scope and constraints.
- Required plan rigor was applied for task class.
- Validation evidence is complete and honest.
- Documentation and reporting align with implementation.

## Global Failure Criteria
- Objective/end point not achieved and not clearly reported.
- Unapproved scope expansion occurred.
- Required validation is missing or undisclosed.
- Unresolved security/data/operational risk remains undisclosed.
- Completion Report omits critical information.

## Cross-Document Alignment
- Task classes and rigor: `docs/protocols/stage_definitions.md`
- Stop conditions and recovery behavior: `docs/protocols/failure_and_recovery.md`
- Planning rules: `PLANS.md`
- Validation requirements: `docs/standards/validation_matrix.md`
- Documentation/security/coding standards: `docs/standards/`
- Templates: `docs/templates/`
