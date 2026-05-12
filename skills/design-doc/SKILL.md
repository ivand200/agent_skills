---
name: design-doc
description: Create or refine a compact `design.md` centered on module/interface decisions, options, tradeoffs, context research, and oracle proof before coding.
---

# Design Doc

Create or refresh `tasks/<task-name>/design.md`. Do not write implementation code or source edits.

The design doc is a decision artifact: what changes, which option won, why, and how we will know implementation is correct.

Use `architecture-principles` for module/interface judgment. Use `research-context` only when facts would change the decision. Use `oracle-gate` before implementation when a wrong implementation would be plausible.

## Use When

- requirements or bug analysis are approved and implementation needs direction
- the task touches module boundaries, public interfaces, data, auth/security/privacy, operations, migrations, performance, concurrency, or cross-module behavior
- multiple viable implementation options exist
- implementation would likely churn without a decision
- `tasks.md` needs a clear source for implementation slices

Skip or keep minimal for tiny, localized, low-risk work.

## Rules

- Start from the outside boundary callers/users rely on, then trace inward only as needed.
- Record decision-relevant evidence, not every file inspected.
- Put research in `## Context Research`; do not create `context.md`.
- Put proof in `## Oracle Gate`; do not create `oracle-gate.md`.
- Prefer the smallest design that satisfies accepted requirements.
- Prefer 1-3 critical proof claims over one check per requirement.
- Use `grill-me` for blocking or important product, architecture, system-design, interface, or proof questions not answerable from artifacts, guidance, or targeted research.
- Keep workflow status in `state.json`; this skill may recommend state changes but must not make them.

## Workflow

1. Read `task.md` or `bugfix.md` first.
2. Read `state.json`, existing `design.md`, and `tasks.md` when present.
3. Read project guidance when relevant: `steering/`, `README.md`, `AGENTS.md`, `CLAUDE.md`.
4. Trace affected modules/interfaces from public boundary inward.
5. Use `research-context` only for facts that change options or risk.
6. Identify viable options before choosing.
7. Choose the smallest safe option.
8. Use `oracle-gate` to define the smallest useful proof.
9. Write or refresh `design.md`.
10. Call out stale downstream artifacts when scope, proof, or task order changes.

## Output

```md
# Design: [Task Name]

## Goal

...

## Context Research

- Question:
- Evidence:
  - Repo:
  - Docs:
- Options:
  - Option A:
  - Option B:
- Decision impact:
- Open risk:
- Confidence: `high | medium | low`

## Module / Interface Design

| Module | Outside Boundary | Public Interface | Change | Hidden Details |
| --- | --- | --- | --- | --- |
| ... | ... | ... | `none | changed | new | unclear` | ... |

## Options Considered

- Option A:
- Option B:

## Decision

- Chosen option:
- Why:
- Invariants:
- Tradeoffs:

## Data / Operations

- Data/model impact:
- Migration/rollout/rollback:
- Runtime/ops concerns:
- Security/privacy concerns:

## Oracle Gate

| Claim | Oracle | Boundary | Check | Failure it catches |
| --- | --- | --- | --- | --- |
| ... | `specified | contract | metamorphic | human` | ... | ... | ... |

Verdict: `pass | block`

## Review Scope

- Interface changed: `yes | no`
- Contract behavior changed: `yes | no`
- Risk flags: `auth | security | privacy | money | data integrity | migration | concurrency | performance | operations | none`
- Reviewer mode: `skip | full`
- Why:

## Open Questions

- ...

## Downstream Impact

- `tasks.md`: `current | stale | not-created`
```
