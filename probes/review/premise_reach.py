"""Which results of derived/ use each starting point of the core, and how (NOTES.md §17). Exploratory, not a check.
Usage: python3 probes/review/premise_reach.py, from the repository's root

For each imported axiom (M), background condition (B) and premise (A) of CORE.md, the results of derived/ whose
Statement or Proof cite it, directly or through other items ("logically"), and those that reach it once the core's
reasons, statuses and interpretations are followed too ("through justifications"). Then, for each definition, how many
results use it logically. References are read as lint reads them (tools/lint.py).
"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import lint                                                                          # noqa: E402

items = lint.parse_items((ROOT / "CORE.md").read_text(encoding="utf-8"), "CORE.md")[1]
for f in lint.derived_files(ROOT, []):
    items += lint.parse_items((ROOT / "derived" / f).read_text(encoding="utf-8"), f"derived/{f}")[1]
ids = {it["id"] for it in items}


def graph(fields):
    return {it["id"]: {r for f in fields for r in lint.REF.findall(it["fields"].get(f, "")) if r in ids and r != it["id"]}
            for it in items}


def reaching(g, target):
    """The items whose dependencies, followed to the end, include target."""
    out = set()
    for start in g:
        seen, stack = set(), [start]
        while stack:
            for m in g.get(stack.pop(), ()):
                if m not in seen:
                    seen.add(m); stack.append(m)
        if target in seen:
            out.add(start)
    return out


def key(i):
    return ("MBADPTLCR".index(i[0]), int(i[1:]))


logical = graph(["Statement", "Proof"])
justified = graph(["Statement", "Proof", "Interpretation", "Status", "Why this choice"])
results = sorted((i for i in ids if i[0] in "PTLC"), key=key)
print(f"{len(results)} results in derived/")
for a in sorted((i for i in ids if i[0] in "MBA"), key=key):
    direct = [r for r in results if a in logical[r]]
    lg = [r for r in results if r in reaching(logical, a)]
    jg = [r for r in results if r in reaching(justified, a)]
    print(f"{a}: cited in a result's Statement or Proof by {', '.join(direct) or 'none'}; results that use it "
          f"logically: {len(lg)}; through justifications too: {len(jg)}")
for d in sorted((i for i in ids if i[0] == "D"), key=key):
    print(f"{d}: {sum(r in reaching(logical, d) for r in results)} results use it logically")
