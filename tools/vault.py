"""
tools/vault.py — maintain the Obsidian vault (v7.0). The vault is the source of truth.

  python3 tools/vault.py sync                   recompute every derived field and generated section (idempotent)
  python3 tools/vault.py lint                   check schema, links, DAG, definition order, tags, checks, sources
  python3 tools/vault.py compile                write linear views to build/ (core.md, dictionary.md, boundary.md, status.md)
  python3 tools/vault.py compile --check DIR    also compare the live vault with the flat files in DIR (differences = later edits)
  python3 tools/vault.py migration-check        re-prove the one-time migration: a fresh build from archive/v6.6_flat must reproduce it
  python3 tools/vault.py deps "Thm 13"          direct and transitive dependencies and dependents of a note
  python3 tools/vault.py scan A3                every item whose statement or proof matches an assumption pattern

Derived fields are never edited by hand:
- depends_on: logical references in the Statement and Proof sections;
- mentions: every other reference in the note;
- checks, assumes, tier, status;
- verifies, cited_by and affects on checks, sources and retractions.

`sync` writes them, and `lint` fails if they are stale. Generated regions sit between `<!-- gen:... -->`
markers and are rewritten by sync.
"""
import re, os, sys, json, glob, collections
sys.path.insert(0, os.path.dirname(__file__))
import vaultlib as V

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
VAULT = ROOT
ITEM_TYPES = set(V.KIND_TYPE.values())
REQUIRED = {  # type -> required frontmatter keys
    **{t: ['id', 'type', 'title', 'section', 'order', 'tier', 'assumes', 'status', 'depends_on', 'mentions', 'checks', 'sources', 'aliases', 'updated'] for t in ITEM_TYPES},
    'dictionary-entry': ['id', 'type', 'title', 'layer', 'order', 'depends_on', 'mentions', 'checks', 'sources', 'aliases', 'updated'],
    'attack-surface': ['id', 'type', 'title', 'order', 'depends_on', 'mentions', 'checks', 'aliases', 'updated'],
    'check': ['id', 'type', 'script', 'verifies', 'last_run', 'updated'],
    'source': ['id', 'type', 'status_code', 'where', 'cited_by', 'external', 'bibkey', 'updated'],
    'retraction': ['id', 'type', 'number', 'found_by', 'affects', 'updated'],
    'hypothesis': ['id', 'type', 'title', 'defined_in', 'assumed_by', 'updated'],
    'section': ['id', 'type', 'order', 'updated'], 'index': ['id', 'type', 'updated'],
    'census': ['id', 'type', 'updated'], 'method': ['id', 'type', 'updated'], 'project': ['id', 'type', 'updated'],
    'working-notes': ['id', 'type', 'updated'], 'report': ['id', 'type', 'updated'], 'log': ['id', 'type', 'updated'],
    'home': ['id', 'type', 'updated'], 'template': ['type'],
}
ALLOW_FORWARD = {('Rem 7.1', 'Prop 10'): 'historical remark that restates a later result; not used by it'}
NOT_E = {'Prop 24': 'p̂ = p_{F,t} is a test case on the intended family, not a hypothesis about the actor',
         'Prop 25': 'part (c) states its entropic attribution explicitly',
         'Prop 33': 'p̂ = p_{F,t} is a test case on the intended (capped) segment, not a hypothesis about the actor',
         'Prop 35': 'p̂ = p_{F,t} is a test case on the intended segment, not a hypothesis about the actor'}
EPAT = r'p̂ ∝|p_\{F̂,|R_J\(E|p̂ = p_\{F|p_\{F\+E|p_\{sF̂'
TAGRX = r'\[Assumes|\*\[\(g1\)|assumes \(E\)|assume \(E_A\)'
QAPAT = r'q_A'
# R7-3: symbols are dependencies too. A statement or proof that uses a defined symbol depends on the note that
# defines it, whether or not it cites that note. Hand-maintained: add a row when a definition introduces a symbol.
SYMBOLS = [(r'F̂', 'Def 13'), (r'Λ\(|Λ_q', 'Def 13'), (r'q_A', 'Def 13'),
           (r'C_δ', 'Def 5'), (r'p\^C', 'Def 5'), (r'R\^C', 'Def 15'),
           (r'J_F|J_G|J_\{', 'Def 2'), (r'R_J', 'Def 3'), (r'ΔF', 'Def 3'),
           (r'M_budget|M_free|M_price|D_⊥|𝓡⁺', 'Def 10'), (r'σ_δ\(|w_δ\(', 'Def 6'),
           (r'ρ_ev|ρ_dep', 'Def 9'), (r'M_own|R_own', 'Def 14'), (r'D_∥|X_anti', 'Thm 13'),
           (r'W_c|m_c|s_c\(', 'Def 16'), (r'κ_c', 'Prop 27'),
           (r'𝒯|\[F\]_ord|M_ord|(?<!\^)C_F|I_free|I_budget', 'Def 17'),
           (r'p\^max|\^cap|𝓡⁺_F\(', 'Def 18'), (r'M_𝓘|𝓘', 'Def 19'), (r'p\^min|\^seg', 'Def 20'),
           (r'M\^𝒢|p̂_𝒢|q_𝒢', 'Def 21')]
# R7-3: explanation vocabulary, forbidden in the Statement and Proof of measurement-layer items
EXPL_VOCAB = r'W_c|m_c|κ_c|F̂|(?<![\w_(\[])E(?![\w_\[(|)])|E₀|Ē|Λ\(|Λ_q|q_A|\[Assumes|R\^C|M_own|R_own|σ_δ\(|w_δ\('                     # R7-2: statements that use the actor's own reference must assume (E_A) or be definitions

# ---------------------------------------------------------------- IO
def parse_fm(txt):
    if not txt.startswith('---\n'): return {}, txt
    end = txt.index('\n---\n', 4); fm = {}
    for line in txt[4:end].split('\n'):
        if not line.strip() or ':' not in line: continue
        k, v = line.split(':', 1); v = v.strip()
        if v == '': fm[k.strip()] = None; continue
        try: fm[k.strip()] = json.loads(v)
        except Exception:
            fm[k.strip()] = [x.strip().strip('"\'') for x in v[1:-1].split(',') if x.strip()] if v.startswith('[') else v
    return fm, txt[end + 5:]
def dump_fm(fm):
    out = ['---']
    for k, v in fm.items():
        if v is None: out.append(f"{k}:")
        elif isinstance(v, bool): out.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, list): out.append(f"{k}: [" + ', '.join(json.dumps(x, ensure_ascii=False) for x in v) + "]")
        elif isinstance(v, (int, float)): out.append(f"{k}: {v}")
        else: out.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    return '\n'.join(out + ['---', ''])
def load_state():
    st = json.load(open(VAULT + 'tools/vault_state.json', encoding='utf-8'))
    V.SECTION_NOTES.clear()
    V.SECTION_NOTES.update({tuple(k.split('|')): v for k, v in st['section_notes'].items()})
    return st
def load():
    load_state(); notes = {}
    for p in glob.glob(VAULT + '**/*.md', recursive=True):
        rel = os.path.relpath(p, VAULT)
        if rel.startswith(('reviews/', 'build/', 'archive/', 'tools/', 't1/', '_templates/')) or rel == 'README.md': continue
        fm, body = parse_fm(open(p, encoding='utf-8').read())
        name = os.path.basename(p)[:-3]
        if name in notes: raise SystemExit(f"duplicate note name: {name} ({rel} and {notes[name]['path']})")
        notes[name] = {'path': rel, 'fm': fm, 'body': body}
    return notes
def save(n):
    open(VAULT + n['path'], 'w', encoding='utf-8').write(dump_fm(n['fm']) + n['body'])

# ---------------------------------------------------------------- note anatomy
def section(body, heading):
    m = re.search(r'^## ' + re.escape(heading) + r'\s*\n(.*?)(?=^## |^<!-- gen:links -->|\Z)', body, re.M | re.S)
    return m.group(1) if m else ''
def strip_gen(body):
    return re.sub(r'<!-- gen:(\w+) -->.*?<!-- /gen:\1 -->\n?', '', body, flags=re.S)
def logic_text(name, n):
    t = n['fm'].get('type')
    if t in ITEM_TYPES: return section(n['body'], 'Statement') + '\n' + section(n['body'], 'Proof')
    if t in ('dictionary-entry', 'attack-surface'): return strip_gen(n['body'])
    return ''
def all_text(n): return strip_gen(n['body'])

# ---------------------------------------------------------------- derived fields
def live_tier_table(notes):
    """R7-2: tiers come from the live table in 'Core A3 Assumption tiers', not from the migration snapshot.
    A result cell may split into '(E): …', '(E_A): …', '(C): …' segments."""
    n = notes.get('Core A3 Assumption tiers'); out = {}
    if not n: return out
    for row in re.findall(r'^\| \*\*([^*|]+)\*\* \|[^\n]*?\|([^\n]*)\|\s*$', V.unlink(n['body']), re.M):
        tier, cell = row[0].strip(), row[1]
        segs = re.split(r'(\((?:E|E_A|E_R|C)\):)', cell)
        cur = tier
        for seg in segs:
            m = re.match(r'\((E|E_A|E_R|C)\):', seg)
            if m: cur = f"{tier} ({m.group(1)})"; continue
            for iid in V.logical_refs(seg):
                out.setdefault(iid, [])
                if cur not in out[iid]: out[iid].append(cur)
    return out

def derive(notes, state):
    items = {k for k, n in notes.items() if n['fm'].get('type') in ITEM_TYPES | {'dictionary-entry'}}
    live_tiers = live_tier_table(notes)
    D = {}
    src_where = {k: n['fm'].get('where') or '' for k, n in notes.items() if n['fm'].get('type') == 'source'}
    cited = collections.defaultdict(list)
    for s, w in src_where.items():
        for tgt in where_targets(w, notes):
            cited[tgt].append(s)
    for k, n in notes.items():
        t = n['fm'].get('type'); d = {}
        txt = all_text(n)
        links = [x for x in V.link_targets(txt) if x in notes]
        if t in ITEM_TYPES | {'dictionary-entry', 'attack-surface'}:
            lt = logic_text(k, n)
            dep = [x for x in V.logical_refs(lt) if x in items and x != k] if t != 'overview' else []
            if t != 'overview':
                for rx, owner in SYMBOLS:
                    if owner != k and owner in items and owner not in dep and re.search(rx, lt): dep.append(owner)
            d['depends_on'] = dep
            d['mentions'] = sorted({x for x in V.logical_refs(txt) + links if x in notes and x != k and x not in dep and not x.startswith(('V', 'F', 'W')) or False} - set(dep) - {k} - {x for x in links if re.match(r'^(V\d\d|F\d|W\d)$', x)})
            d['checks'] = sorted({x for x in links if re.match(r'^(V\d\d|F\d|W\d)$', x)})
            if t in ITEM_TYPES or t == 'dictionary-entry':
                d['sources'] = sorted(set(cited.get(k, [])))
        if t in ITEM_TYPES:
            stmt = section(n['body'], 'Statement') + section(n['body'], 'Proof')
            a = []
            if t in ('definition', 'overview'): stmt = ''      # definitions state conventions and hypotheses; they assume none
            if re.search(r'\[Assumes \(E\)|\[Assumes \(E\),|assumes \(E\)|\*\[\(g1\)–\(g3\) assume \(E\)', stmt): a.append('Hyp E')
            if re.search(r'\[Assumes \(E_A\)|assumes? \(E_A\)', stmt): a.append('Hyp E_A')
            if re.search(r'\[Assumes \(E_R\)', stmt): a.append('Hyp E_R')
            if re.search(r'\[Assumes \(C\)', stmt): a.append('Hyp C')
            d['assumes'] = a
            tl = list(live_tiers.get(k, []))
            for hyp, lab in (('Hyp E', '4 (E)'), ('Hyp E_A', '4 (E_A)'), ('Hyp E_R', '4 (E_R)'), ('Hyp C', '4 (C)')):
                if hyp in a and lab not in tl and not any(x.startswith('4') for x in tl): tl.append(lab)
            d['tier'] = tl
            if t == 'definition' or t == 'overview': d['status'] = 'definition'
            elif 'historical' in (n['fm'].get('title') or '').lower(): d['status'] = 'historical'
            elif section(n['body'], 'Proof').strip(): d['status'] = 'proved'
            elif t == 'remark': d['status'] = 'remark'
            else: d['status'] = 'stated'
        if t == 'retraction':
            d['affects'] = sorted({x for x in V.logical_refs(txt) + links if x in items or re.match(r'^C\d\d$', x)})
        D[k] = d
    # reverse maps
    used_by = collections.defaultdict(list); mentioned = collections.defaultdict(list); verified = collections.defaultdict(list)
    retr = collections.defaultdict(list); assumed = collections.defaultdict(list)
    for k, d in D.items():
        for x in d.get('depends_on', []): used_by[x].append(k)
        for x in d.get('mentions', []): mentioned[x].append(k)
        for x in d.get('checks', []): verified[x].append(k)
        for x in d.get('affects', []): retr[x].append(k)
        for x in d.get('assumes', []): assumed[x].append(k)
    for k, n in notes.items():
        t = n['fm'].get('type')
        if t == 'check': D[k]['verifies'] = sorted(verified.get(k, []), key=sortkey)
        if t == 'source': D[k]['cited_by'] = sorted(where_targets(n['fm'].get('where') or '', notes), key=sortkey)
        if t == 'hypothesis': D[k]['assumed_by'] = sorted(assumed.get(k, []), key=sortkey)
    return D, used_by, mentioned, retr
def where_targets(w, notes):
    """parse a REFERENCES 'Where' or role cell, e.g. 'A Props 6, 7, 10; B §2; C14; MSG' or free text with references"""
    out = [x for x in V.link_targets(w) if x in notes]; txt = V.unlink(w)      # v7.3.1: explicit links count too
    out += [x for x in V.logical_refs(txt) if x in notes]
    for m in re.finditer(r'\bB\s*§§?\s*(\d+)(?:\s*[–-]\s*(\d+))?|\bB(\d+)(?:\([a-e]\))?', txt):
        a = int(m.group(1) or m.group(3)); b = int(m.group(2) or a)
        out += [f"B{i:02d}" for i in range(a, b + 1) if f"B{i:02d}" in notes]
    for m in re.finditer(r'\bC\s*§§?\s*([\d.,\s]+)', txt):
        for n in re.findall(r'(\d+)(?:\.\d+)?', m.group(1)):
            k = V.SECTION_NOTES.get(('C', n))
            if k: out.append(k)
    for m in re.finditer(r'(?<![§\w])C(\d{1,2})\b', txt):
        k = f"C{int(m.group(1)):02d}"
        if k in notes: out.append(k)
    for m in re.finditer(r'\bA\s*§\s*(\d+)', txt):
        k = V.SECTION_NOTES.get(('A', m.group(1)))
        if k: out.append(k)
    if 'MSG' in txt: out.append('MESSAGE_to_previous_executor')
    if 'NOTES' in txt: out.append('NOTES_claude')
    if 'census' in txt.lower(): out.append('Census')
    return [x for x in dict.fromkeys(out) if x in notes]

def sortkey(x):
    m = re.match(r'([A-Za-z ]+?)\s*(\d+)(?:\.(\d+))?', x)
    return (m.group(1), int(m.group(2)), int(m.group(3) or 0)) if m else (x, 0, 0)

# ---------------------------------------------------------------- generated regions
def title_of(notes, x):
    n = notes.get(x)
    if not n: return ''
    t = n['fm'].get('title') or ''
    return f" — {t}" if t else ''
def gen_region(body, tag, content):
    rx = re.compile(r'<!-- gen:' + tag + r' -->.*?<!-- /gen:' + tag + r' -->', re.S)
    block = f"<!-- gen:{tag} -->\n{content}<!-- /gen:{tag} -->"
    return rx.sub(lambda m: block, body) if rx.search(body) else body
def sync(write=True):
    notes = load(); state = json.load(open(VAULT + 'tools/vault_state.json'))
    D, used_by, mentioned, retr = derive(notes, state); changed = []
    for k, n in notes.items():
        old = dump_fm(n['fm']) + n['body']
        fm = dict(n['fm']); fm.update(D.get(k, {}))
        t = fm.get('type'); body = n['body']
        lk = lambda xs: ''.join(f"- [[{x}]]{title_of(notes, x)}\n" for x in sorted(xs, key=sortkey)) or "- none\n"
        if t in ITEM_TYPES | {'dictionary-entry', 'attack-surface', 'retraction', 'check', 'source', 'hypothesis'}:
            hdr = {'check': f"> [!check] Check · `{fm.get('script')}` · verifies {len(fm.get('verifies', []))} notes\n",
                   'source': f"> [!quote] Source · status {fm.get('status_code')} · cited by {len(fm.get('cited_by', []))} notes\n",
                   'retraction': f"> [!warning] Retraction {fm.get('number')} · found by {fm.get('found_by')}\n",
                   'hypothesis': f"> [!important] Hypothesis about the actual actor · assumed by {len(fm.get('assumed_by', []))} results\n"}.get(t)
            if hdr is None:
                bits = [t.replace('-', ' ').capitalize()]
                if fm.get('tier'): bits.append('tier ' + ' / '.join(fm['tier']) if isinstance(fm['tier'], list) else f"tier {fm['tier']}")
                if fm.get('assumes'): bits.append('assumes ' + ', '.join(f"[[{a}]]" for a in fm['assumes']))
                if fm.get('status'): bits.append(fm['status'])
                if fm.get('section'): bits.append(f"in [[{fm['section']}]]")
                hdr = f"> [!abstract] {' · '.join(bits)}\n"
            body = gen_region(body, 'header', hdr)
            L = []
            if t in ITEM_TYPES | {'dictionary-entry', 'attack-surface'}:
                L += ["## Depends on (logical: statement and proof)\n", lk(fm.get('depends_on', [])),
                      "\n## Used by\n", lk(used_by.get(k, [])),
                      "\n## Mentions\n", lk(fm.get('mentions', [])),
                      "\n## Mentioned in\n", lk([x for x in mentioned.get(k, []) if x not in used_by.get(k, [])]),
                      "\n## Checks\n", lk(fm.get('checks', [])),
                      "\n## Sources\n", lk(fm.get('sources', [])) if t != 'attack-surface' else "- see the linked results\n",
                      "\n## Retractions touching this note\n", lk(retr.get(k, []))]
            elif t == 'check': L += ["## Verifies\n", lk(fm.get('verifies', []))]
            elif t == 'source': L += ["## Cited by\n", lk(fm.get('cited_by', []))]
            elif t == 'retraction': L += ["## Affects\n", lk(fm.get('affects', []))]
            elif t == 'hypothesis': L += ["## Assumed by\n", lk(fm.get('assumed_by', []))]
            body = gen_region(body, 'links', ''.join(L))
        if k == 'Status 02 Retraction history':
            rows = sorted([x for x in notes if notes[x]['fm'].get('type') == 'retraction'], key=lambda x: notes[x]['fm']['number'])
            tbl = "| # | Retracted | Replaced by | Found by |\n|---|---|---|---|\n" + ''.join(
                f"| [[{r}\\|{notes[r]['fm']['number']}]] | {cell(notes[r]['body'], 'Retracted')} | {cell(notes[r]['body'], 'Replaced by')} | {cell(notes[r]['body'], 'Found by')} |\n" for r in rows)
            body = gen_region(body, 'retractions', tbl)
        if k == 'Sources index':
            def srcblock(m):
                names = re.findall(r'<!-- src:(.*?) -->', m.group(0))
                lst = ''.join(f"- [[{s}]] — {notes[s]['fm'].get('where')} · status {notes[s]['fm'].get('status_code')}\n" for s in names)
                return m.group(0).split('<!-- gen:srclist -->')[0].rstrip('\n') + f"\n<!-- gen:srclist -->\n{lst}<!-- /gen:srclist -->\n"
            body = re.sub(r'(?:<!-- srctable:.*? -->\n)?(?:<!-- src:.*? -->\n)+(?:<!-- gen:srclist -->.*?<!-- /gen:srclist -->\n)?', srcblock, body, flags=re.S)
        if t in ('index', 'home') and fm.get('index_of'):
            body = gen_region(body, 'index', index_content(notes, fm['index_of'], used_by))
        if not fm.get('frozen'): body = V.normalize_tables(body)     # R7-4: table pipes (see vaultlib.normalize_tables)
        n['fm'] = fm; n['body'] = body
        if dump_fm(fm) + body != old:
            changed.append(k)
            if write: save(n)
    if 'Sources index' in notes:                                   # v7.3.1: the bibliography's order is derived
        cb = canonical_bib(notes)
        if cb != open(VAULT + 'references.bib', encoding='utf-8').read():
            changed.append('references.bib')
            if write: open(VAULT + 'references.bib', 'w', encoding='utf-8').write(cb)
    return changed
BIB_HEADER = """% references.bib — the bibliography of every source note in `50 Sources/` (Parts A and B of the Sources index).
% Entry text is edited here by hand. Their ORDER is generated: `tools/vault.py sync` sorts the entries into the
% sections of the Sources index. Each source note names its entries in the frontmatter field `bibkey`, and
% `lint` requires a one-to-one match between notes and entries.
% note={check ...} marks status U: some detail should be checked before publication.
% Census attributions (Part C, status C) are not here: they are short attributions with no checked details.
% They are listed in `50 Sources/Sources census attributions.md`, and each needs a full reference before use.
"""
def bib_entries():
    p = VAULT + 'references.bib'
    lines = open(p, encoding='utf-8').read().split('\n') if os.path.exists(p) else []
    return {re.match(r'@\w+\{([^,]+),', l).group(1): l for l in lines if l.startswith('@')}
def canonical_bib(notes):
    E = bib_entries(); out = [BIB_HEADER]; used = set()
    sec = None
    for l in notes['Sources index']['body'].split('\n'):
        h = re.match(r'^### (.+)$', l)
        if h: sec = V.unlink(h.group(1)).strip(); first = True; continue
        s = re.match(r'<!-- src:(.*?) -->', l)
        if s and s.group(1) in notes:
            if first: out.append(f"\n% ---------- {sec} ----------"); first = False
            for k in notes[s.group(1)]['fm'].get('bibkey', []):
                if k in E and k not in used: out.append(E[k]); used.add(k)
    rest = [k for k in E if k not in used]
    if rest: out.append("\n% ---------- not claimed by any source note (lint error) ----------"); out += [E[k] for k in rest]
    return '\n'.join(out) + '\n'
PLURAL = {'corollary': 'Corollaries'}
TYPE_ORDER = ['overview', 'definition', 'theorem', 'proposition', 'corollary', 'lemma', 'remark']
def index_content(notes, what, used_by):
    L = []
    def row(x):
        f = notes[x]['fm']; bits = []
        if f.get('tier'): bits.append('tier ' + '/'.join(f['tier']))
        if f.get('assumes'): bits.append('assumes ' + ', '.join(f['assumes']))
        if f.get('status'): bits.append(f['status'])
        return f"- [[{x}]]{title_of(notes, x)}" + (f"  · {' · '.join(bits)}" if bits else '') + "\n"
    def part(p): return sorted([k for k, n in notes.items() if n['fm'].get('part') == p and n['fm'].get('type') in ('section', 'dictionary-entry')],
                               key=lambda k: notes[k]['fm'].get('order', 0))
    if what == 'core':
        L.append("## Sections, in reading order\n"); L += [f"- [[{k}]]\n" for k in part('core')]
        L.append("\n## Hypotheses about the actual actor\n"); L += [row(k) for k in sorted(k for k, n in notes.items() if n['fm'].get('type') == 'hypothesis')]
        for lay, blurb in (('measurement', 'what misalignment is and how it is measured — the declared reference, the target, the conventions and the actual behaviour only'),
                           ('explanation', 'why behaviour departs — evaluators, errors, the actor\'s own reference, actor models')):
            ks = [k for k, n in notes.items() if n['fm'].get('type') in TYPE_ORDER and n['fm'].get('layer') == lay]
            L.append(f"\n## {lay.capitalize()} layer ({len(ks)} items)\n*{blurb}.*\n\n")
            for ty in TYPE_ORDER:
                kt = sorted([k for k in ks if notes[k]['fm'].get('type') == ty], key=sortkey)
                if kt: L.append(f"**{PLURAL.get(ty, ty.capitalize() + 's')} ({len(kt)})**\n"); L += [row(k) for k in kt]; L.append("\n")
    elif what in ('dictionary', 'boundary', 'status'):
        L.append("## Notes, in reading order\n")
        for k in part(what):
            L.append(f"- [[{k}]]{title_of(notes, k)}\n")
            if what == 'boundary' and k.startswith('Boundary 01'):
                L += [f"  - [[{c}]]{title_of(notes, c)}\n" for c in sorted([c for c, n in notes.items() if n['fm'].get('type') == 'attack-surface'], key=sortkey)]
        if what == 'status':
            rs = sorted([k for k, n in notes.items() if n['fm'].get('type') == 'retraction'], key=sortkey)
            L.append(f"\n## Retractions ({len(rs)})\nEach retraction is a note; the ledger table is generated in [[Status 02 Retraction history]].\n")
    elif what == 'checks':
        for pre, lab in (('V', 'verify.py'), ('F', 'final_audit.py'), ('W', 'verify_addendum.py')):
            ks = sorted([k for k, n in notes.items() if n['fm'].get('type') == 'check' and k.startswith(pre)], key=sortkey)
            L.append(f"\n## `{lab}` ({len(ks)})\n")
            L += [f"- [[{k}]] — verifies " + (', '.join(f"[[{x}]]" for x in notes[k]['fm'].get('verifies', [])[:8]) or 'nothing cited yet') + "\n" for k in ks]
    elif what == 'home':
        c = collections.Counter(n['fm'].get('type') for n in notes.values())
        L.append("| Type | Notes |\n|---|---|\n" + ''.join(f"| {t} | {c[t]} |\n" for t in sorted(c)))
    return ''.join(L)

def cell(body, heading):
    return section(body, heading).strip().replace('\n', ' ').replace('|', '\\|').replace('\\\\|', '\\|')

# ---------------------------------------------------------------- compile (linear views) and the lossless check
def item_text(n):
    b = strip_gen(n['body'])
    parts = [section(b, h).strip() for h in ('Statement', 'Proof', 'Notes and checks')]
    return '\n\n'.join(p for p in parts if p) + '\n'
def expand(notes, body):
    out, last = [], None
    for line in body.split('\n'):
        m = re.match(r'^!\[\[([^\]#|]+)(?:#[^\]]*)?\]\]\s*$', line)
        if m:
            if m.group(1) != last: out.append(item_or_entry(notes, m.group(1)).rstrip('\n') + '\n')
            last = m.group(1); continue
        last = None; out.append(line)
    return '\n'.join(out)
def item_or_entry(notes, k):
    n = notes[k]
    if n['fm'].get('type') in ITEM_TYPES: return item_text(n) + '\n'
    return strip_gen(n['body']).rstrip('\n') + '\n\n'
def compile_all(notes):
    part = lambda p: sorted([k for k, n in notes.items() if n['fm'].get('part') == p and n['fm'].get('type') in ('section', 'dictionary-entry', 'index')],
                            key=lambda k: notes[k]['fm'].get('order', 0))
    out = {}
    out['A_core.md'] = ''.join(expand(notes, strip_gen(notes[k]['body'])) for k in part('core'))
    out['B_dictionary.md'] = ''.join(strip_gen(notes[k]['body']) for k in part('dictionary'))
    out['C_boundary.md'] = ''.join(expand(notes, strip_gen(notes[k]['body'])) for k in part('boundary'))
    st = ''
    for k in part('status'):
        b = notes[k]['body']
        if k == 'Status 02 Retraction history':
            rows = sorted([x for x in notes if notes[x]['fm'].get('type') == 'retraction'], key=lambda x: notes[x]['fm']['number'])
            tbl = "| # | Retracted | Replaced by | Found by |\n|---|---|---|---|\n" + ''.join(
                f"| {notes[r]['fm']['number']} | {cell(notes[r]['body'], 'Retracted')} | {cell(notes[r]['body'], 'Replaced by')} | {cell(notes[r]['body'], 'Found by')} |\n" for r in rows)
            b = re.sub(r'<!-- gen:retractions -->.*?<!-- /gen:retractions -->\n?', lambda m: tbl, b, flags=re.S)
            b = b.replace("| # | Retracted | Replaced by | Found by |\n|---|---|---|---|\n| # |", "| # |")
        st += strip_gen(b)
    out['D_status.md'] = st
    ref = ''
    for k in sorted([k for k in notes if notes[k]['fm'].get('part') == 'sources'], key=lambda k: notes[k]['fm'].get('order', -1) if k != 'Sources index' else -1):
        b = strip_gen(notes[k]['body'])
        def rows(m):
            names = re.findall(r'<!-- src:(.*?) -->', m.group(0))
            hm = re.search(r'<!-- srctable:(.*?) -->', m.group(0))
            return (hm.group(1) if hm else "| Reference | Where | Status |") + "\n|---|---|---|\n" + ''.join(
                f"| {section(notes[s]['body'], 'Reference').strip()} | {section(notes[s]['body'], 'Where it is used, or its role (as recorded)').strip()} | {section(notes[s]['body'], 'Status of the bibliographic details').strip()} |\n" for s in names)
        ref += re.sub(r'(?:<!-- srctable:.*? -->\n)?(?:<!-- src:.*? -->\n)+', rows, b)
    out['REFERENCES.md'] = ref
    for k, n in notes.items():
        if n['fm'].get('source_file'): out[n['fm']['source_file']] = strip_gen(n['body'])
    return {f: V.unlink(t) for f, t in out.items()}
def norm(t):
    """compare token streams: the vault stores statement, proof and notes as separate sections, so line breaks and
    blank lines between them may differ from the flat file; every non-whitespace character must match in order"""
    return re.sub(r'\s+', ' ', t.replace('\r', '')).strip()
def compile_cmd(check_dir=None):
    notes = load(); outs = compile_all(notes); os.makedirs(VAULT + 'build', exist_ok=True)
    names = {'A_core.md': 'core.md', 'B_dictionary.md': 'dictionary.md', 'C_boundary.md': 'boundary.md', 'D_status.md': 'status.md', 'REFERENCES.md': 'references.md'}
    for f, t in outs.items():
        if f in names: open(VAULT + 'build/' + names[f], 'w', encoding='utf-8').write(t)
    print(f"compiled {len(names)} linear views into build/")
    if check_dir:
        bad = 0
        for f, t in sorted(outs.items()):
            orig = open(os.path.join(check_dir, f), encoding='utf-8').read()
            # modulo the R7-4 table rule: the flat files had unescaped pipes in table rows, which the vault escapes
            want = norm(V.normalize_tables(V.display_rewrite(orig))); got = norm(V.normalize_tables(t))
            if want != got:
                bad += 1
                import difflib
                d = list(difflib.unified_diff(want.split(' '), got.split(' '), lineterm='', n=3))
                print(f"  DIFF {f}: {len(d)} lines"); [print('    ' + x[:160]) for x in d[:12]]
            else:
                print(f"  identical (token stream, after the display rewrite): {f}")
        print(f"lossless check: {len(outs) - bad}/{len(outs)} files reproduce exactly")
        return bad

# ---------------------------------------------------------------- lint
def lint():
    notes = load(); state = json.load(open(VAULT + 'tools/vault_state.json')); errs, warns = [], []
    for k, n in notes.items():
        t = n['fm'].get('type')
        if t not in REQUIRED: errs.append(f"{k}: unknown or missing type {t!r}"); continue
        for f in REQUIRED[t]:
            if f not in n['fm']: errs.append(f"{k}: missing frontmatter field '{f}'")
        for x in V.link_targets(n['body']):
            if x not in notes and not x.startswith('_templates'): errs.append(f"{k}: broken link [[{x}]]")
    stale = sync(write=False)
    if stale: errs.append(f"derived fields or generated sections are stale in {len(stale)} notes (run sync): {stale[:8]}")
    items = {k: n for k, n in notes.items() if n['fm'].get('type') in ITEM_TYPES}
    G = {k: n['fm'].get('depends_on', []) for k, n in notes.items() if n['fm'].get('type') in ITEM_TYPES | {'dictionary-entry', 'attack-surface'}}
    color = {}; cyc = []
    def dfs(u, st):
        color[u] = 1; st.append(u)
        for v in G.get(u, []):
            if color.get(v) == 1: cyc.append(st[st.index(v):] + [v])
            elif color.get(v) is None: dfs(v, st)
        st.pop(); color[u] = 2
    for u in G:
        if color.get(u) is None: dfs(u, [])
    for c in cyc: errs.append("dependency cycle: " + ' -> '.join(c))
    # R7-4: tables. Every row must have as many cells as the header (an unescaped pipe silently moves or drops content)
    for k, n in notes.items():
        for start, rows in V.table_blocks(n['body']):
            if len(rows) < 2 or not re.match(r'^\s*\|?\s*:?-{3,}', rows[1]): continue
            h = V.table_cells(rows[0])
            for j, r in enumerate(rows):
                if V.table_cells(r) != h: errs.append(f"{k}: table at body line {start + 1}, row {j + 1} has {V.table_cells(r)} cells, header has {h}")
    # v7.3.1: bibliography — one-to-one between source notes and references.bib entries
    E = bib_entries(); claim = collections.defaultdict(list)
    for k, n in notes.items():
        if n['fm'].get('type') != 'source': continue
        bk = n['fm'].get('bibkey') or []
        if not bk: errs.append(f"{k}: no bibkey")
        for b_ in bk:
            if b_ not in E: errs.append(f"{k}: bibkey {b_} is not in references.bib")
            claim[b_].append(k)
        st_ = str(n['fm'].get('status_code', '')); u = bool(re.search(r'\bU\b', st_)) or 'not checked' in st_; chk = any(re.search(r'note=\{[^}]*check', E.get(b_, '')) for b_ in bk)
        if u != chk: warns.append(f"{k}: status {n['fm'].get('status_code')!r} but the bib entry {'lacks' if u else 'has'} note={{check ...}}")
    for b_ in E:
        fl = re.findall(r'[,{]\s*([a-zA-Z]+)=\{', E[b_])
        if len(fl) != len(set(fl)): errs.append(f"references.bib: entry {b_} repeats a field")
        if len(claim[b_]) != 1: errs.append(f"references.bib: entry {b_} is claimed by {len(claim[b_])} source notes {claim[b_]}")
    # R7-4: frozen files (pre-registrations, the migration archive) must match their recorded sha256
    import hashlib
    fz = json.load(open(VAULT + 'tools/frozen.json'))['files']
    for f, h in fz.items():
        if not os.path.exists(VAULT + f): errs.append(f"frozen file missing: {f}")
        elif hashlib.sha256(open(VAULT + f, 'rb').read()).hexdigest() != h: errs.append(f"frozen file changed: {f}")
    errs += version_errors(notes)
    for k, n in items.items():
        o = n['fm'].get('order', 0)
        for v in n['fm'].get('depends_on', []):
            if v in items and items[v]['fm'].get('order', 0) > o:
                if (k, v) in ALLOW_FORWARD: continue
                (errs if n['fm']['type'] == 'definition' else warns).append(f"forward dependency {k} -> {v}" + (" (definitions may cite only earlier items)" if n['fm']['type'] == 'definition' else ''))
            if n['fm']['type'] == 'definition' and v in items and items[v]['fm']['type'] not in ('definition', 'overview'):
                warns.append(f"definition {k} cites result {v} (allowed only for well-definedness; review)")
        stmt = section(n['body'], 'Statement') + section(n['body'], 'Proof')
        lay = n['fm'].get('layer')
        if lay not in ('measurement', 'explanation'): errs.append(f"{k}: layer must be 'measurement' or 'explanation', not {lay!r}")
        if lay == 'measurement':
            m = re.search(EXPL_VOCAB, stmt)
            if m: errs.append(f"{k}: measurement-layer statement or proof uses explanation vocabulary {m.group(0)!r}")
            for v in n['fm'].get('depends_on', []):
                if notes.get(v, {}).get('fm', {}).get('layer') == 'explanation':
                    errs.append(f"{k}: measurement-layer item depends on explanation-layer item {v}")
        if re.search(QAPAT, stmt) and not re.search(r'\(E_A\)|\(E_R\)', stmt) and n['fm']['type'] != 'definition':
            errs.append(f"{k}: uses the actor's own reference q_A without assuming (E_A) or (E_R)")
        if re.search(EPAT, stmt) and not re.search(TAGRX, stmt) and n['fm']['type'] != 'definition' and k not in NOT_E:
            errs.append(f"{k}: uses the entropic actual actor without an [Assumes ...] tag")
        for c in n['fm'].get('checks', []):
            if c not in notes: errs.append(f"{k}: check {c} does not exist")
        if n['fm']['type'] in ('theorem', 'proposition', 'corollary', 'lemma') and not n['fm'].get('checks'):
            # R7-3: the measurement layer defines misalignment, so every result in it must be checked
            meas = n['fm'].get('layer') == 'measurement'
            (errs if meas else warns).append(f"{k}: no check linked" + (" (measurement layer: required)" if meas else ''))
    for k, n in notes.items():
        if n['fm'].get('type') == 'check' and not n['fm'].get('verifies'): warns.append(f"{k}: check not cited by any note")
        if n['fm'].get('type') == 'source' and not n['fm'].get('cited_by'): warns.append(f"{k}: source with no resolvable citing note")
    print(f"notes: {len(notes)} ({dict(collections.Counter(n['fm'].get('type') for n in notes.values()))})")
    print(f"errors: {len(errs)}"); [print('  E ' + e) for e in errs[:60]]
    print(f"warnings: {len(warns)}"); [print('  W ' + w) for w in warns[:80]]
    return len(errs)

# ---------------------------------------------------------------- version banners (v7.3.3)
# The current version is stated in four places, which must agree. Each part's status banner — the first
# "**Status: vX**" in the part's reading order — must be at least as recent as the newest version its own text
# refers to, as vX.Y or as a completed R7 step (the step's version comes from its hygiene-log row). It is a lower
# bound: an edit that carries no version tag cannot be seen. Before this rule the Dictionary banner said v6.3, the
# Boundary banner v6.4 and the Status abstract v6.6, while their parts cited R7-2 to R7-4.
VTAG = re.compile(r'(?<![\w.])v([5-9](?:\.\d+){1,2})(?!\.?\d)')
PART_DIRS = {'core': ('10 Core/', '15 Hypotheses/'), 'dictionary': ('20 Dictionary/',), 'boundary': ('30 Boundary/',),
             'status': ('60 Status/',)}
def vkey(v): return tuple(int(x) for x in v.split('.'))
def version_errors(notes):
    errs = []
    hyg = notes.get('Status 05 Hygiene log'); home = notes.get('00 Home'); rm = notes.get('ROADMAP')
    if not (hyg and home and rm): return ["version check: 00 Home, ROADMAP or the hygiene log is missing"]
    steps = {s: v for s, v in re.findall(r'\*\*(R7-\d+)\b[^*(]*\((?:v)?(\d+(?:\.\d+)+)\)', hyg['body'])}
    rows = [l for l in hyg['body'].split('\n') if l.startswith('| ') and not l.startswith('| Change')]
    stated = {'00 Home title': re.search(r'^# .*?\bv(\d+(?:\.\d+)+)\s*$', home['body'], re.M),
              'README.md title': re.search(r'^# .*?\bv(\d+(?:\.\d+)+)\s*$', open(VAULT + 'README.md', encoding='utf-8').read(), re.M),
              'ROADMAP §0 Current': re.search(r'^\|\s*\*\*Current\*\*\s*\|\s*\*\*v(\d+(?:\.\d+)+)', rm['body'], re.M),
              'hygiene log, newest row': VTAG.search(rows[0]) if rows else None}
    missing = [w for w, m in stated.items() if not m]
    if missing: return [f"version check: no version found in {missing}"]
    stated = {w: m.group(1) for w, m in stated.items()}
    cur = stated['00 Home title']
    if len(set(stated.values())) > 1: errs.append(f"the current version is stated inconsistently: {stated}")
    for part, dirs in PART_DIRS.items():
        ks = [k for k, n in notes.items() if n['path'].startswith(dirs)]
        newest, where = None, None
        for k in ks:
            t = strip_gen(notes[k]['body'])
            tags = VTAG.findall(t) + [steps[s] for s in re.findall(r'\b(R7-\d+)\b', t) if s in steps]
            for v in tags:
                if newest is None or vkey(v) > vkey(newest): newest, where = v, k
        heads = sorted([k for k in ks if notes[k]['fm'].get('part') == part and notes[k]['fm'].get('type') == 'section'],
                       key=lambda k: notes[k]['fm'].get('order', 0))
        banner = next(((k, m.group(1)) for k in heads for m in [re.search(r'\*\*Status: v(\d+(?:\.\d+)+)', notes[k]['body'])] if m), None)
        if not banner: errs.append(f"{part}: no '**Status: vX**' banner in the part's section notes"); continue
        bk, bv = banner
        if vkey(bv) > vkey(cur): errs.append(f"{bk}: status banner v{bv} is later than the current version v{cur}")
        if newest and vkey(bv) < vkey(newest):
            errs.append(f"{bk}: status banner v{bv} is older than the part's own text, which refers to v{newest} (in {where})")
    return errs

# ---------------------------------------------------------------- queries
def deps(k):
    notes = load(); G = {x: n['fm'].get('depends_on', []) for x, n in notes.items()}
    R = collections.defaultdict(list)
    for x, ds in G.items():
        for d in ds: R[d].append(x)
    def closure(start, M):
        seen, todo = set(), [start]
        while todo:
            u = todo.pop()
            for v in M.get(u, []):
                if v not in seen: seen.add(v); todo.append(v)
        return sorted(seen, key=sortkey)
    print(f"{k}\n  depends on (direct): {G.get(k)}\n  depends on (all): {closure(k, G)}\n  used by (direct): {sorted(R.get(k, []), key=sortkey)}\n  used by (all): {closure(k, R)}")
SCAN = {'A1': r'p̂ = p_\{|p_\{F̂|p̂ ∝|entropic actor|Gibbs actor', 'A2': r'F̂|(?<![\w_])E(?![\w_\[(|])|σ_δ\(E|osc\(E|w_δ\(E',
        'A3': r'(?<![\w*])q(?![\w*])|q\(·', 'A4': r'KL|nats|Gibbs|e\^\{', 'A5': r'E_\{?p[^ `]*\}?F(?!̂)|E_pF(?!̂)|E_qF(?!̂)',
        'A6': r'(?<![\w_{])F(?![̂\w])', 'A7': r'min q|min_x|finite|Σ_x|log 1/q\('}
def scan(tag):
    notes = load(); hits = []
    for k, n in notes.items():
        if n['fm'].get('type') in ITEM_TYPES | {'dictionary-entry'} and re.search(SCAN[tag], logic_text(k, n)): hits.append(k)
    R = collections.defaultdict(list)
    for x, n in notes.items():
        for d in n['fm'].get('depends_on', []) or []: R[d].append(x)
    seen, todo = set(hits), list(hits)
    while todo:
        u = todo.pop()
        for w in R.get(u, []):
            if w not in seen: seen.add(w); todo.append(w)
    print(f"[{tag}] direct: {len(hits)}: {', '.join(sorted(hits, key=sortkey))}\n  plus dependents: {', '.join(sorted(seen - set(hits), key=sortkey))}")

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'lint'
    if cmd == 'sync':
        total = set()
        for _ in range(5):                       # derived fields can depend on other notes' derived fields: iterate to a fixed point
            ch = sync(); total |= set(ch)
            if not ch: break
        else: raise SystemExit("sync did not reach a fixed point in 5 passes")
        print(f"sync: {len(total)} notes updated")
    elif cmd == 'lint': sys.exit(1 if lint() else 0)
    elif cmd == 'compile': sys.exit(1 if compile_cmd(sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == '--check' else None) else 0)
    elif cmd == 'migration-check':
        # re-prove the one-time migration: rebuild from the frozen flat files into a temporary vault and compare
        import tempfile, subprocess, shutil
        tmp = tempfile.mkdtemp(); os.makedirs(tmp + '/tools')
        for f in ('vaultlib.py', 'vault.py', 'build_vault.py'): shutil.copy(VAULT + 'tools/' + f, tmp + '/tools/')
        subprocess.run([sys.executable, tmp + '/tools/build_vault.py', VAULT + 'archive/v6.6_flat', tmp], check=True, capture_output=True)
        r = subprocess.run([sys.executable, tmp + '/tools/vault.py', 'compile', '--check', VAULT + 'archive/v6.6_flat'], capture_output=True, text=True)
        print(r.stdout.strip().split('\n')[-1]); shutil.rmtree(tmp); sys.exit(r.returncode)
    elif cmd == 'deps': deps(sys.argv[2])
    elif cmd == 'scan': scan(sys.argv[2])
    else: print(__doc__)
