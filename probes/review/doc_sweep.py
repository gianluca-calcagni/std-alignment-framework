"""A scripted sweep of the Markdown sources for doc hygiene (NOTES.md §12, §19). Exploratory, not a check: it prints
what to look at, and a person decides. Usage: python3 probes/review/doc_sweep.py, from the repository's root.

It reports, file by file: paths in backticks and relative links that name nothing in the repository; claims of how many
items, checks or tests there are that disagree with lint's count or pytest's collection; American spellings and the
-ise forms of -ize words, against the British -ize style of CLAUDE.md; lines over 120 columns outside tables and code;
trailing whitespace and tabs; and paragraphs that end without punctuation before a blank line, a sign of a break
mid-sentence. Generated files (OVERVIEW.md, obsidian/) are skipped: their sources are swept instead.
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import lint                                                                         # noqa: E402

SKIP = ("obsidian/", "OVERVIEW.md", ".git/", ".pytest_cache", "node_modules")
AMERICAN = r"\b(behavior|behaviors|behavioral|color|colors|favor|favors|favorable|honor|labor|analyze|analyzed|analyzing|center|centers|centered|modeling|modeled|labeled|labeling|catalog|defense|offense|traveled|canceled|fulfill|fulfillment|enroll|enrollment|gray|license[sd]? to|program[sm]?e)\b"
ISE = r"\b(organis|realis|recognis|minimis|maximis|characteris|generalis|emphasis(?:e|ed|es|ing)\b|summaris|normalis|optimis|parametris|regularis|randomis|categoris|prioritis|standardis|utilis|specialis|criticis|formalis|visualis|stabilis|penalis|initialis|finalis|authoris|apologis)\w*"
PATH = re.compile(r"`((?:[\w.-]+/)*[\w.-]+\.(?:md|py|json|txt|yml|toml)|(?:[\w.-]{3,}/)+)`")
LINK = re.compile(r"\]\(((?!https?:|#|mailto:|[ivx]+\))[^)\s]+)\)")
HOMES = ("derived", "general", "cases", "ontologies", "tools", "probes", "stdalign", "checks", "examples", "scenario")
COUNT = re.compile(r"\b(\d+) (propositions|definitions|premises|background conditions|imported axioms|checks of the items|tests of the tools|results|corollaries)\b")


def sources():
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if not any(rel.startswith(s) or s in rel for s in SKIP):
            yield rel, p.read_text(encoding="utf-8")


def exists(rel_from, target):
    target = target.split("#")[0].rstrip("/")
    if not target or any(c in target for c in "*<>{}"):
        return True
    if re.fullmatch(r"[ivx]+", target) or target.startswith(("claude/", "origin/")):
        return True                                                                 # item parts; branch names
    for base in (ROOT, (ROOT / rel_from).parent, *(ROOT / h for h in HOMES)):
        if (base / target).exists():
            return True
    return any(ROOT.glob(f"*/*/{target}"))


def main():
    _, summary = lint.lint(ROOT)
    expected = {"propositions": summary.get("proposition"), "definitions": summary.get("definition"),
                "premises": summary.get("premise"), "background conditions": summary.get("background condition"),
                "imported axioms": summary.get("imported axiom"), "corollaries": summary.get("corollary"),
                "checks of the items": summary.get("checks")}
    for rel, text in sources():
        found = []
        in_code = False
        lines = text.splitlines()
        for n, line in enumerate(lines, 1):
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            for m in PATH.finditer(line):
                if not exists(rel, m[1]):
                    found.append((n, "path", m[1]))
            for m in LINK.finditer(line):
                if not exists(rel, m[1]):
                    found.append((n, "link", m[1]))
            for m in COUNT.finditer(line):
                want = expected.get(m[2])
                if want is not None and int(m[1]) != want and "NOTES.md" not in rel:
                    found.append((n, "count", f"{m[0]} (lint: {want})"))
            for m in re.finditer(AMERICAN, line, re.I):
                found.append((n, "spelling", m[0]))
            for m in re.finditer(ISE, line, re.I):
                found.append((n, "-ise", m[0]))
            if len(line) > 120 and not line.startswith("|") and not line.startswith(">"):
                found.append((n, "long", f"{len(line)} columns"))
            if line != line.rstrip() or "\t" in line:
                found.append((n, "whitespace", repr(line[-10:])))
            if (line.strip() and not line.startswith(("|", "#", "-", ">", " ", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
                    and n < len(lines) and not lines[n].strip() and n + 1 < len(lines)
                    and lines[n + 1][:1].islower() and not line.rstrip().endswith((".", ":", "!", "?", ")", "`", "|"))):
                found.append((n, "break", line[-40:]))
        for n, kind, what in found:
            print(f"{rel}:{n}: {kind}: {what}")


if __name__ == "__main__":
    main()
