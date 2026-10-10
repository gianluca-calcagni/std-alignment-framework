"""What a measured misalignment is made of: the diagnostics of `derived/diagnostics.md` ([P43]–[P51]).

Each function names the item it computes. They take behaviours known exactly, as distributions on finitely many
outcomes; from draws, estimate the behaviours first, and report the cost of any reweighting ([P47], `estimation`).
"""
import itertools
from dataclasses import dataclass
import numpy as np
from scipy.optimize import minimize, minimize_scalar
from .core import kl, tilt
from .misalignment import misalignment, nearest_intended
from .projection import project_linear


# [P43] Misalignment at any intensity

@dataclass(frozen=True)
class IntensityTerms:
    """[P43](i): what KL(p‖p_{F,t}) depends on besides `t`, for one behaviour: its misalignment, its nearest intended
    behaviour, and the anti-pursuit gap [E_q F − E_p F]⁺. `at(t)` gives the three terms at intensity `t`."""
    misalignment: float
    nearest: np.ndarray
    anti_pursuit: float
    q: np.ndarray
    F: np.ndarray

    def at(self, t):
        """(misalignment, intensity mismatch KL(p°‖p_{F,t}), t·[E_q F − E_p F]⁺); their sum is KL(p‖p_{F,t})."""
        return self.misalignment, kl(self.nearest, tilt(self.q, t * self.F)), t * self.anti_pursuit


def intensity_terms(p, q, F):
    """The `IntensityTerms` of the behaviour `p` under the standard specification of `F` from `q` ([P43](i))."""
    q, F = np.asarray(q, dtype=float), np.asarray(F, dtype=float)
    return IntensityTerms(misalignment(p, q, F), nearest_intended(p, q, F), max(q @ F - np.asarray(p) @ F, 0.0), q, F)


def min_over_intensity(f):
    """The minimum over t ≥ 0 of a convex function of `t`, located on a grid and refined by a bounded search."""
    grid = np.r_[0.0, np.logspace(-3, 2, 300)]
    k = int(np.argmin([f(t) for t in grid]))
    lo, hi = grid[max(k - 1, 0)], grid[min(k + 1, len(grid) - 1)]
    res = minimize_scalar(f, bounds=(lo, hi), method="bounded", options={"xatol": 1e-13})
    return min(res.fun, f(lo), f(hi))


@dataclass(frozen=True)
class SharedIntensity:
    """[P43](ii): misalignment when several conditions are judged at one shared intensity, the sum of their own
    misalignments weighted by frequency, and the excess of the first over the second."""
    misalignment: float
    own: float
    excess: float


def shared_intensity(ps, qs, Fs, rho):
    """Behaviours `ps` in conditions with defaults `qs`, objectives `Fs` and frequencies `rho`, judged at one shared
    intensity ([P43](ii), [P24] Notes)."""
    rho = np.asarray(rho, dtype=float)
    if not (len(ps) == len(qs) == len(Fs) == rho.size) or np.any(rho <= 0) or abs(rho.sum() - 1) > 1e-9:
        raise ValueError("one behaviour, default and objective per condition, and positive frequencies adding up to 1")
    shared = min_over_intensity(lambda t: sum(rc * kl(pc, tilt(qc, t * np.asarray(Fc, float)))
                                              for rc, pc, qc, Fc in zip(rho, ps, qs, Fs)))
    own = sum(rc * misalignment(pc, qc, Fc) for rc, pc, qc, Fc in zip(rho, ps, qs, Fs))
    return SharedIntensity(shared, own, shared - own)


# [P44] What named objectives explain

def named_pursuit(p, q, F, Gs):
    """[P44]: the behaviour nearest to p° among those with p's averages of F and of the named objectives `Gs`."""
    A = np.vstack([F, *Gs])
    return project_linear(nearest_intended(p, q, F), A, A @ np.asarray(p, dtype=float))


def named_split(p, q, F, Gs):
    """[P44](ii): (unexplained, named) misalignment, KL(p‖p̃) and M(p̃), adding up to M(p)."""
    pt = named_pursuit(p, q, F, Gs)
    return kl(p, pt), misalignment(pt, q, F)


# [P45], [P46] Runs of one procedure

def _weights(w, m):
    w = np.asarray(w, dtype=float)
    if w.shape != (m,) or np.any(w <= 0) or abs(w.sum() - 1) > 1e-9:
        raise ValueError("one positive weight per run, adding up to 1")
    return w


def drift(ps, w):
    """[P45]: the drift D = Σ_i w_i·KL(p_i‖p̄) of the runs `ps` with weights `w`, and their average p̄."""
    w = _weights(w, len(ps))
    pbar = sum(wi * np.asarray(pi, dtype=float) for wi, pi in zip(w, ps))
    return sum(wi * kl(pi, pbar) for wi, pi in zip(w, ps)), pbar


def condition_split(pe, pu, w):
    """[P46](i): between two conditions e and u, the reproducible difference KL(p̄_u‖p̄_e) and the run-specific
    difference Σ_x p̄_u(x)·KL(ν_u(·|x)‖ν_e(·|x)), for runs behaving as `pe` and `pu` with weights `w`."""
    w = _weights(w, len(pe))
    bu, be = sum(a * b for a, b in zip(w, pu)), sum(a * b for a, b in zip(w, pe))
    nu_u = np.array([a * b for a, b in zip(w, pu)]); nu_e = np.array([a * b for a, b in zip(w, pe)]) / be
    specific = sum(bu[x] * kl(nu_u[:, x] / bu[x], nu_e[:, x]) for x in range(bu.size) if bu[x] > 0)
    return kl(bu, be), specific


# [P47] The cost of reweighting

def reweighting_moments(p, r):
    """[P47]: E_p[w] and E_p[w²] for the weights w = r/p on the support of `p`; the second is 1 + χ²(r‖p), at least
    e^{KL(r‖p)}."""
    p, r = np.asarray(p, dtype=float), np.asarray(r, dtype=float)
    s = p > 0
    return float(np.sum(r[s])), float(np.sum(r[s] ** 2 / p[s]))


# [P48], [P49] Uncertain targets, outer and inner misalignment

def most_charitable(p, q, Phi):
    """[P48]: the tilt of `q` by a combination of the rows of `Phi` with p's averages of them, and that combination's
    coefficients (read off its log-ratio to `q`)."""
    Phi = np.atleast_2d(np.asarray(Phi, dtype=float))
    pt = project_linear(q, Phi, Phi @ np.asarray(p, dtype=float))
    B = np.column_stack([np.ones(len(q)), Phi.T])
    return pt, np.linalg.lstsq(B, np.log(pt / q), rcond=None)[0][1:]


def uncertain_target_interval(p, q, Phi):
    """[P48](iii): the least and the largest misalignment of `p` over the principals whose objective lies in the span
    of the rows of `Phi`: KL(p‖p̃), for the most charitable p̃, and the departure KL(p‖q)."""
    return kl(p, most_charitable(p, q, Phi)[0]), kl(p, q)


def outer_misalignment(q, F, Fh, t):
    """[P49](i): the principal's misalignment, under the standard specification of `F`, of the trainer's optimum at
    intensity `t` for the evaluator `Fh`."""
    return misalignment(tilt(q, t * np.asarray(Fh, dtype=float)), q, F)


def inner_split(p, q, F, Fh):
    """[P49](ii): the strict inner misalignment U, and the parts left to the principal and to the trainer, from the one
    tilt of `q` by a combination of `F` and `Fh` with p's averages of both."""
    pt = most_charitable(p, q, np.vstack([F, Fh]))[0]
    return kl(p, pt), misalignment(pt, q, F), misalignment(pt, q, Fh)


# [P50], [P51] Tampering

def pairs(pW, K):
    """[P50]: the behaviour on world–signal pairs that produces the world as `pW` and measures it through the channel
    `K` (rows: worlds, columns: signals), as a |W| × |S| array: p(w, s) = pW(w)·K(s|w)."""
    return np.asarray(pW, dtype=float)[:, None] * np.asarray(K, dtype=float)


def tampering(p, K):
    """[P50]: T(p) = Σ_w p_W(w)·KL(p(·|w)‖K(·|w)), for a behaviour on world–signal pairs given as a |W| × |S| array."""
    p, K = np.asarray(p, dtype=float), np.asarray(K, dtype=float)
    pW = p.sum(1)
    return sum(pW[w] * kl(p[w] / pW[w], K[w]) for w in range(len(pW)) if pW[w] > 0)


def grounded_pursuit(qW, K, Fh, t):
    """[P50](iv): the best grounded behaviour for the evaluator `Fh` on signals at intensity `t`: the world pursues the
    expected signal score E_K[Fh | w] at the same intensity, and the channel is left alone."""
    return pairs(tilt(qW, t * (np.asarray(K, dtype=float) @ np.asarray(Fh, dtype=float))), K)


def least_tampering(pS, K):
    """[P51](i): L = min over world behaviours pW of KL(pS‖Kᵀ·pW), the least tampering consistent with the signals.

    The multiplicative fixed point of its optimality conditions, pW ← pW·c with c(w) = Σ_s K(s|w)·pS(s)/(Kᵀ·pW)(s), is
    slow near the boundary, so a constrained solver polishes it between two runs of it. Whatever the solver, the
    certificate of (i) bounds the distance to the minimum by log max_w c(w). Returns the value at the last pW, that
    certified gap, and the behaviour on pairs of (i) built from pW."""
    pS, K = np.asarray(pS, dtype=float), np.asarray(K, dtype=float)
    W = K.shape[0]

    def fixed_point(pW, steps):
        for _ in range(steps):
            mu = pW @ K; ratio = np.divide(pS, mu, out=np.zeros_like(pS), where=pS > 0); c = K @ ratio
            if np.log(c.max()) <= 1e-12:
                break
            pW = pW * c
        return pW
    f = lambda x: -pS @ np.log(np.maximum(x @ K, 1e-300))
    g = lambda x: -(K @ (pS / np.maximum(x @ K, 1e-300)))
    pW = fixed_point(np.full(W, 1 / W), 500)
    res = minimize(f, pW, jac=g, method="SLSQP", bounds=[(0, 1)] * W, options={"ftol": 1e-16, "maxiter": 1000},
                   constraints=[{"type": "eq", "fun": lambda x: x.sum() - 1, "jac": lambda x: np.ones(W)}])
    pW = np.clip(res.x, 0, None) + 1e-9 / W                       # back inside, so the fixed point can move every pW(w)
    pW = fixed_point(pW / pW.sum(), 2000)
    mu = pW @ K; ratio = np.divide(pS, mu, out=np.zeros_like(pS), where=pS > 0); c = K @ ratio
    return kl(pS, mu), float(np.log(c.max())), pW[:, None] * K * ratio[None, :]


def most_tampering(pS, K):
    """[P51](ii): the largest tampering among the behaviours with signals `pS` in which every signal comes from a
    single world, by enumerating the maps from signals to worlds (|W|^|S| of them: for small channels)."""
    pS, K = np.asarray(pS, dtype=float), np.asarray(K, dtype=float)
    W, S = K.shape; best = 0.0
    for a in itertools.product(range(W), repeat=S):
        p = np.zeros((W, S)); p[list(a), range(S)] = pS
        best = max(best, tampering(p, K))
    return best


def remeasured(p, K, Fh, qW):
    """[P51](iv): each world measured a second time through the honest channel `K`, as the joint of the two signals;
    the evaluator's honest gain over the default, E_{p_W}[E_K[Fh|w]] − E_{q_W}[E_K[Fh|w]]; and its channel gain, how
    much the average score falls from the first measurement to the second. Returns (honest gain, channel gain, joint)."""
    p, K, Fh, qW = (np.asarray(a, dtype=float) for a in (p, K, Fh, qW))
    again = np.einsum("ws,wv->sv", p, K)
    return p.sum(1) @ (K @ Fh) - qW @ (K @ Fh), again.sum(1) @ Fh - again.sum(0) @ Fh, again
