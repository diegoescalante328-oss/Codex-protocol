# Stage Definitions

## Purpose
Classify tasks so process rigor, planning depth, validation requirements, and rollback expectations match risk.

## Small Task
A narrowly scoped, low-risk change with minimal coupling.

**Characteristics**
- Touches a small number of files in one area.
- No architecture shift or critical interface change.
- Low likelihood of regression.
- No sensitive security/data/deployment surface.

**Required protocol level**
- Use all stages in lightweight form.
- ExecPlan is optional unless Discovery reveals ambiguity/risk.

**Validation rigor**
- Run checks directly relevant to touched surfaces.
- Provide at least a clear smoke/manual verification path.

## Non-Trivial Task
A broader change with moderate uncertainty or cross-area impact.

**Characteristics**
- Multi-file or multi-component impact.
- Requires explicit design decisions.
- Has meaningful regression risk if unplanned.
- May touch behavior with downstream dependencies.

**Required protocol level**
- Full stage execution required.
- ExecPlan required before Implementation.
- Plan must include target files, risks, validation plan, and Done Definition.

**Validation rigor**
- Run broad applicable checks (tests/lint/format/type/build/smoke/manual as relevant).
- Record command evidence and unresolved exceptions.

## High-Risk Task
A change with material security, reliability, data, or operational risk.

**Characteristics**
- Touches auth/authorization, secrets, data lifecycle, schema/migrations, deployment controls, or critical runtime paths.
- Failure can cause outage, data loss, compliance exposure, or hard rollback.

**Required protocol level**
- Full stage execution with strict gating.
- ExecPlan is mandatory and must include explicit rollback/recovery notes.
- Design Contract must document invariants and non-goals in detail.

**Validation rigor**
- Deep validation and hardening are mandatory.
- Include targeted negative-path checks and explicit risk notes.
- Include dedicated security note in handoff when sensitive surfaces are changed.

## Escalation Rule
If uncertainty remains after Discovery, classify upward (`small` → `non-trivial` → `high-risk`) and apply stricter controls.
