---
name: behavior-tests
description: Write or review BDD-style automated tests that prove business rules, contracts, and module interfaces through stable seams. Prefer fixtures for setup, exactly one Act, 1-2 meaningful assertions, and delete or rewrite low-value legacy tests instead of preserving implementation-detail coverage.
---

# Behavior Tests

Write tests around observable business behavior, contracts, and module interfaces.

## Core Rules

- Test observable business behavior through the strongest stable seam available: route, command/workflow, module interface, exported domain operation, or UI behavior only when it proves business logic.
- Prove outcomes users, business rules, or callers care about: permissions, validation, status transitions, calculations, error semantics, idempotency, invariants, and visible side effects.
- Avoid implementation and platform details: private helpers, method-call order, mock interaction counts, built-in library/framework behavior, CRUD pass-throughs, storage layout, logs, cache details, and private state.

## Test Shape

Use Arrange-Act-Assert:

- Arrange: move setup into fixtures/helpers/builders.
- Act: exactly one meaningful business action.
- Assert: 1-2 assertions about the business outcome, returned value, contract status, domain effect, error, or preserved invariant.

Use fakes, fixtures, factories, builders, or harnesses for setup; mock only real external, flaky, or expensive seams.

Name tests as business scenarios, e.g. `rejects expired coupons`, not implementation events such as `calls_save_once`.

## Existing Test Triage

When touching tests:

- `keep`: proves a distinct rule through a stable seam.
- `rewrite`: valid intent, but too coupled to internals, too broad, or assertion-heavy.
- `delete`: implementation-only, duplicate, technical wiring, or would fail after a safe refactor.

Preserve or improve behavior coverage. Pause only if removing a test would drop the only known coverage for a relevant rule and the replacement is unclear.

## Workflow

1. Identify the rule or contract.
2. Pick the highest-value stable seam.
3. Express Given / When / Then.
4. Arrange with fixtures/helpers.
5. Perform one Act.
6. Assert 1-2 meaningful outcomes.
7. Remove implementation-detail assertions or low-value tests you touch.

## Final Check

The test should prove behavior or a public contract, survive safe internal refactors, use one Act, keep assertions tight, and avoid implementation-detail coupling.
