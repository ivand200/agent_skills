---
name: bugfix-spec
description: Create or refine bugfix `task.md` with current behavior, expected behavior, unchanged behavior, reproduction, acceptance examples, routing facts, and open questions.
---

# Bugfix Spec

Create or refresh `tasks/<task-name>/task.md` for defect work. Do not edit source code or workflow state.

Use a surgical bugfix shape: current behavior, expected behavior, unchanged behavior, examples, questions.

Use `task-requirements` for routine feature work.

## Use When

- the user describes a bug, regression, broken behavior, failing test, or current-vs-expected report
- the fix should stay narrower than a feature request
- unchanged behavior matters for regression prevention

## Rules

- Capture facts only; do not choose the workflow route, pass gates, or advance stages.
- Prefer concrete reproduction details over abstract summaries.
- Separate confirmed current behavior from suspected root cause.
- Record unchanged behavior when regressions would be costly.
- Inspect repository evidence, logs, or tests before asking questions when the answer should be discoverable.
- Use `research-context` later only when root cause or subsystem behavior is unclear enough to affect design.
- Keep workflow status in `state.json`, not this artifact.

## Output

```md
# Bugfix: [Task Name]

## Goal

Brief defect and why it matters.

## Routing Facts

- type: `bugfix`
- scale: `low | medium | large`
- confidence: `high | medium | low`
- interface impact: `none | internal-only | public-contract | unclear`
- risk flags: `auth | security | privacy | money | data integrity | migration | concurrency | performance | operations | none`
- review hint: `skip | full | unknown`

## Bug Map

- [BUG-1] Current: When ..., the system currently ...
- [FIX-1] Expected: When ..., the system shall ...
- [REG-1] Unchanged: When ..., the system shall continue to ...

## Reproduction

- Preconditions:
- Steps:
- Observed:

## Acceptance Examples

### AC-1: [Short Name]
Covers: `BUG-1`, `FIX-1`

Given ...
When ...
Then ...

## Questions

- ...
```
