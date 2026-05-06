---
name: research-context
description: Investigate repo and external context only as far as needed to support safe design or implementation, including current code behavior, module boundaries, docs, external contracts, approaches, and risk signals when relevant.
---

# Research Context

Investigate only far enough to reduce design or implementation risk. `context.md` is evidence for safe work; it may include repo facts, official docs, external API contracts, library behavior, migration notes, or approach comparisons.

## Use When

- the user asks for investigation, current-state analysis, or external research
- current behavior is unclear
- the task crosses subsystem boundaries
- root cause, data, auth, infrastructure, external contracts, performance, or regression risk matters
- library/framework/API behavior or current best practice materially affects the design

Skip when steering docs plus minimal reading are enough, or when the task is low-risk and clear.

## Rules

- Do not implement code.
- Prefer current code over stale planning docs.
- Distinguish confirmed facts from assumptions.
- Keep research proportional.
- Call out stale artifacts and whether re-approval is needed.
- Search the web only when repo evidence is insufficient, current docs matter, or the external dependency/approach affects the design. Prefer primary sources and distinguish sourced facts from inference.

## Workflow

1. Read the task or bug description first.
2. Read relevant steering and companion artifacts.
3. Check for spec gaps: missing scope, examples, constraints, acceptance IDs, or open questions.
4. Trace real entry points and main flows to system boundaries when repo behavior matters.
5. Identify module boundaries, public interfaces, hidden details, and contract-test coverage when relevant.
6. Inspect nearby models, schemas, config, persistence, tests, and integrations only as needed.
7. Research official docs, external contracts, migration notes, or approach tradeoffs only when they reduce real uncertainty.
8. Record risks, omissions, freshness, sources, and handoff facts for manager/design.

## Output

If input is `tasks/<task-name>/task.md`, write `tasks/<task-name>/context.md`; otherwise answer in this structure:

```md
# Context Report: [Task Name]

## Summary
- Task and touched system area.

## Spec Gaps
- Ambiguities or missing scope/examples/constraints/IDs.

## Companion Artifacts
- State/task/context/design/tasks status when relevant.

## Artifact Freshness
- Status: `current` | `stale`
- Last reviewed against: ...
- Re-approval required: `yes` | `no`
- Why: ...

## Repo Evidence
- `path`: fact or risk.

## External Evidence
- Source/link: fact, constraint, or approach note.

## Current Flow
- Entry point, path, side effects, errors.

## Data / Contracts
- Entities, schemas, APIs, permissions, invariants, contract-test gaps.

## Patterns / Conventions
- Relevant architecture, naming, error, and testing conventions.

## Risks / Open Questions
- ...

## Handoff
- Manager/design facts.

## Confidence
- high | medium | low, with why.
```
