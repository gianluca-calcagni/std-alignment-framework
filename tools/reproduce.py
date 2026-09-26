"""
tools/reproduce.py — rerun the numerical checks and compare them with the committed reference runs.

  python3 tools/reproduce.py verify V1 V3 ...   rerun these verify.py blocks; compare with verify_output.txt
  python3 tools/reproduce.py audit              rerun final_audit.py; compare with final_audit_output.txt

The comparison is exact for text and for every printed number, with one exception: two numbers that are both
at residual scale (|x| <= 1e-9) are treated as equal. Residuals such as "max 1.4e-13" legitimately move in their
last digits across CPUs and BLAS builds; a count, a fraction or a bound that moves is a real difference.
Lines that measure numerical noise (finite differences, for instance) may be given a relative tolerance in
tools/reproduce_tolerances.json, each with its reason.
Exit status 1 if any block differs (or is missing), 0 otherwise. A GitHub step summary is written when
$GITHUB_STEP_SUMMARY is set.
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUM = re.compile(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?')
RESIDUAL = 1e-9


def blocks(text, tag):
    """split an output into blocks keyed by their [V12] / [F3] header"""
    out, cur = {}, None
    for line in text.split('\n'):
        m = re.match(r'^\[(' + tag + r'\d+)\]', line)
        if m:
            cur = m.group(1); out[cur] = []
        if cur:
            out[cur].append(line.rstrip())
    return {k: '\n'.join(v).strip() for k, v in out.items()}


TOL = {k: v for k, v in json.load(open(os.path.join(ROOT, 'tools', 'reproduce_tolerances.json'), encoding='utf-8')).items() if not k.startswith('_')}


def same_line(a, b, rel=0.0):
    ta, tb = NUM.split(a), NUM.split(b)
    na, nb = NUM.findall(a), NUM.findall(b)
    if ta != tb or len(na) != len(nb):
        return False
    for x, y in zip(na, nb):
        if x == y:
            continue
        fx, fy = float(x), float(y)
        if abs(fx) <= RESIDUAL and abs(fy) <= RESIDUAL:
            continue
        if rel and abs(fx - fy) <= rel * max(abs(fx), abs(fy)):
            continue
        return False
    return True


def annotate(level, title, msg):
    """a GitHub Actions annotation: readable through the public check-runs API, unlike the raw logs"""
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        esc = msg.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
        t = title.replace('%', '%25').replace(':', '%3A').replace(',', '%2C')
        print(f"::{level} title={t}::{esc}")


def compare(ref, new, keys):
    report, bad = [], 0
    for k in keys:
        if k not in new:
            report.append(f"- **{k}: missing from the new run**"); bad += 1; continue
        if k not in ref:
            report.append(f"- {k}: new block, no reference yet"); continue
        ra, na = ref[k].split('\n'), new[k].split('\n')
        tol = lambda x: max([t['rel'] for t in TOL.get(k, []) if t['line'] in x] or [0.0])
        diff = [(i, x, y) for i, (x, y) in enumerate(zip(ra, na)) if not same_line(x, y, tol(x))]
        tolerated = [x for x, y in zip(ra, na) if x != y and tol(x) and same_line(x, y, tol(x))]
        if len(ra) != len(na) or diff:
            bad += 1
            report.append(f"- **{k}: differs** ({len(diff)} line(s); {len(ra)} reference lines, {len(na)} new)")
            for i, x, y in diff[:6]:
                report.append(f"  - reference: `{x.strip()}`")
                report.append(f"  - this run:  `{y.strip()}`")
                annotate('error', f"{k} differs from the reference", f"reference: {x.strip()}\nthis run:  {y.strip()}")
            if len(ra) != len(na):
                annotate('error', f"{k} differs from the reference", f"{len(ra)} reference lines, {len(na)} lines in this run")
        else:
            exact = ref[k] == new[k]
            why = [] if exact else (["residual-scale digits"] if len(tolerated) < sum(x != y for x, y in zip(ra, na)) else []) + \
                  ([f"{len(tolerated)} line(s) within a declared tolerance (tools/reproduce_tolerances.json)"] if tolerated else [])
            report.append(f"- {k}: reproduces" + (f" — differences only in: {'; '.join(why)}" if why else ""))
    return bad, report


def run(cmd):
    r = subprocess.run([sys.executable] + cmd, cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-4000:]); print(r.stderr[-4000:])
        raise SystemExit(f"{' '.join(cmd)} exited with {r.returncode}")
    return r.stdout


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('verify', 'audit'):
        print(__doc__); sys.exit(2)
    if sys.argv[1] == 'verify':
        keys = sys.argv[2:]
        ref = blocks(open(os.path.join(ROOT, 'verify_output.txt'), encoding='utf-8').read(), 'V')
        new = blocks(run(['verify.py'] + keys), 'V')
        title = 'verify.py ' + ' '.join(keys)
    else:
        ref = blocks(open(os.path.join(ROOT, 'final_audit_output.txt'), encoding='utf-8').read(), 'F')
        new = blocks(run(['final_audit.py']), 'F')
        keys = sorted(set(ref) | set(new), key=lambda k: int(k[1:]))
        title = 'final_audit.py'
    bad, report = compare(ref, new, keys)
    text = f"### {title}: {'all blocks reproduce' if not bad else f'{bad} block(s) differ'}\n\n" + '\n'.join(report) + '\n'
    print(text)
    annotate('notice' if not bad else 'error', f"{title}: {'reproduces' if not bad else 'differs'}",
             f"{len(keys) - bad} of {len(keys)} blocks reproduce the committed reference output")
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8').write(text + '\n')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
