# ExecPlan: Project Repositioning Pass

## Task
Reposition top-level identity and entry-point documentation so this repository is explicitly framed as a Codex-first operating system for work that outgrows ChatGPT project constraints.

## Why This Task Exists
Current docs explain governance and process well, but do not yet consistently and explicitly position the repository as the scaling path from a chat-based workflow to a governed repo-based workflow.

## Objective
Make repository identity, onboarding docs, and project profile clearly communicate when to stay in ChatGPT project workflow, when to move to Codex repository workflow, and what changes after transition.

## Start Point
- Existing docs emphasize governance/process and reusable Codex execution system.
- Relationship to ChatGPT project limits and transition guidance is implicit or absent.

## End Point
- `README.md`, `HOW_TO_USE_THIS_PROJECT.md`, `PROJECT_QUICKSTART.md`, and `docs/project_profile.md` are aligned around the same positioning model.
- New users can quickly understand purpose, transition triggers, and practical startup path.

## Task Class
- `non-trivial`

## Scope
### In Scope
- Repositioning and alignment edits in:
  - `README.md`
  - `HOW_TO_USE_THIS_PROJECT.md`
  - `PROJECT_QUICKSTART.md`
  - `docs/project_profile.md`
- Add explicit guidance for ChatGPT vs Codex usage and transition.
- Align terminology across entry-point docs.

### Out of Scope
- Changes to authority chain or governance policy documents (`AGENTS.md`, `PLANS.md`, protocols, standards, templates).
- New governance layers or speculative integrations.
- Structural repository refactors.

## Constraints
- Preserve existing governance model and workflow vocabulary.
- Keep documentation concise and avoid duplication.
- Maintain clear role separation across entry docs (identity vs operations vs quickstart vs profile).

## Target Files
- `README.md`
- `HOW_TO_USE_THIS_PROJECT.md`
- `PROJECT_QUICKSTART.md`
- `docs/project_profile.md`

## Discovery Notes
- Current state: entry docs are operationally strong but under-emphasize ChatGPT→Codex transition and scaling rationale.
- Desired state: consistent top-level messaging that this repo is the structured scaling layer beyond ChatGPT project limits.
- Dependencies: existing governance docs remain authoritative and referenced.
- Assumptions requiring verification: terminology can be aligned without breaking existing cross-references.
- Risks discovered during Discovery: over-duplicating explanations across docs could reduce clarity.

## Risks and Mitigations
- Risk: Terminology drift across entry docs.
  - Mitigation: Define shared phrases and apply consistently in each file with role-specific depth.
- Risk: Scope creep into governance docs.
  - Mitigation: Limit edits strictly to four in-scope files.
- Risk: Redundant/bloated narrative.
  - Mitigation: Keep each doc focused on its designated purpose and link outward for detail.

## Design Contract
- Planned files/components/interfaces: four entry docs only; markdown content updates only.
- Invariants to preserve: authority chain, stage vocabulary, governance references, and planning/validation expectations.
- Non-goals: altering protocols/standards/templates or adding new system layers.
- Compatibility/migration considerations: existing links and onboarding flow remain valid; only positioning language changes.

## Implementation Plan
1. Update `README.md` identity and overview with explicit ChatGPT-limit and Codex-scaling framing.
2. Add prominent "when to move to Codex" operational guidance in `HOW_TO_USE_THIS_PROJECT.md`.
3. Tighten `PROJECT_QUICKSTART.md` messaging for post-ChatGPT-limit fast path.
4. Update `docs/project_profile.md` to formalize scaling-layer purpose and external-origin work transition model.
5. Run docs validation checks and terminology alignment review.

## Validation Plan
| Check | Command | Expected Result | Notes |
|---|---|---|---|
| Unit tests | N/A | N/A | Docs-only change. |
| Integration tests | N/A | N/A | Docs-only change. |
| Lint | `markdownlint README.md HOW_TO_USE_THIS_PROJECT.md PROJECT_QUICKSTART.md docs/project_profile.md` | PASS or BLOCKED | Run if tool exists; otherwise record blocked. |
| Formatting check | N/A | N/A | Markdown style checked during review. |
| Typecheck | N/A | N/A | Docs-only change. |
| Build | N/A | N/A | Docs-only change. |
| Smoke test | `rg -n "ChatGPT project workflow|Codex repository workflow|scaling path|transition from chat" README.md HOW_TO_USE_THIS_PROJECT.md PROJECT_QUICKSTART.md docs/project_profile.md` | PASS | Confirms terminology alignment presence. |
| Manual acceptance check | Manual review | PASS | Verify role separation and non-duplication across entry docs. |

## Rollback / Recovery
- Rollback trigger(s): conflicting positioning, broken links, or misalignment with governance authority.
- Rollback steps: restore prior versions of the four edited markdown files via git checkout/revert.
- Post-rollback verification: confirm prior docs render and cross-links resolve.

## Done Definition
- Entry docs clearly state repository purpose as scaling layer beyond ChatGPT project constraints.
- Explicit guidance exists for when to stay in ChatGPT vs move to Codex and how workflow changes.
- Terminology is consistent across edited entry docs.
- Governance structure and authority chain remain unchanged.
- Validation evidence recorded with applicable checks.

## Final Report Requirements
- Summary and objective status (`Complete`, `Partial`, `Blocked`)
- Plan vs actual summary (including deviations)
- Files changed
- Commands run
- Validation results
- Documentation updates
- Known risks
- Follow-up recommendations
