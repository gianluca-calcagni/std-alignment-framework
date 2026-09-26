"""
tools/vaultlib.py — shared code for the Obsidian vault (v7.0).

This module does three things:
- names every note from its canonical id;
- parses references in text: the logical references used for dependency tracking, and the navigation
  references used for links;
- converts references to wiki-links, with an exact inverse. The inverse is what lets a migration or an edit
  be checked for loss.

Used by tools/build_vault.py (the one-time migration from the v6.6 flat files) and by tools/vault.py (lint,
sync, compile).
"""
import re

# ---------------------------------------------------------------- canonical ids and note names
KIND_SHORT = {'Definition': 'Def', 'Theorem': 'Thm', 'Proposition': 'Prop', 'Corollary': 'Cor', 'Lemma': 'Lemma',
              'Remark': 'Rem', 'Overview': 'Overview'}
KIND_TYPE = {'Def': 'definition', 'Thm': 'theorem', 'Prop': 'proposition', 'Cor': 'corollary', 'Lemma': 'lemma',
             'Rem': 'remark', 'Overview': 'overview'}
ITEM_HEAD = re.compile(r'^\*\*(Definition|Theorem|Proposition|Corollary|Lemma|Remark|Overview) (B?\d+(?:\.\d+)?)[ *(.]', re.M)
B_PROPS = {'4', '6', '7', '11', '12', '13'}           # dictionary entries that carry a numbered proposition "Prop. Bk"

def item_id(short, num):
    """canonical id = note name: 'Thm 13', 'Cor 1.1', 'Def 10', 'Rem 13.5'; dictionary props map to their entry note"""
    if num.startswith('B'):
        return f"B{int(num[1:]):02d}"
    return f"{short} {num}"

# ---------------------------------------------------------------- logical references (dependencies)
REF = re.compile(r'\b(Thms?|Theorem|Props?\.?|Proposition|Cors?\.?|Corollary|Lemma|Defs?\.?|Definition|Remarks?|Rems?\.?)\s+'
                 r'((?:B?\d+(?:\.\d+)?(?:\([a-z]+\)(?:[–-]\([a-z]+\))?)?(?:\s*(?:,|and|–|-)\s*)?)+)')
NORM = {'Thm': 'Thm', 'Thms': 'Thm', 'Theorem': 'Thm', 'Prop.': 'Prop', 'Props': 'Prop', 'Props.': 'Prop', 'Prop': 'Prop',
        'Proposition': 'Prop', 'Cor.': 'Cor', 'Cors': 'Cor', 'Cor': 'Cor', 'Cors.': 'Cor', 'Corollary': 'Cor', 'Lemma': 'Lemma',
        'Def.': 'Def', 'Defs': 'Def', 'Def': 'Def', 'Defs.': 'Def', 'Definition': 'Def', 'Remark': 'Rem', 'Remarks': 'Rem',
        'Rem.': 'Rem', 'Rem': 'Rem', 'Rems': 'Rem', 'Rems.': 'Rem'}
BREF = re.compile(r'(?<![\w/])B(4|6|7|11|12|13)(?:\([a-e]+\)|\((?:i|ii|iii|iv)\))?(?![\w])')

def _expand(kind, numpart):
    nums = re.findall(r'B?\d+(?:\.\d+)?', numpart)
    for a, b in re.findall(r'(B?\d+(?:\.\d+)?)\s*[–-]\s*(B?\d+(?:\.\d+)?)', numpart):
        if '.' in a and '.' in b and a.split('.')[0] == b.split('.')[0]:
            nums += [f"{a.split('.')[0]}.{i}" for i in range(int(a.split('.')[1]), int(b.split('.')[1]) + 1)]
        elif a.isdigit() and b.isdigit() and int(b) - int(a) < 40:
            nums += [str(i) for i in range(int(a), int(b) + 1)]
    out = []
    for n in dict.fromkeys(nums):
        out.append(item_id(kind, n))
    return out

def logical_refs(text):
    """canonical ids of numbered items referenced in text (ranges expanded); text may contain wiki-links"""
    t = re.sub(r'`[^`\n]*`', ' ', unlink(text))       # code spans never carry logical references
    r = []
    for m in REF.finditer(t):
        r += _expand(NORM.get(m.group(1), m.group(1)), m.group(2))
    for m in BREF.finditer(t):
        r.append(f"B{int(m.group(1)):02d}")
    return list(dict.fromkeys(r))

# ---------------------------------------------------------------- link conversion (with an exact inverse)
FILE_NOTES = {  # flat file -> (note name, display)
    'A_core.md': ('Core index', 'Core'), 'B_dictionary.md': ('Dictionary index', 'Dictionary'),
    'C_boundary.md': ('Boundary index', 'Boundary'), 'D_status.md': ('Status index', 'Status'),
    'E_census.md': ('Census', 'Census'), 'F_method.md': ('Method', 'Method'), 'ROADMAP.md': ('ROADMAP', 'ROADMAP'),
    'NOTES_claude.md': ('NOTES_claude', 'NOTES_claude'), 'REFERENCES.md': ('Sources index', 'References'),
    'T1_census_routing.md': ('T1_census_routing', 'T1_census_routing'), 'T1_preregistration.md': ('T1_preregistration', 'T1_preregistration'),
    'T1_RULES_FROZEN.md': ('T1_RULES_FROZEN', 'T1_RULES_FROZEN'), 'R3_FIX_LOG.md': ('R3_FIX_LOG', 'R3_FIX_LOG'),
    'R4_LOG.md': ('R4_LOG', 'R4_LOG'), 'R5_LOG.md': ('R5_LOG', 'R5_LOG'), 'R6_LOG.md': ('R6_LOG', 'R6_LOG'),
    'MSG_1_findings.md': ('MSG_1_findings', 'MSG_1_findings'), 'MSG_2_steering.md': ('MSG_2_steering', 'MSG_2_steering'),
    'MESSAGE_to_previous_executor.md': ('MESSAGE_to_previous_executor', 'MESSAGE_to_previous_executor'),
    'README.md': ('00 Home', 'Home'),
}
SECTION_NOTES = {}   # filled by the builder: ('B', '4') -> 'B04', ('C', '3') -> 'Boundary 03 ...', ('D','2') -> ..., ('A','9') -> ...

def _link(target, display):
    return f"[[{target}|{display}]]" if display != target else f"[[{target}]]"

def _file_rules():
    """ordered (pattern, replacement-function) pairs; each pattern consumes a backticked file name"""
    rules = []
    def sec(letter):
        def f(m):
            n = m.group(1); sub = m.group(2) or ''
            tgt = SECTION_NOTES.get((letter, n))
            disp = {'B': f"B §{n}{sub}", 'C': f"Boundary §{n}{sub}", 'D': f"Status §{n}{sub}", 'A': f"Core §{n}{sub}",
                    'T': f"T1 routing §{n}{sub}", 'R': f"ROADMAP §{n}{sub}", 'F': f"T1 rules §{n}{sub}"}[letter]
            return _link(tgt, disp) if tgt else m.group(0)
        return f
    rules.append((re.compile(r'`B_dictionary\.md`\s*§\s*(\d+)((?:\([a-e]\))?)'), sec('B')))
    rules.append((re.compile(r'`C_boundary\.md`\s*§\s*(\d+)((?:\.\d+)?)'), sec('C')))
    rules.append((re.compile(r'`D_status\.md`\s*§\s*(\d+)((?:\.\d+)?)'), sec('D')))
    rules.append((re.compile(r'`A_core\.md`\s*§\s*(\d+)((?:\.\d+)?)'), sec('A')))
    rules.append((re.compile(r'`B_dictionary\.md`\s*B(\d+)((?:\((?:[a-e]|i|ii|iii|iv)(?:[–-](?:[a-e]|i|ii|iii|iv))?\))?)'),
                  lambda m: _link(f"B{int(m.group(1)):02d}", f"B{m.group(1)}{m.group(2)}")))
    rules.append((re.compile(r'`C_boundary\.md`\s*C(\d+)'), lambda m: _link(f"C{int(m.group(1)):02d}", f"C{m.group(1)}")))
    def rows(m):
        a = int(m.group(2)); b = m.group(3)
        if b:
            return f"rows {_link(f'R{a:03d}', str(a))}–{_link(f'R{int(b):03d}', b)}"
        return _link(f"R{a:03d}", f"row {a}")
    rules.append((re.compile(r'`D_status\.md`\s*(rows?)\s*(\d+)(?:\s*[–-]\s*(\d+))?'), rows))
    rules.append((re.compile(r'`final_audit\.py`\s*F(\d)'), lambda m: _link(f"F{m.group(1)}", f"F{m.group(1)}")))
    rules.append((re.compile(r'`V(\d+)`'), lambda m: _link(f"V{int(m.group(1)):02d}", f"V{m.group(1)}")))
    rules.append((re.compile(r'`(W[1-5])`'), lambda m: _link(m.group(1), m.group(1))))
    for fname, (note, disp) in FILE_NOTES.items():
        rules.append((re.compile(r'`' + re.escape(fname) + r'`'), (lambda n, d: (lambda m: _link(n, d)))(note, disp)))
    return rules

D_ROW = re.compile(r'(?<![\w\[|])\bD (rows?) (\d+)(?:[–-](\d+))?\b')

def _outside(text, fn):
    """apply fn to the parts of text outside code spans and existing wiki-links"""
    parts = re.split(r'(`[^`\n]*`|\[\[[^\]]*\]\])', text)
    return ''.join(p if (p.startswith('`') or p.startswith('[[')) else fn(p) for p in parts)

def linkify(text, self_id=None, known=None, d_rows=False):
    """convert references in text to wiki-links. unlink(linkify(t)) == display_rewrite(t) exactly."""
    for pat, fn in _file_rules():
        text = pat.sub(fn, text)
    def refs(seg):
        def one(m):
            kind = NORM.get(m.group(1), m.group(1))
            prefix = m.group(0)[:m.start(2) - m.start(0)]
            def num(mm):
                n = mm.group(0); tgt = item_id(kind, n)
                if tgt == self_id or (known is not None and tgt not in known):
                    return n
                return _link(tgt, n)
            return prefix + re.sub(r'B?\d+(?:\.\d+)?', num, m.group(2))
        seg = REF.sub(one, seg)
        def bref(m):
            tgt = f"B{int(m.group(1)):02d}"
            if tgt == self_id or (known is not None and tgt not in known):
                return m.group(0)
            return _link(tgt, m.group(0))
        seg = _outside(seg, lambda s: BREF.sub(bref, s))
        if d_rows:
            def drow(m):
                a = int(m.group(2)); b = m.group(3)
                if b:
                    return f"D {m.group(1)} {_link(f'R{a:03d}', str(a))}–{_link(f'R{int(b):03d}', b)}"
                return f"D {m.group(1)} {_link(f'R{a:03d}', str(a))}"
            seg = D_ROW.sub(drow, seg)
        return seg
    return escape_table_links(_outside(text, refs))

def _table_row(l):
    """escape every pipe in a table row that must not split a cell: the alias pipe of a wiki-link, and any pipe
    inside a code span (GFM and Obsidian split cells on those unless they are written as \\|)"""
    out = []; i = 0; code = None; link = False
    while i < len(l):
        c = l[i]
        if c == '\\' and i + 1 < len(l): out.append(l[i:i + 2]); i += 2; continue
        if c == '`':
            j = i
            while j < len(l) and l[j] == '`': j += 1
            run = j - i
            if code is None:
                if not link and re.search(r'(?<!`)' + '`' * run + r'(?!`)', l[j:]): code = run
            elif run == code: code = None
            out.append(l[i:j]); i = j; continue
        if code is None and l.startswith('[[', i): link = True; out.append('[['); i += 2; continue
        if code is None and link and l.startswith(']]', i): link = False; out.append(']]'); i += 2; continue
        if c == '|' and (code is not None or link): out.append('\\|'); i += 1; continue
        out.append(c); i += 1
    return ''.join(out)

def table_blocks(text):
    """yield (first line index, [lines]) for each markdown table outside fenced code"""
    lines = text.split('\n'); fence = False; cur = []; start = 0
    for i, l in enumerate(lines + ['']):
        if l.lstrip().startswith('```'):
            fence = not fence
            if cur: yield start, cur
            cur = []; continue
        if not fence and l.lstrip().startswith('|'):
            if not cur: start = i
            cur.append(l)
        else:
            if cur: yield start, cur
            cur = []

def normalize_tables(text):
    """R7-4: the one table rule, applied by sync to every note (derived, so lint catches hand edits that break it)"""
    lines = text.split('\n'); fence = False
    for i, l in enumerate(lines):
        if l.lstrip().startswith('```'): fence = not fence; continue
        if not fence and l.lstrip().startswith('|'): lines[i] = _table_row(l)
    return '\n'.join(lines)
escape_table_links = normalize_tables     # the v7.0 name; it was defined but never applied

def table_cells(row):
    """number of cells in a table row, splitting on unescaped pipes only"""
    r = row.strip()
    if r.startswith('|'): r = r[1:]
    if r.endswith('|') and not r.endswith('\\|'): r = r[:-1]
    return len(re.split(r'(?<!\\)\|', r))

def display_rewrite(text, d_rows=False):
    """what the text reads as after linkify, with links removed — used by the lossless check"""
    return unlink(linkify(text, d_rows=d_rows))

LINK = re.compile(r'!?\[\[([^\]|#\\]+)(?:#[^\]|]*)?(?:\\?\|([^\]]*))?\]\]')

def unlink(text):
    return LINK.sub(lambda m: m.group(2) if m.group(2) is not None else m.group(1), text)

def link_targets(text):
    t = re.sub(r'`[^`\n]*`', ' ', text)          # links inside code spans are examples, not links
    return [m.group(1).strip() for m in LINK.finditer(t)]
