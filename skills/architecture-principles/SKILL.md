---
name: architecture-principles
description: Apply module/interface architecture principles during design, implementation, and review. Use for deep modules, seams, adapters, interface-first proof, coupling, cohesion, and abstraction tradeoffs.
---

# Architecture Principles

Architecture starts with modules and interfaces.

Use `LANGUAGE.md` vocabulary exactly: `Module`, `Interface`, `Implementation`, `Depth`, `Seam`, `Adapter`, `Leverage`, and `Locality`. Do not drift into "component," "service," "API," or "boundary." Full definitions live in `skills/glossary/LANGUAGE.md` and `$CODEX_HOME/skills/glossary/LANGUAGE.md`.

Use only `steering/` for project facts and domain names.

Prefer deep modules: small, stable interfaces that hide meaningful implementation complexity and give callers leverage while preserving locality for maintainers.

Decision priority: correctness, clarity, simplicity, maintainability, then deduplication.

## Rules

- Start from the module and its interface: what callers must know, and what implementation details stay hidden.
- Keep related behavior together; split modules around ownership of design decisions, not processing steps alone.
- The interface is the test surface. Callers and tests should cross the same seam.
- Use the deletion test: if deleting a module removes complexity, it was a pass-through; if complexity reappears across callers, the module was earning its keep.
- Add abstraction only when it hides real complexity, creates locality, supports real variation, enables useful adapters, or stabilizes an important interface.
- Avoid shallow modules: speculative hooks, pass-through wrappers, catch-all modules, and interfaces that expose implementation details.
- One adapter means a hypothetical seam. Two adapters mean a real seam.
- Respect current `steering/` docs; call out stale or missing steering instead of inventing durable project rules.

## Friction Signals

Recommend architecture changes only when there is real friction: concepts scattered across many modules, interfaces nearly as complex as implementations, repeated caller rules, tests reaching past interfaces, or small changes requiring many caller edits.

## Use When Relevant

- Layering: use `UI / transport -> business workflow -> data access / infrastructure` as a default mental model. Keep business decisions out of UI handlers and persistence details out of business workflows.
- Repository pattern: use when persistence behavior is complex, reused, business-significant, needs useful test adapters, or hides storage volatility. Avoid pass-through repositories that only rename storage calls.
- Steering: read `steering/product.md`, `steering/tech.md`, and `steering/structure.md` when present.

## Interface-First Review

Review behavior through interfaces before internals. Use `skip` only when the change is internal-only, low risk, and protected by reliable behavior or contract tests.

Use `full` when a change affects user-visible behavior, schemas, events, commands, auth/security/privacy, money, data integrity, migrations, concurrency, performance, operations, module seams, or weak/flaky/implementation-coupled tests.

For review, keep two axes separate:

- `Spec Review`: does the change implement the accepted task, design, implementation slice, and oracle proof without scope drift?
- `Standards Review`: does the change follow `steering/`, module/interface principles, behavior-test guidance, and repo conventions?

## Output Lens

When useful, explain: `Module`, `Seam`, `Interface`, hidden `Implementation`, depth/leverage/locality, adapters, tests/proof, and complexity avoided.

This skill supports `design-doc`, implementation judgment, and review. Do not inflate small work just because richer architecture is imaginable.
