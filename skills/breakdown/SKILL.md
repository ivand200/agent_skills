---
name: breakdown
description: Turn an accepted design into a short vertical implementation checklist with outcome, check, and review scope for each task.
---

# Breakdown

Create or refresh `tasks/<task-name>/tasks.md`. Do not implement code.

`tasks.md` is the implementation loop contract: what changes, why it matters, how to prove it, and who reviews it.

Use only when manager asks for an explicit implementation checklist: multiple ordered tasks, integration steps, mixed review scopes, or multi-agent execution.

Use tracer-bullet slices: each task should cut through the needed modules/interfaces end to end and be verifiable on its own.

## Inputs

- preferred: `design.md`, especially `Decision` and `Oracle Gate`
- optional: `task.md`
- optional: relevant `steering/` docs for project constraints, domain names, module seams, frontend design, test guidance, or other durable project rules

## Rules

- Stay within accepted task/design scope.
- Stop if design is not settled enough or its `Oracle Gate` verdict is `block`.
- Prefer 2-10 vertical tasks, each one clean implementation pass.
- Each task should produce a demoable or independently verifiable behavior, contract, or integration outcome, not just a layer.
- Prefer thin complete slices over horizontal tasks such as "add data layer" or "add UI layer."
- Use `Oracle Gate` claims for checks whenever possible.
- Do not create one task for tests only unless the product behavior already exists and only proof is missing.
- Carry forward review scope.
- Split tasks when low-risk work mixes with interface, cross-module, or high-risk work.
- Mark each task `AFK` when an implementation agent can complete it from accepted artifacts, or `HITL` when a human decision, design review, unavailable environment, or manual proof is required.
- Manager owns routing, completion state, and task status; this file owns checklist content only.

## Task Shape

Each task answers:

- what will change
- why it matters
- how to prove it
- whether it is `AFK` or `HITL`
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
  - **Mode:** `AFK | HITL`
  - **Covers:** `REQ-1`, `AC-1`, or design goal
  - **Outcome:** User/business/module result this task delivers
  - **Do:** Specific implementation step
  - **Check:** Focused behavior, contract, regression, integration, or manual check
  - **Review:** `skip | full`, plus short reason

## Notes

- Blockers, deferred work, or follow-up validation.
```
