---
name: breakdown
description: Turn an accepted design into a short ordered implementation backlog with validation and skip/full review scope.
---

# Breakdown

Create or refresh `tasks/<task-name>/tasks.md`. Do not implement code.

Use only when manager asks for an explicit backlog: multiple ordered tasks, integration steps, mixed review scopes, or multi-agent execution.

## Inputs

- preferred: `design.md`
- optional: `task.md`, `context.md`, `oracle-gate.md`

## Rules

- Stay within accepted task/design scope.
- Stop if design is not settled enough or a required oracle gate is missing, failed, or unapproved.
- Prefer 3-12 tasks, each one clean implementation pass.
- Include verification through observable behavior or public contracts from `oracle-gate.md` when present.
- Carry forward review scope.
- Split tasks when low-risk work mixes with interface, cross-module, or high-risk work.
- Manager owns routing and completion state; this file owns backlog content only.

## Output

```md
# Implementation Tasks: [Task Name]

## Traceability Matrix

| Source  | Task     | Validation |
| ------- | -------- | ---------- |
| `REQ-1` | `Task 1` | `VAL-1`    |

## Backlog

- [ ] **Task 1: [Title]**
  - **Covers:** `REQ-1`, `AC-1`, or design goal
  - **Validation:** `VAL-1` or oracle proof item
  - **Review:** `skip | full` plus short reason
  - **Depends on:** `None`
  - **Files:** `path/to/file`
  - **Action:** Specific implementation step
  - **Verify:** Focused test, check, or manual validation

## Notes

- Blockers, deferred work, or follow-up validation.
```
