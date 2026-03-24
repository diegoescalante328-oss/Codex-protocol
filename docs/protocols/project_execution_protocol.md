# Project Execution Protocol

## Objective
Define the authoritative lifecycle for Codex Project Kit tasks so work is scoped, staged, validated, hardened, and handed off with clear evidence.

## Stage 0: Intake / Readiness
**Purpose**
- Confirm the task is actionable before Discovery.

**Required inputs/actions**
- Capture intake using `docs/templates/project_intake_template.md`.
- Confirm objective, start point, end point, in-scope/out-of-scope boundaries, constraints, Success Criteria, and Failure Criteria.
- Identify blockers, missing dependencies, and environment assumptions.

**Required outputs**
- Completed intake record.
- Task class decision: small, non-trivial, or high-risk.

**Exit criteria**
- Intake is complete and unambiguous.
- Task is ready for Stage 1 (Discovery).

## Stage 1: Discovery
**Purpose**
- Build an accurate understanding of current state and impact area.

**Required inputs/actions**
- Read relevant repository instructions and impacted files.
- Identify likely target files, dependencies, assumptions, and risks.
- Define a realistic validation path.

**Required outputs**
- Discovery notes with assumptions, dependencies, and risk highlights.

**Exit criteria**
- Current state and constraints are clear enough to plan safely.

## Stage 2: Plan
**Purpose**
- Define execution sequence, validation gates, and rollback approach.

**Required inputs/actions**
- Draft ordered implementation steps.
- Define applicable validation checks from `docs/standards/validation_matrix.md`.
- For non-trivial/high-risk tasks, create or update an ExecPlan in `plans/active/` using `docs/templates/execplan_template.md`.

**Required outputs**
- Plan with file targets, risks, validation strategy, and rollback notes.

**Exit criteria**
- Plan is actionable, scoped, and traceable to objective and constraints.

## Stage 3: Design Contract
**Purpose**
- Lock design intent and reduce ambiguity before editing.

**Required inputs/actions**
- Define touched files/components and interface implications.
- Record invariants, non-goals, and compatibility expectations.
- Capture key decisions in the ExecPlan or task record.

**Required outputs**
- Design Contract section aligned to planned implementation.

**Exit criteria**
- Implementation can proceed without unresolved architectural ambiguity.

## Stage 4: Implementation
**Purpose**
- Apply scoped changes that satisfy the Design Contract.

**Required inputs/actions**
- Implement minimal, reviewable diffs using existing patterns.
- Keep work within declared scope.
- Track deviations and rationale.

**Required outputs**
- Updated code/docs/config ready for validation.

**Exit criteria**
- In-scope implementation is complete and coherent.

## Stage 5: Validation
**Purpose**
- Demonstrate correctness and readiness with explicit evidence.

**Required inputs/actions**
- Run all applicable checks in the validation matrix.
- Capture exact commands and results.
- Distinguish pre-existing failures from introduced failures.

**Required outputs**
- Validation evidence table and status summary.

**Exit criteria**
- Required checks pass, or exceptions/blockers are explicitly documented.

## Stage 6: Hardening
**Purpose**
- Reduce operational, reliability, and security risk before handoff.

**Required inputs/actions**
- Review edge cases and failure paths.
- Confirm security-sensitive surfaces and rollback instructions.
- Remove temporary/debug-only artifacts.

**Required outputs**
- Hardened change set with residual risk notes.

**Exit criteria**
- No unresolved high-severity risk remains without explicit escalation.

## Stage 7: Documentation
**Purpose**
- Keep repository documentation aligned with implemented behavior.

**Required inputs/actions**
- Update affected docs using `docs/standards/documentation_rules.md`.
- Update setup/config/limitations/migration notes when relevant.
- Ensure terminology is consistent with protocol stages.

**Required outputs**
- Accurate docs reflecting new behavior and operational expectations.

**Exit criteria**
- Documentation is complete, cross-referenced, and implementation-aligned.

## Stage 8: Handoff / Closeout
**Purpose**
- Deliver a complete, auditable Completion Report.

**Required inputs/actions**
- Produce handoff using `docs/reports/completion_report_template.md`.
- Include objective status, files changed, commands run, Validation results, known risks, rollback notes (if relevant), and follow-ups.

**Required outputs**
- Completion Report and PR-ready summary.

**Exit criteria**
- Work can be reviewed, reproduced, and safely operated.

## Global Success Criteria
- Objective and end point are met within constraints.
- Scope boundaries are respected.
- Validation evidence is complete and honest.
- Documentation reflects implementation.
- Recovery/rollback guidance exists when risk warrants it.

## Global Failure Criteria
- End point is not met or objective is materially incomplete.
- Unapproved scope expansion occurred.
- Required validation is missing, blocked, or failing without disclosure.
- Unresolved security/data-integrity/operational risk remains.
- Completion Report omits critical information.

## Cross-Document Alignment
- Stage details in this file map to task classes in `docs/protocols/stage_definitions.md`.
- Blocking, partial completion, and recovery behavior are defined in `docs/protocols/failure_and_recovery.md`.
- Validation requirements are governed by `docs/standards/validation_matrix.md`.
- Coding, docs, and security expectations are governed by `docs/standards/`.
- Intake, task, and planning artifacts use templates in `docs/templates/`.
