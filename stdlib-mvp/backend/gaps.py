"""Real-data gap scoring: sim-to-real, cross-embodiment, batch alpha, collapse.

Idea 1 patent vectors #1 (Frechet sim-to-real), #2 (provenance + ratio
enforcement), #5 (cross-embodiment degradation). Stdlib only, deterministic.

Pair scorecards reuse the SAME DRAFT_RULES thresholds as the policy engine
for comparability; pairs lack action-sensitivity and spread gates, so the
verdict is fail-closed over the 6 applicable gates only.
"""

from __future__ import annotations

import math
import random

import metrics_std as M

PAIR_GATES = ("frechet_sim_real", "mean_drift", "final_drift",
              "coherence_horizon_ratio", "max_jerk_proxy",
              "bound_violation_rate")

MAX_EPISODES = 40
MAX_T = 2000
MAX_BODY = 3 * 1024 * 1024

# DRAFT cross-embodiment bands (centered paths, SAME frame required).
# Shape: centered Frechet in native units. Scale: workspace span ratio.
XEMB_SHAPE_GREEN = 0.10
XEMB_SHAPE_AMBER = 0.25
XEMB_SCALE_GREEN = 0.80
XEMB_SCALE_AMBER = 0.60

# DRAFT batch alpha policy (Idea 1 vector #2, ratio enforcement).
ALPHA_GREEN = 0.50
ALPHA_AMBER = 0.80


def _fail_closed_verdict(bands: list) -> tuple:
    if "red" in bands:
        return ("BLOCKED", "Fails trust gates", "red")
    if "amber" in bands:
        return ("REVIEW", "Marginal - needs engineer sign-off", "amber")
    return ("TRUSTED", "Passes all gates", "green")


def score_pair(sim, real) -> dict:
    """Gap scorecard for one pair: sim = commanded, real = executed."""
    drift = M.drift_at_horizon(real, sim)
    frechet = M.discrete_frechet(real, sim)
    exe = M.executability_proxy(real)
    score = {
        "frechet_sim_real": round(frechet, 4),
        "mean_drift": round(drift["mean_err"], 4),
        "final_drift": round(drift["final_err"], 4),
        "coherence_horizon_ratio": round(drift["horizon_ratio"], 3),
        "max_jerk_proxy": round(exe["max_jerk"], 4),
        "bound_violation_rate": round(exe["violation_rate"], 4),
    }
    gates = []
    for key in PAIR_GATES:
        direction, green, amber, desc = M.DRAFT_RULES[key]
        gates.append({"metric": key, "value": score[key],
                      "band": M.band(direction, score[key], green, amber),
                      "desc": desc, "tag": "Estimated"})
    label, detail, band = _fail_closed_verdict([g["band"] for g in gates])
    return {"score": score, "gates": gates,
            "verdict": {"label": label, "detail": detail, "band": band},
            "thresholds": "DRAFT", "T": len(sim)}


def resample(traj, n: int = 200) -> list:
    """Uniform-index resample to n points (lengths may differ)."""
    t = len(traj)
    if t == n:
        return [row[:] for row in traj]
    if t == 1:
        return [traj[0][:] for _ in range(n)]
    out = []
    for i in range(n):
        f = i * (t - 1) / float(n - 1)
        lo = int(math.floor(f))
        hi = min(lo + 1, t - 1)
        w = f - lo
        out.append([traj[lo][0] * (1 - w) + traj[hi][0] * w,
                    traj[lo][1] * (1 - w) + traj[hi][1] * w])
    return out


def center(traj) -> list:
    """Remove translation only. Scale is PRESERVED: reach differences
    between embodiments are signal, not noise."""
    xs = [p[0] for p in traj]
    ys = [p[1] for p in traj]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    return [[x - mx, y - my] for x, y in zip(xs, ys)]


def span_of(traj) -> float:
    xs = [p[0] for p in traj]
    ys = [p[1] for p in traj]
    return max(max(xs) - min(xs), max(ys) - min(ys))


def xemb_distance(traj_a, traj_b, n: int = 200) -> dict:
    """Cross-embodiment divergence between two executed paths.

    Compares CENTERED shapes (translation removed, scale kept) plus the
    workspace span ratio. Caller must ensure both paths share one frame
    (meters vs abstract units never mix - the server enforces this).
    Verdict is fail-closed over the shape band and the scale band.
    DRAFT bands; higher = more divergent morphology or behavior.
    """
    a = center(resample(traj_a, n))
    b = center(resample(traj_b, n))
    frechet = M.discrete_frechet(a, b)
    drift = sum(math.dist(p, q) for p, q in zip(a, b)) / n
    sa = span_of(resample(traj_a, n))
    sb = span_of(resample(traj_b, n))
    ratio = min(sa, sb) / max(sa, sb, 1e-9)
    if frechet <= XEMB_SHAPE_GREEN:
        shape_band = "green"
    elif frechet <= XEMB_SHAPE_AMBER:
        shape_band = "amber"
    else:
        shape_band = "red"
    if ratio >= XEMB_SCALE_GREEN:
        scale_band = "green"
    elif ratio >= XEMB_SCALE_AMBER:
        scale_band = "amber"
    else:
        scale_band = "red"
    worst = "green"
    for bnd in (shape_band, scale_band):
        if bnd == "red":
            worst = "red"
        elif bnd == "amber" and worst == "green":
            worst = "amber"
    label = {"green": "ALIGNED", "amber": "DIVERGED", "red": "SEVERE"}[worst]
    return {"frechet_centered": round(frechet, 4),
            "mean_drift_centered": round(drift, 4),
            "span_a": round(sa, 4), "span_b": round(sb, 4),
            "span_ratio": round(ratio, 4),
            "shape_band": shape_band, "scale_band": scale_band,
            "band": worst, "label": label,
            "thresholds": "DRAFT", "n": n,
            "tag": "Estimated"}


def _clean_traj(raw, cap: int = MAX_T):
    if not isinstance(raw, list) or len(raw) < 10:
        return None
    if len(raw) > cap:
        return None
    out = []
    for pt in raw:
        if (not isinstance(pt, list) or len(pt) != 2
                or not all(isinstance(v, (int, float)) and math.isfinite(v)
                           for v in pt)):
            return None
        out.append([float(pt[0]), float(pt[1])])
    return out


def batch_audit(episodes: list) -> dict:
    """Governance audit for an uploaded batch (Idea 1 vector #2).

    Each episode: {id?, source: real|synthetic, generation?, sim, real}.
    Computes the alpha ratio (synthetic fraction), per-source drift, and a
    fail-closed governance verdict plus collapse risk. Deterministic.
    """
    if not isinstance(episodes, list) or not episodes:
        raise ValueError("episodes must be a non-empty list")
    if len(episodes) > MAX_EPISODES:
        raise ValueError("too many episodes (max %d)" % MAX_EPISODES)
    rows = []
    for i, ep in enumerate(episodes):
        if not isinstance(ep, dict):
            raise ValueError("episode %d is not an object" % i)
        src = ep.get("source")
        if src not in ("real", "synthetic"):
            raise ValueError("episode %d: source must be real|synthetic" % i)
        sim = _clean_traj(ep.get("sim"))
        real = _clean_traj(ep.get("real"))
        if sim is None or real is None or len(sim) != len(real):
            raise ValueError("episode %d: bad sim/real trajectories" % i)
        gen = ep.get("generation", 0)
        if not isinstance(gen, int) or gen < 0 or gen > 50:
            raise ValueError("episode %d: bad generation" % i)
        drift = sum(math.dist(a, b) for a, b in zip(sim, real)) / len(sim)
        rows.append({"id": str(ep.get("id", "ep%d" % i))[:64],
                     "source": src, "generation": gen, "T": len(sim),
                     "mean_drift": round(drift, 4)})
    n = len(rows)
    n_synth = sum(1 for r in rows if r["source"] == "synthetic")
    alpha = n_synth / n
    real_d = [r["mean_drift"] for r in rows if r["source"] == "real"]
    synth_d = [r["mean_drift"] for r in rows if r["source"] == "synthetic"]
    gen_mean = {}
    for r in rows:
        if r["source"] == "synthetic":
            gen_mean.setdefault(r["generation"], []).append(r["mean_drift"])
    gen_curve = [{"generation": g,
                  "mean_drift": round(sum(v) / len(v), 4), "n": len(v)}
                 for g, v in sorted(gen_mean.items())]
    slope = 0.0
    if len(gen_curve) >= 2:
        slope = gen_curve[-1]["mean_drift"] - gen_curve[0]["mean_drift"]
    if alpha <= ALPHA_GREEN:
        band, label = "green", "GOVERNED"
    elif alpha <= ALPHA_AMBER:
        band, label = "amber", "REVIEW"
    else:
        band, label = "red", "BLOCKED"
    if alpha > ALPHA_AMBER:
        risk = "HIGH"
    elif alpha > ALPHA_GREEN or slope > 0:
        risk = "ELEVATED"
    else:
        risk = "LOW"
    return {"n": n, "n_real": n - n_synth, "n_synthetic": n_synth,
            "alpha": round(alpha, 4),
            "drift_real_mean": round(sum(real_d) / len(real_d), 4) if real_d else None,
            "drift_synth_mean": round(sum(synth_d) / len(synth_d), 4) if synth_d else None,
            "generation_curve": gen_curve, "generation_slope": round(slope, 4),
            "verdict": {"label": label, "band": band,
                        "detail": "alpha %.2f vs policy 0.50/0.80 (DRAFT)" % alpha},
            "collapse_risk": risk,
            "episodes": rows,
            "policy": ("DRAFT: alpha<=0.50 governed, <=0.80 review, above "
                       "blocked; collapse risk HIGH above 0.80, ELEVATED "
                       "above 0.50 or when generation drift rises")}


def collapse_demo(seed: int = 1, gens: int = 10, n: int = 400,
                  bins: int = 40) -> dict:
    """ILLUSTRATION (not a training run): recursive histogram resampling.

    A bimodal population is refit to an empirical histogram each
    generation and resampled from it. Bins seen fewer than twice are
    dropped, modelling finite capacity: rare events the synthetic data
    barely shows vanish from the next model's world. Tails and the
    minority mode starve within a few generations - the textbook model
    collapse shape. Deterministic for fixed seed.
    """
    rng = random.Random(seed)
    pop = [rng.gauss(-2.0, 0.5) if rng.random() < 0.35 else rng.gauss(2.0, 0.5)
           for _ in range(n)]
    curve = []
    for g in range(gens):
        lo, hi = min(pop), max(pop)
        w = (hi - lo) / bins or 1.0
        counts = [0] * bins
        for x in pop:
            counts[min(int((x - lo) / w), bins - 1)] += 1
        occupied = sum(1 for c in counts if c)
        mu = sum(pop) / len(pop)
        var = sum((x - mu) ** 2 for x in pop) / len(pop)
        minority = sum(1 for x in pop if x < 0) / len(pop)
        curve.append({"generation": g, "occupied_bins": occupied,
                      "variance": round(var, 4),
                      "minority_mass": round(minority, 4)})
        pool = []
        for i, c in enumerate(counts):
            if c >= 2:
                pool.extend([lo + (i + 0.5) * w] * c)
        if not pool:
            pool = [lo + (i + 0.5) * w for i, c in enumerate(counts) if c]
        pop = [rng.choice(pool) + rng.gauss(0.0, w * 0.05) for _ in range(n)]
    kept = curve[-1]["occupied_bins"] / max(curve[0]["occupied_bins"], 1)
    minnow = curve[-1]["minority_mass"] / max(curve[0]["minority_mass"], 1e-9)
    if kept < 0.75 or minnow < 0.5:
        label, band = "COLLAPSE SHOWN", "red"
    else:
        label, band = "MILD DECAY", "amber"
    return {"kind": "illustration",
            "note": "Simulated recursive resampling, not a policy training run",
            "seed": seed, "curve": curve,
            "verdict": {"label": label, "band": band,
                        "detail": "bins kept %.2f, minority kept %.2f at gen %d"
                                  % (kept, minnow, gens - 1)}}
