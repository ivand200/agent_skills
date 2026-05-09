---
name: verification-report
description: Create a compact human-readable verification report after implementation, testing, and review, highlighting the most important tests, E2E checks, manual checks, and residual risks an engineer should inspect before accepting AI-generated work.
---

# Verification Report

Create or refresh `tasks/<task-name>/verification-report.md`.

Use after implementation, testing, required review, and accepted reviewer fixes. Do not edit code, tests, task artifacts, or workflow state.

## Inputs

Read all available task artifacts in `tasks/<task-name>/`:

- `state.json`
- `task.md`
- `context.md`
- `design.md`
- `oracle-gate.md`
- `tasks.md`
- developer/tester/reviewer returns when present
- changed files, test output, CI logs, screenshots, or E2E artifacts when available

## Core Rules

- Specification artifacts are the source of truth; code and tests are evidence.
- Report only the highest-value proof, not every test.
- Call out weak proof, missing proof, skipped proof, and residual risk plainly.

## Workflow

1. Map accepted claims from task/design/oracle artifacts to actual evidence.
2. Select the 1-3 most critical automated tests for this feature.
3. Select the 1-2 most relevant E2E/workflow tests when present.
4. Write what the engineer should inspect, manually verify, or distrust.
5. Decide verdict: `ready_for_engineer_check`, `warn`, or `blocked`.

## Output

```md
# Verification Report: [Task Name]

## Verdict
- `ready_for_engineer_check | warn | blocked`

## Spec Claims Covered

| Claim | Source | Evidence | Status |
| --- | --- | --- | --- |
| `AC-1` | `task.md` | `tests/test_x.py::test_name` | passed |

## Most Important Tests To Inspect

1. `tests/...::test_name`
   - Proves: ...
   - Why inspect: ...
   - What to check: ...

## Most Important E2E Tests

1. `e2e/...spec.ts`
   - Proves: ...
   - Scenario: ...
   - What to check manually: ...

## Engineer Verification Checklist

- Check that ...
- Check that ...
- Check that ...

## Residual Risk

- ...
```

## Quality Bar

A good report lets an engineer quickly see:

- which spec claims are covered
- which tests are worth reading closely
- which E2E checks matter
- what still needs human verification
- what risk remains
