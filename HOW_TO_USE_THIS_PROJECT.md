# HOW TO USE THIS PROJECT

Practical operator manual for recurring work in this repository.

> This file is a routing guide, **not** a policy authority. Authoritative rules remain in `AGENTS.md`, `PLANS.md`, and docs under `docs/`.

## 1) Choose your entry path

### If you are new to this repo
1. Read [`PROJECT_QUICKSTART.md`](PROJECT_QUICKSTART.md) for a fast start.
2. Then read [`AGENTS.md`](AGENTS.md) and [`docs/project_profile.md`](docs/project_profile.md).

### If you are starting a real task
1. Confirm objective/scope/constraints from the task intake.
2. Follow stage order from [`docs/protocols/project_execution_protocol.md`](docs/protocols/project_execution_protocol.md):
   - Discovery → Plan → Design Contract → Implementation → Validation → Hardening → Documentation → Handoff
3. Apply planning trigger rules in [`PLANS.md`](PLANS.md) before implementation.

### If you are returning to ongoing work
1. Check active plans in [`plans/active/`](plans/active/).
2. Re-open the relevant ExecPlan and validation expectations.
3. Continue from the current stage, then hand off with a Completion Report.

## 2) When to stay in ChatGPT vs move to Codex

This is the key transition decision.

### Stay in ChatGPT project workflow when work is:
- Lightweight and bounded.
- Primarily exploratory (brainstorming, first-draft outlining, short Q&A).
- Small enough to manage in a single chat/project context.
- Not yet dependent on strict file history, staged execution, or formal validation evidence.

### Move to Codex repository workflow when work becomes:
- Multi-step, multi-file, or cross-component.
- Long-running and likely to require iterative hardening.
- Sensitive to quality variance from repeated prompting.
- In need of governed execution (explicit scope, planning gates, validation matrix, Completion Report).

### How to transition from chat → repo
1. Bring in the confirmed objective, scope boundaries, constraints, and success criteria from ChatGPT.
2. Start Discovery in this repo and identify target files/dependencies.
3. Classify task size; create/update ExecPlan when required by [`PLANS.md`](PLANS.md).
4. Execute through stages with validation evidence and handoff artifacts.

### What changes after moving
- Guidance shifts from repeated prompts to repository-native instructions (`AGENTS.md`, protocols, standards, templates).
- Work becomes staged and auditable rather than purely conversational.
- Validation and reporting expectations become explicit and repeatable.

## 3) Where authority lives

- Operating rules and priority: [`AGENTS.md`](AGENTS.md)
- Planning trigger/quality policy: [`PLANS.md`](PLANS.md)
- Stage behavior and stop/recovery: [`docs/protocols/`](docs/protocols/)
- Validation, documentation, security, coding standards: [`docs/standards/`](docs/standards/)
- Canonical templates: [`docs/templates/`](docs/templates/)
- Completion reporting: [`docs/reports/`](docs/reports/)
- Example artifacts: [`docs/examples/`](docs/examples/)

## 4) Minimal operating checklist

1. **Discovery**: confirm target files, assumptions, dependencies, risks.
2. **Plan**: decide task class (`small` / `non-trivial` / `high-risk`) and create/update ExecPlan if required by `PLANS.md`.
3. **Implement**: keep diffs minimal and in scope.
4. **Validate**: run applicable checks; mark non-run checks `N/A` or `BLOCKED` with reason/impact.
5. **Handoff**: produce a Completion Report using [`docs/reports/completion_report_template.md`](docs/reports/completion_report_template.md).

## 5) Fast links by intent

- “I need to start quickly” → [`PROJECT_QUICKSTART.md`](PROJECT_QUICKSTART.md)
- “Do I need an ExecPlan?” → [`PLANS.md`](PLANS.md)
- “What are the exact stages?” → [`docs/protocols/project_execution_protocol.md`](docs/protocols/project_execution_protocol.md)
- “How do I classify task size?” → [`docs/protocols/stage_definitions.md`](docs/protocols/stage_definitions.md)
- “How do I report validation?” → [`docs/standards/validation_matrix.md`](docs/standards/validation_matrix.md)
- “What does good handoff look like?” → [`docs/reports/completion_report_template.md`](docs/reports/completion_report_template.md), [`docs/examples/reports/example_completion_report.md`](docs/examples/reports/example_completion_report.md)
