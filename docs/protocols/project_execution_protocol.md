# Project Execution Protocol

## Objective
Define a repeatable execution lifecycle for Codex-driven delivery with explicit scope control, validation gates, and handoff quality.

## Stage 0: Intake / Readiness
**Purpose**
- Ensure the task is actionable before any implementation starts.

**Required inputs/actions**
- Capture intake using `docs/templates/project_intake_template.md`.
- Confirm objective, start point, end point, constraints, scope boundaries, and success/failure criteria.
- Identify missing prerequisites.

**Required outputs**
- Completed intake record.
- Initial task classification (small, non-trivial, high-risk).

**Exit criteria**
- Intake is complete and unambiguous.
- Task is classified and ready for Discovery.

## Stage 1: Discovery
**Purpose**
- Build factual understanding of the current state and impacted areas.

**Required inputs/actions**
- Read relevant code/docs and repository instructions (`AGENTS.md`).
- Identify dependencies, risks, and assumptions.
- Clarify unknowns and blockers.

**Required outputs**
- Discovery notes covering impacted files, constraints, and risks.

**Exit criteria**
- Current state and risks are sufficiently understood to plan.

## Stage 2: Plan
**Purpose**
- Define a controlled approach before coding.

**Required inputs/actions**
- Create a stepwise plan with validation gates.
- For non-trivial/high-risk tasks, create an ExecPlan in `plans/active/` from `docs/templates/execplan_template.md`.
- Define rollback/recovery path.

**Required outputs**
- Approved implementation plan and validation plan.

**Exit criteria**
- Plan maps directly to objective and constraints.
- Validation and rollback are defined.

## Stage 3: Design Contract
**Purpose**
- Lock implementation intent to prevent scope drift.

**Required inputs/actions**
- Specify target files and interfaces.
- Document invariants and non-goals.
- Confirm compatibility and migration expectations.

**Required outputs**
- Design contract section (standalone note or embedded in ExecPlan).

**Exit criteria**
- Planned design is specific enough to implement without ambiguity.

## Stage 4: Implementation
**Purpose**
- Produce code/doc/config changes that satisfy the design contract.

**Required inputs/actions**
- Execute planned changes with minimal, readable diffs.
- Keep work in-scope and architecture-consistent.
- Track deviations from plan.

**Required outputs**
- Implemented changes ready for validation.

**Exit criteria**
- Changes complete against defined scope.

## Stage 5: Validation
**Purpose**
- Prove the implementation meets quality and correctness requirements.

**Required inputs/actions**
- Run applicable checks from `docs/standards/validation_matrix.md`.
- Record commands and outcomes.
- Resolve failures or explicitly report blockers.

**Required outputs**
- Validation log with pass/fail status and evidence.

**Exit criteria**
- All required checks pass or approved exceptions are documented.

## Stage 6: Hardening
**Purpose**
- Reduce operational and security risk before closeout.

**Required inputs/actions**
- Review error paths, edge cases, and security-sensitive behavior.
- Confirm rollback notes and failure recovery steps.
- Remove temporary/debug artifacts.

**Required outputs**
- Hardened change set and risk notes.

**Exit criteria**
- No unresolved high-severity risks remain.

## Stage 7: Documentation
**Purpose**
- Ensure repository knowledge reflects delivered behavior.

**Required inputs/actions**
- Update affected docs following `docs/standards/documentation_rules.md`.
- Include setup, usage, constraints, and limitations where relevant.
- Cross-link related docs.

**Required outputs**
- Updated, accurate documentation.

**Exit criteria**
- Documentation is complete, coherent, and aligned with implementation.

## Stage 8: Handoff / Closeout
**Purpose**
- Deliver an auditable completion package for reviewers and operators.

**Required inputs/actions**
- Produce completion report using `docs/reports/completion_report_template.md`.
- Summarize objective status, changed files, commands run, results, risks, and follow-ups.
- Note partial completion or blockers, if any.

**Required outputs**
- Final handoff report and PR-ready summary.

**Exit criteria**
- Work is reviewable, reproducible, and operationally understandable.

## Global Success Criteria
- Objective achieved within stated constraints.
- Scope boundaries respected.
- Required validation completed and reported.
- Documentation and handoff are complete and accurate.
- Rollback/recovery guidance is available.

## Global Failure Criteria
- End state does not satisfy objective.
- Scope drift introduced unapproved changes.
- Required validation is missing or failing without explicit exception.
- Security, data integrity, or operational risks are left unresolved.
- Handoff omits critical implementation or recovery details.
