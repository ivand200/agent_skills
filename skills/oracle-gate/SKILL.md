---
name: oracle-gate
description: Review the approved task/design before implementation to define the behavior, contract, regression, and manual proof required. Use after design-doc and before breakdown/implementation in spec-driven, BDD, or AI-agent workflows when planned tests should be derived from the design.
---

# Oracle Gate

Plan the proof before implementation starts.

Create or refresh `tasks/<task-name>/oracle-gate.md`. Do not implement code or write tests. Do not update `state.json` or `tasks.md`; manager owns workflow state and task lists.

## Inputs

Read only what is needed:

- steering docs when relevant
- `task.md`
- `context.md`
- approved `design.md`
- existing `oracle-gate.md` when refreshing

If an artifact is missing, note the gap and continue.

## Core Rules

- Use 20/80 judgment: focus on the proof most likely to catch a wrong implementation.
- Prefer behavior tests and module interface tests that prove business logic, rules, permissions, invariants, and observable outcomes through stable boundaries.
- Avoid planning tests around private helpers, method-call order, storage layout, logs, cache behavior, framework mechanics, or mock counts.
- CI/typecheck/lint are supporting checks, not proof of business behavior.
- Good planned proof would fail if the business rule, public contract, or invariant were broken.
- If the design cannot be tested from a stable boundary, require design clarification before breakdown.

## Workflow

1. Identify approved claims:
   - user stories
   - acceptance criteria
   - business rules
   - module interfaces
   - invariants
   - non-goals
   - risk flags

2. Map claims to required proof:
   - behavior tests
   - module interface tests
   - regression tests
   - integration/e2e tests
   - manual validation, screenshots, or logs

3. Judge planned proof strength:
   - `strong`: would prove the claim through a stable boundary
   - `weak`: partially proves the claim, depends on implementation details, or needs manual support
   - `missing`: no meaningful proof

4. List needed proof for weak or missing claims:
   - what behavior or module interface needs testing
   - preferred test boundary
   - fixtures, fakes, or external boundaries that matter
   - manual validation only when automated proof is not enough

5. Decide readiness:
   - `pass`: proof plan is sufficient for breakdown and implementation
   - `warn`: implementation can proceed, but named proof gaps or manual checks remain
   - `fail`: design is not ready because required proof is missing, unstable, or unclear

6. Recommend post-implementation review scope:
   - `skip`: proof plan is strong, risk is low, and no public contract or high-risk behavior changes
   - `full`: proof is weak/missing or risk involves auth, security, privacy, money, data integrity, migration, concurrency, performance, operations, public contracts, or module boundaries

## Output

```md
# Oracle Gate: [Task Name]

## Verdict
- `pass | warn | fail`

## Claim / Proof Map
| Claim | Source | Required Proof | Preferred Boundary | Strength | Status |
| --- | --- | --- | --- | --- | --- |
| `AC-1` | `task.md` | reject expired sessions | API behavior test | strong | planned |

## Test Design
- Behavior tests: ...
- Contract tests: ...
- Regression tests: ...
- Manual validation: ...

## Gaps
- Missing, weak, or implementation-coupled proof.

## Needed Proof
| Claim | What To Test | Preferred Boundary |
| --- | --- | --- |
| `AC-2` | rejected users cannot access the workflow | module interface test |

## Required Design Changes
- Must fix before breakdown/implementation.

## Review Scope
- `skip | full`
- Why: ...

## Confidence
- `high | medium | low`, with reason.
```
