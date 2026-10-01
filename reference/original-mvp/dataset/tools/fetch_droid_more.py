"""Fetch MORE real DROID episodes into the dataset (collection only).

Discovers episode URLs honestly (no guessing):
  1. GCS public listing of the known day-folder, else
  2. trajectory.h5 URLs published in droid-dataset docs.
Downloads up to MAX_NEW episodes, converts with the same mapping as
convert_droid_ep.py, writes pair+card, updates manifest real_captures.

Needs _incoming/pylibs (h5py, numpy) + network. Run from dataset folder:
  python tools/fetch_droid_more.py
Prints a JSON summary. Exit 0 even if nothing new found (verdict field).
"""

import io
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "_incoming", "pylibs"))

KNOWN_URL = ("https://storage.googleapis.com/gresearch/robotics/droid_raw/1.0.1/"
             "AUTOLab/success/2023-07-07/Fri_Jul__7_09:42:23_2023/trajectory.h5")
LIST_URL = ("https://storage.googleapis.com/storage/v1/b/gresearch/o"
            "?prefix=robotics/droid_raw/1.0.1/AUTOLab/success/2023-07-07/"
            "&maxResults=200")
DOC_URLS = [
    "https://raw.githubusercontent.com/droid-dataset/droid/main/README.md",
    "https://raw.githubusercontent.com/droid-dataset/droid/main/DATASET.md",
    "https://raw.githubusercontent.com/droid-dataset/droid/main/docs/dataset.md",
]
MAX_NEW = 4
MIN_BYTES = 1000000


def wget(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": "ltts-vv-mvp/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()


def discover():
    """Return (method, [trajectory.h5 https urls])."""
    try:
        status, raw = wget(LIST_URL)
        if status == 200:
            items = json.loads(raw.decode("utf-8")).get("items", [])
            urls = ["https://storage.googleapis.com/gresearch/" + it["name"]
                    for it in items if it.get("name", "").endswith("trajectory.h5")]
            urls = sorted(set(urls))
            if urls:
                return ("gcs-listing", urls)
    except Exception as exc:
        print("listing failed: %s" % exc)
    found = []
    for doc in DOC_URLS:
        try:
            status, raw = wget(doc)
            if status != 200:
                continue
            text = raw.decode("utf-8", "replace")
            for m in re.findall(r"https://[^\s\"']+trajectory\.h5", text):
                found.append(m)
            for m in re.findall(r"gs://([^\s\"']+trajectory\.h5)", text):
                found.append("https://storage.googleapis.com/" + m)
        except Exception as exc:
            print("doc fetch failed %s: %s" % (doc, exc))
    return ("docs", sorted(set(found)))


def pick(urls):
    urls = [u for u in urls if u != KNOWN_URL]
    if len(urls) <= MAX_NEW:
        return urls
    step = len(urls) / float(MAX_NEW)
    return [urls[int(i * step)] for i in range(MAX_NEW)]


def slug(url, idx):
    m = re.search(r"/((?:success|failure)/\d{4}-\d{2}-\d{2}/[^/]+)/trajectory\.h5", url)
    if m:
        s = re.sub(r"[^A-Za-z0-9]+", "_", m.group(1)).strip("_").lower()
        return "droid_%s" % s[:48] if not s.startswith("droid") else s[:54]
    return "droid_more_%d" % idx


def find_keys(f):
    paths = []

    def visit(name, obj):
        paths.append(name)
    f.visititems(visit)
    low = [(p.lower(), p) for p in paths]
    tgt = [p for l, p in low if "target" in l and "cartesian" in l]
    act = [p for l, p in low if "cartesian_position" in l and "target" not in l]
    return (tgt[0] if tgt else None, act[0] if act else None, paths)


def convert(url, idx):
    import h5py
    status, raw = wget(url, timeout=120)
    if status != 200 or len(raw) < MIN_BYTES or raw[:4] != b"\x89HDF":
        return {"url": url, "ok": False, "reason": "bad download %s bytes" % len(raw)}
    inc = os.path.join(ROOT, "_incoming", "droid_more_%d.h5" % idx)
    with open(inc, "wb") as fh:
        fh.write(raw)
    with h5py.File(inc, "r") as f:
        tk, ak, paths = find_keys(f)
        if not tk or not ak:
            return {"url": url, "ok": False, "reason": "keys missing",
                    "paths_sample": paths[:40]}
        sim = f[tk][:, 0:2].tolist()
        real = f[ak][:, 0:2].tolist()
        attrs = {k: str(v)[:200] for k, v in dict(f.attrs).items()}
    if len(sim) != len(real) or len(sim) < 50:
        return {"url": url, "ok": False, "reason": "bad lengths"}
    sim = [[round(float(x), 4), round(float(y), 4)] for x, y in sim]
    real = [[round(float(x), 4), round(float(y), 4)] for x, y in real]
    pid = slug(url, idx)
    folder = os.path.join(ROOT, "scenarios", pid)
    os.makedirs(folder, exist_ok=True)
    pair = {"id": pid, "T": len(sim), "dt": None,
            "dt_note": "native order kept, rate not asserted",
            "fields": ["x", "y"], "frame": "meters, Franka base frame",
            "sim": sim, "real": real}
    with open(os.path.join(folder, "pair.json"), "w", encoding="utf-8") as fh:
        json.dump(pair, fh)
    card = {"id": pid, "scenario": "droid_real (public real capture)",
            "seed": 0, "seed_note": "seeds do not apply to real captures",
            "T": len(sim),
            "description": "DROID raw episode, Franka arm, real commanded vs actual EE xy",
            "source": url, "generator": "tools/fetch_droid_more.py v1",
            "license": "DROID raw, see https://github.com/droid-dataset/droid",
            "mapping": {"sim": "%s[:, 0:2]" % tk, "real": "%s[:, 0:2]" % ak,
                        "dropped": "z, orientation, gripper, torques (format is [x,y])"},
            "transforms": ["rounded to 4 decimals", "no smoothing", "no resample"],
            "h5_attrs": attrs}
    with open(os.path.join(folder, "card.json"), "w", encoding="utf-8") as fh:
        json.dump(card, fh, indent=1, sort_keys=True)
    mpath = os.path.join(ROOT, "manifest.json")
    manifest = json.load(open(mpath, encoding="utf-8"))
    manifest.setdefault("real_captures", [])
    if all(e.get("id") != pid for e in manifest["real_captures"]):
        manifest["real_captures"].append({"id": pid, "T": len(sim), "source": url})
    with open(mpath, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
    return {"url": url, "ok": True, "id": pid, "T": len(sim),
            "keys": [tk, ak]}


def main():
    method, urls = discover()
    print("discovery=%s candidates=%d" % (method, len(urls)))
    chosen = pick(urls)
    print("chosen=%d" % len(chosen))
    results = [convert(u, i) for i, u in enumerate(chosen)]
    ok = [r for r in results if r.get("ok")]
    print(json.dumps({"method": method, "downloaded": len(ok),
                      "results": results}, indent=1)[:4000])


if __name__ == "__main__":
    main()
