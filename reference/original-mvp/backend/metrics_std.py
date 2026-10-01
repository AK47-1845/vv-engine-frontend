"""Genuity Verify MVP · trust-score metrics core (stdlib port, no numpy).

Same formulas as verify-mvp/metrics.py, pure Python so the demo server has
zero dependencies. Trajectory = list of [x, y] points, T=200, D=2.

One DELIBERATE change vs Day-1: action_sensitivity() now compares a nominal
rollout against a PROBED rollout (same seed, perturbed actions) instead of
two different seeds. Seed-shuffle was a weak proxy; the probe is a real
control-response test. See docs/TECHNICAL_PROMPT.md §5.
"""

from __future__ import annotations

import math


def _l2(a, b) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def drift_at_horizon(pred, true, threshold: float = 0.5, breach_run: int = 3) -> dict:
    """Per-timestep L2 error + coherence horizon.

    Breach = first t where err exceeds threshold for `breach_run` CONSECUTIVE
    steps (debounced). Single-frame spikes are sensor glitches, not drift -
    real V&V gates debounce transients. Sustained breach (drift, playback)
    trips exactly as before.
    """
    err = [_l2(p, t) for p, t in zip(pred, true)]
    over = len(err)
    for i in range(len(err) - breach_run + 1):
        if all(e > threshold for e in err[i:i + breach_run]):
            over = i
            break
    return {
        "mean_err": sum(err) / len(err),
        "final_err": err[-1],
        "coherence_horizon": over,
        "horizon_ratio": over / len(err),
    }


def discrete_frechet(p, q) -> float:
    """Classic discrete Frechet distance between two polygonal curves."""
    n, m = len(p), len(q)
    ca = [[-1.0] * m for _ in range(n)]
    ca[0][0] = _l2(p[0], q[0])
    for i in range(1, n):
        ca[i][0] = max(ca[i - 1][0], _l2(p[i], q[0]))
    for j in range(1, m):
        ca[0][j] = max(ca[0][j - 1], _l2(p[0], q[j]))
    for i in range(1, n):
        row, prow = ca[i], ca[i - 1]
        for j in range(1, m):
            row[j] = max(
                min(prow[j], prow[j - 1], row[j - 1]),
                _l2(p[i], q[j]),
            )
    return ca[n - 1][m - 1]


def action_sensitivity(nominal, probed) -> dict:
    """E[||T(a) - T(a+probe)||^2], normalized by rollout energy.

    Same seed, perturbed actions. Near 0 -> policy IGNORES control (BAD).
    Large -> policy responds to actions (GOOD). Playback scores exactly 0.0.
    """
    diffs = [sum((x - y) ** 2 for x, y in zip(a, b)) for a, b in zip(nominal, probed)]
    raw = sum(diffs) / len(diffs)
    energy = sum(x * x for pt in nominal for x in pt) / len(nominal) + 1e-9
    return {"raw": raw, "normalized": raw / energy}


def rollout_spread(rollouts) -> dict:
    """Inter-seed variance across N stochastic rollouts of the same policy."""
    n = len(rollouts)
    t_len = len(rollouts[0])
    per_t = []
    for t in range(t_len):
        xs = [r[t][0] for r in rollouts]
        ys = [r[t][1] for r in rollouts]
        mx, my = sum(xs) / n, sum(ys) / n
        per_t.append(
            (sum((x - mx) ** 2 for x in xs) + sum((y - my) ** 2 for y in ys)) / (2 * n)
        )
    return {"mean_spread": sum(per_t) / len(per_t), "final_spread": per_t[-1]}


def executability_proxy(traj, bounds=(-2.0, 2.0)) -> dict:
    """PROXY ONLY · jerk + workspace violations. Real contact-dynamics proof
    needs a physics sim (Phase 2). Never present as a dynamics proof."""
    lo, hi = bounds
    vel = [[(traj[i + 1][d] - traj[i][d]) for d in range(2)] for i in range(len(traj) - 1)]
    acc = [[(vel[i + 1][d] - vel[i][d]) for d in range(2)] for i in range(len(vel) - 1)]
    jerk = [[(acc[i + 1][d] - acc[i][d]) for d in range(2)] for i in range(len(acc) - 1)]
    jmags = [math.sqrt(j[0] ** 2 + j[1] ** 2) for j in jerk]
    violations = sum(1 for pt in traj if pt[0] < lo or pt[0] > hi or pt[1] < lo or pt[1] > hi)
    return {
        "max_jerk": max(jmags) if jmags else 0.0,
        "mean_jerk": (sum(jmags) / len(jmags)) if jmags else 0.0,
        "bound_violations": violations,
        "violation_rate": violations / len(traj),
        "proxy_warning": "PROXY - not a contact-dynamics proof",
    }


# DRAFT thresholds: (green_if_below, amber_if_below, else red). Lower = better,
# EXCEPT coherence_horizon_ratio and action_sensitivity where higher = better.
# Identical to verify-mvp/report.py. DRAFT until Month-1 OXE calibration.
DRAFT_RULES = {
    "frechet_sim_real": ("lo", 0.30, 1.00, "Sim-to-real path distance (Idea 1 patent vector #1)"),
    "mean_drift": ("lo", 0.15, 0.50, "Mean drift error (Genesis FM-1)"),
    "final_drift": ("lo", 0.30, 1.00, "Terminal drift at horizon end"),
    "coherence_horizon_ratio": ("hi", 0.80, 0.50, "Horizon fraction before drift breach"),
    "action_sensitivity": ("hi", 0.10, 0.01, "Response to control input (Genesis FM-4)"),
    "mean_spread": ("lo", 0.05, 0.20, "Inter-seed uncertainty spread"),
    "max_jerk_proxy": ("lo", 1.00, 5.00, "PROXY: motion jerk (not a dynamics proof)"),
    "bound_violation_rate": ("lo", 0.01, 0.10, "Workspace-bound violation rate"),
}


def band(direction: str, value: float, green: float, amber: float) -> str:
    if direction == "lo":
        if value <= green:
            return "green"
        if value <= amber:
            return "amber"
        return "red"
    if value >= green:
        return "green"
    if value >= amber:
        return "amber"
    return "red"


def verdict(score: dict) -> tuple:
    """Overall verdict: worst band wins (fail-closed)."""
    bands = [band(d, score[k], g, a) for k, (d, g, a, _) in DRAFT_RULES.items()]
    if "red" in bands:
        return ("BLOCKED", "Fails trust gates", "red")
    if "amber" in bands:
        return ("REVIEW", "Marginal · needs engineer sign-off", "amber")
    return ("TRUSTED", "Passes all gates", "green")


def score_policy(name, pred, true, probed, seeds) -> dict:
    """One-call full scorecard. Returns rounded plain floats."""
    drift = drift_at_horizon(pred, true)
    sens = action_sensitivity(pred, probed)
    spread = rollout_spread(seeds)
    exe = executability_proxy(pred)
    frechet = discrete_frechet(pred, true)
    return {
        "policy": name,
        "frechet_sim_real": round(frechet, 4),
        "mean_drift": round(drift["mean_err"], 4),
        "final_drift": round(drift["final_err"], 4),
        "coherence_horizon_ratio": round(drift["horizon_ratio"], 3),
        "action_sensitivity": round(sens["normalized"], 4),
        "mean_spread": round(spread["mean_spread"], 4),
        "max_jerk_proxy": round(exe["max_jerk"], 4),
        "bound_violation_rate": round(exe["violation_rate"], 4),
    }


def gates(score: dict) -> list:
    """Per-metric gate rows for the report card."""
    rows = []
    for key, (direction, green, amber, desc) in DRAFT_RULES.items():
        rows.append({
            "metric": key,
            "value": score[key],
            "band": band(direction, score[key], green, amber),
            "desc": desc,
            "tag": "Estimated",  # DRAFT thresholds
        })
    return rows
