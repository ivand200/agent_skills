---
name: module-interface-sketch
description: Create bright, minimal sketch-style PNG diagrams of software modules, public interfaces, and important connections from steering docs such as `steering/structure.md` Module Interface Map. Use when Codex should visualize service architecture, module boundaries, interface contracts, or Ousterhout-style deep modules as an easy-to-understand image.
---

# Module Interface Sketch

Create a one-page, sketch-style module interface diagram that helps someone understand a service through module names, public interfaces, and labeled connections.

Optimize for "understand the system in 20 seconds." Do not create database ERDs, file inventories, UML class diagrams, or implementation call graphs unless the user explicitly asks for them.

## Workflow

1. Read `steering/structure.md` first, especially `Module Interface Map`.
2. If the map is missing or too vague, inspect only minimal durable evidence: README, entry points, routes/commands, manifests, and representative tests.
3. Run `scripts/build_sketch_prompt.py` from the skill folder to draft a compact image prompt when `steering/structure.md` exists.
4. Edit the generated prompt before image generation:
   - keep 5-9 modules by default
   - keep each module to 1-3 short interface labels
   - keep each connection label specific
   - remove hidden implementation details unless they are useful as "do not depend on" warnings
5. Use the available image-generation tool to create a PNG from the final prompt.
6. Report the generated image path and mention if labels may need a second pass.

## Prompt Helper

Use the bundled helper from the repository root:

```bash
python3 ~/.codex/skills/module-interface-sketch/scripts/build_sketch_prompt.py \
  --structure steering/structure.md \
  --title "Project: Module Interfaces"
```

Optional flags:

- `--max-modules 8` limits the number of module cards.
- `--output /path/to/prompt.txt` writes the prompt to a file.

The helper produces a draft only. Always review it against the repo and the user's request before calling image generation.

## Diagram Rules

- Make the diagram minimal, bright, and hand-drawn.
- Use cards or sticky notes, not database tables.
- Put the module name at the top of each card.
- Put only public interface labels inside cards: endpoints, commands, events, exported operations, schemas, or service operations.
- Label arrows with what crosses the boundary, such as `POST /api/chat/messages/stream`, `claim job`, or `ready chunk search`.
- Use dashed arrows for async/background flows.
- Prefer 2-4 words for responsibilities and arrow labels.
- If a label cannot fit inside a card or arrow, shorten it or leave it in documentation.
- Keep implementation details out of the picture: helper order, storage layout, prompts, retry mechanics, log text, private state, and algorithms.

## Visual Style

Read `references/sketch-style.md` when choosing or revising the final image prompt.

Default style:

- white paper or light notebook background
- colorful rounded sketch cards
- thick marker arrows
- sparse labels
- small legend only when it teaches line meaning
- cheerful but professional

## Quality Check

Before generating:

- Every card has a module name.
- Every card has at least one interface label.
- Every arrow has a specific label.
- The diagram is not an ERD or file tree.
- The prompt explicitly says "no tiny text, no database columns, no long paragraphs."

After generating:

- Verify text is readable enough to be useful.
- If labels drift, shorten the prompt and regenerate.
- If exact labels are critical, recommend a deterministic SVG/HTML/D2 renderer instead of pure image generation.
