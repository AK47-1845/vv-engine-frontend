"""Dataset integrity check (format only, no scoring).

Walks dataset/scenarios, verifies every pair.json parses, sim and real
match in length, all values are finite numbers, and every card carries
provenance (source, license, seed). Exit code 0 means clean.

Run from the dataset folder:  python validate.py
"""

import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "scenarios")
CARD_KEYS = ("id", "scenario", "seed", "T", "source", "license")


def check_pair(folder):
    pid = os.path.basename(folder)
    pair_p = os.path.join(folder, "pair.json")
    card_p = os.path.join(folder, "card.json")
    if not os.path.isfile(pair_p):
        return "missing pair.json"
    if not os.path.isfile(card_p):
        return "missing card.json"
    try:
        pair = json.load(open(pair_p, encoding="utf-8"))
        card = json.load(open(card_p, encoding="utf-8"))
    except (json.JSONDecodeError, ValueError) as exc:
        return "bad json: %s" % exc
    for key in CARD_KEYS:
        if key not in card:
            return "card missing key: %s" % key
    sim, real = pair.get("sim"), pair.get("real")
    if not isinstance(sim, list) or not isinstance(real, list):
        return "sim/real must be lists"
    if len(sim) != len(real) or len(sim) < 50:
        return "length mismatch or too short: %d vs %d" % (len(sim), len(real))
    for traj in (sim, real):
        for pt in traj:
            if (not isinstance(pt, list) or len(pt) != 2
                    or not all(isinstance(v, (int, float)) and math.isfinite(v)
                               for v in pt)):
                return "non numeric point in %s" % pid
    return None


def main():
    if not os.path.isdir(OUT):
        print("no scenarios folder, run generate.py first")
        sys.exit(1)
    bad = 0
    total = 0
    for name in sorted(os.listdir(OUT)):
        folder = os.path.join(OUT, name)
        if not os.path.isdir(folder):
            continue
        total += 1
        err = check_pair(folder)
        if err:
            bad += 1
            print("FAIL %s: %s" % (name, err))
    print("checked %d pairs, %d bad" % (total, bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
