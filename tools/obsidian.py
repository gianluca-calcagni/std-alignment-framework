"""Build a read-only Obsidian view of the framework in obsidian/.

The source files stay the single source of truth; the view is generated from them and never edited. Every item becomes
one note, every reference like [P3] becomes a link, every note lists what it depends on and what depends on it (as lint
R5 defines dependencies), and each derived file becomes a folder, numbered in reading order. The generator never
touches obsidian/.obsidian/ (Obsidian's settings) or obsidian/Annotations/ (notes of one's own).

Usage: python3 tools/obsidian.py            write the view
       python3 tools/obsidian.py --check    exit 1 if the committed view differs from what the sources generate
"""
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint  # one definition of what an item is, and of what it depends on

REPO = "https://github.com/gianluca-calcagni/std-alignment-framework/blob/main/"
KEEP = {".obsidian", "Annotations"}
DOCS = {"README.md": "About", "STANDARD.md": "Standard", "RECORD.md": "Record", "TERMS.md": "Terms",
        "RELATED.md": "Related", "IMPORT.md": "Import", "NOTES.md": "Notes", "REFERENCES.md": "References",
        "derived/README.md": "Reading order", "ontologies/README.md": "Ontologies"}


def anchor(heading):
    """GitHub's anchor for a heading: lower case, punctuation dropped, spaces as hyphens."""
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


def build(root):
    """Return {relative path: text} for the whole view."""
    root, errors, notes = Path(root), [], {}
    sources = [("CORE.md", "Core")] + [(f"derived/{n}", f"Derived/{i:02d} {n[:-3]}")
                                        for i, n in enumerate(lint.derived_files(root, errors), 1)]
    items, intros = [], {}
    for path, folder in sources:
        text = (root / path).read_text(encoding="utf-8")
        titles = {m[1] + m[2]: m[3] for m in map(lint.ITEM.match, text.splitlines()) if m}
        for it in lint.parse_items(text, path)[1]:
            it["title"], it["folder"] = titles[it["id"]], folder
            it["note"] = f"{it['id']} — {it['title']}"
            items.append(it)
        intros[path] = text.split("\n### ", 1)[0].strip()
    by_id = {it["id"]: it for it in items}

    def linked(text):
        """Every [P3] and [@key] as a link. In a table row the link's own '|' must be escaped, or Obsidian reads it as a
        cell boundary."""
        def line(row):
            bar = "\\|" if row.lstrip().startswith("|") else "|"
            row = lint.REF.sub(lambda m: f"[[{by_id[m[1]]['note']}{bar}{m[1]}]]" if m[1] in by_id else m[0], row)
            return lint.CITE.sub(lambda m: f"[[References{bar}@{m[1]}]]", row)
        return "\n".join(line(row) for row in text.split("\n"))

    def bullet(i):
        return f"- [[{by_id[i]['note']}|{i}]] — {by_id[i]['title']}"

    for it in items:
        body = " ".join(t for f, t in it["fields"].items() if f in lint.DEPENDENCY_FIELDS)
        it["deps"] = sorted({r for r in lint.REF.findall(body) if r in by_id and r != it["id"]},
                            key=lambda r: items.index(by_id[r]))
        it["used_by"] = []
    for it in items:
        for d in it["deps"]:
            by_id[d]["used_by"].append(it["id"])

    for it in items:
        url = f"{REPO}{it['file']}#{anchor(it['note'])}"
        lines = ["---", f"kind: {lint.KINDS[it['kind']]}", f"id: {it['id']}", f"aliases: [\"{it['id']}\"]",
                 f"source: \"{it['file']}\"", "---", f"# {it['note']}",
                 f"> [!info] Generated from [{it['file']}]({url}). Edit the source, not this note.", ""]
        for f in lint.FIELDS:
            if f in it["fields"] and f != "Checks":
                lines += [f"## {f}", linked(it["fields"][f].strip()), ""]
        checks = lint.CHECK.findall(it["fields"].get("Checks", ""))
        if checks:
            lines += ["## Checks"] + [f"- [`{p}::{t}`]({REPO}{p})" for p, t in checks] + [""]
        lines += ["## Depends on"] + ([bullet(d) for d in it["deps"]] or ["- nothing"]) + [""]
        lines += ["## Used by"] + ([bullet(u) for u in it["used_by"]] or ["- no later item"])
        notes[f"{it['folder']}/{it['note']}.md"] = "\n".join(lines) + "\n"

    for path, folder in sources:
        name = "Core" if path == "CORE.md" else folder.split(" ", 1)[1]
        body = [linked(intros[path]), "", "## Items, in order"] + [bullet(it["id"]) for it in items if it["file"] == path]
        notes[f"{folder}/{name}.md"] = "\n".join(body) + "\n"

    for src, name in DOCS.items():
        if (root / src).exists():
            notes[f"{name}.md"] = linked((root / src).read_text(encoding="utf-8"))
    ontologies = sorted((root / "ontologies").glob("*/README.md"))
    for o in ontologies:
        notes[f"Ontologies/{o.parent.name}.md"] = linked(o.read_text(encoding="utf-8"))

    home = ["# Home", "", "A read-only view of the framework, generated from the repository by `tools/obsidian.py`. "
            "Edit the sources, not these notes; notes of your own go in `Annotations/`, which is never touched.", "",
            "- [[About]] · [[Standard]] · [[Record]] · [[Terms]] · [[Related]] · [[Import]] · [[Notes]] · "
            "[[References]]", "- [[Core]]: premises and definitions", "", "## Derived, in reading order"]
    home += [f"- [[{folder.split(' ', 1)[1]}]]" for _, folder in sources[1:]]
    home += ["", "## Ontologies", "- [[Ontologies]]: the slots"] + [f"- [[{o.parent.name}]]" for o in ontologies]
    notes["00 Home.md"] = "\n".join(home) + "\n"

    names = [Path(p).stem for p in notes]
    clashes = sorted({n for n in names if names.count(n) > 1})
    if clashes:
        raise ValueError(f"two notes share a name, so links would be ambiguous: {clashes}")
    return notes


def broken_links(notes):
    """Every wiki-link whose target is not a note."""
    names = {Path(p).stem for p in notes}
    return sorted({t for text in notes.values() for t in re.findall(r"\[\[([^\]|#\\]+)", text) if t not in names})


def on_disk(out):
    """The generated files now in out, skipping the folders the generator never touches."""
    return {p.relative_to(out).as_posix(): p.read_text(encoding="utf-8") for p in out.rglob("*.md")
            if p.relative_to(out).parts[0] not in KEEP}


def write(notes, out):
    for path in on_disk(out):
        if path not in notes:
            (out / path).unlink()
    for path, text in notes.items():
        (out / path).parent.mkdir(parents=True, exist_ok=True)
        (out / path).write_text(text, encoding="utf-8")
    for d in sorted((p for p in out.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
        if d.relative_to(out).parts[0] not in KEEP and not any(d.iterdir()):
            d.rmdir()


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    out, notes = root / "obsidian", build(root)
    if broken_links(notes):
        sys.exit(f"broken links: {broken_links(notes)}")
    if "--check" in sys.argv:
        stale = sorted(set(notes.items()) ^ set(on_disk(out).items()))
        if stale:
            sys.exit(f"obsidian/ is stale ({len({p for p, _ in stale})} files): run python3 tools/obsidian.py")
        print(f"obsidian/ is fresh: {len(notes)} notes")
    else:
        write(notes, out)
        print(f"obsidian/: {len(notes)} notes written")
