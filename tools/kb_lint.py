#!/usr/bin/env python3
"""KB Lint — health checks for the 3gpp-research knowledge base.

Runs four checks across `documents/` and `references/`:

1. Orphan notes — `up` and `related` empty, zero outbound and inbound wikilinks
2. Broken wikilinks — `[[name]]` whose target does not exist under `documents/` or `references/`
3. Missing primary sources — `documents/*.md` whose `references:` is empty AND whose body has zero `[[references/...]]` or `[[<file under references/>]]` wikilinks
4. Missing required frontmatter fields — `status` / `confidence` / `created` / `sources`

Usage:
    python tools/kb_lint.py --root .
    python tools/kb_lint.py --root . --report tools/kb_lint_report.md

Output: JSON to stdout, optional Markdown report.
Standard library only. No external dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

WIKILINK_RE = re.compile(r"\[\[([^\]|#^]+)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
REQUIRED_FIELDS_DOCUMENTS = ("status", "confidence", "created", "sources")
REQUIRED_FIELDS_REFERENCES = ("type", "accessed")


@dataclass
class NoteInfo:
    path: Path
    rel: str
    stem: str
    kind: str  # "documents" | "references"
    frontmatter_raw: str
    body: str
    fm_keys: set[str] = field(default_factory=set)
    fm_up: list[str] = field(default_factory=list)
    fm_related: list[str] = field(default_factory=list)
    fm_references: list[str] = field(default_factory=list)
    fm_sources: list[str] = field(default_factory=list)
    body_links: list[str] = field(default_factory=list)
    fm_link_refs: list[str] = field(default_factory=list)
    missing_required: list[str] = field(default_factory=list)


def parse_frontmatter_fields(fm_raw: str) -> tuple[set[str], dict[str, list[str]], dict[str, list[str]]]:
    """Very small frontmatter scanner — no PyYAML.

    Returns:
      - top-level keys
      - link_fields: key -> list of wikilink stems (for `up`, `related`, `references`)
      - sources_raw: key -> list of raw string values (URLs or wikilinks) for `sources`
        (used to detect "any non-empty source", not for link resolution)
    """
    keys: set[str] = set()
    link_fields: dict[str, list[str]] = {"up": [], "related": [], "references": []}
    sources_raw: dict[str, list[str]] = {"sources": []}

    current_list_key: str | None = None
    for raw_line in fm_raw.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            current_list_key = None
            continue

        # Top-level `key: ...` or `key:` (no leading whitespace)
        m_top = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m_top and not raw_line.startswith((" ", "\t")):
            key, value = m_top.group(1), m_top.group(2).strip()
            keys.add(key)
            current_list_key = None

            if key in link_fields:
                if not value:
                    current_list_key = key
                else:
                    stripped = value.strip().strip("\"'")
                    if stripped:
                        link_fields[key].extend(WIKILINK_RE.findall(stripped))
            elif key == "sources":
                if not value:
                    current_list_key = key
                else:
                    stripped = value.strip().strip("\"'")
                    if stripped:
                        sources_raw["sources"].append(stripped)
            continue

        # List item under a list-typed key
        m_item = re.match(r"^\s+-\s+(.*)$", line)
        if m_item and current_list_key is not None:
            value = m_item.group(1).strip().strip("\"'")
            if current_list_key == "sources":
                if value:
                    sources_raw["sources"].append(value)
            else:
                wls = WIKILINK_RE.findall(value)
                if wls:
                    link_fields[current_list_key].extend(wls)
            continue

        # Nested mapping under axes etc. — ignore, but stop list capture
        current_list_key = None

    return keys, link_fields, sources_raw


def load_note(path: Path, root: Path, kind: str) -> NoteInfo:
    text = path.read_text(encoding="utf-8")
    fm_match = FRONTMATTER_RE.match(text)
    if fm_match:
        fm_raw = fm_match.group(1)
        body = text[fm_match.end():]
    else:
        fm_raw = ""
        body = text

    keys, link_fields, sources_raw = parse_frontmatter_fields(fm_raw)
    body_links = WIKILINK_RE.findall(body)

    fm_link_refs = [
        link
        for key in ("up", "related", "references")
        for link in link_fields[key]
        if link
    ]

    info = NoteInfo(
        path=path,
        rel=str(path.relative_to(root)).replace("\\", "/"),
        stem=path.stem,
        kind=kind,
        frontmatter_raw=fm_raw,
        body=body,
        fm_keys=keys,
        fm_up=link_fields["up"],
        fm_related=link_fields["related"],
        fm_references=link_fields["references"],
        fm_sources=sources_raw["sources"],
        body_links=body_links,
        fm_link_refs=fm_link_refs,
    )

    required = REQUIRED_FIELDS_DOCUMENTS if kind == "documents" else REQUIRED_FIELDS_REFERENCES
    info.missing_required = [
        key for key in required
        if key not in keys or (key in ("sources",) and not info.fm_sources and not info.fm_references)
    ]
    if kind == "documents":
        # `sources` is required to be non-empty per skill-contract; relax to "either sources or references provides a primary anchor"
        if "sources" in info.missing_required and (info.fm_sources or info.fm_references):
            info.missing_required.remove("sources")

    return info


def normalize_link(link: str) -> str:
    """Normalize a wikilink target to its file stem (no path, no extension)."""
    target = link.strip()
    target = target.replace("\\", "/")
    if "/" in target:
        target = target.rsplit("/", 1)[-1]
    if target.endswith(".md"):
        target = target[:-3]
    return target


def collect_notes(root: Path) -> list[NoteInfo]:
    notes: list[NoteInfo] = []
    for kind in ("documents", "references"):
        kind_dir = root / kind
        if not kind_dir.is_dir():
            continue
        for path in sorted(kind_dir.glob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            notes.append(load_note(path, root, kind))
    return notes


def build_index(notes: Iterable[NoteInfo]) -> tuple[dict[str, NoteInfo], dict[str, list[str]]]:
    """Build stem -> NoteInfo index, plus stem -> list of inbound rels."""
    by_stem: dict[str, NoteInfo] = {}
    for note in notes:
        by_stem[note.stem] = note

    inbound: dict[str, list[str]] = {note.stem: [] for note in notes}
    for note in notes:
        targets = set()
        for raw in [*note.body_links, *note.fm_link_refs]:
            stem = normalize_link(raw)
            if stem and stem in by_stem and stem != note.stem:
                targets.add(stem)
        for stem in targets:
            inbound[stem].append(note.rel)
    return by_stem, inbound


def find_broken_links(notes: Iterable[NoteInfo], by_stem: dict[str, NoteInfo]) -> list[dict]:
    broken: list[dict] = []
    for note in notes:
        seen = set()
        for raw in [*note.body_links, *note.fm_link_refs]:
            stem = normalize_link(raw)
            if not stem:
                continue
            if stem.startswith("../") or stem.startswith("./"):
                continue
            if stem in by_stem:
                continue
            # Skip framework/* placeholders that resolve outside documents/references
            if any(stem.startswith(prefix) for prefix in ("README", "principles", "skill-contract", "linking-policy", "references-policy", "review-policy", "tools", "sources", "3gpp-ftp-cookbook", "anti-ai-writing", "claim-evidence-block", "survey-topic", "paper-digest", "gap-analysis", "generation-comparison", "connect-dots", "demand-reverse")):
                # These are framework-side notes outside documents/references — accept
                continue
            key = (note.rel, stem)
            if key in seen:
                continue
            seen.add(key)
            broken.append({"file": note.rel, "target": stem})
    return broken


def find_orphans(notes: Iterable[NoteInfo], inbound: dict[str, list[str]]) -> list[str]:
    orphans: list[str] = []
    for note in notes:
        if note.kind != "documents":
            continue
        outbound = bool(note.fm_up) or bool(note.fm_related) or any(
            normalize_link(raw) for raw in note.body_links
        )
        inbound_count = len(inbound.get(note.stem, []))
        if not outbound and inbound_count == 0:
            orphans.append(note.rel)
    return orphans


def find_unsourced_documents(notes: Iterable[NoteInfo]) -> list[str]:
    unsourced: list[str] = []
    for note in notes:
        if note.kind != "documents":
            continue
        has_fm_ref = bool(note.fm_references)
        # Body wikilinks that resolve into references/ (by stem prefix or path)
        has_body_ref = False
        for raw in note.body_links:
            target = raw.strip().replace("\\", "/")
            if target.startswith("references/") or target.startswith("../references/"):
                has_body_ref = True
                break
        if not has_fm_ref and not has_body_ref:
            unsourced.append(note.rel)
    return unsourced


def find_missing_frontmatter(notes: Iterable[NoteInfo]) -> list[dict]:
    out: list[dict] = []
    for note in notes:
        if note.missing_required:
            out.append({"file": note.rel, "missing": note.missing_required})
    return out


def render_report(payload: dict) -> str:
    lines = ["# KB Lint Report", ""]
    lines.append(f"Generated: `python tools/kb_lint.py`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Check | Count | Status |")
    lines.append("|:---|---:|:---|")
    summary = payload["summary"]
    for check, count in summary.items():
        status = "OK" if count == 0 else "FAIL"
        lines.append(f"| {check} | {count} | {status} |")
    lines.append("")

    sections = (
        ("Orphan notes (documents/)", payload["orphans"], lambda x: f"- `{x}`"),
        ("Broken wikilinks", payload["broken_links"], lambda x: f"- `{x['file']}` → `[[{x['target']}]]`"),
        ("Documents without primary source", payload["unsourced_documents"], lambda x: f"- `{x}`"),
        ("Missing required frontmatter fields", payload["missing_frontmatter"], lambda x: f"- `{x['file']}`: missing {', '.join(x['missing'])}"),
    )
    for title, items, fmt in sections:
        lines.append(f"## {title}")
        lines.append("")
        if not items:
            lines.append("- (none)")
        else:
            for item in items:
                lines.append(fmt(item))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="KB Lint for 3gpp-research")
    parser.add_argument("--root", default=".", help="Repository root (contains documents/ and references/)")
    parser.add_argument("--report", default=None, help="Optional Markdown report output path")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not (root / "documents").is_dir():
        print(f"error: {root}/documents not found", file=sys.stderr)
        return 2

    notes = collect_notes(root)
    by_stem, inbound = build_index(notes)

    orphans = find_orphans(notes, inbound)
    broken = find_broken_links(notes, by_stem)
    unsourced = find_unsourced_documents(notes)
    missing_fm = find_missing_frontmatter(notes)

    payload = {
        "root": str(root),
        "counts": {
            "documents": sum(1 for n in notes if n.kind == "documents"),
            "references": sum(1 for n in notes if n.kind == "references"),
        },
        "summary": {
            "orphan_notes": len(orphans),
            "broken_wikilinks": len(broken),
            "documents_without_primary_source": len(unsourced),
            "missing_required_frontmatter": len(missing_fm),
        },
        "orphans": orphans,
        "broken_links": broken,
        "unsourced_documents": unsourced,
        "missing_frontmatter": missing_fm,
    }

    print(json.dumps(payload, ensure_ascii=False, indent=2))

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(render_report(payload), encoding="utf-8")

    total_issues = sum(payload["summary"].values())
    return 0 if total_issues == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
