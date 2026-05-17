---
name: project-specs
description: Create or refresh tiny project steering docs in `steering/` for durable product purpose, technical constraints, and module/interface seams.
---

# Project Specs

Maintain small, durable project-level steering docs.

## Glossary

Use these terms exactly in every suggestion. Consistent language is the point - do not drift into "component," "service," "API," or "boundary." Full definitions live in `skills/glossary/LANGUAGE.md` in this repo and in `$CODEX_HOME/skills/glossary/LANGUAGE.md` when installed globally.

- `Module`: anything with an interface and an implementation; a function, class, package, or slice can all be modules.
- `Interface`: everything a caller must know to use the module correctly, including types, invariants, error modes, ordering, and config. Not just the type signature.
- `Implementation`: the code inside.
- `Depth`: leverage at the interface. Deep means high leverage; shallow means the interface is nearly as complex as the implementation.
- `Seam`: where an interface lives; a place behavior can be altered without editing in place. Use this instead of "boundary."
- `Adapter`: a concrete thing satisfying an interface at a seam.
- `Leverage`: what callers get from depth.
- `Locality`: what maintainers get from depth: change, bugs, and knowledge concentrated in one place.

Key principles from `LANGUAGE.md`:

- Deletion test: imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep.
- The interface is the test surface.
- One adapter means a hypothetical seam. Two adapters mean a real seam.

This skill is informed by the project's domain model. Domain language gives names to good modules and seams. Existing steering records decisions this skill should not re-litigate.

These docs are not task plans, repo summaries, file inventories, or onboarding guides. They capture stable facts that future agents should not have to rediscover and cannot cheaply infer from repository-visible structure.

Project steering should answer only three questions:

- What is this project and who is it for?
- What technical constraints must future work respect?
- What modules exist, where are their seams, and which interfaces may callers rely on?

## Outputs

Use `steering/` by default:

- `steering/product.md`
- `steering/tech.md`
- `steering/structure.md`

Additional steering files are allowed when a durable project rule does not fit those three files, such as frontend design, test strategy, operations, or domain vocabulary.

Refresh existing files in place with targeted edits. Do not create parallel copies.

## Required Shape

`product.md` should be tiny:

- `Purpose`: what this project is, in 1-3 sentences
- `What It Does`: main user-visible jobs or capabilities
- `Users`: who uses it or depends on it

`tech.md` should focus on constraints:

- `Technical Constraints`: durable constraints future work must respect

Only include stack, commands, external providers, runtime dependencies, or conventions when they are non-obvious, easy to violate, or not cheaply inferable from repository files.

`structure.md` should focus on modules and interfaces:

- `Module Interface Map`
- `Module Rules`, only when broad cross-module rules are stable and useful

## Module Interface Map

Use the map only when stable module seams are known and the map will prevent repeated rediscovery or seam mistakes.

For each stable module, write only:

- `Module`: module name, using the project's domain language when a domain concept owns the design decision
- `Seam`: where the interface lives
- `Interface`: what callers may rely on
- `Implementation`: 1-2 sentences max about what is hidden inside

If the seam or interface is not clear, do not invent it. Say the seam or interface is unclear.

## Module Rules

Use `Module Rules` only for broad, stable rules that apply across multiple modules:

- ownership rules
- dependency direction
- public contract rules
- interface test surfaces
- review-risk triggers

Keep this section short. If a rule only matters for one module, put it in that module's map entry.

## Workflow

1. Check whether steering docs already exist.
2. Read enough repo evidence to understand durable product, tech, module, seam, and interface facts.
3. Read existing `steering/` docs, including custom steering files when present.
4. Create missing docs or patch existing docs with targeted edits.
5. Keep each foundational file readable in 1-2 minutes.
6. Report what changed and why.

If the user asks for audit, review, or recommendations only, do not edit files.

## Quality Bar

Prefer no update over noisy steering.

Each steering fact should be concise, durable, evidence-backed or explicitly user-directed, and useful across future tasks.

Use project domain vocabulary to name modules and seams. Use `LANGUAGE.md` vocabulary for architecture concepts.

Use relative links in repo-tracked Markdown. Do not save absolute local filesystem links.

Update steering only when durable truth changed. Task size is irrelevant.

Downstream skills should treat current steering as baseline context. If steering is missing, stale, noisy, or irrelevant, call out the gap instead of forcing it.
