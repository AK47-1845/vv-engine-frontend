"""Paired trajectory dataset generator (stdlib only, fully deterministic).

Writes dataset/scenarios/<id>_s<seed>/pair.json + card.json, plus manifest.json.
Every pair holds ONE scenario in two versions:
  sim  : clean tracking of the intended path (small sim noise only)
  real : sim path plus a documented degradation stack (bias ramp, Gaussian
         noise, dropout spikes, time lag, contact stick)

Provenance is honest by construction: every card carries source, generator
version, seed, and exact degradation params. Public real captures slot into
the same layout later (see README), with source:url on their cards.

Run from the dataset folder:  python generate.py
"""

import json
import math
import os
import random
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "scenarios")
VERSION = "generate.py v1"
SEEDS = [1, 2, 3]


# ---------- path builders (all stay inside the +/-2 workspace) ----------

def _wp(points, T):
    segs = len(points) - 1
    out = []
    for i in range(T):
        x = i / (T - 1) * segs
        s = min(int(x), segs - 1)
        f = x - s
        a, b = points[s], points[s + 1]
        out.append([a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f])
    return out


def _curve(T):
    return [[math.sin(4 * math.pi * t / (T - 1)),
             math.cos(2 * math.pi * t / (T - 1))] for t in range(T)]


def _circle(T, r=0.9):
    return [[r * math.cos(2 * math.pi * t / (T - 1)),
             r * math.sin(2 * math.pi * t / (T - 1))] for t in range(T)]


def _eight(T, a=1.0):
    out = []
    for t in range(T):
        u = 2 * math.pi * t / (T - 1)
        d = 1 + math.sin(u) ** 2
        out.append([a * math.cos(u) / d, a * math.sin(u) * math.cos(u) / d])
    return out


def _raster(T, passes=3):
    pts = []
    for p in range(passes):
        y = -0.6 + 1.2 * p / (passes - 1)
        xs = [-0.8, 0.8] if p % 2 == 0 else [0.8, -0.8]
        pts += [[xs[0], y], [xs[1], y]]
    return _wp(pts, T)


def _pick_place(T):
    return _wp([[-1.2, 0.9], [-0.4, 0.9], [-0.4, 0.2], [-0.4, 0.9],
                [0.8, 0.9], [0.8, 0.3], [0.8, 0.9]], T)


def _insert_push(T):
    return _wp([[-1.2, 0.0], [-0.2, 0.0], [0.35, 0.0], [0.35, 0.0],
                [-0.8, 0.4]], T)


def _hesitant(T):
    base = _curve(24)
    anch = []
    for i, p in enumerate(base):
        anch.append(p)
        if i in (5, 11, 17):
            anch.append(p)
    return _wp(anch, T)


# ---------- degradation stack ----------

def degrade(path, rng, bias=(0.0, 0.0), sigma=0.0, dropout_p=0.0,
           spike=0.0, lag=0, stick=None):
    T = len(path)
    out = []
    for t, (x, y) in enumerate(path):
        ramp = t / max(T - 1, 1)
        px = x + bias[0] * ramp + rng.gauss(0.0, sigma)
        py = y + bias[1] * ramp + rng.gauss(0.0, sigma)
        if dropout_p > 0.0 and rng.random() < dropout_p:
            sx = 1.0 if rng.random() < 0.5 else -1.0
            sy = 1.0 if rng.random() < 0.5 else -1.0
            px += sx * rng.uniform(0.5, 1.0) * spike
            py += sy * rng.uniform(0.5, 1.0) * spike
        out.append([px, py])
    if stick is not None:
        (f0, f1, strength) = stick
        i0, i1 = int(f0 * T), int(f1 * T)
        anchor = out[i0][:]
        for i in range(i0, min(i1, T)):
            out[i][0] += (anchor[0] - out[i][0]) * strength
            out[i][1] += (anchor[1] - out[i][1]) * strength
    if lag:
        out = [row[:] for row in out[:1]] * lag + out[:T - lag]
    return [[round(p[0], 4), round(p[1], 4)] for p in out]


SCENARIOS = [
    {"id": "reach_straight", "desc": "Straight line reach, mild degradation",
     "make": lambda T: _wp([[-1.4, 0.0], [1.4, 0.0]], T), "T": 200,
     "real": {"bias": (0.10, -0.06), "sigma": 0.02, "dropout_p": 0.01, "spike": 0.4}},
    {"id": "reach_curve", "desc": "Curved reach (console reference family)",
     "make": _curve, "T": 200,
     "real": {"bias": (0.10, -0.06), "sigma": 0.03, "dropout_p": 0.02, "spike": 0.5}},
    {"id": "pick_place", "desc": "Pick and place waypoint tour with dwells",
     "make": _pick_place, "T": 200,
     "real": {"bias": (0.08, -0.05), "sigma": 0.025, "dropout_p": 0.02, "spike": 0.45}},
    {"id": "wipe_raster", "desc": "Back and forth wipe raster, 3 passes",
     "make": _raster, "T": 200,
     "real": {"bias": (0.12, 0.0), "sigma": 0.03, "dropout_p": 0.02, "spike": 0.4}},
    {"id": "insert_push", "desc": "Approach, push, retract (insertion stand in)",
     "make": _insert_push, "T": 200,
     "real": {"bias": (0.06, -0.04), "sigma": 0.02, "dropout_p": 0.015, "spike": 0.4}},
    {"id": "circle_trace", "desc": "Clean circle trace",
     "make": _circle, "T": 200,
     "real": {"bias": (0.09, -0.07), "sigma": 0.025, "dropout_p": 0.02, "spike": 0.45}},
    {"id": "figure_eight", "desc": "Lemniscate, hard curvature changes",
     "make": _eight, "T": 200,
     "real": {"bias": (0.10, -0.08), "sigma": 0.03, "dropout_p": 0.025, "spike": 0.5}},
    {"id": "hesitant_operator", "desc": "Curve with dwell pauses mid path",
     "make": _hesitant, "T": 200,
     "real": {"bias": (0.07, -0.05), "sigma": 0.03, "dropout_p": 0.02, "spike": 0.45}},
    {"id": "dropout_heavy", "desc": "Curve under heavy sensor dropout",
     "make": _curve, "T": 200,
     "real": {"bias": (0.05, -0.03), "sigma": 0.03, "dropout_p": 0.08, "spike": 0.7}},
    {"id": "bias_drift", "desc": "Curve with strong sim to real bias ramp",
     "make": _curve, "T": 200,
     "real": {"bias": (0.30, -0.20), "sigma": 0.02, "dropout_p": 0.01, "spike": 0.4}},
    {"id": "latency_lag", "desc": "Real lags sim by 6 steps (delay stand in)",
     "make": _curve, "T": 200,
     "real": {"bias": (0.04, -0.02), "sigma": 0.02, "dropout_p": 0.01,
              "spike": 0.4, "lag": 6}},
    {"id": "aggressive_fast", "desc": "Fast curve, real overshoots",
     "make": lambda T: [[p[0] * 1.2, p[1] * 1.2] for p in _curve(T)], "T": 200,
     "real": {"bias": (0.15, -0.10), "sigma": 0.05, "dropout_p": 0.03, "spike": 0.55}},
    {"id": "cautious_slow", "desc": "Slow curve, real nearly matches (control)",
     "make": lambda T: [[p[0] * 0.6, p[1] * 0.6] for p in _curve(T)], "T": 200,
     "real": {"bias": (0.02, -0.01), "sigma": 0.01, "dropout_p": 0.005, "spike": 0.3}},
    {"id": "contact_slide", "desc": "Straight slide with friction stick mid path",
     "make": lambda T: _wp([[-1.2, 0.0], [1.2, 0.0]], T), "T": 200,
     "real": {"bias": (0.05, -0.03), "sigma": 0.02, "dropout_p": 0.01,
              "spike": 0.4, "stick": (0.35, 0.65, 0.5)}},
    {"id": "long_horizon", "desc": "Curve at 400 steps (horizon scaling)",
     "make": _curve, "T": 400,
     "real": {"bias": (0.12, -0.08), "sigma": 0.03, "dropout_p": 0.02, "spike": 0.5}},
]


def build_pair(spec, seed):
    T = spec["T"]
    path = spec["make"](T)
    rng = random.Random(seed * 100003 + len(spec["id"]))
    sim = degrade(path, random.Random(seed * 7717 + 1), sigma=0.01)
    real = degrade(path, rng, **spec["real"])
    return sim, real


def main():
    os.makedirs(OUT, exist_ok=True)
    manifest = {"generator": VERSION, "seeds": SEEDS,
                "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "pairs": []}
    n = 0
    for spec in SCENARIOS:
        for seed in SEEDS:
            pid = "%s_s%d" % (spec["id"], seed)
            sim, real = build_pair(spec, seed)
            folder = os.path.join(OUT, pid)
            os.makedirs(folder, exist_ok=True)
            with open(os.path.join(folder, "pair.json"), "w", encoding="utf-8") as fh:
                json.dump({"id": pid, "T": spec["T"], "dt": 0.05,
                           "fields": ["x", "y"],
                           "frame": "abstract 2D workspace units, bounds +/-2",
                           "sim": sim, "real": real}, fh)
            card = {"id": pid, "scenario": spec["id"], "seed": seed,
                    "T": spec["T"], "description": spec["desc"],
                    "source": "synthetic/generator", "generator": VERSION,
                    "license": "internal demo, no restriction",
                    "sim_params": {"sigma": 0.01}, "real_params": spec["real"]}
            with open(os.path.join(folder, "card.json"), "w", encoding="utf-8") as fh:
                json.dump(card, fh, indent=1, sort_keys=True)
            manifest["pairs"].append({"id": pid, "scenario": spec["id"],
                                      "seed": seed, "T": spec["T"]})
            n += 1
    keep = []
    mpath = os.path.join(ROOT, "manifest.json")
    if os.path.isfile(mpath):
        try:
            keep = json.load(open(mpath, encoding="utf-8")).get("real_captures", [])
        except (json.JSONDecodeError, ValueError):
            keep = []
    manifest["real_captures"] = keep
    manifest["count"] = n
    with open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
    print("wrote %d pairs (%d scenarios x %d seeds)" % (n, len(SCENARIOS), len(SEEDS)))


if __name__ == "__main__":
    main()
