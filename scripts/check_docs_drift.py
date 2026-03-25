#!/usr/bin/env python3
"""Lightweight docs-governance drift checks.

This script intentionally stays conservative:
- verifies required governance artifacts exist
- verifies core template sections still exist
- verifies examples include key template-aligned fields
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_ARTIFACTS = [
    'AGENTS.md',
    'PLANS.md',
    'README.md',
    'docs/project_profile.md',
    'docs/protocols/project_execution_protocol.md',
    'docs/protocols/stage_definitions.md',
    'docs/protocols/failure_and_recovery.md',
    'docs/standards/validation_matrix.md',
    'docs/templates/execplan_template.md',
    'docs/reports/completion_report_template.md',
    'docs/examples/README.md',
    'docs/reports/README.md',
    'plans/active/README.md',
    'plans/completed/README.md',
]

SECTION_EXPECTATIONS = {
    'docs/templates/execplan_template.md': [
        '## Task',
        '## Objective',
        '## Task Class',
        '## Validation Plan',
        '## Done Definition',
    ],
    'docs/reports/completion_report_template.md': [
        '## Summary',
        '## Objective Status',
        '## Plan Reference',
        '## Validation Results',
        '## Follow-Up Recommendations',
    ],
    'docs/examples/execplans/example_protocol_docs_hardening_execplan.md': [
        '## Task',
        '## Objective',
        '## Validation Plan',
        '## Done Definition',
    ],
    'docs/examples/reports/example_completion_report.md': [
        '## Summary',
        '## Objective Status',
        '## Plan Reference',
        '## Validation Results',
        '## Follow-Up Recommendations',
    ],
}


def fail(msg: str) -> None:
    print(f'FAIL: {msg}')


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_ARTIFACTS:
        if not (ROOT / rel).exists():
            errors.append(f'missing required artifact: {rel}')

    for rel, expected_snippets in SECTION_EXPECTATIONS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f'missing file for section checks: {rel}')
            continue
        text = path.read_text(encoding='utf-8')
        for snippet in expected_snippets:
            if snippet not in text:
                errors.append(f'{rel} missing expected section/snippet: {snippet}')

    if errors:
        for error in errors:
            fail(error)
        return 1

    print('PASS: docs drift check passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
