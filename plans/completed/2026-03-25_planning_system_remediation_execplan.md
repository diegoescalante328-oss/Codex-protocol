# Execution Plan (ExecPlan): Planning System Remediation Pass

## Task
Restore and harden planning authority routing and trigger clarity after audit findings and verification follow-up.

## Why This Task Exists
Planning authority is currently degraded because `PLANS.md` is missing while multiple docs route to it. This creates broken references, weak trigger discoverability, and policy duplication risk.

## Objective
Recreate `PLANS.md` as the authoritative planning routing/enforcement guide and align planning references, trigger clarity, and duplication controls across directly affected docs.

## Start Point
- `PLANS.md` does not exist.
- Multiple docs reference `PLANS.md` as planning authority.
- Trigger language is distributed across files and can be tightened via single-source routing.

## End Point
- `PLANS.md` exists and clearly defines trigger rules, plan location, quality bar, protocol alignment, and reporting linkage.
- Planning references in key routing docs resolve and remain non-conflicting.
- Trigger rules are explicit and durable, with concise cross-references in other docs.

## Task Class
- `non-trivial`

## Scope
### In Scope
- Create/restore `PLANS.md`.
- Update planning-related references and concise routing in `AGENTS.md`, `README.md`, protocol/template docs, and `plans/active/README.md` as needed.
- Tighten explicit ExecPlan trigger criteria and reduce low-value duplicated policy text.

### Out of Scope
- Broad governance restructuring.
- Unrelated standards/protocol cleanup.
- Workflow vocabulary changes outside consistency fixes.

## Constraints
- Keep diffs tightly scoped to planning-system integrity.
- Keep `AGENTS.md` concise.
- Preserve existing workflow vocabulary and authority ordering.
- Do not invent automation or integrations.

## Target Files
- `PLANS.md` (create)
- `AGENTS.md`
- `README.md`
- `docs/protocols/project_execution_protocol.md`
- `docs/templates/execplan_template.md`
- `plans/active/README.md`
- Other directly affected planning-routing docs only if required by discovered conflicts

## Discovery Notes
- Current state: routing docs already point to `PLANS.md`, but file is absent.
- Desired state: `PLANS.md` acts as single planning authority with concise downstream references.
- Dependencies: existing stage model in `docs/protocols/`; validation/reporting expectations in standards/templates.
- Assumptions requiring verification: no additional hidden planning authority docs conflict with `PLANS.md`.
- Risks discovered during Discovery:
  - Over-editing non-planning docs could create scope creep.
  - Trigger language may drift from stage definitions if not carefully aligned.

## Risks and Mitigations
- Risk: conflicting trigger definitions across documents.
  - Mitigation: keep detailed trigger logic only in `PLANS.md` and cross-reference elsewhere.
- Risk: accidental authority inversion.
  - Mitigation: preserve `AGENTS.md` instruction priority and route detail downward.
- Risk: broken references after edits.
  - Mitigation: run targeted `rg`/existence checks across planning keywords and links.

## Design Contract
- Planned files/components/interfaces: docs-only changes to planning policy routing and wording.
- Invariants to preserve: stage vocabulary, instruction priority in `AGENTS.md`, lightweight path for small tasks.
- Non-goals: changing non-planning governance content.
- Compatibility/migration considerations: no runtime impact; documentation routing must remain easy to discover.

## Implementation Plan
1. Create `PLANS.md` with concise authority chain, trigger rules, quality bar, protocol/validation/report linkage, and usage flow.
2. Update key planning-routing docs to reference `PLANS.md` without duplicating detailed policy.
3. Tighten concise trigger statements where weak/implicit and ensure consistency across docs.
4. Run docs/governance validations (existence, reference integrity, terminology consistency, markdown sanity, manual authority review).

## Validation Plan
| Check | Command | Expected Result | Notes |
|---|---|---|---|
| File existence | `test -f PLANS.md` | PASS | Restored authority doc exists |
| Planning reference integrity | `rg -n "PLANS.md|ExecPlan|plans/active/|execplan_template" AGENTS.md README.md docs plans` | PASS | No broken/contradictory planning routing in touched docs |
| Trigger clarity spot-check | `rg -n "non-trivial|high-risk|multiple files|interfaces|config|rollback" PLANS.md AGENTS.md docs/protocols docs/templates plans/active/README.md README.md` | PASS | Trigger language explicit and aligned |
| Terminology consistency | `rg -n "Success Criteria|Failure Criteria|Done Definition|Stop Conditions|ExecPlan|Completion Report" AGENTS.md README.md docs PLANS.md` | PASS | Required vocabulary remains present/consistent |
| Markdown sanity | `python - <<'PY'\nimport pathlib\nfor p in [pathlib.Path('PLANS.md'), pathlib.Path('AGENTS.md'), pathlib.Path('README.md'), pathlib.Path('docs/protocols/project_execution_protocol.md'), pathlib.Path('docs/templates/execplan_template.md'), pathlib.Path('plans/active/README.md')]:\n    text=p.read_text()\n    assert text.startswith('#'), f'{p} missing top heading'\nprint('ok')\nPY` | PASS | Basic markdown sanity for touched docs |
| Manual authority-chain review | N/A (manual review) | PASS | Confirm authority and routing clarity improved |

## Rollback / Recovery
- Rollback trigger(s): conflicting policy definitions, unresolved broken references, or reviewer-reported authority ambiguity.
- Rollback steps: revert this docs patch; restore prior wording; re-apply minimal fixes iteratively.
- Post-rollback verification: rerun reference integrity and terminology checks.

## Done Definition
- `PLANS.md` exists as authoritative planning guide.
- Planning references in in-scope docs resolve and are non-conflicting.
- Trigger rules are explicit for required scenarios.
- Duplicative planning-policy text reduced in favor of routing where appropriate.
- Validation checks executed and reported with clear pass/N/A status.

## Final Report Requirements
- Structured Completion Report sections required by task prompt.
- Explicit list of files changed.
- Validation evidence with exact commands and outcomes.
- Remaining gaps and one next hardening recommendation.
