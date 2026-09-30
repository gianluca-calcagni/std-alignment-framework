"""Lint the core. Every rule below is a property the core claims about itself; a property not checked here is not claimed.

Usage: python3 tools/lint.py [root]      (exit status 1 on any error)

Rules
  R1  CORE.md starts with a '# ' title; every '### ' heading is an item: '### <K><n> — <title>',
      K in D (definition), P (proposition), T (theorem), L (lemma), C (corollary), R (remark).
  R2  Item ids are unique, and numbers increase within each kind, in reading order.
  R3  Fields start a line with a bold label, appear at most once, in this order:
      Statement, In plain terms, Why this choice, Proof, Example, Checks, Notes, Lineage.
  R4  Required fields: every item has Statement, In plain terms and Lineage; a definition has Why this choice;
      a result (P, T, L, C) has Proof and Checks. No field is empty; In plain terms has at least 8 words.
  R5  References are written [D1], [P3], ...; each names an existing item. In Statement, Why this choice and Proof
      they name an item that comes earlier (dependencies follow reading order, so they cannot form a cycle).
  R6  Checks cite pytest functions as checks/<file>.py::<test_name>; each exists. A result cites at least one.
  R7  Every test function in checks/ is cited by some item (no check without a claim).
  R8  Citations are written [@key]; each key is listed in REFERENCES.md as '- [@key] ...', listed once, and every
      listed key is cited in CORE.md.
"""
import re, sys
from pathlib import Path

KINDS = {"D": "definition", "P": "proposition", "T": "theorem", "L": "lemma", "C": "corollary", "R": "remark"}
RESULTS = set("PTLC")
FIELDS = ["Statement", "In plain terms", "Why this choice", "Proof", "Example", "Checks", "Notes", "Lineage"]
ORDERED_DEPS = {"Statement", "Why this choice", "Proof"}
ITEM = re.compile(r"^### ([DPTLCR])(\d+) — (\S.*)$")
LABEL = re.compile(r"^\*\*(" + "|".join(re.escape(f) for f in FIELDS) + r")\.\*\*")
REF = re.compile(r"\[([DPTLCR]\d+)\]")
CHECK = re.compile(r"(checks/[\w/]+\.py)::(\w+)")
CITE = re.compile(r"\[@([\w:-]+)\]")
LISTED = re.compile(r"^- \[@([\w:-]+)\] \S")
TESTDEF = re.compile(r"^def (test_\w+)\(", re.M)


def parse_items(text):
    """Return (errors, items); each item is a dict with id, kind, number, line, fields {label: text}."""
    errors, items, cur, field, fenced = [], [], None, None, False
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced and re.match(r"^#{1,3} ", line):
            cur = field = None
            if line.startswith("### "):
                m = ITEM.match(line)
                if not m:
                    errors.append(f"CORE.md:{n}: R1 a '### ' heading must be an item '### <K><n> — <title>': {line!r}")
                    continue
                cur = {"id": m[1] + m[2], "kind": m[1], "number": int(m[2]), "line": n, "fields": {}, "order": []}
                items.append(cur)
            continue
        if cur is None:
            continue
        m = None if fenced else LABEL.match(line)
        if m:
            field = m[1]
            if field in cur["fields"]:
                errors.append(f"CORE.md:{n}: R3 {cur['id']} has a second '{field}' field")
            cur["fields"][field] = line[m.end():]
            cur["order"].append(field)
        elif field is not None:
            cur["fields"][field] += "\n" + line
    return errors, items


def lint(root):
    root = Path(root); errors = []
    core = root / "CORE.md"
    if not core.exists():
        return [f"R1 CORE.md is missing"], {}
    text = core.read_text(encoding="utf-8")
    if not text.startswith("# "):
        errors.append("CORE.md:1: R1 must start with a '# ' title")
    perr, items = parse_items(text); errors += perr

    # R2
    pos, last = {}, {}
    for i, it in enumerate(items):
        if it["id"] in pos:
            errors.append(f"CORE.md:{it['line']}: R2 duplicate id {it['id']}")
        else:
            pos[it["id"]] = i
        if it["number"] <= last.get(it["kind"], 0):
            errors.append(f"CORE.md:{it['line']}: R2 {it['id']} does not increase on the previous {KINDS[it['kind']]}")
        last[it["kind"]] = max(last.get(it["kind"], 0), it["number"])

    # R5, existence: anywhere in the document
    for n, line in enumerate(text.splitlines(), 1):
        for ref in REF.findall(line):
            if ref not in pos:
                errors.append(f"CORE.md:{n}: R5 [{ref}] names no item")

    # R3, R4, R5 (order), R6
    cited_checks, test_defs = set(), {}
    for f in sorted((root / "checks").rglob("*.py")) if (root / "checks").exists() else []:
        rel = f.relative_to(root).as_posix()
        test_defs[rel] = set(TESTDEF.findall(f.read_text(encoding="utf-8")))
    for i, it in enumerate(items):
        where, fields = f"CORE.md:{it['line']}: {it['id']}", it["fields"]
        if it["order"] != sorted(it["order"], key=FIELDS.index):
            errors.append(f"{where}: R3 fields out of order: {', '.join(it['order'])}")
        required = ["Statement", "In plain terms", "Lineage"]
        if it["kind"] == "D":
            required.append("Why this choice")
        if it["kind"] in RESULTS:
            required += ["Proof", "Checks"]
        for f in required:
            if f not in fields:
                errors.append(f"{where}: R4 missing field '{f}'")
        for f, body in fields.items():
            if not body.strip():
                errors.append(f"{where}: R4 field '{f}' is empty")
        if "In plain terms" in fields and len(fields["In plain terms"].split()) < 8:
            errors.append(f"{where}: R4 'In plain terms' has fewer than 8 words")
        for f, body in fields.items():
            for ref in REF.findall(body):
                if f in ORDERED_DEPS and ref in pos and pos[ref] > i:
                    errors.append(f"{where}: R5 '{f}' uses [{ref}], which comes later")
        checks = CHECK.findall(fields.get("Checks", ""))
        if it["kind"] in RESULTS and "Checks" in fields and not checks:
            errors.append(f"{where}: R6 a result must cite at least one check")
        for path, name in checks:
            if name not in test_defs.get(path, set()):
                errors.append(f"{where}: R6 {path}::{name} does not exist")
            cited_checks.add((path, name))

    # R7
    for path, names in sorted(test_defs.items()):
        for name in sorted(names):
            if (path, name) not in cited_checks:
                errors.append(f"{path}: R7 {name} is cited by no item")

    # R8
    refs_file = root / "REFERENCES.md"
    listed = [m[1] for line in (refs_file.read_text(encoding="utf-8").splitlines() if refs_file.exists() else [])
              if (m := LISTED.match(line))]
    for key in sorted({k for k in listed if listed.count(k) > 1}):
        errors.append(f"REFERENCES.md: R8 {key} is listed twice")
    cited = set(CITE.findall(text))
    for key in sorted(cited - set(listed)):
        errors.append(f"CORE.md: R8 [@{key}] is not in REFERENCES.md")
    for key in sorted(set(listed) - cited):
        errors.append(f"REFERENCES.md: R8 [@{key}] is cited nowhere in CORE.md")

    counts = {KINDS[k]: sum(it["kind"] == k for it in items) for k in KINDS}
    summary = {"items": len(items), **{k: v for k, v in counts.items() if v},
               "checks": sum(len(v) for v in test_defs.values()), "references": len(set(listed))}
    return errors, summary


if __name__ == "__main__":
    errs, summary = lint(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
    for e in errs:
        print(e)
    print("lint:", ", ".join(f"{k} {v}" for k, v in summary.items()), f"— {len(errs)} error(s)")
    sys.exit(1 if errs else 0)
