---
name: task-requirements
description: Create or refine feature `task.md` with scope, acceptance criteria, interface facts, and risk facts. Manager owns routing.
---

# Task Requirements

Create or refresh `tasks/<task-name>/task.md` for feature work. Do not edit source code or workflow state.

If the request is a defect, regression, broken behavior, failing test, or current-vs-expected report, stop and use `bugfix-spec`.

## Rules

- Capture facts only; do not choose the workflow route, pass gates, or advance stages.
- Read the user request first.
- Read `AGENTS.md`, `CLAUDE.md`, `steering/`, and companion artifacts only when relevant.
- Inspect repository evidence before asking questions.
- Use `grill-me` for important questions that repository evidence cannot answer.
- Keep workflow status in `state.json`, not this artifact.
- Use the vocabularies shown in the template.

## Output

```md
# Task: [Task Name]

## Goal

...

## Routing Facts

- type: `feature`
- scale: `low | medium | large`
- interface impact: `none | internal-only | public-contract`
- risk flags: `auth | security | privacy | money | data integrity | migration | concurrency | performance | operations | none`
- review hint: `skip | full | unknown`

## User Stories

- As a [actor], I want [capability], so that [outcome].

## Rules

- [REQ-1] ...

## Module / Interface Notes

- Affected module: ...
- Affected entities: ...
- Public contract impact: `none | changed | new | unclear`
- Behavior tests expected: ...
- Contract tests expected: ...

## Examples

- Input / action: ...
- Expected result: ...

## Open Questions

- ...

## Acceptance Criteria

### AC-1: [Short Name]

Given ...
When ...
Then ...
```
