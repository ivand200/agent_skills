# Spec-Driven Development Workflow for AI Coding Agents

This repository contains a practical implementation of a Spec-Driven Development workflow for working with AI coding agents.

The workflow is designed around one engineering problem: AI agents can generate code quickly, but professional software delivery needs controlled scope, explicit intent, proof of correctness, and reviewable decisions.

Instead of sending an agent directly from request to code, this workflow scales the process by task risk. Small changes stay lightweight. Risky changes go through requirements, research, design, oracle/proof planning, task breakdown, bounded implementation, validation, and review.

![Spec-Driven Agent Workflow](spec-driven-agent-workflow.png)

## Executive Summary

This is a lightweight governance model for AI-assisted engineering.

It treats requirements, design decisions, validation strategy, and agent boundaries as first-class artifacts. The goal is not to create more documentation. The goal is to make AI-generated changes:

- easier to control
- easier to review
- easier to test
- easier to resume after context loss
- safer around public contracts, data, security, operations, and cross-module behavior

The central idea is simple:

> Define the intent and proof before asking an agent to implement.

## Workflow

The manager chooses the smallest safe path for each task.

```text
low risk:
task/brief -> implementation -> verification

medium risk:
task -> design with small validation intent -> implementation -> verification

large or risky:
task -> research -> design -> oracle-gate -> tasks -> implementation -> verification
```

Use `low` for tiny, localized, clear work.

Use `medium` when design or small validation intent would reduce churn, but strict oracle proof or task breakdown is not required by default.

Use `large` when current behavior, root cause, module boundaries, data, operations, integrations, or strict proof planning need investigation before implementation.

Planning is approval-gated one step at a time: the manager creates or refreshes one artifact, records state, and stops for engineer approval before moving to the next planning stage.

Implementation loops happen only inside the implementation stage. Developer and tester run per approved implementation task; reviewer runs once after all implementation tasks pass testing, unless a high-risk task needs per-task review. Agents must stop if product intent, design, proof strategy, or approved scope changes.

## Artifacts

Each task can produce a small set of durable artifacts under `tasks/<task-name>/`.

| Artifact | Purpose |
| --- | --- |
| `state.json` | Workflow state, current stage, artifact status, and routing notes. |
| `task.md` | Requirements, acceptance criteria, scope, risk flags, and interface impact. |
| `context.md` | Research evidence about current behavior, module boundaries, contracts, or external docs. |
| `design.md` | Accepted design, tradeoffs, impacted modules, contract impact, and planned validation. |
| `oracle-gate.md` | Proof plan: what must be tested or manually verified before the work can be trusted. |
| `tasks.md` | Ordered implementation backlog with traceability to requirements and validation. |
| `verification-report.md` | Final verification summary: important proof, tests to inspect, manual checks, and residual risk. |

## Skills

The workflow is implemented as reusable agent skills. Each skill is plain Markdown so it can be adapted to different agent runtimes.

| Skill | Responsibility |
| --- | --- |
| [`manager`](skills/manager/SKILL.md) | Owns workflow state, selects the smallest safe path, runs one step at a time, and stops for engineer approval at gates. |
| [`task-requirements`](skills/task-requirements/SKILL.md) | Captures feature requirements, user stories, examples, acceptance criteria, interface impact, risk flags, and review hints. |
| [`bugfix-spec`](skills/bugfix-spec/SKILL.md) | Captures defects with reproduction steps, current behavior, expected behavior, unchanged behavior, and regression properties. |
| [`research-context`](skills/research-context/SKILL.md) | Investigates current code, module boundaries, tests, contracts, external docs, and risk signals when design or implementation needs evidence. |
| [`design-doc`](skills/design-doc/SKILL.md) | Records accepted design decisions, tradeoffs, module impact, public contract impact, validation strategy, and review scope. |
| [`oracle-gate`](skills/oracle-gate/SKILL.md) | Defines the proof required before implementation: behavior tests, contract tests, regression tests, integration checks, or manual validation. |
| [`breakdown`](skills/breakdown/SKILL.md) | Turns an accepted design and oracle plan into ordered implementation tasks with traceability and validation. |
| [`verification-report`](skills/verification-report/SKILL.md) | Summarizes the most important proof after implementation, testing, and review so an engineer knows which tests, E2E checks, and residual risks to inspect. |
| [`grill-me`](skills/grill-me/SKILL.md) | Resolves material ambiguity through one-question-at-a-time design interrogation before the workflow moves forward. |
| [`architecture-principles`](skills/architecture-principles/SKILL.md) | Supports design and review with lightweight architecture rules: deep modules, stable interfaces, boundary ownership, and abstraction tradeoffs. |
| [`behavior-tests`](skills/behavior-tests/SKILL.md) | Supports implementation and validation with behavior-focused tests around stable public boundaries instead of private implementation details. |
| [`module-interface-sketch`](skills/module-interface-sketch/SKILL.md) | Creates bright module/interface sketches that make system boundaries and public contracts understandable at a glance. |

## Agents

The workflow uses bounded agent roles with narrow ownership instead of one unrestricted implementation agent. The files below are role definitions that can be adapted to different agent runtimes.

| Agent | Responsibility |
| --- | --- |
| [`developer`](agents/developer.toml) | Implements exactly one approved task within accepted artifacts. May edit product code and relevant tests. Must not edit workflow state or expand scope. |
| [`tester`](agents/tester.toml) | Validates one implemented task against accepted artifacts and oracle proof. May edit tests only. Must not edit product code. |
| [`reviewer`](agents/reviewer.toml) | Performs read-only review of the completed implementation batch. Focuses on public interfaces, module boundaries, proof coverage, scope drift, and risk-bearing changes. |

The developer and tester loop runs per implementation task. The reviewer is the final integrated check before `verification-report.md`, with per-task review reserved for high-risk exceptions.

## Worked Example

Example request:

> Add password reset by email. Users should request a reset link, use it once before expiry, and keep existing login behavior unchanged.

Because this touches authentication and user account recovery, the manager routes it as a `medium` task.

```text
tasks/add-password-reset/
  state.json
  task.md
  design.md
  oracle-gate.md
  tasks.md
  verification-report.md
```

`task.md` captures intent and acceptance criteria:

```md
# Task: Add Password Reset

## Rules
- [REQ-1] A user can request a password reset email for an existing account.
- [REQ-2] A reset token can be used once before expiry.
- [REQ-3] Existing email/password login behavior remains unchanged.

## Acceptance Criteria
### AC-1: Request Reset
Given an existing user
When they request a password reset
Then the system sends a reset link without exposing whether the email exists.
```

`design.md` records the chosen approach:

```md
## Decision Summary
- Store hashed reset tokens with expiry.
- Invalidate a token after successful use.
- Keep login/session behavior unchanged.

## Review Scope
- Interface changed: yes
- Risk flags: auth, security, privacy
- Reviewer mode: full
```

`oracle-gate.md` defines proof before code:

```md
## Claim / Proof Map
| Claim | Required Proof | Preferred Boundary | Strength |
| --- | --- | --- | --- |
| `AC-1` | reset request does not reveal account existence | API behavior test | strong |
| `REQ-2` | token is single-use and expires | service/API behavior test | strong |
| `REQ-3` | existing login still works | regression test | strong |
```

`tasks.md` turns approved scope into bounded work:

```md
- [ ] **Task 1: Add reset request and token persistence**
  - **Covers:** `REQ-1`
  - **Validation:** reset request behavior test
  - **Review:** full because auth flow changes

- [ ] **Task 2: Add reset completion**
  - **Covers:** `REQ-2`, `REQ-3`
  - **Validation:** single-use, expiry, and login regression tests
  - **Review:** full because security behavior changes
```

After implementation, testing, and required review, `verification-report.md` gives the engineer the final check:

```md
## Verdict
- `ready_for_engineer_check`

## Spec Claims Covered
| Claim | Evidence | Status |
| --- | --- | --- |
| `AC-1` | `tests/auth/password_reset_test.py::test_request_does_not_reveal_account` | passed |
| `REQ-2` | `tests/auth/password_reset_test.py::test_token_is_single_use` | passed |

## Residual Risk
- Email delivery provider behavior was faked in tests; verify one real reset email in staging.
```

## What This Demonstrates

This repository is not just a prompt collection. It demonstrates an engineering approach to AI-assisted delivery:

- risk-based workflow selection
- explicit requirements and acceptance criteria
- bugfix specs with regression guardrails
- research before design when current behavior is uncertain
- design approval before risky implementation
- oracle/proof planning before code generation
- bounded developer, tester, and reviewer agents
- traceability from requirement to implementation task to validation
- verification reporting before final engineer acceptance
- workflow state that survives chat history loss
- human approval at meaningful gates

## Repository Structure

```text
.
  README.md
  agents/
    developer.toml
    tester.toml
    reviewer.toml
  skills/
    manager/
      SKILL.md
    task-requirements/
      SKILL.md
    bugfix-spec/
      SKILL.md
    research-context/
      SKILL.md
    design-doc/
      SKILL.md
    oracle-gate/
      SKILL.md
    breakdown/
      SKILL.md
    verification-report/
      SKILL.md
    grill-me/
      SKILL.md
    architecture-principles/
      SKILL.md
    behavior-tests/
      SKILL.md
    module-interface-sketch/
      SKILL.md
```

## Inspiration And References

This workflow is a practical adaptation inspired by existing work in spec-driven development, prompt-driven development, testing strategy, and test-oracle research.

- [Structured-Prompt-Driven Development](https://martinfowler.com/articles/structured-prompt-driven/) - Thoughtworks article on making LLM-assisted changes governable, reviewable, and reusable by treating prompts as first-class artifacts.
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) - Analysis of current SDD tools and the need for workflows that fit different task sizes.
- [Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html) - Testing strategy background for balancing focused tests, service-level tests, and higher-level validation.
- [The Oracle Problem in Software Testing: A Survey](https://discovery.ucl.ac.uk/id/eprint/1471263/) - Research background for why defining expected behavior and proof matters in software testing.
- [Matt Pocock's Skills](https://github.com/mattpocock/skills) - Practical inspiration for packaging reusable AI-agent skills as explicit, shareable instructions.
