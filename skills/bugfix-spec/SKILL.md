---
name: bugfix-spec
description: Shape a bugfix before coding. Use for defects or regressions when you need reproduction, current vs expected behavior, unchanged behavior, scope, interface impact, and whether root-cause research is needed.
---

# Bugfix Spec

Shape a bugfix task so the defect, guardrails, and regression risk are clear before implementation.

## Inputs

- Bug description in chat, or
- Existing bug/task file
- Optional logs, screenshots, traces, or failing tests
- Optional steering docs such as `steering/product.md`, `steering/tech.md`, `steering/structure.md`

## Goal

Produce a concise bugfix spec that makes the defect reproducible, the expected behavior explicit, and unchanged behavior visible enough to reduce regressions.

## When To Use

- The user describes a bug, regression, or broken behavior.
- The root cause is not fully obvious yet.
- The fix touches important flows or could regress adjacent behavior.
- The team wants a durable record of the bug and its expected fix behavior.

Do not use this for routine feature work. Use `task-requirements` for feature tasks.

## Workflow

1. Read the bug description and restate the defect in precise terms.
2. Identify:
   - reproduction steps
   - current behavior
   - expected behavior
   - unchanged behavior that must continue working
   - likely scope boundary
   - affected module/entities and public contract impact
3. Assess whether root-cause research is needed:
   - use `research-context` when call-path tracing or subsystem investigation is needed
   - otherwise keep the bugfix spec lightweight
4. If answers can be found from the repository, logs, or tests, inspect those first instead of asking the user.
5. Record assumptions and ambiguities explicitly instead of silently filling them in.
6. Record scale, research need, interface impact, risk flags, and review hint as routing facts for manager.
7. Do not choose the workflow route or next stage. Manager owns routing from the recorded facts.

## Writing Guidance

- Prefer concrete reproduction details over abstract summaries.
- Separate confirmed current behavior from suspected root cause.
- Preserve scope boundaries so the bugfix does not grow into a feature.
- Capture unchanged behavior explicitly when regressions would be costly.
- Use Given/When/Then acceptance criteria when the fix is testable.

## Output Template

Write or refresh `tasks/<task-name>/task.md` with this compact structure. Include optional details only when they clarify the defect or reduce regression risk.

```markdown
# Bugfix Task: [Short title]

## Goal
Brief defect and why it matters.

## Triage
- Type: bugfix
- Scale: low | medium | large
- Confidence: high | medium | low
- Needs research-context: yes | no
- Routing flags: `research_needed` | `behavior_change` | `contract_change` | `data_change` | `none`
- Interface impact: `none | internal-only | public-contract | unclear`
- Risk flags: `auth | security | privacy | money | data integrity | migration | concurrency | performance | operations | none`
- Review hint: `skip | full | unknown`
- Why: [1-2 short bullets]

## Companion Artifacts
Include State, Task, Context, Design, and Tasks paths; mark missing, skipped, or not yet created.

## Scope
- In scope: ...
- Out of scope: ...

## Reproduction
- Preconditions: ...
- Steps: ...
- Observed result: ...

## Behavior
- Current: ...
- Expected: ...
- Unchanged: ...

## Regression Properties
- `[BUG-DEFECT-1]` When [condition], the system currently [incorrect behavior].
- `[BUG-EXPECT-1]` When [condition], the system shall [correct behavior].
- `[BUG-INVARIANT-1]` When [condition], the system shall continue to [existing behavior].

## Module / Interface Notes
- Affected module/entities: ...
- Public contract impact: `none | changed | unclear`
- Contract tests expected: ...

## Acceptance Criteria
### AC-1: [Short name]
Given ...
When ...
Then ...

## Open Questions
- ...

## Notes
- Logs, screenshots, failing tests, related tasks, or references when useful.
```

## Quality Bar

- A later implementation step should not have to guess what the bug is.
- The bugfix scope should stay narrower than a feature request.
- Unchanged behavior should be explicit when regression risk matters.
- Regression properties should make the defect, fix, and preserved behavior testable without prescribing implementation.
- Scale is only a routing fact for manager; do not turn a bugfix into feature workflow unless root-cause analysis reveals separate feature work.
