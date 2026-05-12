---
name: breakdown
description: Turn an accepted design into a short vertical implementation checklist with outcome, check, and review scope for each task.
---

# Breakdown

Create or refresh `tasks/<task-name>/tasks.md`. Do not implement code.

`tasks.md` is the implementation loop contract: what changes, why it matters, how to prove it, and who reviews it.

Use only when manager asks for an explicit implementation checklist: multiple ordered tasks, integration steps, mixed review scopes, or multi-agent execution.

## Inputs

- preferred: `design.md`, especially `Decision` and `Oracle Gate`
- optional: `task.md`

## Rules

- Stay within accepted task/design scope.
- Stop if design is not settled enough or its `Oracle Gate` verdict is `block`.
- Prefer 2-10 vertical tasks, each one clean implementation pass.
- Each task should produce a behavior, contract, or integration outcome, not just a layer.
- Use `Oracle Gate` claims for checks whenever possible.
- Do not create one task for tests only unless the product behavior already exists and only proof is missing.
- Carry forward review scope.
- Split tasks when low-risk work mixes with interface, cross-module, or high-risk work.
- Manager owns routing, completion state, and task status; this file owns checklist content only.

## Task Shape

Each task answers:

- what will change
- why it matters
- how to prove it
- who reviews it

## Output

```md
# Implementation Tasks: [Task Name]

## Rules

- Work one task at a time.
- Each task ends with its check run or a blocker.
- Do not expand scope without manager approval.

## Tasks

- [ ] **T1: [Behavior Slice]**
  - **Covers:** `REQ-1`, `AC-1`, or design goal
  - **Outcome:** User/business/module result this task delivers
  - **Do:** Specific implementation step
  - **Check:** Focused behavior, contract, regression, integration, or manual check
  - **Review:** `skip | full`, plus short reason

## Notes

- Blockers, deferred work, or follow-up validation.
```
