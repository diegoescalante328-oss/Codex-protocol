# ExecPlan — Docs Ergonomics Entry-Point Pass

## Task
Add lightweight operator and quickstart entry-point docs to improve first-run and repeated-use usability without changing governance authority.

## Why This Task Exists
The latest consolidated audit verification report identifies an entry-point ergonomics gap and an audit expectation mismatch due to missing `HOW_TO_USE_THIS_PROJECT.md` and `PROJECT_QUICKSTART.md`.

## Objective
Create two thin routing-oriented docs, add only directly necessary cross-reference updates, and produce a structured Completion Report while preserving authority in existing governance docs.

## Start Point
- `HOW_TO_USE_THIS_PROJECT.md` does not exist.
- `PROJECT_QUICKSTART.md` does not exist.
- Existing governance authority chain is centered on `AGENTS.md`, `PLANS.md`, protocols, standards, templates, reports, and examples.

## End Point
- Both new docs exist and provide fast routing for first-run and repeated-use flows.
- Cross-references are updated where directly helpful.
- No policy fork or authority duplication is introduced.
- Completion Report is added for this pass.

## Task Class
- `non-trivial` (multiple documentation files and entry-point routing updates)

## Scope
### In Scope
- Add `HOW_TO_USE_THIS_PROJECT.md`.
- Add `PROJECT_QUICKSTART.md`.
- Update directly relevant references (e.g., README and/or examples index).
- Add a structured completion report for this task.

### Out of Scope
- Governance model rewrites.
- Workflow vocabulary changes.
- Major template edits.
- Planning-system redesign.
- Broad documentation cleanup unrelated to entry-point ergonomics.

## Constraints
- Preserve authority chain and vocabulary.
- Keep `AGENTS.md` concise and avoid turning new docs into policy authorities.
- Keep new docs thin, scan-friendly, and routing-first.

## Target Files
- `HOW_TO_USE_THIS_PROJECT.md` (new)
- `PROJECT_QUICKSTART.md` (new)
- `README.md` (cross-reference update)
- `docs/reports/2026-03-25_docs_ergonomics_completion_report.md` (new)

## Discovery Notes
- Current state: governance and planning docs are strong; onboarding requires reading across multiple docs.
- Desired state: add two lightweight entry-point docs that route to authoritative sources.
- Dependencies: existing docs under `AGENTS.md`, `PLANS.md`, `docs/protocols/`, `docs/standards/`, `docs/templates/`, `docs/reports/`, `docs/examples/`.
- Assumptions requiring verification: links remain valid after updates.
- Risks discovered during Discovery: accidental policy duplication if new docs include normative rules instead of pointers.

## Risks and Mitigations
- Risk: New docs become competing authority sources.
  - Mitigation: Explicitly state they are navigation docs; route normative guidance to authoritative documents.
- Risk: Link drift from reference updates.
  - Mitigation: Run explicit cross-reference checks and markdown sanity checks.

## Design Contract
- Planned files/components/interfaces: add two top-level docs plus focused README update and task completion report.
- Invariants to preserve: authority chain, stage vocabulary, planning trigger policy location.
- Non-goals: changing policy content in `AGENTS.md`, `PLANS.md`, protocols/standards/templates.
- Compatibility/migration considerations: backward-compatible documentation-only additions.

## Implementation Plan
1. Draft `HOW_TO_USE_THIS_PROJECT.md` as a practical operator routing manual.
2. Draft `PROJECT_QUICKSTART.md` as a fast-start workflow guide with minimal text and high signal links.
3. Add minimal cross-reference updates in `README.md`.
4. Run validation checks for existence, references, terminology, and markdown sanity.
5. Produce structured completion report artifact.

## Validation Plan
| Check | Command | Expected Result | Notes |
|---|---|---|---|
| File existence | `test -f HOW_TO_USE_THIS_PROJECT.md && test -f PROJECT_QUICKSTART.md` | PASS | Both docs present. |
| Completion report existence | `test -f docs/reports/2026-03-25_docs_ergonomics_completion_report.md` | PASS | Report artifact present. |
| Cross-reference checks | `rg -n "HOW_TO_USE_THIS_PROJECT.md|PROJECT_QUICKSTART.md|AGENTS.md|PLANS.md|docs/protocols|docs/standards|docs/templates|docs/reports|docs/examples" README.md HOW_TO_USE_THIS_PROJECT.md PROJECT_QUICKSTART.md` | PASS | Required routing coverage present. |
| Terminology consistency | `rg -n "Discovery|Plan|Design Contract|Implementation|Validation|Hardening|Documentation|Handoff|Done Definition|ExecPlan|Completion Report" HOW_TO_USE_THIS_PROJECT.md PROJECT_QUICKSTART.md README.md` | PASS | Vocabulary preserved. |
| Markdown sanity | `python - <<'PY'\nimport pathlib\nfiles=[pathlib.Path('HOW_TO_USE_THIS_PROJECT.md'), pathlib.Path('PROJECT_QUICKSTART.md'), pathlib.Path('README.md'), pathlib.Path('docs/reports/2026-03-25_docs_ergonomics_completion_report.md')]\nfor f in files:\n    txt=f.read_text()\n    assert txt.strip(), f'{f} is empty'\n    assert '\\t' not in txt, f'{f} contains tab characters'\nprint('PASS')\nPY` | PASS | Lightweight formatting sanity check. |

## Rollback / Recovery
- Rollback trigger(s): broken links, authority confusion, or incorrect routing.
- Rollback steps: `git checkout --` affected docs or revert commit.
- Post-rollback verification: rerun cross-reference and terminology checks.

## Done Definition
- `HOW_TO_USE_THIS_PROJECT.md` and `PROJECT_QUICKSTART.md` exist, are scan-friendly, and route to authoritative docs.
- Cross-references needed for discoverability are updated.
- No major policy duplication introduced.
- Structured completion report is added.
- Validation evidence captured.

## Final Report Requirements
- Summary and objective status.
- Plan-vs-actual notes.
- Files changed.
- Commands run.
- Validation results.
- Documentation updates.
- Known risks and follow-up recommendations.
