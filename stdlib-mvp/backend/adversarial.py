"""Adversarial edge case hunt: falsification style disturbance search.

Method note: established CPS practice (S-TaLiRo, Breach) finds requirement
violations by optimizing over disturbance inputs. This module is the honest
lite version: seeded random search plus local refinement over a 3-D command
and actuation disturbance space. No gradients, no native deps, fully
deterministic, every hunt ledger logged.

Disturbance model (applied to the reference commands before the policy sees
them; drift is always measured against the TRUE reference, since deployment
is judged against intended path, not disturbed input):
  cmd_bias    [0, 0.5]: systematic ramp offset, grows along the path.
  cmd_noise   [0, 0.3]: Gaussian command noise (own seeded RNG stream).
  noise_scale [1, 6]  : actuation noise multiplier inside the policy.

Trial 0 is always the undisturbed baseline. A policy that already fails
there reports the baseline as its minimal break. A break means the first
trial that leaves green (amber or red).
"""

from __future__ import annotations

import random

import metrics_std
import policies

RANGES = {
    "cmd_bias": (0.0, 0.5),
    "cmd_noise": (0.0, 0.3),
    "noise_scale": (1.0, 6.0),
}
BAND_RANK = {"green": 0, "amber": 1, "red": 2}


def disturb(ref, cmd_bias, cmd_noise, rng):
    out = []
    t_len = len(ref)
    for t, a in enumerate(ref):
        ramp = cmd_bias * (t / t_len)
        out.append([
            a[0] + ramp + rng.gauss(0.0, cmd_noise),
            a[1] - 0.6 * ramp + rng.gauss(0.0, cmd_noise),
        ])
    return out


def score_disturbed(policy_id, cmd_bias, cmd_noise, noise_scale, seed=1):
    """Full scorecard under disturbance. Integer derived RNG seed, so the
    same inputs give identical outputs on any machine and Python build."""
    ref = policies.reference_actions()
    dist_seed = (seed * 1000003
                 + int(round(cmd_bias, 6) * 1e6) * 9176
                 + int(round(cmd_noise, 6) * 1e6) * 131) % (2 ** 31)
    cmds = disturb(ref, cmd_bias, cmd_noise, random.Random(dist_seed))
    probed_cmds = policies.probe_actions(cmds)
    fn = policies.POLICIES[policy_id]["fn"]
    pred = fn(cmds, seed=seed, noise_scale=noise_scale)
    probed = fn(probed_cmds, seed=seed, noise_scale=noise_scale)
    seeds = [fn(cmds, seed=s, noise_scale=noise_scale) for s in range(5)]
    score = metrics_std.score_policy(policy_id, pred, ref, probed, seeds)
    label, detail, band = metrics_std.verdict(score)
    red_gates = [g["metric"] for g in metrics_std.gates(score) if g["band"] == "red"]
    return {
        "score": score,
        "verdict": {"label": label, "detail": detail, "band": band},
        "red_gates": red_gates,
    }


def _norm(params):
    total = 0.0
    for k, (lo, hi) in RANGES.items():
        total += ((params[k] - lo) / (hi - lo)) ** 2
    return total ** 0.5


def hunt(policy_id, hunt_seed=1, budget=24):
    """Search for the smallest disturbance that breaks the policy.

    Returns every trial plus the minimal break (smallest normalized
    disturbance norm among non green trials) or holds=True if the
    policy stayed green across the whole hunt.
    """
    budget = max(4, min(int(budget), 40))
    rng = random.Random(hunt_seed * 7919 + 13)
    trials = []

    def run_trial(params):
        r = score_disturbed(policy_id, seed=1, **params)
        return {
            "params": {k: round(v, 4) for k, v in params.items()},
            "band": r["verdict"]["band"],
            "verdict": r["verdict"]["label"],
            "mean_drift": r["score"]["mean_drift"],
            "frechet": r["score"]["frechet_sim_real"],
            "red_gates": r["red_gates"],
            "norm": round(_norm(params), 4),
        }

    trials.append(run_trial({"cmd_bias": 0.0, "cmd_noise": 0.0, "noise_scale": 1.0}))
    for _ in range(budget):
        trials.append(run_trial(
            {k: round(rng.uniform(lo, hi), 4) for k, (lo, hi) in RANGES.items()}))

    def key(t):
        return (BAND_RANK[t["band"]], t["mean_drift"])

    best = max(trials, key=key)
    for _ in range(8):
        cand = {}
        for k, (lo, hi) in RANGES.items():
            v = best["params"][k] + rng.gauss(0.0, (hi - lo) * 0.1)
            cand[k] = round(min(hi, max(lo, v)), 4)
        trials.append(run_trial(cand))
        if key(trials[-1]) > key(best):
            best = trials[-1]

    broken = [t for t in trials if t["band"] != "green"]
    minimal = min(broken, key=lambda t: t["norm"]) if broken else None
    counts = {"green": 0, "amber": 0, "red": 0}
    for t in trials:
        counts[t["band"]] += 1
    return {
        "policy": policy_id,
        "hunt_seed": hunt_seed,
        "tested": len(trials),
        "counts": counts,
        "holds": minimal is None,
        "minimal_break": minimal,
        "trials": trials,
    }
