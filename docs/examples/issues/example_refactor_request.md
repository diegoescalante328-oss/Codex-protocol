# Example Issue: Refactor Request

## Motivation
Protocol routing is spread across `README.md`, `AGENTS.md`, and protocol docs with some duplicated phrasing. A focused refactor can reduce duplication while preserving authority.

## Current Pain Points
- Planning rules are discoverable but fragmented.
- Repeated-use guidance appears in multiple files with minor wording drift.
- New contributors may not know where planning rules live.

## Target Improvements
- Introduce a single planning guide (`PLANS.md`) and route to it.
- Keep `AGENTS.md` concise by pushing detail into docs.
- Normalize shared terms: `ExecPlan`, `Done Definition`, `Completion Report`.

## Non-Goals
- Changing stage order or status labels.
- Introducing new automation dependencies.

## Scope
### In Scope
- Routing and wording updates in protocol-layer docs.
- Template consistency updates.

### Out of Scope
- Workflow runtime behavior changes.
- Product feature development.

## Risks
- Over-refactor could remove important context.
- New doc could duplicate existing guidance if not tightly scoped.

## Validation Requirements
- Required checks:
  - Cross-reference integrity across routing docs.
  - Vocabulary consistency spot-check across protocol/templates.
- Suggested commands:
  - `rg -n "PLANS.md|ExecPlan|Done Definition|Completion Report" README.md AGENTS.md docs`
  - `test -f PLANS.md`

## Done Definition
- Planning rules are centralized and referenced from AGENTS/README/protocol.
- Duplicate/ambiguous phrasing is reduced.
