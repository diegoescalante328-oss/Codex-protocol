# Execution Plan (ExecPlan): Protocol Hardening Pass

## Task
Repository-governance hardening for repeated Codex-driven execution.

## Why This Task Exists
The repository has a solid scaffold, but planning discoverability, example coverage, and cross-document routing need strengthening so future tasks can run with minimal prompt repetition and tighter discipline.

## Objective
Harden protocol, planning, routing, and examples so the repository is more durable and less ambiguous for repeated use.

## Start Point
- Core protocol/standards/templates exist.
- No top-level planning guide.
- No concrete example issue/plan/report artifacts.
- `AGENTS.md` is strong but can be tightened and better routed.

## End Point
- Planning system has stronger discoverability and constraints.
- Example artifacts demonstrate realistic feature/bugfix/refactor + ExecPlan + Completion Report.
- Lightweight project profile exists and is routed from `AGENTS.md`/README.
- Protocol layer terminology and cross-references are aligned.

## Scope
### In Scope
- Protocol/standards/templates/routing documents.
- Example artifacts for issue, plan, and completion reporting.
- `AGENTS.md` tightening pass after consistency fixes.

### Out of Scope
- Product code features outside protocol/governance layer.
- CI/CD behavior changes beyond lightweight routing/scaffold checks.

## Constraints
- Preserve repository workflow vocabulary and stage sequence.
- Keep `AGENTS.md` concise; push detail into docs.
- Avoid duplicate policy when cross-reference is enough.

## Target Files
- `AGENTS.md`
- `README.md`
- `PLANS.md` (new)
- `docs/project_profile.md` (new)
- `docs/protocols/*.md` (selected updates)
- `docs/templates/*.md` (selected updates)
- `docs/reports/completion_report_template.md`
- `.github/pull_request_template.md`
- `docs/examples/**` (new)
- `plans/active/README.md`

## Discovery Notes
- Current state: Process docs are present but planning rules are split and example artifacts are missing.
- Desired state: Strong routing, clearer plan triggers/quality bar, realistic examples, and consistent vocabulary.
- Dependencies: Existing protocol, standards, templates, and GitHub templates.
- Assumptions: This repository is intentionally docs-first governance scaffold.
- Risks discovered during Discovery: Over-duplication across docs; conflicting terms between templates.

## Risks
- Risk: Adding too many docs could reduce scanability.
  - Mitigation: Keep new docs lightweight and route cleanly.
- Risk: Vocabulary drift during edits.
  - Mitigation: repository-wide term sweep before finalizing.

## Design Contract
- Planned files/components/interfaces: Protocol layer docs, templates, examples, AGENTS routing.
- Invariants to preserve: Stage order, status labels, scope discipline, honest validation reporting.
- Non-goals: Introducing external tooling dependencies or automation integrations.
- Compatibility/migration considerations: Keep existing paths stable; add references for discoverability.

## Implementation Plan
1. Add planning guide and project profile; update README routing.
2. Strengthen protocol/template/report language for tighter plan-validation-handoff linkage.
3. Add realistic examples for issue types, ExecPlan, and Completion Report.
4. Perform consistency pass and tighten `AGENTS.md` last.

## Validation Plan
| Check | Command | Expected Result |
|---|---|---|
| Markdown heading sanity | `find . -type f -name '*.md' -not -path './.git/*' -print0 \| xargs -0 -I{} sh -c 'head -n 1 "{}" \| grep -Eq "^(#|---)" || { echo "bad heading: {}"; exit 1; }'` | PASS |
| Cross-reference existence checks | `test -f <referenced-file>` for key routes | PASS |
| Vocabulary drift spot-check | `rg -n "(Success Criteria|Failure Criteria|Done Definition|Completion Report|ExecPlan|Design Contract)"` | Consistent usage |
| Workflow scaffold sanity | `sed -n '1,260p' .github/workflows/codex-review.yml` | References existing required files |
| Manual alignment review | Manual read of updated protocol/templates/examples | No conflicts/ambiguity |

## Rollback / Recovery
- Rollback trigger(s): Protocol changes introduce conflicting guidance.
- Rollback steps: Revert this commit to previous protocol state.
- Post-rollback verification: Re-run markdown heading sanity + file existence checks.

## Done Definition
- Planning rules are explicitly discoverable and enforceable.
- Example artifacts exist and model expected quality.
- Routing across AGENTS/README/protocol/templates is consistent.
- Completion reporting expectations align with planning and validation.

## Final Report Requirements
- Summary and objective status (`Complete`, `Partial`, `Blocked`)
- Files changed
- Commands run
- Validation results
- Documentation updates
- Known risks
- Follow-up recommendations
