#!/usr/bin/env python3
"""Build a compact image prompt from a steering Module Interface Map."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Module:
    name: str
    interfaces: list[str]
    body: str


STOP_HEADINGS = re.compile(r"^##\s+")
MODULE_BULLET = re.compile(r"^-\s+([^:]+):\s+(.*)$")
BACKTICK = re.compile(r"`([^`]+)`")
HTTP_METHOD_PATH = re.compile(r"\b(GET|POST|PUT|PATCH|DELETE)\s+(/[A-Za-z0-9_./{}?=&:-]+)")
API_PATH = re.compile(r"(/[A-Za-z0-9_./{}-]*api[A-Za-z0-9_./{}-]*)")
FUNC_NAME = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*\(\)|[A-Za-z_][A-Za-z0-9_]*_[A-Za-z0-9_]+)\b")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--structure", default="steering/structure.md")
    parser.add_argument("--title", default="Module Interfaces")
    parser.add_argument("--max-modules", type=int, default=8)
    parser.add_argument("--output")
    args = parser.parse_args()

    structure_path = Path(args.structure)
    text = structure_path.read_text(encoding="utf-8")
    modules = extract_modules(text)[: args.max_modules]
    if not modules:
        raise SystemExit(f"No Module Interface Map bullets found in {structure_path}")

    prompt = build_prompt(args.title, modules)
    if args.output:
        Path(args.output).write_text(prompt, encoding="utf-8")
    else:
        print(prompt)
    return 0


def extract_modules(text: str) -> list[Module]:
    lines = text.splitlines()
    in_map = False
    modules: list[Module] = []

    for line in lines:
        stripped = line.strip()
        if stripped == "## Module Interface Map":
            in_map = True
            continue
        if in_map and STOP_HEADINGS.match(stripped):
            break
        if not in_map:
            continue

        match = MODULE_BULLET.match(stripped)
        if not match:
            continue
        name, body = match.groups()
        modules.append(Module(name=name.strip(), interfaces=extract_interfaces(body), body=body))

    return modules


def extract_interfaces(body: str) -> list[str]:
    labels: list[str] = []

    for method, path in HTTP_METHOD_PATH.findall(body):
        labels.append(f"{method} {path}")
    for label in BACKTICK.findall(body):
        if "/" in label and not label.startswith("/api") and not label.startswith("GET /api"):
            continue
        labels.append(label)
    labels.extend(path for path in API_PATH.findall(body) if "/src/" not in path)
    labels.extend(FUNC_NAME.findall(body))
    labels.extend(owned_phrases(body))

    cleaned: list[str] = []
    seen: set[str] = set()
    for label in labels:
        compact = shorten(clean_label(label))
        key = compact.casefold()
        if compact.startswith("/") and any(item.endswith(compact) for item in cleaned):
            continue
        if compact and key not in seen and not is_noise(compact):
            seen.add(key)
            cleaned.append(compact)
        if len(cleaned) == 3:
            break

    if cleaned:
        return cleaned

    fallback = first_meaningful_phrase(body)
    return [shorten(clean_label(fallback))]


def owned_phrases(body: str) -> list[str]:
    match = re.search(r"\bowns\s+(.+?)(?:;|\.| but | Protected by|$)", body)
    if not match:
        return []
    phrase = match.group(1)
    parts = re.split(r",|\band\b", phrase)
    return [part.strip() for part in parts if part.strip()]


def first_meaningful_phrase(body: str) -> str:
    body = re.sub(r"`[^`/]*[/][^`]*`", "", body)
    body = body.replace("`", "")
    candidates = re.split(r";|,|\.", body)
    for candidate in candidates:
        cleaned = clean_label(candidate)
        if cleaned and not is_noise(cleaned):
            return cleaned
    return "public interface"


def clean_label(label: str) -> str:
    label = label.strip().strip(".,;:")
    label = label.replace("()", "")
    if label.startswith("GET GET "):
        label = label.removeprefix("GET ")
    return " ".join(label.split())


def shorten(label: str, max_chars: int = 34) -> str:
    if len(label) <= max_chars:
        return label
    words = label.split()
    shortened = ""
    for word in words:
        candidate = f"{shortened} {word}".strip()
        if len(candidate) > max_chars:
            break
        shortened = candidate
    return shortened or label[: max_chars - 1].rstrip() + "."


def is_noise(label: str) -> bool:
    lowered = label.lower()
    return (
        label in {"tests/evals"}
        or lowered in {"api", "service", "caller", "callers", "ready"}
        or label.endswith(".ts")
        or label.endswith(".py")
        or "/src/" in label
        or label.startswith("frontend/")
        or label.startswith("backend/")
    )


def build_prompt(title: str, modules: list[Module]) -> str:
    module_lines: list[str] = []
    for index, module in enumerate(modules, start=1):
        module_lines.append(f"{index}. {module.name}")
        module_lines.append("   interfaces: " + ", ".join(module.interfaces))

    connections = suggest_connections(modules)
    connection_lines = [f"- {source} -> {target}: {label}" for source, target, label in connections]

    return "\n".join(
        [
            "Create a bright, minimal, hand-drawn sketch style architecture diagram.",
            "White paper background, colorful rounded sticky-note module cards, thick marker arrows.",
            "Keep text sparse, readable, and professional.",
            "",
            f"Title: {title}",
            "",
            "Cards/modules:",
            *module_lines,
            "",
            "Connections with short arrow labels:",
            *(connection_lines or ["- Add only obvious public-interface connections from the module map."]),
            "",
            "Style requirements:",
            "- not an ERD",
            "- not database tables",
            "- no tiny columns",
            "- no file tree",
            "- no long paragraphs",
            "- 5-9 sketch cards",
            "- one-page overview",
            "- lots of whitespace",
            "- labels should be short and legible",
            "- cheerful but production-minded",
        ]
    )


def suggest_connections(modules: list[Module]) -> list[tuple[str, str, str]]:
    names = [module.name for module in modules]
    lowered = {module.name: module.name.lower() for module in modules}
    connections: list[tuple[str, str, str]] = []

    frontend = find_name(lowered, "frontend")
    auth = find_name(lowered, "auth")
    worker = find_name(lowered, "worker", "ingestion")
    retrieval = find_name(lowered, "retrieval")
    chat = find_name(lowered, "chat")
    documents = find_name(lowered, "document")
    data = find_name(lowered, "data", "db", "database", "storage")

    api_modules = [name for name in names if "api" in lowered[name] and name != frontend]
    if frontend:
        for target in api_modules[:4]:
            label = first_interface(find_module(modules, target))
            connections.append((frontend, target, label))
        if auth:
            connections.append((frontend, auth, "auth token"))
    if chat and retrieval:
        connections.append((chat, retrieval, "search evidence"))
    if documents and worker and documents != worker:
        connections.append((documents, worker, "queued job"))
    if worker and data:
        connections.append((worker, data, "background writes"))
    if retrieval and data:
        connections.append((retrieval, data, "chunks"))

    return unique_connections(connections)


def find_name(lowered: dict[str, str], *needles: str) -> str | None:
    for name, value in lowered.items():
        if any(needle in value for needle in needles):
            return name
    return None


def find_module(modules: list[Module], name: str) -> Module:
    return next(module for module in modules if module.name == name)


def first_interface(module: Module) -> str:
    return module.interfaces[0] if module.interfaces else "public interface"


def unique_connections(
    connections: list[tuple[str, str, str]]
) -> list[tuple[str, str, str]]:
    unique: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    for source, target, label in connections:
        key = (source, target)
        if source != target and key not in seen:
            seen.add(key)
            unique.append((source, target, label))
    return unique[:8]


if __name__ == "__main__":
    raise SystemExit(main())
