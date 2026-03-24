# Codex Project Kit

A reusable repository operating system for running projects with Codex from intake through closeout.

## What this repository is
**Codex Project Kit** is a structured scaffold of protocols, standards, templates, and GitHub collaboration defaults that supports consistent project execution.

## Why it exists
Projects often fail due to unclear scope, weak validation, or incomplete handoff. This kit standardizes execution so every task has:
- a clear start and end state
- explicit scope boundaries
- validation gates
- success and failure criteria
- rollback/recovery guidance
- consistent reporting

## Who it is for
- Engineers using Codex for delivery work
- Technical leads who need repeatable execution quality
- Teams adopting issue/PR driven workflows

## Core workflow
Follow the staged protocol:
1. Discovery
2. Plan
3. Design Contract
4. Implementation
5. Validation
6. Hardening
7. Documentation
8. Handoff

Repository-level execution rules are defined in [`AGENTS.md`](AGENTS.md).

## Repository layout
- `AGENTS.md` — operating instructions for Codex in this repository
- `docs/protocols/` — staged execution protocol and recovery logic
- `docs/standards/` — coding, validation, documentation, and security rules
- `docs/templates/` — reusable task/intake/plan templates
- `docs/reports/` — completion report template
- `.github/` — issue templates, PR template, and review workflow scaffold
- `plans/active/` — active execution plans for non-trivial work

## How to use this for a new task
1. Capture task details with `docs/templates/project_intake_template.md`.
2. Classify task size/risk using `docs/protocols/stage_definitions.md`.
3. For non-trivial tasks, create a plan in `plans/active/` from `docs/templates/execplan_template.md`.
4. Execute using `docs/protocols/project_execution_protocol.md`.
5. Validate with `docs/standards/validation_matrix.md`.
6. Report completion with `docs/reports/completion_report_template.md`.

## Getting started
1. Read `AGENTS.md`.
2. Open the protocol and standards docs under `docs/`.
3. Start work from the intake template and create an ExecPlan when required.
4. Use the PR and issue templates for tracked execution.

## Repository data policy
Large binaries, generated artifacts, and datasets should not be committed to the main repository. Store them in external artifact storage and reference them in docs as needed.
