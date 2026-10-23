"""The MVP's core is complete: every item has its fields, in order, and every check it cites exists and is cited."""
import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORE = (ROOT / "mvp" / "CORE.md").read_text(encoding="utf-8")
FIELDS = {"D": ["Statement", "Interpretation", "Lineage"],
          "R": ["Statement", "In plain terms", "Proof", "Checks", "Lineage"]}


def items():
    parts = re.split(r"^### ", CORE, flags=re.M)[1:]
    return [(re.match(r"([DR])(\d+) — ", p), p) for p in parts]


def test_every_heading_is_an_item_with_its_fields_in_order():
    seen = {"D": [], "R": []}
    for m, body in items():
        assert m, f"a ### heading is not an item: {body[:40]!r}"
        kind, num = m.group(1), int(m.group(2))
        seen[kind].append(num)
        positions = [body.find(f"**{f}.**") for f in FIELDS[kind]]
        assert all(p >= 0 for p in positions), f"{kind}{num} lacks a field: {FIELDS[kind]}"
        assert positions == sorted(positions), f"{kind}{num}: fields out of order"
    for kind, nums in seen.items():
        assert nums == list(range(1, len(nums) + 1)), f"{kind} items not numbered 1..n: {nums}"


def test_every_cited_check_exists_and_every_check_is_cited():
    cited = set()
    for m, body in items():
        if m.group(1) != "R":
            continue
        line = body.split("**Checks.**", 1)[1].split("\n\n", 1)[0]
        names = re.findall(r"::(test_\w+)", line)
        assert names, f"R{m.group(2)} cites no check"
        cited.update(names)
    cited.update(re.findall(r"test_core\.py::(test_\w+)", CORE))
    tree = ast.parse((ROOT / "mvp" / "checks" / "test_core.py").read_text(encoding="utf-8"))
    defined = {n.name for n in tree.body if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")}
    assert cited <= defined, f"cited but missing: {sorted(cited - defined)}"
    assert defined <= cited, f"checks no item cites: {sorted(defined - cited)}"


def test_references_name_existing_items():
    ids = {m.group(1) + m.group(2) for m, _ in items()}
    for ref in re.findall(r"(?<!\[)\b([DR]\d+)\b(?!\])", CORE):     # bracketed ids, such as [D3], are v13's
        assert ref in ids, f"reference to a missing item: {ref}"
