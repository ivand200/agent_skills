---
name: grill-me
description: Stress-test blocking or important product, architecture, system-design, interface, or proof questions one by one until the next safe step is clear.
---

# Grill Me

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one.

Use for questions that are blocking or important enough to change scope, architecture, public interfaces, system behavior, proof strategy, or implementation order.

If a question can be answered by exploring the codebase or existing artifacts, explore them instead of asking.

For each question, provide your recommended answer.

Rules:

- Ask one question at a time.
- Resolve upstream decisions before downstream details.
- Do not silently choose between materially different options.
- Keep going until ambiguity is resolved or explicitly accepted.
- Do not stop at the happy path; cover scope, constraints, edge cases, failure modes, interfaces, rollout, and verification.

When the user needs to choose between valid paths:

- Offer 2-3 concrete options.
- Mark one option as recommended.
- Give one brief tradeoff per option.
- Include:
  - `Recommended answer:`
  - `Why:`

Use this format when options are needed:

```text
Question: [next most important unresolved question]

Options:
1. [option A] (Recommended)
   Tradeoff: [brief tradeoff]
2. [option B]
   Tradeoff: [brief tradeoff]
3. [option C]
   Tradeoff: [brief tradeoff]

Recommended answer: [short recommendation]
Why: [brief reason]
```

When finishing, summarize:

- decisions made
- assumptions accepted
- open questions
- artifact changes implied by the discussion
- recommended next step

If used as a workflow gate, end with one clear outcome:

- requirements gate:
  - ready for direct implementation
  - ready for design
  - ready for research first
  - not ready and needs more clarification
- design gate:
  - ready for breakdown
  - blocked by unresolved design decisions
  - requires task updates first
