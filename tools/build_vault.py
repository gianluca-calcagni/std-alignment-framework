"""
tools/build_vault.py — ONE-TIME migration of the v6.6 flat files into the Obsidian vault (v7.0).

    python3 tools/build_vault.py <flat_dir> <vault_dir>

After the migration the vault is the source of truth. tools/vault.py lints it, regenerates the backlink
sections, and compiles linear views. `vault.py compile --check <flat_dir>` proves the migration lossless.
"""
import re, sys, os, json, shutil
sys.path.insert(0, os.path.dirname(__file__))
import vaultlib as V

FLAT, OUT = sys.argv[1].rstrip('/') + '/', sys.argv[2].rstrip('/') + '/'
DATE = '2026-09-26'
notes = {}          # name -> dict(folder, fm (dict), body (str))

def rd(f): return open(FLAT + f, encoding='utf-8').read()
def add(name, folder, fm, body):
    assert name not in notes, name
    notes[name] = {'folder': folder, 'fm': fm, 'body': body}
def split_sections(text, level='## '):
    """[(heading line or None, text)] split at lines starting with `level`"""
    idx = [m.start() for m in re.finditer(r'^' + re.escape(level), text, re.M)]
    out = [(None, text[:idx[0]] if idx else text)]
    for k, i in enumerate(idx):
        j = idx[k + 1] if k + 1 < len(idx) else len(text)
        chunk = text[i:j]; nl = chunk.find('\n')
        out.append((chunk[:nl], chunk[nl + 1:]))
    return out
def safe(s): return re.sub(r'[\\/:*?"<>|#^\[\]]', '', s).strip()

# ================================================================ Part A: the core
A = rd('A_core.md')
MARKS = ('*Proof.*', '*Check.*', '*Note', '*Reading.*', '**Reading.**', '*Prior art.*', '*Scope.*', '*Measured*', '*(v6', '**Units.**')
core_sections = []; order = 0; tier_of = {}
secs = split_sections(A)
for si, (head, body) in enumerate(secs):
    if head is None:
        title, num = 'Status and scope', '00'
    else:
        t = head[3:].strip(); m = re.match(r'(\d+)\.\s*(.*)', t)
        num, title = (f"{int(m.group(1)):02d}", m.group(2)) if m else ({'Abstract, in plain terms': 'A1', 'Reading path': 'A2', 'Assumption tiers': 'A3'}[t], t)
    sname = f"Core {num} {safe(title)}"
    if head is not None and re.match(r'\d+', num): V.SECTION_NOTES[('A', str(int(num)))] = sname
    heads = [(m.start(), m.group(1), m.group(2)) for m in V.ITEM_HEAD.finditer(body)]
    parts = []; pos = 0
    for k, (p, kind, n) in enumerate(heads):
        if p > pos: parts.append(('text', body[pos:p]))
        end = heads[k + 1][0] if k + 1 < len(heads) else len(body)
        raw = body[p:end]
        tail = ''
        mm = re.search(r'\n(---\s*\n\s*)$', raw)                         # a section rule belongs to the section
        if mm: tail = raw[mm.start() + 1:]; raw = raw[:mm.start() + 1]
        short = V.KIND_SHORT[kind]; iid = V.item_id(short, n)
        cut = min([i for i in (raw.find(x) for x in MARKS) if i > 0] or [len(raw)])
        stmt, proof, rest = raw[:cut], '', raw[cut:]
        if raw.find('*Proof.*') == cut:
            pe = raw.find('∎', cut); pe = len(raw) if pe < 0 else pe + 1
            proof, rest = raw[cut:pe], raw[pe:]
        hm = re.match(r'\*\*(?:\w+) [\dB.]+\s*(?:\((.*?)\))?\.?\*\*', raw, re.S)
        ititle = re.sub(r'\s+', ' ', hm.group(1)) if hm and hm.group(1) else ''
        order += 1
        parts.append(('item', iid))
        add(iid, '10 Core/items', {'id': iid, 'type': V.KIND_TYPE[short], 'title': ititle, 'section': sname, 'order': order,
                                   'layer': None, 'tier': None, 'assumes': [], 'status': None, 'depends_on': [], 'mentions': [],
                                   'checks': [], 'sources': [], 'aliases': [f"{kind} {n}", f"{short}. {n}"], 'updated': DATE},
            {'statement': stmt, 'proof': proof, 'notes': rest})
        if tail: parts.append(('text', tail))
        pos = end
    if pos < len(body) or not heads: parts.append(('text', body[pos:]))
    core_sections.append((sname, head, parts, si))
# tiers from the tier table
tiers_txt = [b for h, b in secs if h and h.startswith('## Assumption tiers')][0]
for row in re.findall(r'^\| \*\*([^*|]+)\*\* \|[^|]*\|([^\n]*)\|\s*$', tiers_txt, re.M):
    tier = row[0].strip()
    for iid in V.logical_refs(row[1]):
        tier_of.setdefault(iid, [])
        if tier not in tier_of[iid]: tier_of[iid].append(tier)
for sname, head, parts, si in core_sections:
    body = (head + '\n' if head else '')
    for kind, x in parts:
        body += x if kind == 'text' else f"![[{x}]]\n"
    add(sname, '10 Core', {'id': sname, 'type': 'section', 'part': 'core', 'order': si, 'updated': DATE}, {'text': body})

# ================================================================ Part B: dictionary
B = rd('B_dictionary.md'); bsecs = split_sections(B)
for si, (head, body) in enumerate(bsecs):
    if head is None: name, title = 'Dictionary 00 Preamble', 'Preamble'
    else:
        t = head[3:].strip(); m = re.match(r'(\d+)\.\s*(.*)', t)
        if not m: name, title = 'Dictionary 00b ' + safe(t), t
        else:
            k = int(m.group(1)); title = m.group(2)
            name = f"B{k:02d}" if 1 <= k <= 13 else f"Dictionary {k:02d} {safe(title)}"
            V.SECTION_NOTES[('B', str(k))] = name
    typ = 'dictionary-entry' if re.match(r'B\d\d$', name) else 'section'
    als = [f"B{int(name[1:])}", f"Prop. B{int(name[1:])}", f"B §{int(name[1:])}"] if typ == 'dictionary-entry' else []
    add(name, '20 Dictionary', {'id': name, 'type': typ, 'title': title, 'part': 'dictionary', 'order': si, 'status': None,
                                'depends_on': [], 'mentions': [], 'checks': [], 'sources': [], 'aliases': als, 'updated': DATE},
        {'text': (head + '\n' if head else '') + body})

# ================================================================ Part C: boundary
C = rd('C_boundary.md'); csecs = split_sections(C)
for si, (head, body) in enumerate(csecs):
    if head is None: name, title = 'Boundary 00 Preamble', 'Preamble'
    else:
        t = head[3:].strip(); m = re.match(r'(\d+)\.\s*(.*)', t)
        name, title = (f"Boundary {int(m.group(1)):02d} {safe(m.group(2))}", m.group(2)) if m else (f"Boundary 00b {safe(t)}", t)
        if m: V.SECTION_NOTES[('C', m.group(1))] = name
    subs = split_sections(body, '### ')
    if head and head.startswith('## 1. The attack surface'):
        text = head + '\n' + subs[0][1]
        for h3, b3 in subs[1:]:
            cm = re.match(r'### C(\d+) — (.*)', h3)
            cid = f"C{int(cm.group(1)):02d}"; text += f"![[{cid}]]\n"
            add(cid, '30 Boundary', {'id': cid, 'type': 'attack-surface', 'title': re.sub(r'\s+', ' ', cm.group(2)), 'part': 'boundary',
                                     'order': int(cm.group(1)), 'depends_on': [], 'mentions': [], 'checks': [], 'aliases': [f"C{int(cm.group(1))}"],
                                     'updated': DATE}, {'text': h3 + '\n' + b3})
        add(name, '30 Boundary', {'id': name, 'type': 'section', 'title': title, 'part': 'boundary', 'order': si, 'updated': DATE}, {'text': text})
    else:
        add(name, '30 Boundary', {'id': name, 'type': 'section', 'title': title, 'part': 'boundary', 'order': si, 'mentions': [], 'updated': DATE},
            {'text': (head + '\n' if head else '') + body})

# ================================================================ Part D: status (retractions become one note each)
D = rd('D_status.md'); dsecs = split_sections(D)
CELL = re.compile(r'(?<!\\)\|')
for si, (head, body) in enumerate(dsecs):
    if head is None: name, title = 'Status 00 Preamble', 'Preamble'
    else:
        t = head[3:].strip(); m = re.match(r'(\d+)\.\s*(.*)', t)
        name, title = (f"Status {int(m.group(1)):02d} {safe(m.group(2))}", m.group(2)) if m else (f"Status 00b {safe(t)}", t)
        if m: V.SECTION_NOTES[('D', m.group(1))] = name
    text = (head + '\n' if head else '') + body
    if head and head.startswith('## 2. Retraction history'):
        lines = text.split('\n'); out = []; done = False
        for l in lines:
            mm = re.match(r'^\| (\d+) \|', l)
            if mm:
                cells = [c.strip() for c in CELL.split(l)[1:-1]]
                n = int(cells[0]); rid = f"R{n:03d}"
                add(rid, '60 Status/retractions', {'id': rid, 'type': 'retraction', 'number': n, 'found_by': cells[3], 'affects': [],
                                                  'updated': DATE}, {'was': cells[1], 'now': cells[2], 'found': cells[3]})
                if not done: out.append('<!-- gen:retractions -->'); done = True
                continue
            if done and out[-1] == '<!-- gen:retractions -->':
                out.append('<!-- /gen:retractions -->')
            out.append(l)
        text = '\n'.join(out)
    add(name, '60 Status', {'id': name, 'type': 'section', 'title': title, 'part': 'status', 'order': si, 'updated': DATE}, {'text': text})

# ================================================================ sources (Parts A and B of REFERENCES.md)
Rf = rd('REFERENCES.md'); rsecs = split_sections(Rf)
keys = {}
def srckey(ref):
    au = re.match(r'\s*([^,(]+?)(?:,| &| and|\()', ref); yr = re.search(r'\((\d{4}[a-z]?)\)', ref)
    k = f"{safe(au.group(1)) if au else 'Anon'} {yr.group(1) if yr else 'nd'}"
    if 'et al' in ref[:80]: k = k.replace(' ', ' et al ', 1) if False else k
    base = f"src {k}"; i = 1; name = base
    while name in keys: i += 1; name = f"{base} ({i})"
    keys[name] = 1; return name
src_text = ''
for si, (head, body) in enumerate(rsecs):
    text = (head + '\n' if head else '') + body
    if head and head.startswith('## Part C'):
        add('Sources census attributions', '50 Sources', {'id': 'Sources census attributions', 'type': 'section', 'part': 'sources', 'order': si,
                                                        'updated': DATE}, {'text': text}); continue
    out = []
    for l in text.split('\n'):
        cells = [c.strip() for c in CELL.split(l)[1:-1]] if l.startswith('|') else []
        if len(cells) == 3 and cells[0] not in ('Reference', '---') and not set(cells[0]) <= set('-'):
            name = srckey(cells[0])
            urls = re.findall(r'(https?://\S+|arXiv:?\s*\d{4}\.\d{4,5}|doi:\S+)', cells[0])
            add(name, '50 Sources', {'id': name, 'type': 'source', 'status_code': cells[2], 'where': cells[1], 'cited_by': [],
                                     'external': urls, 'updated': DATE}, {'ref': cells[0], 'where': cells[1], 'status': cells[2]})
            out.append(f"<!-- src:{name} -->"); continue
        out.append(l)
    src_text += '\n'.join(out) + ('\n' if not text.endswith('\n') else '')
src_text = re.sub(r'^(\| Reference \| [^|\n]+ \| Status \|)\n\|---\|---\|---\|\n(?=<!-- src:)',
                  lambda m: '<!-- srctable:' + m.group(1) + ' -->\n', src_text, flags=re.M)
add('Sources index', '50 Sources', {'id': 'Sources index', 'type': 'index', 'part': 'sources', 'updated': DATE}, {'text': src_text})

# ================================================================ checks: V, F, W blocks from the recorded outputs
def blocks_of(path, letter):
    t = open(FLAT + path, encoding='utf-8').read(); out = {}
    for m in re.finditer(r'^\[(' + letter + r'\d+)\](.*?)(?=^\[' + letter + r'\d+\]|\Z)', t, re.M | re.S):
        out[m.group(1)] = '[' + m.group(1) + ']' + m.group(2)
    return out
for vid, txt in blocks_of('verify_output.txt', 'V').items():
    n = int(vid[1:]); name = f"V{n:02d}"
    add(name, '40 Checks', {'id': name, 'type': 'check', 'script': f"verify.py {vid}", 'verifies': [], 'last_run': DATE, 'updated': DATE},
        {'output': txt.rstrip()})
for fid, txt in blocks_of('final_audit_output.txt', 'F').items():
    add(fid, '40 Checks', {'id': fid, 'type': 'check', 'script': f"final_audit.py {fid}", 'verifies': [], 'last_run': DATE, 'updated': DATE},
        {'output': txt.rstrip()})
for wid, txt in blocks_of('verify_addendum_output.txt', 'W').items():
    add(wid, '40 Checks', {'id': wid, 'type': 'check', 'script': f"verify_addendum.py {wid}", 'verifies': [], 'last_run': DATE, 'updated': DATE},
        {'output': txt.rstrip()})

# ================================================================ whole-file notes
for f, (name, folder, typ) in {'E_census.md': ('Census', '70 Project', 'census'), 'F_method.md': ('Method', '70 Project', 'method'),
        'ROADMAP.md': ('ROADMAP', '70 Project', 'project'), 'NOTES_claude.md': ('NOTES_claude', '70 Project', 'working-notes'),
        'T1_census_routing.md': ('T1_census_routing', '70 Project/T1', 'report'), 'T1_preregistration.md': ('T1_preregistration', '70 Project/T1', 'report'),
        'T1_RULES_FROZEN.md': ('T1_RULES_FROZEN', '70 Project/T1', 'report'), 'R3_FIX_LOG.md': ('R3_FIX_LOG', '80 Logs', 'log'),
        'R4_LOG.md': ('R4_LOG', '80 Logs', 'log'), 'R5_LOG.md': ('R5_LOG', '80 Logs', 'log'), 'R6_LOG.md': ('R6_LOG', '80 Logs', 'log'),
        'MSG_1_findings.md': ('MSG_1_findings', '80 Logs', 'log'), 'MSG_2_steering.md': ('MSG_2_steering', '80 Logs', 'log'),
        'MESSAGE_to_previous_executor.md': ('MESSAGE_to_previous_executor', '80 Logs', 'log')}.items():
    add(name, folder, {'id': name, 'type': typ, 'source_file': f, 'updated': DATE}, {'text': rd(f)})

# ================================================================ linkify and write
known = set(notes)
def L(t, nm, drows=False): return V.linkify(t, self_id=nm, known=known, d_rows=drows)
def fm_dump(fm):
    out = ['---']
    for k, v in fm.items():
        if v is None: out.append(f"{k}:")
        elif isinstance(v, list): out.append(f"{k}: [" + ', '.join(json.dumps(x, ensure_ascii=False) for x in v) + "]")
        elif isinstance(v, (int, float)): out.append(f"{k}: {v}")
        else: out.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    return '\n'.join(out + ['---', ''])
GEN = "<!-- gen:links -->\n<!-- /gen:links -->\n"
for name, n in notes.items():
    fm, b, typ = n['fm'], n['body'], n['fm']['type']
    drows = typ in ('section', 'project', 'working-notes', 'log', 'report', 'method') or name.startswith('Status')
    if typ in V.KIND_TYPE.values():
        t = f"# {name}" + (f" — {fm['title']}" if fm['title'] else '') + "\n<!-- gen:header -->\n<!-- /gen:header -->\n\n"
        t += "## Statement\n\n" + L(b['statement'], name, drows).strip() + "\n\n"
        if b['proof'].strip(): t += "## Proof\n\n" + L(b['proof'], name, drows).strip() + "\n\n"
        if b['notes'].strip(): t += "## Notes and checks\n\n" + L(b['notes'], name, drows).strip() + "\n\n"
        text = t + GEN
    elif typ == 'retraction':
        text = (f"# {name} — retraction {fm['number']}\n<!-- gen:header -->\n<!-- /gen:header -->\n\n## Retracted\n\n{L(b['was'], name, True)}\n\n"
                f"## Replaced by\n\n{L(b['now'], name, True)}\n\n## Found by\n\n{b['found']}\n\n" + GEN)
    elif typ == 'source':
        text = (f"# {name}\n<!-- gen:header -->\n<!-- /gen:header -->\n\n## Reference\n\n{b['ref']}\n\n## Where it is used, or its role (as recorded)\n\n"
                f"{L(b['where'], name, True)}\n\n## Status of the bibliographic details\n\n{b['status']}\n\n## External links\n\n"
                + ('\n'.join(f"- {u}" for u in fm['external']) if fm['external'] else "- none recorded") + "\n\n" + GEN)
    elif typ == 'check':
        text = (f"# {name} — `{fm['script']}`\n<!-- gen:header -->\n<!-- /gen:header -->\n\n## Recorded output (reference run)\n\n```\n{b['output']}\n```\n\n" + GEN)
    else:
        text = L(b['text'], name, drows)
        if typ in ('dictionary-entry', 'attack-surface'): text = text.rstrip('\n') + "\n\n" + GEN
    path = OUT + n['folder'] + '/' + name + '.md'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(fm_dump(fm) + text)
os.makedirs(OUT + 'tools', exist_ok=True)
json.dump({'section_notes': {f"{a}|{b}": c for (a, b), c in V.SECTION_NOTES.items()},
           'tier_of': tier_of}, open(OUT + 'tools/vault_state.json', 'w'), indent=1, ensure_ascii=False)
print(f"notes written: {len(notes)}")
import collections; print(collections.Counter(n['fm']['type'] for n in notes.values()))
