# Example Issue: Feature Request

## Objective
Add a mandatory `Task Class` field to all issue templates so intake is explicit about expected rigor (`small`, `non-trivial`, `high-risk`).

## Current State
Issue templates capture scope and validation expectations, but task classification is implicit and can be missed.

## Desired State
All issue templates require task classification at issue creation time, improving routing to planning and validation requirements.

## In Scope
- Update issue templates in `.github/ISSUE_TEMPLATE/`.
- Ensure wording aligns with stage definitions.

## Out of Scope
- Changes to workflow automation.
- Non-template repository refactors.

## Constraints
- Preserve existing template structure where possible.
- Use repository vocabulary consistently.

## Success Criteria
- All issue templates include a `Task Class` section.
- Field uses exact values `small` / `non-trivial` / `high-risk`.
- Template wording links to protocol stage definitions.

## Failure Criteria
- Any template omits task class guidance.
- Terminology diverges from stage definitions.

## Validation Requirements
- Required checks:
  - File existence and front matter validity.
  - Manual template rendering sanity in GitHub markdown view.
- Suggested commands:
  - `test -f .github/ISSUE_TEMPLATE/feature_request.md`
  - `rg -n "Task Class|small|non-trivial|high-risk" .github/ISSUE_TEMPLATE`

## Extra Context
- Dependencies: `docs/protocols/stage_definitions.md`
- Risks: Inconsistent wording could confuse classification.
