---
name: task-requirements
description: Create or refine feature `task.md` with user stories, rules, acceptance examples, routing facts, and open questions. Manager owns routing.
---

# Task Requirements

Create or refresh `tasks/<task-name>/task.md` for feature work. Do not edit source code or workflow state.

Use a compact BDD shape: user story, rules, examples, questions.

If the request is a defect, regression, broken behavior, failing test, or current-vs-expected report, stop and use `bugfix-spec`.

## Rules

- Capture facts only; do not choose the workflow route, pass gates, or advance stages.
- Read the user request first.
- Inspect repository evidence before asking questions when the answer should be discoverable.
- Use `grill-me` for blocking/important questions that repository evidence cannot answer.
- Keep workflow status in `state.json`, not this artifact.
- Write rules as observable system behavior when possible.
- Write acceptance examples in Given/When/Then form.

## Output

```md
# Task: [Task Name]

## Goal

...

## Routing Facts

- type: `feature`
- scale: `low | medium | large`
- interface impact: `none | internal-only | public-contract | unclear`
- risk flags: `auth | security | privacy | money | data integrity | migration | concurrency | performance | operations | none`
- review hint: `skip | full | unknown`

## User Stories

- As a [actor], I want [capability], so that [outcome].

## Rules

- [REQ-1] When ..., the system shall ...
- [REQ-2] If ..., the system shall ...

## Acceptance Examples

### AC-1: [Short Name]

Covers: `REQ-1`

Given ...
When ...
Then ...

## Questions

- ...
```
