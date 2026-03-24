# Codex Project Kit

Codex Project Kit is a reusable repository operating system for running tasks from intake through Completion Report with clear scope, staged execution, validation evidence, and safe handoff.

## Why this exists
This repository reduces prompt repetition and quality variance in repeated Codex-driven work.

## Start here
1. Read [`AGENTS.md`](AGENTS.md) for operating rules.
2. Read [`docs/project_profile.md`](docs/project_profile.md) for repo-specific conventions.
3. Read planning rules in [`PLANS.md`](PLANS.md).
4. Follow protocol stages in [`docs/protocols/project_execution_protocol.md`](docs/protocols/project_execution_protocol.md).

## Workflow model
Stage sequence:
1. Discovery
2. Plan
3. Design Contract
4. Implementation
5. Validation
6. Hardening
7. Documentation
8. Handoff

Task classification and rigor: [`docs/protocols/stage_definitions.md`](docs/protocols/stage_definitions.md).

## Planning system
- Non-trivial/high-risk tasks require an ExecPlan before Implementation.
- Planning guide: [`PLANS.md`](PLANS.md)
- ExecPlan template: [`docs/templates/execplan_template.md`](docs/templates/execplan_template.md)
- Active plans: [`plans/active/`](plans/active/)
- Example ExecPlan: [`docs/examples/execplans/example_protocol_docs_hardening_execplan.md`](docs/examples/execplans/example_protocol_docs_hardening_execplan.md)

## Validation and reporting
- Validation matrix: [`docs/standards/validation_matrix.md`](docs/standards/validation_matrix.md)
- Completion Report template: [`docs/reports/completion_report_template.md`](docs/reports/completion_report_template.md)
- PR template: [`.github/pull_request_template.md`](.github/pull_request_template.md)

## Examples
Practical reference artifacts live in [`docs/examples/`](docs/examples/):
- issue examples (feature, bugfix, refactor)
- ExecPlan example
- Completion Report example

## Repository layout
- `AGENTS.md`: concise recurring operational rules.
- `PLANS.md`: planning trigger/quality rules for ExecPlans.
- `docs/project_profile.md`: lightweight repository-specific operating profile.
- `docs/protocols/`: lifecycle process, task classes, failure/recovery behavior.
- `docs/standards/`: coding, validation, documentation, security standards.
- `docs/templates/`: intake/task/ExecPlan templates.
- `docs/reports/`: Completion Report template.
- `docs/examples/`: realistic example artifacts.
- `.github/`: issue templates, PR template, workflow scaffold.
- `plans/active/`: active ExecPlans for non-trivial/high-risk tasks.
