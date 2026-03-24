# Documentation Rules

## When Documentation Must Be Updated
Update docs in the same change set when work changes:
- behavior
- interfaces/contracts
- setup or runtime configuration
- validation expectations
- operational, rollback, or recovery procedures
- limitations or known constraints

## Possible Documentation Targets
Depending on scope, update one or more of:
- `README.md`
- `AGENTS.md` (only for recurring operational guidance)
- `docs/project_profile.md`
- `PLANS.md`
- `docs/protocols/`
- `docs/standards/`
- `docs/templates/`
- runbooks/migration notes/architecture notes (if present)

## Quality Standard
Documentation must be:
- accurate to the implemented state
- specific and actionable
- aligned with repository vocabulary (Discovery, Plan, Design Contract, etc.)
- cross-referenced to related docs where useful
- concise and scan-friendly

## Examples and Operational Notes
When relevant, include:
- setup prerequisites and assumptions
- command examples that actually work for the repository
- migration/backward-compatibility notes
- known limitations and non-goals

## Alignment Requirement
Do not leave docs contradicting implementation or protocol. If complete alignment is not possible in the task, report the gap explicitly in Handoff.
