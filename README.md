# Codex Project Kit

Codex Project Kit is a reusable repository operating system for running tasks from intake through Completion Report with clear scope, staged execution, validation evidence, and safe handoff.

## Why this exists
This repository standardizes project execution so future Codex tasks can run with minimal prompt repetition while preserving quality and auditability.

## Who should use it
- Engineers and technical leads delegating delivery work to Codex.
- Teams that want consistent issue/PR workflow and validation reporting.
- Repositories that need repeatable planning, execution, and handoff patterns.

## Start here
1. Read [`AGENTS.md`](AGENTS.md).
2. Read the protocol in [`docs/protocols/project_execution_protocol.md`](docs/protocols/project_execution_protocol.md).
3. Use intake and task templates in [`docs/templates/`](docs/templates/).

## Workflow model
Codex Project Kit uses this stage sequence:
1. Discovery
2. Plan
3. Design Contract
4. Implementation
5. Validation
6. Hardening
7. Documentation
8. Handoff

Task class guidance (small vs non-trivial vs high-risk) lives in [`docs/protocols/stage_definitions.md`](docs/protocols/stage_definitions.md).

## ExecPlan usage
For non-trivial or high-risk tasks, create/update an ExecPlan in [`plans/active/`](plans/active/) using [`docs/templates/execplan_template.md`](docs/templates/execplan_template.md) before Implementation.

## Validation and reporting
- Validation requirements: [`docs/standards/validation_matrix.md`](docs/standards/validation_matrix.md)
- Completion Report template: [`docs/reports/completion_report_template.md`](docs/reports/completion_report_template.md)
- PR template: [`.github/pull_request_template.md`](.github/pull_request_template.md)

## Repository layout
- `AGENTS.md`: compact operating rules for Codex.
- `docs/protocols/`: lifecycle process, task classes, failure/recovery.
- `docs/standards/`: coding, validation, documentation, security rules.
- `docs/templates/`: reusable intake/task/ExecPlan templates.
- `docs/reports/`: Completion Report template.
- `.github/`: issue templates, PR template, and workflow scaffold.
- `plans/active/`: active ExecPlans for in-flight non-trivial/high-risk work.

## Data and artifact policy
Keep large binaries, datasets, and generated artifacts outside the main repository when possible. Store them in approved external storage and reference them from docs.
