"""One-off adapter: DROID raw episode -> dataset pair (documented example).

Reads _incoming/droid_ep_trajectory.h5 + _incoming/droid_ep_metadata.json.
Writes scenarios/droid_pour_s1/{pair.json, card.json} and appends the
manifest real_captures list (no scoring here, collection only).

Mapping (no smoothing, no resample, native 472 steps):
  sim  = action/target_cartesian_position[:, 0:2]  (commanded EE xy, meters)
  real = action/robot_state/cartesian_position[:, 0:2]  (actual EE xy, meters)
Gripper/torques stay in the raw file (format is [x,y]); seed fixed 0
(seeds do not apply to real captures).

Needs _incoming/pylibs (h5py, numpy). Run from dataset folder:
  python tools/convert_droid_ep.py
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "_incoming", "pylibs"))

import h5py  # noqa: E402

EP_URL = ("https://storage.googleapis.com/gresearch/robotics/droid_raw/1.0.1/"
          "AUTOLab/success/2023-07-07/Fri_Jul__7_09:42:23_2023/trajectory.h5")
META_URL = EP_URL.replace("trajectory.h5",
                          "metadata_AUTOLab+5d05c5aa+2023-07-07-09h-42m-23s.json")


def main():
    h5p = os.path.join(ROOT, "_incoming", "droid_ep_trajectory.h5")
    mep = os.path.join(ROOT, "_incoming", "droid_ep_metadata.json")
    meta = json.load(open(mep, encoding="utf-8"))
    with h5py.File(h5p, "r") as f:
        sim = f["action/target_cartesian_position"][:, 0:2].tolist()
        real = f["action/robot_state/cartesian_position"][:, 0:2].tolist()
    assert len(sim) == len(real) and len(sim) >= 50, "bad lengths"
    sim = [[round(float(x), 4), round(float(y), 4)] for x, y in sim]
    real = [[round(float(x), 4), round(float(y), 4)] for x, y in real]
    pid = "droid_pour_s1"
    folder = os.path.join(ROOT, "scenarios", pid)
    os.makedirs(folder, exist_ok=True)
    pair = {"id": pid, "T": len(sim), "dt": None,
            "dt_note": "native order kept, rate not asserted",
            "fields": ["x", "y"], "frame": "meters, Franka base frame",
            "sim": sim, "real": real}
    json.dump(pair, open(os.path.join(folder, "pair.json"), "w", encoding="utf-8"))
    card = {"id": pid, "scenario": "droid_pour (public real capture)",
            "seed": 0, "seed_note": "seeds do not apply to real captures",
            "T": len(sim),
            "description": "DROID raw success episode, Franka FR3, pour task",
            "source": EP_URL, "metadata_source": META_URL,
            "generator": "tools/convert_droid_ep.py v1",
            "license": "DROID raw, see https://github.com/droid-dataset/droid",
            "task": meta.get("current_task"), "success": meta.get("success"),
            "robot": meta.get("robot_serial"), "lab": meta.get("lab"),
            "mapping": {"sim": "action/target_cartesian_position[:, 0:2]",
                        "real": "action/robot_state/cartesian_position[:, 0:2]",
                        "dropped": "z, orientation, gripper, torques (format is [x,y])"},
            "transforms": ["rounded to 4 decimals", "no smoothing", "no resample"]}
    json.dump(card, open(os.path.join(folder, "card.json"), "w", encoding="utf-8"),
              indent=1, sort_keys=True)
    mpath = os.path.join(ROOT, "manifest.json")
    manifest = json.load(open(mpath, encoding="utf-8"))
    manifest.setdefault("real_captures", [])
    if all(e.get("id") != pid for e in manifest["real_captures"]):
        manifest["real_captures"].append({"id": pid, "T": len(sim),
                                          "source": EP_URL})
    json.dump(manifest, open(mpath, "w", encoding="utf-8"), indent=1, sort_keys=True)
    print("wrote %s with T=%d" % (pid, len(sim)))


if __name__ == "__main__":
    main()
