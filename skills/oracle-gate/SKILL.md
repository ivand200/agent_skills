---
name: oracle-gate
description: Define the smallest proof that can distinguish a correct implementation from a wrong one before coding starts.
---

# Oracle Gate

Decide how we will know the implementation is correct before coding.

## Use When

- implementation is about to start
- a wrong implementation would be plausible
- behavior, contracts, data, auth, security, migrations, concurrency, money, or regressions matter
- tests are weak, missing, flaky, or coupled to internals

Skip when the change is tiny, internal-only, and already covered by reliable tests.

## Rules

- Do not implement.
- Do not write tests here.
- Do not plan one test per requirement.
- Pick 1-3 critical claims.
- Prefer public boundaries: API, command, service/use-case, module interface, or user-visible UI.
- A proof is useful only if it would fail when important behavior is wrong.
- If no good proof boundary exists, block and fix the design.
- Default output is `## Oracle Gate` inside `design.md`.
- Do not create `oracle-gate.md`.
- Do not update `state.json` or `tasks.md`.

## Oracle Types

Use the simplest oracle that fits:

- `specified`: expected behavior is known
- `contract`: public API, invariant, schema, or permission must hold
- `metamorphic`: exact output is hard, but a relation must hold
- `human`: automation cannot decide; manual check is explicit

## Output

```md
## Oracle Gate

| Claim | Oracle | Boundary | Check | Failure it catches |
| --- | --- | --- | --- | --- |
| ... | `specified | contract | metamorphic | human` | ... | ... | ... |

Verdict: `pass | block`
```
