# Stage Definitions

## Purpose
Classify work so protocol rigor matches task complexity and risk.

## Task Classes

### Small Task
A change with narrow scope, low coupling, and low risk.

Typical characteristics:
- Touches few files, usually in one area.
- No architectural change.
- Straightforward validation.
- No sensitive security or data impact.

**Required protocol level**
- Stage 0 through Stage 8 still apply, but may be lightweight.
- ExecPlan is optional.

### Non-Trivial Task
A change with broader scope, multi-file impact, or moderate uncertainty.

Typical characteristics:
- Crosses modules or concerns.
- Requires explicit design choices.
- Needs multiple validation checks.
- Risk of regressions if not planned.

**Required protocol level**
- Full staged protocol required.
- ExecPlan in `plans/active/` is mandatory.

### High-Risk Task
A change with significant security, reliability, data, or operational impact.

Typical characteristics:
- Touches auth, permissions, data lifecycle, migrations, or critical runtime behavior.
- Failure could cause outages, data loss, or security exposure.
- Rollback complexity is non-trivial.

**Required protocol level**
- Full staged protocol with strict gating at each stage.
- ExecPlan is mandatory.
- Explicit rollback and failure handling notes are mandatory.
- Elevated validation depth and hardening checks are mandatory.
