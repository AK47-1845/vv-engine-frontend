"""Build upload-ready sample batches + synthetic morph pairs (deterministic).

Reads dataset/scenarios pairs, writes:
  samples/sample-a-real-pour.json      2 real DROID episodes, alpha 0.0
  samples/sample-b-mixed-batch.json    2 real + 3 synthetic, alpha 0.6
  samples/sample-c-synth-heavy.json    1 real + 9 synthetic, alpha 0.9
  samples/sample-d-generations.json    real gen0 + synth gens 1-3, rising noise
  scenarios/morph_pour_short_s1        0.55x short-arm replay of droid_pour_s1
  scenarios/morph_pour_tall_s1         1.40x long-arm replay of droid_pour_s1
  scenarios/morph_pour_narrow_s1       aspect-variant replay of droid_pour_s1
Morphs are SYNTHETIC cross-kinematic proxies in meters, honestly labeled.
Real OXE WidowX/RT-1 pairs plug into the same xemb endpoint in Month 1.

Run from the dataset folder:  python tools/make_samples.py
Rerunnable: same bytes every run. Then run validate.py.
"""

import json
import os
import random
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCEN = os.path.join(ROOT, "scenarios")
OUT = os.path.join(ROOT, "samples")

REAL_A = "droid_pour_s1"
REAL_B = "droid_success_2023_07_07_fri_jul_7_09_43_39_2023"
SYNTH_3 = ["bias_drift_s1", "dropout_heavy_s1", "latency_lag_s1"]
SYNTH_9 = ["bias_drift_s1", "dropout_heavy_s1", "latency_lag_s1",
           "reach_straight_s1", "reach_curve_s1", "pick_place_s1",
           "hesitant_operator_s1", "contact_slide_s1", "aggressive_fast_s1"]
MORPHS = {
    "morph_pour_short_s1": {"scale": (0.55, 0.55), "offset": (0.10, 0.05),
                            "desc": "0.55x short-arm replay"},
    "morph_pour_tall_s1": {"scale": (1.40, 1.40), "offset": (-0.15, 0.10),
                           "desc": "1.40x long-arm replay"},
    "morph_pour_narrow_s1": {"scale": (0.50, 1.00), "offset": (0.12, 0.0),
                             "desc": "aspect-variant replay (0.50x/1.00x)"},
}
OLD_MORPHS = ("morph_reach_s1", "morph_curve_s1", "morph_pick_s1")


def load_pair(pid):
    return json.load(open(os.path.join(SCEN, pid, "pair.json"), encoding="utf-8"))


def ep(pid, source, generation=0, sim=None, real=None):
    p = load_pair(pid)
    return {"id": pid, "source": source, "generation": generation,
            "sim": sim if sim is not None else p["sim"],
            "real": real if real is not None else p["real"]}


def write_sample(sid, blurb, episodes):
    os.makedirs(OUT, exist_ok=True)
    doc = {"id": sid, "blurb": blurb,
           "format": "vv-batch/1: episodes[{id, source, generation, sim, real}]",
           "episodes": episodes}
    path = os.path.join(OUT, sid + ".json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh)
    print("wrote %s (%d eps, %d bytes)" % (sid, len(episodes),
                                           os.path.getsize(path)))


def make_batches():
    write_sample("sample-a-real-pour", "real-only baseline, alpha 0.0",
                 [ep(REAL_A, "real"), ep(REAL_B, "real")])
    write_sample("sample-b-mixed-batch", "mixed batch, alpha 0.6",
                 [ep(REAL_A, "real"), ep(REAL_B, "real")] +
                 [ep(pid, "synthetic") for pid in SYNTH_3])
    write_sample("sample-c-synth-heavy", "synth-heavy batch, alpha 0.9",
                 [ep(REAL_A, "real")] +
                 [ep(pid, "synthetic") for pid in SYNTH_9])
    rng = random.Random(7)
    base = load_pair(REAL_A)
    gens = [ep(REAL_A, "real", 0)]
    for g in (1, 2, 3):
        sig = 0.02 * g
        noisy = [[x + rng.gauss(0.0, sig), y + rng.gauss(0.0, sig)]
                 for x, y in base["real"]]
        gens.append({"id": "droid_pour_s1_gen%d" % g, "source": "synthetic",
                     "generation": g, "sim": base["sim"], "real": noisy,
                     "note": "synthetic generation %d: real executed + N(0,%.2f)" % (g, sig)})
    write_sample("sample-d-generations", "generation ladder, collapse curve", gens)


def make_morphs():
    for old in OLD_MORPHS:
        folder = os.path.join(SCEN, old)
        if os.path.isdir(folder):
            shutil.rmtree(folder)
            print("removed %s" % old)
    base = load_pair(REAL_A)
    for mid, spec in MORPHS.items():
        (sx, sy), (ox, oy) = spec["scale"], spec["offset"]
        sim = [[round(x * sx + ox, 4), round(y * sy + oy, 4)]
               for x, y in base["sim"]]
        real = [[round(x * sx + ox, 4), round(y * sy + oy, 4)]
                for x, y in base["real"]]
        folder = os.path.join(SCEN, mid)
        os.makedirs(folder, exist_ok=True)
        pair = {"id": mid, "T": len(sim), "dt": None,
                "dt_note": "native order kept, rate not asserted",
                "fields": ["x", "y"],
                "frame": "meters, synthetic morph proxy",
                "sim": sim, "real": real}
        with open(os.path.join(folder, "pair.json"), "w", encoding="utf-8") as fh:
            json.dump(pair, fh)
        card = {"id": mid, "scenario": "morph_proxy (SYNTHETIC)",
                "seed": 0, "seed_note": "derived from a real capture, fixed",
                "T": len(sim),
                "description": "Synthetic cross-kinematic proxy: %s of %s. "
                               "NOT real data." % (spec["desc"], REAL_A),
                "source": "synthetic/tools/make_samples.py v2",
                "generator": "tools/make_samples.py v2",
                "license": "synthetic, same as generator set",
                "morph_of": REAL_A,
                "transforms": ["x*%.2f+%.2f, y*%.2f+%.2f applied to sim and real"
                               % (sx, ox, sy, oy)]}
        with open(os.path.join(folder, "card.json"), "w", encoding="utf-8") as fh:
            json.dump(card, fh, indent=1, sort_keys=True)
        print("wrote %s (%s)" % (mid, spec["desc"]))


def main():
    make_batches()
    make_morphs()


if __name__ == "__main__":
    main()
