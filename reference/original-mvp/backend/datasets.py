"""Dataset registry for the Evidence page (stdlib only).

Walks dataset/scenarios directly (robust to generate.py regen), joins card
provenance, and serves short demo labels plus the per-demo dataset guide:
which dataset to load for which live demo. No scoring here, lookup only.
"""

from __future__ import annotations

import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET = os.path.join(BASE, "dataset")
SCEN = os.path.join(DATASET, "scenarios")
SAMPLES = os.path.join(DATASET, "samples")

SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.\-]{0,120}$")


def _load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _task_short(card: dict) -> str:
    attrs = card.get("h5_attrs") or {}
    task = attrs.get("current_task") or card.get("description") or ""
    low = task.lower()
    if "pour" in low:
        return "pour"
    if "pick" in low or "place" in low:
        return "pick-place"
    if "wipe" in low:
        return "wipe"
    if "fold" in low:
        return "fold"
    if "open" in low or "drawer" in low or "door" in low:
        return "open/close"
    return "manipulation"


def _time_short(pid: str) -> str:
    m = re.search(r"(\d{2})_(\d{2})_(\d{2})_2023$", pid)
    if m:
        return "%s:%s" % (m.group(1), m.group(2))
    m = re.search(r"_s(\d+)$", pid)
    if m:
        return "s" + m.group(1)
    return pid[-8:]


def _kind_of(card: dict) -> str:
    src = str(card.get("source", ""))
    if src.startswith("http"):
        return "real"
    return "synthetic"


def list_datasets() -> list:
    """Every pair folder: id, label, kind, T, task, source. Real first."""
    out = []
    if not os.path.isdir(SCEN):
        return out
    for pid in sorted(os.listdir(SCEN)):
        folder = os.path.join(SCEN, pid)
        if not os.path.isdir(folder):
            continue
        try:
            card = _load_json(os.path.join(folder, "card.json"))
        except (OSError, ValueError):
            continue
        kind = _kind_of(card)
        if kind == "real":
            label = "Real DROID %s %s" % (_task_short(card), _time_short(pid))
            if pid == "droid_pour_s1":
                label = "Real DROID pour 09:42"
        elif pid.startswith("morph_"):
            label = "Morph proxy %s (synthetic)" % pid[len("morph_"):]
        else:
            label = "Synthetic %s" % pid
        out.append({
            "id": pid,
            "label": label,
            "kind": kind,
            "T": card.get("T"),
            "task": _task_short(card) if kind == "real" else card.get("scenario"),
            "source": card.get("source"),
            "license": card.get("license"),
        })
    out.sort(key=lambda e: (0 if e["kind"] == "real" else 1, e["id"]))
    return out


def get_pair(pid: str):
    """Full pair + card for one id, or None. Rejects path traversal."""
    if not pid or not SAFE_ID.match(pid):
        return None
    folder = os.path.join(SCEN, pid)
    scen_real = os.path.realpath(SCEN)
    if os.path.realpath(folder) != scen_real and \
            not os.path.realpath(folder).startswith(scen_real + os.sep):
        return None
    try:
        pair = _load_json(os.path.join(folder, "pair.json"))
        card = _load_json(os.path.join(folder, "card.json"))
    except (OSError, ValueError):
        return None
    return {"pair": pair, "card": card}


def list_samples() -> list:
    """Curated upload-ready batch files for the live demo."""
    info = {
        "sample-a-real-pour": "Sample A: real-only batch (alpha 0.0) - governed baseline",
        "sample-b-mixed-batch": "Sample B: mixed batch (alpha 0.6) - review demo",
        "sample-c-synth-heavy": "Sample C: synth-heavy batch (alpha 0.9) - blocked + collapse risk",
        "sample-d-generations": "Sample D: 4 synthetic generations - collapse curve demo",
    }
    out = []
    for sid, blurb in info.items():
        path = os.path.join(SAMPLES, sid + ".json")
        if os.path.isfile(path):
            out.append({"id": sid, "blurb": blurb,
                        "bytes": os.path.getsize(path)})
    return out


def get_sample(sid: str):
    if not sid or not SAFE_ID.match(sid):
        return None
    path = os.path.join(SAMPLES, sid + ".json")
    if not os.path.isfile(path):
        return None
    try:
        return _load_json(path)
    except ValueError:
        return None


def demo_guide() -> list:
    """Per-demo dataset map. Shown on the Evidence page and in the pitch.
    Ids here must exist; tests enforce it."""
    return [
        {"demo": "Sim-to-real gap on REAL data",
         "use": "droid_pour_s1",
         "expect": "TRUSTED, Frechet under 0.30 m",
         "why": "DROID commanded vs actual EE, 472 steps, 3.8 cm mean error"},
        {"demo": "Sim-to-real gap, degraded synthetic",
         "use": "bias_drift_s1",
         "expect": "REVIEW, Frechet near 0.50",
         "why": "Same engine, bias-ramp degradation stack - contrast with real"},
        {"demo": "Cross-embodiment baseline (same arm)",
         "use": "droid_pour_s1 + droid_success_2023_07_07_fri_jul_7_09_43_39_2023",
         "expect": "scale agrees (ratio near 0.87), shape varies by task",
         "why": "Two real Franka episodes - scale pins the embodiment"},
        {"demo": "Cross-embodiment morph proxy",
         "use": "droid_pour_s1 + morph_pour_short_s1",
         "expect": "span ratio near 0.55, scale band red",
         "why": "Real Franka vs short-arm morph - harness live, OXE pairs plug in"},
        {"demo": "Batch governance, mixed data",
         "use": "Sample B",
         "expect": "alpha 0.6, REVIEW",
         "why": "Upload sample-b-mixed-batch.json - ratio enforced per batch"},
        {"demo": "Batch governance, synth-heavy",
         "use": "Sample C",
         "expect": "alpha 0.9, BLOCKED + collapse risk HIGH",
         "why": "Upload sample-c-synth-heavy.json - ung governed tail caught"},
        {"demo": "Model collapse curve",
         "use": "Sample D",
         "expect": "diversity falls across generations",
         "why": "Upload sample-d-generations.json - recursive synthetic decay"},
    ]
