---
name: research-context
description: Research only the repo facts, external docs, options, and risks that change a design decision. Use when current behavior, external contracts, or implementation options are unclear.
---

# Research Context

Research only facts that change the design.

## Use When

- current repo behavior is unclear
- external docs, APIs, libraries, or contracts affect the choice
- multiple design options need evidence
- risk is real: auth, security, data, migrations, integrations, performance, operations, or regressions

Skip when the task is clear enough to design from existing artifacts and nearby code.

## Rules

- Do not implement.
- Prefer current code over docs.
- Use primary sources for external facts.
- Distinguish facts from assumptions.
- Stop when the design choice is clear.
- Default output is `## Context Research` inside `design.md`.
- Do not create `context.md`.
- Do not update `state.json`.

## Workflow

1. Read the task first.
2. Read only the code/docs needed to answer the design question.
3. Compare viable options when options exist.
4. Record only evidence that changes the decision.
5. Call out uncertainty that still matters.

## Output

```md
## Context Research

- Question:
- Evidence:
  - Repo:
  - Docs:
- Options:
  - Option A:
  - Option B:
- Decision impact:
- Open risk:
- Confidence: `high | medium | low`
```
