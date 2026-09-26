"""
tools/reproduce.py — rerun the numerical checks and compare them with the committed reference runs.

  python3 tools/reproduce.py verify V1 V3 ...   rerun these verify.py blocks; compare with verify_output.txt
  python3 tools/reproduce.py audit              rerun final_audit.py; compare with final_audit_output.txt

The comparison is exact for text and for every printed number, with one exception: two numbers that are both
at residual scale (|x| <= 1e-9) are treated as equal. Residuals such as "max 1.4e-13" legitimately move in their
last digits across CPUs and BLAS builds; a count, a fraction or a bound that moves is a real difference.
Exit status 1 if any block differs (or is missing), 0 otherwise. A GitHub step summary is written when
$GITHUB_STEP_SUMMARY is set.
"""
import os, re, subprocess, sys

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


def same_line(a, b):
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
        return False
    return True


def compare(ref, new, keys):
    report, bad = [], 0
    for k in keys:
        if k not in new:
            report.append(f"- **{k}: missing from the new run**"); bad += 1; continue
        if k not in ref:
            report.append(f"- {k}: new block, no reference yet"); continue
        ra, na = ref[k].split('\n'), new[k].split('\n')
        diff = [(i, x, y) for i, (x, y) in enumerate(zip(ra, na)) if not same_line(x, y)]
        if len(ra) != len(na) or diff:
            bad += 1
            report.append(f"- **{k}: differs** ({len(diff)} line(s); {len(ra)} reference lines, {len(na)} new)")
            for i, x, y in diff[:6]:
                report.append(f"  - reference: `{x.strip()}`")
                report.append(f"  - this run:  `{y.strip()}`")
        else:
            exact = ref[k] == new[k]
            report.append(f"- {k}: reproduces" + ("" if exact else " (residual-scale digits differ only)"))
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
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8').write(text + '\n')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
