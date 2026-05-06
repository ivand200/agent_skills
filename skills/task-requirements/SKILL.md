---
name: task-requirements
description: Create or refine `task.md` with requirements, acceptance criteria, interface facts, and risk facts. Manager owns routing.
---

# Task Requirements

Create or refresh `tasks/<task-name>/task.md`. Do not write implementation code or source edits.

Capture facts; do not choose workflow route, pass gates, or advance stages.

## Read

- User request first.
- `AGENTS.md`, `CLAUDE.md`, and `steering/` only when present and relevant.
- Existing companion artifacts only when refreshing accepted scope.
- Repository evidence before asking questions.

If the request is a defect, regression, broken behavior, failing test, or current-vs-expected report, stop and use `bugfix-spec`.

## Capture

- type: `feature` or `bugfix`
- scale: `low`, `medium`, or `large`
- interface impact: `none`, `internal-only`, or `public-contract`
- risk flags: `auth`, `security`, `privacy`, `money`, `data integrity`, `migration`, `concurrency`, `performance`, `operations`, or `none`
- review hint: `skip`, `full`, or `unknown`
- user stories, rules, examples, open questions
- Given / When / Then acceptance criteria
- public contract and behavior-test expectations

Use `grill-me` for any questions that you cannot get answers from the repo.

## Output

```md
# Task: [Task Name]

## Goal

...

## Artifact Flag

- type: `feature | bugfix`
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
- Contract tests expected: ...
- Notes: ...

## Examples

- **Example 1**
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

Keep workflow status in `state.json`, not this artifact.
