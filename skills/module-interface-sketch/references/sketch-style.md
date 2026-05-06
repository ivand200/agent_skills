# Sketch Style Reference

Use this reference when revising the final image prompt.

## Default Prompt Style

- Bright white paper or notebook background.
- Colorful rounded cards that look like sticky notes or marker boxes.
- Thick hand-drawn arrows with short labels.
- Minimal legend only when line style matters.
- Sparse, readable text.
- Cheerful but professional.

## Avoid

- Database schema tables.
- ERD crow's-foot notation.
- UML class diagrams.
- File trees.
- Tiny code text.
- Long paragraphs inside cards.
- Decorative detail that competes with interface labels.

## Good Card Content

```text
Chat API + Service
interfaces:
- /api/chat
- SSE stream
- citations
```

## Good Arrow Labels

```text
bearer token
upload/delete
queued job
ready chunk search
background writes
```

## Regeneration Tip

If text is wrong or crowded, do not add more instructions. Shorten module labels, reduce the card count, and regenerate.
