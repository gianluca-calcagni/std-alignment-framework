"""Write the computed part of RESULTS.md from output.json and the registration: every number is filled in from them,
so the text cannot drift from the computation. The readings after the verdicts are written by hand below the marker
line, and kept when this script is run again. Usage: python3 make_results.py <registration commit>"""
import hashlib, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARKER = "<!-- written by hand below this line -->"


def f(x, d=3):
    return f"{x:.{d}f}".replace("-", "−")


def ci(s, d=3):
    lo, hi = s["interval_95"]
    return f"`{f(s['mean'], d)}` (`{f(lo, d)}` to `{f(hi, d)}`)"


def main(commit):
    out = json.loads((HERE / "output.json").read_text())
    reg, rep = out["registered"], out["reported"]
    digest = hashlib.sha256((HERE / "REGISTRATION.md").read_bytes()).hexdigest()
    s1, s2 = reg["S1"], reg["S2"]
    named = lambda key: "\n".join(f"| {name} | {ci(v, 2)} |" for name, v in rep[key].items())
    text = f"""# W4 — Is W3's off-reward change systematic, or drift? — Results

**Registered in commit:** `{commit}`, pushed before any computation on the test's contexts.
**Registration SHA-256:** `{digest}`
**Computed by:** `run.py` in this folder, by the executor (a Claude model), in one run. Its output is `output.json`,
aggregates only; `make_results.py` writes this part of the file from it.

## Verdicts

| Id | Label | Held if | Result | Verdict |
|---|---|---|---|---|
| S0 | verification | sampler and scorer agree within `10⁻⁴` nats on every draw | worst difference `{reg['S0']['worst_abs_difference']:.1e}` | {"held" if reg["S0"]["held"] else "**failed**"} |
| S1 | diagnostic | the 95% interval of the mean coefficient of `log R` lies above `{s1['margin']}` | {ci(s1['coefficient_of_log_reference'])} | **{s1['verdict']}** |
| S2 | diagnostic | the 95% interval of the mean coefficient of `log(B/R)` lies above `{s2['margin']}` | {ci(s2['coefficient_of_the_other_run'])} | **{s2['verdict']}** |

## Reported without a prediction

| Quantity | Value |
|---|---|
| departure of A from R, `KL(A‖R)`, nats | {ci(rep['departure_A'], 2)} |
| departure of B from R, nats | {ci(rep['departure_B'], 2)} |
| `KL(A‖B)` and `KL(B‖A)`, nats | {ci(rep['kl_A_B'], 2)} and {ci(rep['kl_B_A'], 2)} |
| drift between the runs ([P45]), at most `log 2 = 0.693` | {ci(rep['drift'])} |
| misalignment as a share of the departure, A and B | {ci(rep['M_share_A'])} and {ci(rep['M_share_B'])} |
| B's coefficient of `log R`, and of `log(A/R)` | {ci(rep['coefficient_of_log_reference_B'])} and {ci(rep['coefficient_of_the_other_run_B'])} |
| A's revealed intensity, median; contexts where it is infinite | `{f(rep['t_star_A_median'], 2)}`; {rep['t_star_A_infinite']} |
| effective draws behind A's last named pursuit, median of 192 ([P47]) | `{f(rep['effective_draws_median_A'], 1)}` |
| contexts with a reward that did not vary; with repeated draws | {rep['contexts_with_a_flat_reward']}; {rep['contexts_with_repeated_draws']} of {rep['contexts']} |

Named misalignment as a share of the run's misalignment ([P44]), after each named objective in the declared order:

| A, after naming | share |
|---|---|
{named('named_share_A')}

| B, after naming | share |
|---|---|
{named('named_share_B')}

{MARKER}
"""
    path = HERE / "RESULTS.md"
    if path.exists() and MARKER in path.read_text():
        text += path.read_text().split(MARKER, 1)[1].lstrip("\n")
    path.write_text(text)
    print("RESULTS.md written")


if __name__ == "__main__":
    main(sys.argv[1])
