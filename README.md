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
task -> implementation

medium risk:
task -> design -> oracle -> tasks -> implementation

large risk:
task -> research -> design -> oracle -> tasks -> implementation
```

Use `low` for localized, clear, low-risk work.

Use `medium` when design, validation strategy, or task breakdown would reduce churn.

Use `large` when current behavior, root cause, module boundaries, data, operations, or integrations need investigation before design.

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
| [`reviewer`](agents/reviewer.toml) | Performs read-only review of one implemented and tested task. Focuses on public interfaces, module boundaries, proof coverage, scope drift, and risk-bearing changes. |

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

## Status

This is a portfolio project and a working personal engineering workflow.

The next useful addition is a complete worked example showing one task from request to task spec, design, oracle gate, implementation return, tester return, and reviewer return.
