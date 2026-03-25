# Codex Project Kit

Codex Project Kit is a **Codex-first operating system for work that outgrows ChatGPT project constraints**.

It is the structured alternative to keeping complex work inside ChatGPT project folders once scope, file count, and iteration depth start to exceed lightweight chat workflows.

## Why this repository exists
This repository is the scaling path from a **ChatGPT project workflow** to a **Codex repository workflow**:
- ChatGPT project workflow is great for lightweight, bounded, exploratory tasks.
- Codex repository workflow is better for multi-step, multi-file, governed execution.

Inside this repo, work runs through explicit stages (Discovery → Handoff), planning gates, validation evidence, and completion reporting so larger efforts stay consistent and auditable.

## What this gives you
- A transition layer from chat-based work to repo-based execution.
- Structured execution in Codex for non-trivial tasks.
- Reduced prompt repetition by moving guidance into repo-native docs, templates, and standards.
- Better scalability for long-running, multi-file work with clear governance.

## Operator entry points
- Fast start: [`PROJECT_QUICKSTART.md`](PROJECT_QUICKSTART.md)
- Practical operator manual: [`HOW_TO_USE_THIS_PROJECT.md`](HOW_TO_USE_THIS_PROJECT.md)
- Core authority: [`AGENTS.md`](AGENTS.md), [`PLANS.md`](PLANS.md), and [`docs/`](docs/)

## Start here
1. Read [`AGENTS.md`](AGENTS.md) for operating rules.
2. Read [`docs/project_profile.md`](docs/project_profile.md) for repository positioning and conventions.
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
- Planning authority and trigger rules: [`PLANS.md`](PLANS.md)
- ExecPlan template: [`docs/templates/execplan_template.md`](docs/templates/execplan_template.md)
- Active plans: [`plans/active/`](plans/active/)
- Completed plans archive: [`plans/completed/`](plans/completed/)
- Example ExecPlan: [`docs/examples/execplans/example_protocol_docs_hardening_execplan.md`](docs/examples/execplans/example_protocol_docs_hardening_execplan.md)

## Validation and reporting
- Validation matrix: [`docs/standards/validation_matrix.md`](docs/standards/validation_matrix.md)
- Completion Report template: [`docs/reports/completion_report_template.md`](docs/reports/completion_report_template.md)
- Reports index (latest audit + completion routing): [`docs/reports/README.md`](docs/reports/README.md)
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
- `docs/reports/`: Completion Report template and report index.
- `docs/examples/`: realistic example artifacts.
- `.github/`: issue templates, PR template, workflow scaffold.
- `plans/active/`: active ExecPlans for non-trivial/high-risk tasks.
- `plans/completed/`: closed ExecPlans (`Complete`/`Partial`/`Cancelled`/`Superseded`).
