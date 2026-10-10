"""Mutation testing: break the code on purpose, and check that the tests notice.

A mutants file, in JSON, gives the tests to run and a list of mutants; each mutant is a name and a list of edits
[file, old, new], each `old` occurring exactly once in its file. For each mutant the repository is copied (without
.git), the edits are applied to the copy, and the tests run there with -x; the mutant is caught when they fail. A
mutant that survives is either a gap in the tests or equivalent to the original: say which in its "note", and when it
is a gap, add the test that catches it (`NOTES.md` §1, "A check that omits the constraint it tests").

Usage: python3 tools/mutate.py tools/mutants/<name>.json [mutant name ...]
The exit status is 1 if any mutant survives or an edit does not apply.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def apply(work, edits):
    """Apply the edits to the copy in `work`; raise if an `old` text does not occur exactly once."""
    for f, old, new in edits:
        p = work / f
        text = p.read_text(encoding="utf-8")
        if text.count(old) != 1:
            raise ValueError(f"{f}: the text to mutate occurs {text.count(old)} times, not once: {old[:60]!r}")
        p.write_text(text.replace(old, new), encoding="utf-8")


def run(spec, only=(), root=ROOT):
    """Run each mutant of `spec`; return a list of (name, caught, seconds, first failing test)."""
    results = []
    for m in spec["mutants"]:
        if only and m["name"] not in only:
            continue
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp) / "repo"
            shutil.copytree(root, work, ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"))
            apply(work, m["edits"])
            t0 = time.time()
            res = subprocess.run([sys.executable, "-m", "pytest", "-x", "-q", "-p", "no:cacheprovider", *spec["tests"]],
                                 cwd=work, capture_output=True, text=True)
            failed = next((line for line in res.stdout.splitlines() if line.startswith("FAILED")), "")
            results.append((m["name"], res.returncode != 0, time.time() - t0, failed))
    return results


def main(argv):
    spec = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    results = run(spec, set(argv[1:]))
    for name, caught, seconds, failed in results:
        print(f"{'caught  ' if caught else 'SURVIVED'} {name}  ({seconds:.0f}s) {failed[:100]}")
    survived = [r for r in results if not r[1]]
    print(f"{len(results) - len(survived)} of {len(results)} caught")
    return 1 if survived else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
