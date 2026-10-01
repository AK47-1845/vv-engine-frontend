"""Deterministic policy fixtures as functions of (actions, seed).

Position-command interface: actions[t] is the commanded [x, y]. The reference
command sequence is a sin/cos path. The sensitivity PROBE is a step offset on
the second half of the command sequence · policies that obey controls respond,
playback ignores it (exactly 0.0 response).

All randomness via random.Random(seed): byte-identical across runs/machines.
noise_scale knob exists ONLY for the Module-2-lite threshold sweep; default 1.0.
"""

from __future__ import annotations

import math
import random

T = 200
PROBE_OFFSET = (0.5, -0.3)  # step added to second-half commands


def reference_actions():
    return [
        [math.sin(4 * math.pi * t / (T - 1)), math.cos(2 * math.pi * t / (T - 1))]
        for t in range(T)
    ]


def probe_actions(actions):
    out = [row[:] for row in actions]
    for t in range(T // 2, T):
        out[t][0] += PROBE_OFFSET[0]
        out[t][1] += PROBE_OFFSET[1]
    return out


def _gauss(rng, sigma):
    return rng.gauss(0.0, sigma)


def clean_rollout(actions, seed: int = 0, noise_scale: float = 1.0):
    rng = random.Random(seed)
    s = 0.03 * noise_scale
    return [[a[0] + _gauss(rng, s), a[1] + _gauss(rng, s)] for a in actions]


def drifty_rollout(actions, seed: int = 0, noise_scale: float = 1.0):
    rng = random.Random(seed)
    s = 0.05 * noise_scale
    wx, wy = 0.0, 0.0
    out = []
    for a in actions:
        wx += _gauss(rng, s)
        wy += _gauss(rng, s)
        out.append([a[0] + wx, a[1] + wy])  # error compounds with horizon
    return out


def playback_rollout(actions, seed: int = 0, noise_scale: float = 1.0):
    _ = (actions, seed, noise_scale)  # ignores everything: fixed tape
    return [[t / (T - 1), 0.0] for t in range(T)]


def synthfed_rollout(actions, seed: int = 0, noise_scale: float = 1.0):
    """Synthetic-data-trained profile: responsive but higher spread + dropout
    spikes + small sim-to-real bias ramp. The 'synthetic in, governance out'
    demo case. Tuned to land REVIEW (amber), not green or red."""
    rng = random.Random(seed)
    s = 0.08 * noise_scale
    out = []
    for t, a in enumerate(actions):
        x = a[0] + _gauss(rng, s) + 0.10 * (t / T)   # sim bias ramp
        y = a[1] + _gauss(rng, s) - 0.06 * (t / T)
        if rng.random() < 0.05:  # sensor dropout spike
            sx = 1.0 if rng.random() < 0.5 else -1.0
            sy = 1.0 if rng.random() < 0.5 else -1.0
            x += sx * rng.uniform(0.35, 0.55) * noise_scale
            y += sy * rng.uniform(0.35, 0.55) * noise_scale
        out.append([x, y])
    return out


POLICIES = {
    "clean": {
        "fn": clean_rollout,
        "title": "Clean policy",
        "story": "Tracks commands with small noise. Expected: TRUSTED.",
    },
    "drifty": {
        "fn": drifty_rollout,
        "title": "Drifty policy",
        "story": "Random-walk error compounds down-horizon. Expected: BLOCKED on drift.",
    },
    "playback": {
        "fn": playback_rollout,
        "title": "Playback policy",
        "story": "Replays a fixed tape, ignores controls. Expected: BLOCKED, sensitivity 0.0.",
    },
    "synthfed": {
        "fn": synthfed_rollout,
        "title": "Synthetic-trained policy",
        "story": "Trained on synthetic data: responsive but spiky. Expected: REVIEW.",
    },
}
