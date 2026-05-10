---
name: oracle-gate
description: Review the approved task/design before implementation to define the smallest behavior-shaped proof required. Use after design-doc and before breakdown/implementation in spec-driven, BDD, or AI-agent workflows when planned tests should be derived from the design.
---

# Oracle Gate

Plan the smallest useful proof before implementation starts.

Use `behavior-tests` for automated test plans. Oracle Gate decides what must be proven; Behavior Tests defines what acceptable automated proof looks like.

Create or refresh `tasks/<task-name>/oracle-gate.md`. Do not implement code or write tests. Do not update `state.json` or `tasks.md`; manager owns workflow state and task lists.

## Inputs

Read all existing task artifacts when present:

- `task.md`
- `context.md`
- approved `design.md`
- existing `oracle-gate.md` when refreshing
- steering docs only when relevant to durable product, tech, structure, or design decisions

Extract only the business rules, module interfaces, risks, and non-goals needed to choose proof. If an artifact is missing, note the gap and continue.

## Core Rules

- Use 20/80 judgment: plan the few proofs most likely to catch a wrong implementation.
- Do not plan one test per acceptance criterion. Group claims into the critical rules/interfaces that matter most.
- Prefer stable boundaries: API endpoint, workflow/command, service/use-case entry point, module interface, or UI only when it proves user-visible behavior.
- Automated test plans must satisfy `behavior-tests`:
  - Arrange in fixtures, helpers, builders, or harnesses.
  - Act exactly once.
  - Assert 1-2 primary outcomes.
  - Use business scenario names.
  - Avoid private helpers, private fields, method-call order, storage layout, logs, cache behavior, framework mechanics, and mock counts.
- A planned test is not `strong` if it violates behavior-test shape.
- If a proof needs many assertions, split it or choose a higher-level contract assertion.
- CI, typecheck, lint, source scans, screenshots, and logs are supporting checks, not business proof.
- Good proof would fail if the business rule, public contract, or invariant were broken.
- If a critical rule cannot be tested from a stable boundary, require design clarification before breakdown.

## Proof Budget

Default proof budget:

- 1-2 critical behavior or contract tests.
- 0-2 E2E/manual checks when lower-level proof is insufficient.

Increase only when the task changes multiple independent rules, public contracts, auth/security/data integrity, migrations, concurrency, or money/user-visible workflows.

## Workflow

1. Identify the 1-2 most critical business rules and module interfaces for this task.
2. Define the smallest behavior-shaped proof for each, using `behavior-tests`.
3. Add E2E/manual proof only if required by user-visible or integration risk.
4. Decide readiness and review scope.

## Output

```md
# Oracle Gate: [Task Name]

## Verdict
- `pass | warn | fail`
- Why:

## Critical Rules And Interfaces

| Priority | Rule / Interface | Source | Why It Matters |
| --- | --- | --- | --- |
| 1 | ... | `task.md` | ... |

## Planned Proof

| Scenario | Boundary | One Act | Primary Assertions | Fixtures / Builders | Notes |
| --- | --- | --- | --- | --- | --- |
| ... | API | `POST ...` | ... | ... | No private assertions |

## E2E / Manual Proof

- Optional:
- Why needed:

## Not Testing

- Explicitly not testing:
- Why safe:

## Gaps

- Missing, weak, or implementation-coupled proof:

## Required Design Changes
- Must fix before breakdown/implementation.

## Review Scope
- `skip | full`
- Why: ...

## Confidence
- `high | medium | low`, with reason.
```
