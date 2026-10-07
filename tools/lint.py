"""Lint the framework. Every rule below is a property the framework claims about itself; a property not checked here is
not claimed.

Usage: python3 tools/lint.py [root]      (exit status 1 on any error)

Where items live. CORE.md holds premises (A) and definitions (D). derived/ holds results (P proposition, T theorem,
L lemma, C corollary) and remarks (R), one file per topic; derived/README.md lists the files in reading order.

Rules
  R1  CORE.md starts with a '# ' title. Every '### ' heading in CORE.md and in derived/*.md is an item:
      '### <K><n> — <title>'. CORE.md holds only premises and definitions; derived/ holds only results and remarks.
      derived/README.md names every derived file once, in reading order, and names no missing file.
  R2  Item ids are unique; within each file, numbers increase within each kind.
  R3  Fields start a line with a bold label, appear at most once, in this order:
      Statement, In plain terms, Why this choice, Proof, Example, Checks, Notes, Lineage.
  R4  Required fields: every item has Statement, In plain terms and Lineage; a premise or definition has Why this choice;
      a result has Proof and Checks. No field is empty; In plain terms has at least 8 words.
  R5  References are written [D1], [P3], ...; each names an existing item. Dependencies are the references in
      Statement, Why this choice and Proof. A core Statement depends only on earlier core items. A result depends only
      on core items and on results earlier in the reading order. A core "why" may cite any item, but the dependencies
      form no cycle.
  R6  Checks cite pytest functions as checks/<file>.py::<test_name>; each exists. A result cites at least one.
  R7  Every test function in checks/ is cited by some item (no check without a claim).
  R8  Citations are written [@key]; each key is listed in REFERENCES.md as '- [@key] ...', listed once, and every
      listed key is cited in CORE.md, CORE-GENERAL.md, general/, derived/, ontologies/, STANDARD.md or RELATED.md.
  R9  Every term an item defines (a bold span in its Statement that does not end with '.') has an entry in TERMS.md
      (a bold name in the first column of a table row), and every item TERMS.md names exists. Matching ignores case,
      hyphens and a final 's' on each word.
  R10 Ontologies. ontologies/README.md lists the slots, one table row each: '| **<slot>** | [<item>] | ...'. Each
      ontology lives in its own folder, as ontologies/<name>/README.md, with a '# Ontology — ' title and the sections
      ONTOLOGY_SECTIONS, in order. Its section 1 has a table with the columns SLOT_COLUMNS; every slot appears in it
      once, its Core cell names the slot's item, its Fit cell starts with a word of FITS, and no other row appears.
      Section 2 cites a source, and has a paragraph starting '**Data.**' that says what numbers the discipline offers
      for the slots. Every bullet of section 3 starts with '**Consequence** of', '**Prediction** from' or
      '**Reading** with', and names at least one item before its first ':'; a prediction is labelled, as
      '**Prediction** (empirical) from' or '**Prediction** (verification) from', and says '*Refuted if*'.
      Sections 4 and 5 are not empty. Every item named in an ontology exists.
  R11 STANDARD.md names only existing items, and names every definition of the core: the reporting standard covers the
      whole shared vocabulary.
  R12 RELATED.md, the survey of related theories, IMPORT.md, the map from the archive to the core, CORE-GENERAL.md, the
      draft of the core for outcomes that are not finite, general/*.md, its results, SCENARIO.md, the worked scenario,
      ROADMAP.md, and cases/**/*.md, the registered tests, name only existing items; their citations count for R8.
  R13 RECORD.md, the record of predictions and retractions, names only existing items, and its citations count for
      R8. Its ledger (the table with the columns LEDGER_COLUMNS) has exactly one row for every prediction of the
      ontologies, keyed by the ontology's folder and the items the prediction is from, with the same label, and a
      state that starts with one of STATES; and no other row. RECORD.md must exist once any ontology predicts.
  R14 Cases. Every folder cases/<name>/ has a REGISTRATION.md. Once it has a RESULTS.md, that file records the SHA-256
      of REGISTRATION.md on a line starting '**Registration SHA-256:**', and the hash matches: a registration does not
      change after its result is written.
  R15 Design rules. A registration made after the design rules (cases/README.md), that is, of every case but those in
      BEFORE_THE_DESIGN_RULES, follows cases/TEMPLATE.md: it has the sections of REGISTRATION_SECTIONS; its declaration
      has a row for every field of the first table of STANDARD.md (the declaration); its predictions table has a
      column "Threshold from", filled in every row; and its folder holds rehearsal.json, the rehearsal's record. A field
      added to the declaration later is not required of the cases registered before it (FIELDS_ADDED_LATER).
"""
import hashlib, re, sys
from pathlib import Path

KINDS = {"A": "premise", "D": "definition", "P": "proposition", "T": "theorem", "L": "lemma", "C": "corollary",
         "R": "remark"}
CORE_KINDS, RESULTS, DERIVED_KINDS = set("AD"), set("PTLC"), set("PTLCR")
FIELDS = ["Statement", "In plain terms", "Why this choice", "Proof", "Example", "Checks", "Notes", "Lineage"]
DEPENDENCY_FIELDS = {"Statement", "Why this choice", "Proof"}
ITEM = re.compile(r"^### ([ADPTLCR])(\d+) — (\S.*)$")
LABEL = re.compile(r"^\*\*(" + "|".join(re.escape(f) for f in FIELDS) + r")\.\*\*")
REF = re.compile(r"\[([ADPTLCR]\d+)\]")
CHECK = re.compile(r"(checks/[\w/]+\.py)::(\w+)")
CITE = re.compile(r"\[@([\w:-]+)\]")
LISTED = re.compile(r"^- \[@([\w:-]+)\] \S")
TESTDEF = re.compile(r"^def (test_\w+)\(", re.M)
BOLD = re.compile(r"\*\*([^*]+?)\*\*")
ONTOLOGY_SECTIONS = ["1. Slots", "2. Known result", "3. What the core says", "4. Limits", "5. Open questions"]
SLOT_COLUMNS = ["Slot", "Core", "In this discipline", "Observed as", "Fit"]
FITS = ("exact", "approximate", "assumed", "absent")
CLAIM = re.compile(r"^- \*\*(Consequence)\*\* of |^- \*\*(Prediction)\*\*(?: \((verification|empirical)\))? from "
                   r"|^- \*\*(Reading)\*\* with ")
LEDGER_COLUMNS = ["Ontology", "From", "Label", "State", "Where"]
STATES = ("untested", "held", "refuted", "untestable")


def norm_term(t):
    words = re.sub(r"[-–]", " ", t.lower()).split()
    return " ".join(w[:-1] if len(w) > 3 and w.endswith("s") else w for w in words)


def parse_items(text, name):
    """Return (errors, items); each item has file, id, kind, number, line, fields {label: text}, order."""
    errors, items, cur, field, fenced = [], [], None, None, False
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced and re.match(r"^#{1,3} ", line):
            cur = field = None
            if line.startswith("### "):
                m = ITEM.match(line)
                if not m:
                    errors.append(f"{name}:{n}: R1 a '### ' heading must be an item '### <K><n> — <title>': {line!r}")
                    continue
                cur = {"file": name, "id": m[1] + m[2], "kind": m[1], "number": int(m[2]), "line": n, "fields": {},
                       "order": []}
                items.append(cur)
            continue
        if cur is None:
            continue
        m = None if fenced else LABEL.match(line)
        if m:
            field = m[1]
            if field in cur["fields"]:
                errors.append(f"{name}:{n}: R3 {cur['id']} has a second '{field}' field")
            cur["fields"][field] = line[m.end():]
            cur["order"].append(field)
        elif field is not None:
            cur["fields"][field] += "\n" + line
    return errors, items


def derived_files(root, errors):
    """The derived files in reading order, as listed in derived/README.md (R1)."""
    folder = root / "derived"
    if not folder.exists():
        return []
    readme = folder / "README.md"
    present = sorted(f.name for f in folder.glob("*.md") if f.name != "README.md")
    if not readme.exists():
        errors.append("derived: R1 README.md, with the reading order, is missing")
        return present
    listed = []
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            names = re.findall(r"`([\w.-]+\.md)`", line)
            if names:
                listed.append(names[0])
    for name in sorted(set(listed)):
        if listed.count(name) > 1:
            errors.append(f"derived/README.md: R1 {name} is listed {listed.count(name)} times")
        if name not in present:
            errors.append(f"derived/README.md: R1 {name} is listed but does not exist")
    for name in present:
        if name not in listed:
            errors.append(f"derived/README.md: R1 {name} is not listed in the reading order")
    return [n for i, n in enumerate(listed) if n in present and n not in listed[:i]]


def lint(root):
    root = Path(root); errors = []
    core = root / "CORE.md"
    if not core.exists():
        return ["CORE.md: R1 the core is missing"], {}
    core_text = core.read_text(encoding="utf-8")
    if not core_text.startswith("# "):
        errors.append("CORE.md:1: R1 must start with a '# ' title")
    perr, core_items = parse_items(core_text, "CORE.md"); errors += perr
    texts, items = {"CORE.md": core_text}, list(core_items)
    for it in core_items:
        if it["kind"] not in CORE_KINDS:
            errors.append(f"CORE.md:{it['line']}: R1 {it['id']} is a {KINDS[it['kind']]}; results belong in derived/")
    for name in derived_files(root, errors):
        path = f"derived/{name}"; text = (root / path).read_text(encoding="utf-8"); texts[path] = text
        perr, ditems = parse_items(text, path); errors += perr
        for it in ditems:
            if it["kind"] not in DERIVED_KINDS:
                errors.append(f"{path}:{it['line']}: R1 {it['id']} is a {KINDS[it['kind']]}; it belongs in CORE.md")
        items += ditems

    # R2
    pos, last = {}, {}
    for i, it in enumerate(items):
        if it["id"] in pos:
            errors.append(f"{it['file']}:{it['line']}: R2 duplicate id {it['id']}")
        else:
            pos[it["id"]] = i
        key = (it["file"], it["kind"])
        if it["number"] <= last.get(key, 0):
            errors.append(f"{it['file']}:{it['line']}: R2 {it['id']} does not increase on the previous "
                          f"{KINDS[it['kind']]} in this file")
        last[key] = max(last.get(key, 0), it["number"])

    # R5, existence: anywhere in the item files
    for name, text in texts.items():
        for n, line in enumerate(text.splitlines(), 1):
            for ref in REF.findall(line):
                if ref not in pos:
                    errors.append(f"{name}:{n}: R5 [{ref}] names no item")

    # R3, R4, R5 (order and cycles), R6
    cited_checks, test_defs, deps = set(), {}, {}
    for f in sorted((root / "checks").rglob("*.py")) if (root / "checks").exists() else []:
        rel = f.relative_to(root).as_posix()
        test_defs[rel] = set(TESTDEF.findall(f.read_text(encoding="utf-8")))
    for i, it in enumerate(items):
        where, fields = f"{it['file']}:{it['line']}: {it['id']}", it["fields"]
        if it["order"] != sorted(it["order"], key=FIELDS.index):
            errors.append(f"{where}: R3 fields out of order: {', '.join(it['order'])}")
        required = ["Statement", "In plain terms", "Lineage"]
        if it["kind"] in CORE_KINDS:
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
        deps[it["id"]] = set()
        for f, body in fields.items():
            if f not in DEPENDENCY_FIELDS:
                continue
            for ref in REF.findall(body):
                if ref not in pos or ref == it["id"]:
                    continue
                deps[it["id"]].add(ref)
                target = items[pos[ref]]; in_core = target["file"] == "CORE.md"
                if it["file"] == "CORE.md" and f == "Statement" and (not in_core or pos[ref] > i):
                    errors.append(f"{where}: R5 its Statement uses [{ref}], which is not an earlier core item")
                if it["file"] != "CORE.md" and not in_core and pos[ref] > i:
                    errors.append(f"{where}: R5 '{f}' uses [{ref}], which comes later in the reading order")
        checks = CHECK.findall(fields.get("Checks", ""))
        if it["kind"] in RESULTS and "Checks" in fields and not checks:
            errors.append(f"{where}: R6 a result must cite at least one check")
        for path, name in checks:
            if name not in test_defs.get(path, set()):
                errors.append(f"{where}: R6 {path}::{name} does not exist")
            cited_checks.add((path, name))
    state = {}
    def visit(node, trail):
        state[node] = 1
        for nxt in sorted(deps.get(node, ())):
            if state.get(nxt) == 1:
                cycle = trail[trail.index(nxt):] + [nxt] if nxt in trail else [node, nxt]
                errors.append(f"{items[pos[node]]['file']}: R5 the dependencies form a cycle: {' → '.join(cycle)}")
            elif nxt not in state:
                visit(nxt, trail + [nxt])
        state[node] = 2
    for node in sorted(deps):
        if node not in state:
            visit(node, [node])

    # R7
    for path, names in sorted(test_defs.items()):
        for name in sorted(names):
            if (path, name) not in cited_checks:
                errors.append(f"{path}: R7 {name} is cited by no item")

    # R10 and R11 (before R8, which counts their citations)
    onto_errors, onto_cited, n_onto, predictions = lint_ontologies(root, pos)
    errors += onto_errors
    cited = {(name, k) for name, text in texts.items() for k in CITE.findall(text)} | onto_cited
    standard = root / "STANDARD.md"
    if standard.exists():
        stext = standard.read_text(encoding="utf-8")
        cited |= {("STANDARD.md", k) for k in CITE.findall(stext)}
        named = set()
        for n, line in enumerate(stext.splitlines(), 1):
            for ref in REF.findall(line):
                named.add(ref)
                if ref not in pos:
                    errors.append(f"STANDARD.md:{n}: R11 [{ref}] names no item")
        for it in core_items:
            if it["kind"] == "D" and it["id"] not in named:
                errors.append(f"STANDARD.md: R11 the definition {it['id']} is not covered by the standard")
    elif any(it["kind"] == "D" for it in core_items):
        errors.append("STANDARD.md: R11 the reporting standard is missing")
    # R13
    record = root / "RECORD.md"
    if record.exists():
        rtext = record.read_text(encoding="utf-8")
        cited |= {("RECORD.md", k) for k in CITE.findall(rtext)}
        for n, line in enumerate(rtext.splitlines(), 1):
            for ref in REF.findall(line):
                if ref not in pos:
                    errors.append(f"RECORD.md:{n}: R13 [{ref}] names no item")
        errors += lint_ledger(rtext, predictions)
    elif predictions:
        errors.append("RECORD.md: R13 the record, with the ledger of the ontologies' predictions, is missing")
    folder, cases = root / "general", root / "cases"
    general = sorted(f.relative_to(root).as_posix() for f in folder.glob("*.md")) if folder.exists() else []
    case_docs = sorted(f.relative_to(root).as_posix() for f in cases.rglob("*.md")) if cases.exists() else []
    for name in ["RELATED.md", "IMPORT.md", "CORE-GENERAL.md", "SCENARIO.md", "ROADMAP.md"] + general + case_docs:
        survey = root / name
        if survey.exists():
            rtext = survey.read_text(encoding="utf-8")
            cited |= {(name, k) for k in CITE.findall(rtext)}
            for n, line in enumerate(rtext.splitlines(), 1):
                for ref in REF.findall(line):
                    if ref not in pos:
                        errors.append(f"{name}:{n}: R12 [{ref}] names no item")

    # R14, R15
    if cases.exists():
        errors += lint_cases(cases)
        standard_file = root / "STANDARD.md"
        if standard_file.exists():
            errors += lint_design_rules(cases, standard_file.read_text(encoding="utf-8"))

    # R8
    refs_file = root / "REFERENCES.md"
    listed = [m[1] for line in (refs_file.read_text(encoding="utf-8").splitlines() if refs_file.exists() else [])
              if (m := LISTED.match(line))]
    for key in sorted({k for k in listed if listed.count(k) > 1}):
        errors.append(f"REFERENCES.md: R8 {key} is listed twice")
    for name, key in sorted(cited):
        if key not in listed:
            errors.append(f"{name}: R8 [@{key}] is not in REFERENCES.md")
    for key in sorted(set(listed) - {k for _, k in cited}):
        errors.append(f"REFERENCES.md: R8 [@{key}] is cited nowhere")

    # R9
    defined = {}
    for it in items:
        for term in BOLD.findall(it["fields"].get("Statement", "")):
            if not term.rstrip().endswith("."):
                defined.setdefault(norm_term(term), (it["id"], term))
    terms_file = root / "TERMS.md"
    glossary = set()
    terms_text = terms_file.read_text(encoding="utf-8") if terms_file.exists() else ""
    for line in terms_text.splitlines():
        if line.startswith("|") and not line.startswith("|---"):
            first = line.split("|")[1]
            glossary.update(norm_term(t) for t in BOLD.findall(first))
    for key, (iid, term) in sorted(defined.items()):
        if key not in glossary:
            errors.append(f"{items[pos[iid]]['file']}: {iid}: R9 the term '{term}' has no entry in TERMS.md")
    for n, line in enumerate(terms_text.splitlines(), 1):
        for ref in REF.findall(line):
            if ref not in pos:
                errors.append(f"TERMS.md:{n}: R9 [{ref}] names no item")

    counts = {KINDS[k]: sum(it["kind"] == k for it in items) for k in KINDS}
    summary = {"items": len(items), **{k: v for k, v in counts.items() if v},
               "checks": sum(len(v) for v in test_defs.values()), "references": len(set(listed)),
               "terms": len(glossary), "ontologies": n_onto}
    return errors, summary


def lint_cases(cases):
    """R14: every case has a registration, and a result records the registration's hash, which still matches."""
    errors = []
    for case in sorted(d for d in cases.iterdir() if d.is_dir()):
        name, registration, results = f"cases/{case.name}", case / "REGISTRATION.md", case / "RESULTS.md"
        if not registration.exists():
            errors.append(f"{name}: R14 a case has no REGISTRATION.md")
            continue
        if not results.exists():
            continue
        digest = hashlib.sha256(registration.read_bytes()).hexdigest()
        text = results.read_text(encoding="utf-8")
        recorded = re.findall(r"^\*\*Registration SHA-256:\*\*\s*`?([0-9a-f]{64})`?", text, re.M)
        if not recorded:
            errors.append(f"{name}/RESULTS.md: R14 the SHA-256 of REGISTRATION.md is not recorded")
        elif recorded[0] != digest:
            errors.append(f"{name}/RESULTS.md: R14 REGISTRATION.md changed after its result: its SHA-256 is {digest}")
    return errors


BEFORE_THE_DESIGN_RULES = {"c1-collusion-simulation", "c2-stopping-rule", "w1-best-of-n-slope", "w3-ppo-pursuit"}
FIELDS_ADDED_LATER = {"Principal": {"w4-two-runs"}}                            # field: cases registered before it
REGISTRATION_SECTIONS = ["## Declaration", "## Auxiliary assumptions", "## Predictions", "## Readings, fixed now",
                         "## Rehearsal", "## Licences"]


def sections(text):
    """The lines of each '## ' section of a markdown text, by heading."""
    out, cur = {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = line.strip(); out[cur] = []
        elif cur:
            out[cur].append(line)
    return out


def lint_design_rules(cases, standard):
    """R15: a registration made after the design rules follows cases/TEMPLATE.md."""
    errors = []
    first = next((block for block in re.split(r"\n\s*\n", standard) if block.lstrip().startswith("|")), "")
    fields = [row[0] for row in table_rows(first.splitlines())[1:]]
    for case in sorted(d for d in cases.iterdir() if d.is_dir() and d.name not in BEFORE_THE_DESIGN_RULES):
        registration = case / "REGISTRATION.md"
        if not registration.exists():
            continue                                                                # R14 reports it
        name, secs = f"cases/{case.name}/REGISTRATION.md", sections(registration.read_text(encoding="utf-8"))
        for heading in REGISTRATION_SECTIONS:
            if heading not in secs:
                errors.append(f"{name}: R15 the section '{heading}' is missing (cases/TEMPLATE.md)")
        declared = {row[0] for row in table_rows(secs.get("## Declaration", []))}
        for field in fields:
            if field not in declared and case.name not in FIELDS_ADDED_LATER.get(field, set()):
                errors.append(f"{name}: R15 the declaration has no row for the field '{field}' of STANDARD.md")
        rows = table_rows(secs.get("## Predictions", []))
        if not rows or "Threshold from" not in rows[0]:
            errors.append(f"{name}: R15 the predictions table has no column 'Threshold from'")
        else:
            k = rows[0].index("Threshold from")
            for row in rows[1:]:
                if len(row) <= k or not row[k]:
                    errors.append(f"{name}: R15 prediction {row[0]} does not say where its threshold comes from")
        if not (case / "rehearsal.json").exists():
            errors.append(f"cases/{case.name}: R15 the rehearsal's record, rehearsal.json, is missing")
    return errors


def table_rows(lines):
    """The cells of each table row in lines, skipping separator rows."""
    return [[c.strip() for c in line.strip().strip("|").split("|")] for line in lines
            if line.strip().startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", line.strip())]


def lint_ontologies(root, pos):
    """R10. Returns (errors, {(file name, cited key)}, number of ontologies)."""
    folder = root / "ontologies"
    if not folder.exists():
        return [], set(), 0, {}
    errors, cited, predictions = [], set(), {}
    readme = folder / "README.md"
    if not readme.exists():
        return ["ontologies: R10 README.md, with the slot table, is missing"], cited, 0, predictions
    rtext = readme.read_text(encoding="utf-8")
    cited |= {("ontologies/README.md", k) for k in CITE.findall(rtext)}
    slots = {}
    for cells in table_rows(rtext.splitlines()):
        m = re.fullmatch(r"\*\*([^*]+)\*\*", cells[0]) if cells else None
        refs = REF.findall(cells[1]) if len(cells) > 1 else []
        if m and len(refs) == 1 and cells[1] == f"[{refs[0]}]":
            slots[m[1]] = refs[0]
    if not slots:
        errors.append("ontologies/README.md: R10 no slot table ('| **<slot>** | [<item>] | ...')")
    for f in sorted(folder.glob("*.md")):
        if f.name != "README.md":
            errors.append(f"ontologies/{f.name}: R10 an ontology lives in its own folder, as <name>/README.md")
    files = sorted(d / "README.md" for d in folder.iterdir() if d.is_dir() and (d / "README.md").exists())
    for f in [readme] + files:
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for ref in REF.findall(line):
                if ref not in pos:
                    errors.append(f"{f.relative_to(root).as_posix()}:{n}: R10 [{ref}] names no item")
    for f in files:
        where, text = f.relative_to(root).as_posix(), f.read_text(encoding="utf-8")
        cited |= {(where, k) for k in CITE.findall(text)}
        if not text.startswith("# Ontology — "):
            errors.append(f"{where}:1: R10 must start with '# Ontology — <discipline>'")
        heads, body, cur = [], {}, None
        for line in text.splitlines():
            if line.startswith("## "):
                cur = line[3:].strip(); heads.append(cur); body[cur] = []
            elif cur is not None:
                body[cur].append(line)
        if heads != ONTOLOGY_SECTIONS:
            errors.append(f"{where}: R10 sections must be {ONTOLOGY_SECTIONS}, found {heads}")
        rows = table_rows(body.get(ONTOLOGY_SECTIONS[0], []))
        if not rows or rows[0] != SLOT_COLUMNS:
            errors.append(f"{where}: R10 section 1 needs a table with the columns {', '.join(SLOT_COLUMNS)}")
        else:
            seen = []
            for cells in rows[1:]:
                m = re.fullmatch(r"\*\*([^*]+)\*\*", cells[0])
                name = m[1] if m else cells[0]
                if name not in slots:
                    errors.append(f"{where}: R10 '{name}' is not a slot of ontologies/README.md")
                    continue
                seen.append(name)
                if len(cells) != len(SLOT_COLUMNS) or any(not c for c in cells):
                    errors.append(f"{where}: R10 the row of '{name}' must fill all {len(SLOT_COLUMNS)} columns")
                    continue
                if f"[{slots[name]}]" not in cells[1]:
                    errors.append(f"{where}: R10 the Core cell of '{name}' must name [{slots[name]}]")
                if not cells[4].lower().startswith(FITS):
                    errors.append(f"{where}: R10 the Fit of '{name}' must start with one of {', '.join(FITS)}")
            for name in slots:
                if seen.count(name) != 1:
                    errors.append(f"{where}: R10 the slot '{name}' appears {seen.count(name)} times, not once")
        if not CITE.search("\n".join(body.get(ONTOLOGY_SECTIONS[1], []))):
            errors.append(f"{where}: R10 the known result must cite its source [@key]")
        if not any(line.startswith("**Data.**") for line in body.get(ONTOLOGY_SECTIONS[1], [])):
            errors.append(f"{where}: R10 the known result needs a paragraph '**Data.**' on the numbers available")
        claims, cur = [], None
        for line in body.get(ONTOLOGY_SECTIONS[2], []):
            if line.startswith("- "):
                cur = [line]; claims.append(cur)
            elif cur is not None and line.startswith("  "):
                cur.append(line)
            else:
                cur = None
        if not claims:
            errors.append(f"{where}: R10 section 3 has no claims")
        for claim in claims:
            first, whole = claim[0], " ".join(claim)
            m = CLAIM.match(first)
            if not m:
                errors.append(f"{where}: R10 a claim must start with a kind and its items: {first[:60]!r}")
                continue
            head = whole[m.end():].split(":", 1)[0]
            if not REF.search(head):
                errors.append(f"{where}: R10 a claim names no item before its ':': {first[:60]!r}")
            if m[2] and "*Refuted if*" not in whole:
                errors.append(f"{where}: R10 a prediction must say when it is '*Refuted if*': {first[:60]!r}")
            if m[2] and not m[3]:
                errors.append(f"{where}: R10 a prediction must be labelled (verification) or (empirical): {first[:60]!r}")
            if m[2]:
                key = (f.parent.name, tuple(sorted(set(REF.findall(head)))))
                if key in predictions:
                    errors.append(f"{where}: R10 two predictions from the same items {', '.join(key[1])}")
                predictions[key] = m[3]
        for sec in ONTOLOGY_SECTIONS[3:]:
            if sec in body and not "".join(body[sec]).strip():
                errors.append(f"{where}: R10 section '{sec}' is empty")
    return errors, cited, len(files), predictions


def lint_ledger(text, predictions):
    """R13: the ledger has one row per prediction of the ontologies, with its label and a state."""
    errors, lines = [], text.splitlines()
    starts = [i for i, line in enumerate(lines) if table_rows([line]) == [LEDGER_COLUMNS]]
    if not starts:
        return [f"RECORD.md: R13 no ledger: a table with the columns {', '.join(LEDGER_COLUMNS)}"] if predictions else []
    rows, i = [], starts[0] + 1
    while i < len(lines) and lines[i].strip().startswith("|"):
        parsed = table_rows([lines[i]])
        if parsed:
            rows.append((i + 1, parsed[0]))
        i += 1
    seen = {}
    for n, cells in rows:
        if len(cells) != len(LEDGER_COLUMNS):
            errors.append(f"RECORD.md:{n}: R13 a ledger row must fill all {len(LEDGER_COLUMNS)} columns")
            continue
        key = (cells[0], tuple(sorted(set(REF.findall(cells[1])))))
        if key in seen:
            errors.append(f"RECORD.md:{n}: R13 the prediction of {key[0]} from {cells[1]} is listed twice")
        seen[key] = n
        if key not in predictions:
            errors.append(f"RECORD.md:{n}: R13 no prediction of ontologies/{key[0]}/ is from {cells[1]}")
        elif cells[2] != predictions[key]:
            errors.append(f"RECORD.md:{n}: R13 the label is '{cells[2]}' here but '{predictions[key]}' in the ontology")
        if not cells[3].lower().startswith(STATES):
            errors.append(f"RECORD.md:{n}: R13 the state must start with one of {', '.join(STATES)}")
    for key in sorted(set(predictions) - set(seen)):
        errors.append(f"RECORD.md: R13 the prediction of ontologies/{key[0]}/ from {', '.join(key[1])} has no row")
    return errors


if __name__ == "__main__":
    errs, summary = lint(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
    for e in errs:
        print(e)
    print("lint:", ", ".join(f"{k} {v}" for k, v in summary.items()), f"— {len(errs)} error(s)")
    sys.exit(1 if errs else 0)
