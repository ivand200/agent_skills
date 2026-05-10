---
name: project-specs
description: Create or refresh tiny project steering docs in `steering/` for durable product purpose, technical constraints, and module interface boundaries.
---

# Project Specs

Maintain small, durable project-level steering docs.

These docs are not task plans, repo summaries, file inventories, or onboarding guides. They capture stable facts that future agents should not have to rediscover and cannot cheaply infer from public repository boundaries.

Project steering should answer only three questions:

- What is this project and who is it for?
- What technical constraints must future work respect?
- What modules exist, and which public interfaces may callers rely on?

## Outputs

Use `steering/` by default:

- `steering/product.md`
- `steering/tech.md`
- `steering/structure.md`

Refresh existing files in place with targeted edits. Do not create parallel copies.

## Required Shape

`product.md` should be tiny:

- `Purpose`: what this project is, in 1-3 sentences
- `What It Does`: main user-visible jobs or capabilities
- `Users`: who uses it or depends on it

`tech.md` should focus on constraints:

- `Technical Constraints`: durable constraints future work must respect

Only include stack, commands, services, or conventions when they are non-obvious, easy to violate, or not cheaply inferable from repository files.

`structure.md` should focus on modules and interfaces:

- `Module Interface Map`
- `Module Rules`, only when broad cross-module rules are stable and useful

## Module Interface Map

Use the map only when stable module boundaries are known and the map will prevent repeated rediscovery or boundary mistakes.

For each stable module, write only:

- `Module`: module or subsystem name
- `Public interface`: what callers may rely on
- `Inner implementation`: 1-2 sentences max about what is hidden inside

If the public interface is not clear, do not invent it. Say the boundary is unclear.

## Module Rules

Use `Module Rules` only for broad, stable rules that apply across multiple modules:

- ownership boundaries
- dependency direction
- public contract rules
- testing boundaries
- review-risk triggers

Keep this section short. If a rule only matters for one module, put it in that module's map entry.

## Workflow

1. Check whether steering docs already exist.
2. Read enough repo evidence to understand durable product, tech, and module-interface facts.
3. Create missing docs or patch existing docs with targeted edits.
4. Keep each foundational file readable in 1-2 minutes.
5. Report what changed and why.

If the user asks for audit, review, or recommendations only, do not edit files.

## Quality Bar

Prefer no update over noisy steering.

Each steering fact should be concise, durable, evidence-backed or explicitly user-directed, and useful across future tasks.

Use relative links in repo-tracked Markdown. Do not save absolute local filesystem links.

Update steering only when durable truth changed. Task size is irrelevant.

Downstream skills should treat current steering as baseline context. If steering is missing, stale, noisy, or irrelevant, call out the gap instead of forcing it.
