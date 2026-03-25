# Execution Plan (ExecPlan): Operational Hygiene Pass

## Task
Non-trivial operational hygiene pass to harden plan lifecycle semantics, improve report discoverability, and add lightweight drift-prevention checks.

## Why This Task Exists
Recent audit findings call out lifecycle ambiguity in `plans/active/`, weak report discoverability, and absence of conservative drift-prevention between templates/examples/governance artifacts.

## Objective
Implement scoped documentation and lightweight automation updates that improve repository operational hygiene while preserving current authority chain and governance model.

## Start Point
- `plans/active/` contains historical plans and ambiguous completion handling language.
- No dedicated report index/routing document for latest audit/completion artifacts.
- Existing workflow checks required scaffold files and markdown heading sanity, but not template/example/governance alignment drift.

## End Point
- Lifecycle policy explicitly defines active/completed/cancelled-superseded plan states and routing.
- `plans/active/` semantics are unambiguous (active work only), with destination path for completed plans.
- `docs/reports/` has a lightweight index clarifying latest audit/completion reports and report artifact purposes.
- Conservative drift-prevention check exists and is wired into existing lightweight workflow.

## Task Class
- `non-trivial`

## Scope
### In Scope
- Plan lifecycle policy updates in planning/routing docs.
- Creation of completed-plan destination and routing documentation.
- Report discoverability index for `docs/reports/`.
- Lightweight drift-prevention check for required governance artifacts and template/example alignment.
- Only directly necessary cross-reference updates.

### Out of Scope
- Authority-chain redesign.
- Planning-system redesign.
- Workflow vocabulary changes.
- Broad template rewrites or broad documentation cleanup.
- Heavy or speculative automation.

## Constraints
- Preserve existing authority hierarchy.
- Keep `AGENTS.md` concise.
- Avoid unnecessary policy duplication.
- Keep checks lightweight and maintainable for a docs-first repository.

## Target Files
- `PLANS.md`
- `plans/active/README.md`
- `plans/completed/README.md` (new)
- `plans/completed/*.md` (moved prior completed ExecPlans, if applicable)
- `README.md`
- `docs/project_profile.md`
- `docs/reports/README.md` (new)
- `scripts/check_docs_drift.py` (new)
- `.github/workflows/codex-review.yml`
- `docs/reports/<dated completion report for this task>` (new)

## Discovery Notes
- Current state:
  - `PLANS.md` defines where active plans live but not explicit lifecycle transitions.
  - `plans/active/README.md` says “close or remove completed plans according to repository policy,” but no concrete archival policy is defined.
  - Reports directory has dated files but no consolidated discoverability index.
- Desired state:
  - Explicit lifecycle policy with clear transitions and storage locations.
  - Active folder semantically strict and clean.
  - Report routing index and lightweight drift checks that fit governance-repo posture.
- Dependencies:
  - Existing planning/protocol standards docs, report artifacts, and CI scaffold workflow.
- Assumptions requiring verification:
  - Current plans in `plans/active/` correspond to completed historical work and can be archived.
- Risks discovered during Discovery:
  - Overly strict drift checks could create maintenance burden/noise.
  - Moving plan files without updating references could break historical links.

## Risks and Mitigations
- Risk: False-positive drift checks create friction.
  - Mitigation: Keep checks existence-and-keyphrase based, not structural parsing heavy.
- Risk: Breaking references after plan relocation.
  - Mitigation: run repository-wide reference scan for `plans/active/` and update only directly necessary links.
- Risk: Policy duplication across docs.
  - Mitigation: keep detailed lifecycle policy in `PLANS.md`; use concise routing summaries elsewhere.

## Design Contract
- Planned files/components/interfaces:
  - docs and lightweight script/workflow updates only.
- Invariants to preserve:
  - authority chain (`AGENTS.md` then `PLANS.md` then protocols/standards/templates), stage vocabulary, docs-first posture.
- Non-goals:
  - replacing current governance model or introducing heavy CI policy engines.
- Compatibility/migration considerations:
  - Preserve historical plan history by moving files rather than deleting.

## Implementation Plan
1. Add/clarify lifecycle policy in planning docs and create `plans/completed/` destination docs.
2. Move clearly historical completed ExecPlans from `plans/active/` to `plans/completed/` and fix direct references where needed.
3. Add `docs/reports/README.md` index for latest audit/completion report discoverability and artifact purpose.
4. Add lightweight `scripts/check_docs_drift.py` and integrate into `.github/workflows/codex-review.yml`.
5. Add task completion report and run required validation checks.

## Validation Plan
| Check | Command | Expected Result | Notes |
|---|---|---|---|
| File existence checks | `test -d plans/completed && test -f plans/completed/README.md && test -f docs/reports/README.md && test -f scripts/check_docs_drift.py` | PASS | New lifecycle/index/check artifacts exist |
| Plan lifecycle routing review | `rg -n "plans/active|plans/completed|cancelled|superseded|lifecycle" PLANS.md plans/active/README.md plans/completed/README.md README.md docs/project_profile.md` | PASS | Lifecycle semantics explicit and coherent |
| Cross-reference checks | `rg -n "plans/active/2026-03-24_protocol_hardening_execplan.md|plans/active/2026-03-25_planning_system_remediation_execplan.md|plans/active/2026-03-25_docs_ergonomics_entrypoints_execplan.md"` | PASS | No stale references remain to moved completed plans |
| Reports discoverability review | `cat docs/reports/README.md` | PASS | Latest report routing and artifact purpose are clear |
| Workflow/YAML sanity | `python - <<'PY'\nimport yaml, pathlib\npath = pathlib.Path('.github/workflows/codex-review.yml')\nyaml.safe_load(path.read_text())\nprint('PASS')\nPY` | PASS | Workflow YAML remains valid |
| Drift-check sanity | `python scripts/check_docs_drift.py` | PASS | Script passes with current repository state |

## Rollback / Recovery
- Rollback trigger(s): lifecycle policy contradictions, broken references, or noisy drift check behavior.
- Rollback steps: revert affected docs/script/workflow and restore moved plans to prior location if needed.
- Post-rollback verification: rerun cross-reference scan and drift check.

## Done Definition
- Explicit lifecycle policy exists and is applied.
- `plans/active/` clearly represents active-only plans.
- Completed plan destination exists and is in use.
- Reports index improves audit/completion discoverability.
- Conservative drift-prevention check exists and is runnable.
- Only scoped cross-reference updates were made.

## Final Report Requirements
- Summary, files changed, lifecycle/report/drift sections, validations, remaining gaps, and follow-up recommendations.
- Include plan-vs-actual notes and objective status.
