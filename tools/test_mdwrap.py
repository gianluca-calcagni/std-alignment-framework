"""Tests of tools/mdwrap.py: broken and over-long paragraphs are rewrapped with their text unchanged; block starts,
tables, code and headings are kept; whitespace is cleaned; and the repository's own sources are kept wrapped."""
import re
import mdwrap

LONG = " ".join(f"word{i}" for i in range(60))


def same_text(a, b):
    return re.sub(r"\s+", " ", a).strip() == re.sub(r"\s+", " ", b).strip()


def test_a_broken_paragraph_is_rejoined_and_its_text_kept():
    src = "A paragraph whose first line\nbroke early, as an insertion leaves it, and goes on.\n"
    out = mdwrap.tidy(src)
    assert out == "A paragraph whose first line broke early, as an insertion leaves it, and goes on.\n"
    nearly_full = "x" * 100 + "\nshort tail.\n"                         # a break with room left for the next word
    assert mdwrap.tidy(nearly_full) == "x" * 100 + " short tail.\n"


def test_a_long_line_is_wrapped_greedily_at_the_width():
    out = mdwrap.tidy(LONG + "\n")
    lines = out.rstrip("\n").split("\n")
    assert len(lines) > 1 and all(len(line) <= mdwrap.WIDTH for line in lines) and same_text(out, LONG)
    for a, b in zip(lines, lines[1:]):                              # greedy: the next word never fitted
        assert len(a) + 1 + len(b.split()[0]) > mdwrap.WIDTH


def test_bullets_keep_their_indentation_and_code_is_never_broken():
    code = "`" + "x" * 30 + " y " + "z" * 30 + "`"
    out = mdwrap.tidy("- " + LONG + " " + code + " end\n")
    lines = out.rstrip("\n").split("\n")
    assert lines[0].startswith("- ") and all(line.startswith("  ") for line in lines[1:])
    assert code in out


def test_block_starts_tables_code_and_headings_are_kept():
    src = ("Intro.\n**Statement.** Short.\n(i) First part.\n(ii) Second part.\n*Notes.* A run-in.\n- an item\n\n"
           "# Heading\n| a | b |\n|---|---|\n\n```\nshort\nlines\n```\n1. one\n2. two\n")
    assert mdwrap.tidy(src) == src


def test_whitespace_is_cleaned():
    assert mdwrap.tidy("a  \n\n\n\nb") == "a\n\nb\n"
    assert mdwrap.tidy("c\n\n\nd\n\n") == "c\n\nd\n"


def test_check_mode_reports_without_writing(tmp_path):
    p = tmp_path / "x.md"
    p.write_text("A line that\nbroke.\n")
    assert mdwrap.main(["--check", str(p)]) == 1 and p.read_text() == "A line that\nbroke.\n"
    assert mdwrap.main([str(p)]) == 0 and mdwrap.main(["--check", str(p)]) == 0


def test_hashed_records_are_not_sources():
    names = {p.relative_to(mdwrap.ROOT).as_posix() for p in mdwrap.sources()}
    assert "CORE.md" in names and "REFERENCES.md" not in names
    assert not any(re.match(r"cases/[^/]+/", n) or n.startswith("obsidian/") for n in names)


def test_the_repository_is_wrapped():
    """Every Markdown source is as the tool would leave it: run `python3 tools/mdwrap.py` to fix."""
    unwrapped = [str(p) for p in mdwrap.sources() if mdwrap.tidy(text := p.read_text(encoding="utf-8")) != text]
    assert unwrapped == []
