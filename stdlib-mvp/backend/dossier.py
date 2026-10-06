"""Evidence dossier builder: scorecard results mapped to compliance clauses.

Draft generator, not legal advice and not a certificate. Every claim
carries a verification tag. Deterministic except generated_ts and the
ledger ref the server attaches after hashing.
"""

from __future__ import annotations

import hashlib
import json
import time

import metrics_std
import policies

CLAUSES = {
    "frechet_sim_real": [
        "EU 2023/1230 Item 24: objective test record of path deviation",
        "ISO 25785-1 (draft): neural policy test method output",
    ],
    "mean_drift": ["OTA per-release evidence: tracking error record"],
    "final_drift": ["OTA per-release evidence: terminal error record"],
    "coherence_horizon_ratio": ["OTA per-release evidence: trusted horizon record"],
    "action_sensitivity": ["EU 2023/1230 Item 24: control authority evidence"],
    "mean_spread": ["Insurer input: uncertainty quantification across seeds"],
    "max_jerk_proxy": ["ISO 13849/IEC 61508 dossier input (proxy, needs sim proof)"],
    "bound_violation_rate": ["ISO 13849/IEC 61508 dossier input: workspace containment"],
}

METHOD = [
    "Discrete Frechet per the Eiter and Mannila 1994 algorithm, O(pq).",
    "Sensitivity probe offsets second half commands; an identical response means ignored controls.",
    "Horizon breach needs 3 consecutive over threshold steps, so single frame spikes do not trip it.",
    "Same policy plus same seed replays byte identical numbers on any machine.",
]

LIMITATIONS = [
    "Gate thresholds are DRAFT until Month 1 OXE calibration. [Estimated]",
    "Jerk and bound rows are proxies, not contact dynamics proofs. Phase 2 adds a physics sim. [Reported]",
    "Demo policies are synthetic fixtures. The scoring engine is the real artifact. [Verified]",
    "This dossier is machine generated evidence support, not a conformity certificate. [Verified]",
]

TAG_LEGEND = {
    "Verified": "Recomputed live, deterministic, ledger chained",
    "Reported": "External citation, needs primary source check before print",
    "Estimated": "DRAFT assumption, labeled, never silent",
}


def build(policy_id, seed=1):
    ref = policies.reference_actions()
    probed_actions = policies.probe_actions(ref)
    fn = policies.POLICIES[policy_id]["fn"]
    pred = fn(ref, seed=seed)
    probed = fn(probed_actions, seed=seed)
    seeds = [fn(ref, seed=s) for s in range(5)]
    score = metrics_std.score_policy(policy_id, pred, ref, probed, seeds)
    label, detail, band = metrics_std.verdict(score)
    gates = []
    for g in metrics_std.gates(score):
        gates.append({
            "metric": g["metric"],
            "value": g["value"],
            "band": g["band"],
            "desc": g["desc"],
            "tag": g["tag"],
            "clauses": CLAUSES[g["metric"]],
        })
    return {
        "title": "V&V evidence dossier (machine generated draft)",
        "console": "LTTS Physical AI V&V Console, Module 1",
        "generated_ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "policy": policy_id,
        "seed": seed,
        "verdict": {"label": label, "detail": detail, "band": band},
        "score": score,
        "gates": gates,
        "method": METHOD,
        "limitations": LIMITATIONS,
        "tag_legend": TAG_LEGEND,
    }


def digest(body):
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
