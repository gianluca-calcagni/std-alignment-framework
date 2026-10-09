"""Keep the Markdown sources wrapped at 120 columns, and their whitespace clean.

A paragraph or bullet is rewrapped, greedily, when one of its lines could have taken the next line's first word, or
when a line of several words runs past 120 columns. That covers both ways of writing: a paragraph typed as one long
line, and a paragraph left broken mid-sentence by an insertion. Block starts are kept as they are: headings, tables,
code, quotes, list items, field labels (**Statement.**), parts ((i), (ii), ...) and italic run-ins (*Notes.*), so the
rendered text never changes, only where its source lines break. Text in `code` is never broken. Trailing spaces, runs
of blank lines and a missing final newline are fixed too.

Not touched: the generated view (obsidian/), REFERENCES.md (one entry per line), and the files inside each case's folder
and probes/general/PREDICTIONS.md, whose hashes or registrations must not change (lint R14).

Usage: python3 tools/mdwrap.py [--check] [file ...]     (no file: every Markdown source of the repository)
With --check, nothing is written; the exit status is 1 if any file would change, and the files are listed.
"""
import re
import sys
from pathlib import Path

WIDTH = 120
ROOT = Path(__file__).resolve().parents[1]
ROMAN = r"\((?:i|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii)\)"
BLOCK_START = re.compile(r"^(> )?\s*(- |\d+\. |\*\*[^*]+\*\*|" + ROMAN + r" |\*[A-Z][^*]*\.\* |\*[A-Z][^*]*\*\.? )")


def sources(root=ROOT):
    """Every Markdown source the tool keeps: all .md files but the generated view, the bibliography, and the cases' and
    registered probes' records."""
    out = []
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root).as_posix()
        if rel.startswith((".git/", "obsidian/", ".pytest_cache/", "build/", "dist/")) or rel == "REFERENCES.md":
            continue
        if re.match(r"cases/[^/]+/", rel) or rel in ("probes/general/PREDICTIONS.md", "probes/general/RESULTS.md"):
            continue
        out.append(p)
    return out


def words(text):
    """Split on spaces outside `code` spans."""
    out, cur, inside = [], "", False
    for ch in text:
        if ch == "`":
            inside = not inside
        if ch == " " and not inside:
            if cur:
                out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def _special(line):
    s = line.lstrip()
    return (not s) or s.startswith(("|", "#", "```", "<"))


def _prefixes(line):
    m = re.match(r"^(> )?(\s*)((?:- |\d+\. )?)", line)
    quote, indent, marker = m[1] or "", m[2], m[3]
    return quote + indent + marker, quote + indent + " " * len(marker)


def _blocks(lines):
    """(start, end, first-line prefix, continuation prefix) of each paragraph or bullet outside code and tables."""
    i, n, fence = 0, len(lines), False
    while i < n:
        if lines[i].lstrip().startswith("```"):
            fence = not fence
            i += 1
            continue
        if fence or _special(lines[i]):
            i += 1
            continue
        first, rest = _prefixes(lines[i])
        j = i + 1
        while j < n and not _special(lines[j]) and not lines[j].lstrip().startswith("```"):
            if BLOCK_START.match(lines[j]) or (rest and not lines[j].startswith(rest)) \
                    or (not rest and lines[j].startswith(" ") and not lines[i].startswith(" ")):
                break
            j += 1
        yield i, j, first, rest
        i = j


def _needs_wrap(seg, rest):
    if any(len(line) > WIDTH and len(words(line[len(rest):])) > 1 for line in seg):
        return True
    for a, b in zip(seg, seg[1:]):
        w = words(b[len(rest):])
        if w and len(a) + 1 + len(w[0]) <= WIDTH - 1:            # the next word fitted: a break left by an edit
            return True
    return False


def _wrap(seg, first, rest):
    body = " ".join([seg[0][len(first):].strip()] + [line[len(rest):].strip() for line in seg[1:]])
    out, cur = [], first
    for w in words(body):
        if cur == first:
            cur += w
        elif len(cur) + 1 + len(w) <= WIDTH:
            cur += " " + w
        else:
            out.append(cur)
            cur = rest + w
    out.append(cur)
    return out


def tidy(text):
    """The text with broken or over-long paragraphs rewrapped and its whitespace cleaned."""
    lines = [line.rstrip() for line in text.split("\n")]
    new, last = [], 0
    for i, j, first, rest in _blocks(lines):
        new += lines[last:i]
        seg = lines[i:j]
        new += _wrap(seg, first, rest) if len(seg) >= 1 and _needs_wrap(seg, rest) else seg
        last = j
    new += lines[last:]
    out = re.sub(r"\n{3,}", "\n\n", "\n".join(new))
    return out.rstrip("\n") + "\n"


def main(argv):
    check = "--check" in argv
    files = [Path(a) for a in argv if a != "--check"] or sources()
    changed = []
    for p in files:
        text = p.read_text(encoding="utf-8")
        new = tidy(text)
        if new != text:
            changed.append(p)
            if not check:
                p.write_text(new, encoding="utf-8")
    for p in changed:
        print(("would rewrap " if check else "rewrapped ") + str(p))
    return 1 if (check and changed) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
