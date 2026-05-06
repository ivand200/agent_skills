---
name: design-doc
description: Create or refine `design.md` when decisions, boundaries, contracts, risk tradeoffs, or validation strategy need approval before coding.
---

# Design Doc

Create or refresh `tasks/<task-name>/design.md`. Do not write implementation code or source edits.

Use `architecture-principles`. Manager decides when design is needed and owns routing/gates.

## Use When

- Design decisions, boundaries, tradeoffs, validation strategy, oracle-gate inputs, or review scope need approval.
- Public contracts, schemas, data, auth/security/privacy, migrations, concurrency, performance, operations, or cross-module behavior may change.
- A later backlog needs a settled design.

## Workflow

1. Read `task.md` or brief first.
2. Read `context.md` if present.
3. Read relevant `AGENTS.md`, `CLAUDE.md`, and `steering/` only when present.
4. Research existing patterns only as needed.
5. Use `grill-me` if material ambiguity remains.
6. Write or refresh `design.md`.
7. Note stale downstream artifacts only when design changes accepted scope or task order.

## Output

```md
# Design Document: [Task Name]

## Goal
...

## Discovered Behavior
- Scenarios, edge cases, constraints.

## Decision Summary
- Chosen approach, why, rejected alternatives, tradeoffs, invariants, boundaries.

## Proposed Design
- Architecture / flow: ...
- File / module impact: ...
- API / contract impact: ...
- Module / entity impact:
  - Status: `none | single-module-internal | public-contract | cross-module`
  - Touched modules/entities: ...
  - Public contract impact: ...
  - Contract tests: ...

## Data / Operations
- Data/model, rollout, migration, rollback, operations when relevant.

## Review Scope
- Interface changed: `yes | no`
- Contract tests changed: `yes | no`
- Internal-only change: `yes | no`
- Risk flags: `auth | security | privacy | money | data integrity | migration | concurrency | performance | operations | none`
- Reviewer mode: `skip | full`
- Why: ...

## Traceability / Validation
| Source | Design Response | Planned Task | Planned Validation |
| --- | --- | --- | --- |
| `REQ-1` | ... | `Task 1` | `VAL-1` |

Planned validation should be concrete enough for `oracle-gate` to derive behavior, contract, regression, or manual proof before breakdown.

## Assumptions / Open Questions
- ...
```

Use module/entity detail only when risk or scale justifies it. Keep workflow status in `state.json`.
