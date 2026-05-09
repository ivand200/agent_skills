---
name: architecture-principles
description: Apply lightweight architecture principles during design or implementation. Use for simplicity, module boundaries, explicit module interfaces, interface-first review, and tradeoffs such as DRY, KISS, YAGNI, coupling, and cohesion.
---

# Architecture Principles

Prefer deep modules: small stable interfaces that hide meaningful complexity.

Decision priority:

1. correctness
2. clarity
3. simplicity
4. maintainability
5. deduplication

## Rules

- Prefer existing project patterns unless they are causing real pain.
- Design deep modules: keep public interfaces small and stable while hiding volatile details and meaningful complexity.
- Keep related behavior together; split modules around ownership of design decisions, not processing steps alone.
- Add abstraction only when it hides real complexity, removes meaningful duplication, protects an external boundary, supports useful fakes, or stabilizes a contract.
- Avoid shallow abstractions: speculative hooks, generic layers, pass-through modules, catch-all services, and APIs that expose internals.

## Use When Relevant

- Layering: use `UI / transport -> business logic / use case -> data access / infrastructure` as the default mental model for apps. Keep business decisions out of UI handlers and persistence details out of business workflows.
- Repository pattern: use when persistence queries are complex, reused, business-significant, need useful test fakes, or hide storage volatility. Avoid pass-through repositories that only rename ORM/database calls.

## Module Interfaces

A module interface is what other code may rely on: commands, endpoints, schemas, exported functions/classes, service methods, events, permissions, errors, side effects, ordering, idempotency, and invariants.

It does not require a formal protocol or base class. Add formal abstraction only for multiple implementations, external boundaries, useful fakes, or a clear stability need.

Callers and tests should not depend on storage layout, helper order, algorithms, retry mechanics, cache behavior, log text, prompts, or private state unless explicitly part of the contract.

## Interface-First Review

Review/test public contracts before internals. `skip` deep review only when the change is internal-only, low risk, and protected by reliable behavior or contract tests.

Use `full` review when a change affects public behavior, schemas, events, commands, security/auth/privacy, money, data integrity, migrations, concurrency, performance, operations, module boundaries, or weak/flaky/implementation-coupled tests.

## Output Lens

When useful, explain:

- owner: what owns the decision
- public interface: what callers may rely on
- hidden details: what must stay private
- tests/proof: what protects the boundary
- deep-review triggers: what raises risk
- complexity avoided: what coupling or wrong abstraction is prevented

This skill supports `design-doc` and review. Do not inflate small work just because richer abstractions are imaginable.
