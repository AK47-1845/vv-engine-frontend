"""LTTS Physical AI V&V Console - single-process API + static server (stdlib only).

Run from the MVP folder:   python backend\\server.py
Then open:                 http://127.0.0.1:8000/

No pip, no venv, no numpy. Deterministic seeds. Every scored run is
appended to the hash-chained provenance ledger at data/ledger.jsonl.
"""

from __future__ import annotations

import datetime
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qsl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ledger as ledger_mod
import adversarial
import datasets as datasets_mod
import dossier
import gaps as gaps_mod
import metrics_std
import policies

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND = os.path.join(BASE, "frontend")
LEDGER_PATH = os.path.join(BASE, "data", "ledger.jsonl")
LEDGER = ledger_mod.Ledger(LEDGER_PATH)

EU_DEADLINE = datetime.date(2027, 1, 20)


def score_one(policy_id: str, seed: int = 1, noise_scale: float = 1.0) -> dict:
    ref = policies.reference_actions()
    probed_actions = policies.probe_actions(ref)
    fn = policies.POLICIES[policy_id]["fn"]
    pred = fn(ref, seed=seed, noise_scale=noise_scale)
    probed = fn(probed_actions, seed=seed, noise_scale=noise_scale)
    seeds = [fn(ref, seed=s, noise_scale=noise_scale) for s in range(5)]
    score = metrics_std.score_policy(policy_id, pred, ref, probed, seeds)
    label, detail, band = metrics_std.verdict(score)
    return {
        "policy": policy_id,
        "title": policies.POLICIES[policy_id]["title"],
        "story": policies.POLICIES[policy_id]["story"],
        "seed": seed,
        "noise_scale": noise_scale,
        "score": score,
        "gates": metrics_std.gates(score),
        "verdict": {"label": label, "detail": detail, "band": band},
        "thresholds": "DRAFT",
    }


def downsample(traj, every: int = 4):
    return [[round(p[0], 3), round(p[1], 3)] for p in traj[::every]]


def governance_payload() -> dict:
    days_left = (EU_DEADLINE - datetime.date.today()).days
    return {
        "eu_machinery_reg": "2023/1230",
        "eu_deadline": EU_DEADLINE.isoformat(),
        "days_left": days_left,
        "item_24": "Notified Body assessment mandatory for self-evolving safety AI",
        "ota_rule": "Safety-shifting OTA update = substantial modification -> re-assessment + new CE",
        "nb_queue": "6-12 months (reported)",
        "iso_25785_1": "Unpublished industrial-scope draft (reported)",
        "calibration": "DRAFT - gates calibrate on Open X-Embodiment pairs in Month 1",
        "tag_legend": {
            "Verified": "Recomputed live, deterministic, ledger-chained",
            "Estimated": "DRAFT threshold/assumption - labeled, never silent",
        },
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "LTTS-VV/1.0"

    def _send(self, code: int, body: bytes, ctype: str):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code: int, obj) -> None:
        self._send(code, json.dumps(obj).encode("utf-8"), "application/json")

    def _read_json(self) -> dict:
        try:
            n = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            n = 0
        if not n:
            return {}
        try:
            return json.loads(self.rfile.read(n).decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return {}

    def _query(self) -> dict:
        parts = self.path.split("?", 1)
        if len(parts) < 2:
            return {}
        return dict(parse_qsl(parts[1], keep_blank_values=True))

    # ---------- GET ----------
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        routes = {
            "/": ("index.html", "text/html; charset=utf-8"),
            "/docs": ("docs.html", "text/html; charset=utf-8"),
            "/docs.html": ("docs.html", "text/html; charset=utf-8"),
            "/compliance": ("compliance.html", "text/html; charset=utf-8"),
            "/compliance.html": ("compliance.html", "text/html; charset=utf-8"),
            "/evidence": ("evidence.html", "text/html; charset=utf-8"),
            "/evidence.html": ("evidence.html", "text/html; charset=utf-8"),
            "/app.js": ("app.js", "text/javascript"),
            "/docs.js": ("docs.js", "text/javascript"),
            "/compliance.js": ("compliance.js", "text/javascript"),
            "/evidence.js": ("evidence.js", "text/javascript"),
            "/styles.css": ("styles.css", "text/css"),
            "/assets/ltts-regular-white.png": ("assets/ltts-regular-white.png", "image/png"),
            "/assets/ltts-stacked-white.png": ("assets/ltts-stacked-white.png", "image/png"),
        }
        if path in routes:
            name, ctype = routes[path]
            return self._static(name, ctype)
        if path == "/api/policies":
            return self._json(200, [
                {"id": k, "title": v["title"], "story": v["story"]}
                for k, v in policies.POLICIES.items()
            ])
        if path == "/api/compare":
            return self._handle_compare()
        if path == "/api/datasets":
            ds = datasets_mod.list_datasets()
            return self._json(200, {
                "datasets": ds,
                "samples": datasets_mod.list_samples(),
                "guide": datasets_mod.demo_guide(),
                "counts": {"total": len(ds),
                           "real": sum(1 for d in ds if d["kind"] == "real"),
                           "synthetic": sum(1 for d in ds if d["kind"] != "real")},
            })
        if path == "/api/dataset":
            return self._handle_dataset()
        if path.startswith("/api/sample/"):
            return self._handle_sample(path[len("/api/sample/"):])
        if path == "/api/ledger":
            entries = LEDGER.read_all()
            return self._json(200, {"total": len(entries), "entries": entries[-50:]})
        if path == "/api/ledger/verify":
            return self._json(200, LEDGER.verify())
        if path == "/api/governance":
            return self._json(200, governance_payload())
        if path == "/api/history":
            entries = [e for e in LEDGER.read_all()
                       if e.get("kind") in ("score", "compare", "sweep", "hunt",
                                            "dossier", "pairscore", "xemb",
                                            "batch", "collapse")]
            entries.reverse()
            return self._json(200, {"runs": entries[:20]})
        return self._json(404, {"error": "not found"})

    def _static(self, name: str, ctype: str):
        fpath = os.path.join(FRONTEND, name)
        if not os.path.isfile(fpath):
            return self._json(404, {"error": "missing frontend file: " + name})
        with open(fpath, "rb") as fh:
            self._send(200, fh.read(), ctype)

    def _handle_dataset(self):
        pid = self._query().get("id", "")
        got = datasets_mod.get_pair(pid)
        if got is None:
            return self._json(404, {"error": "unknown dataset: %r" % (pid,)})
        pair, card = got["pair"], got["card"]
        scored = gaps_mod.score_pair(pair["sim"], pair["real"])
        return self._json(200, {
            "id": pid, "card": card,
            "score": scored["score"], "gates": scored["gates"],
            "verdict": scored["verdict"], "thresholds": scored["thresholds"],
            "T": scored["T"],
            "sim": downsample(pair["sim"]),
            "real": downsample(pair["real"]),
        })

    def _handle_sample(self, sid: str):
        doc = datasets_mod.get_sample(sid)
        if doc is None:
            return self._json(404, {"error": "unknown sample: %r" % (sid,)})
        body = json.dumps(doc).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Content-Disposition",
                         "attachment; filename=%s.json" % sid)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _handle_compare(self):
        ref = policies.reference_actions()
        results = []
        for pid in policies.POLICIES:
            r = score_one(pid)
            fn = policies.POLICIES[pid]["fn"]
            r["traj"] = downsample(fn(ref, seed=1))
            results.append(r)
        entry = LEDGER.append("compare", {
            "seed": 1,
            "verdicts": {r["policy"]: r["verdict"]["label"] for r in results},
        })
        return self._json(200, {
            "reference": downsample(ref),
            "results": results,
            "ledger": {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16]},
        })

    # ---------- POST ----------
    def do_POST(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/score":
            return self._handle_score()
        if path == "/api/sweep":
            return self._handle_sweep()
        if path == "/api/hunt":
            return self._handle_hunt()
        if path == "/api/dossier":
            return self._handle_dossier()
        if path == "/api/pairscore":
            return self._handle_pairscore()
        if path == "/api/xemb":
            return self._handle_xemb()
        if path == "/api/batch":
            return self._handle_batch()
        if path == "/api/collapse":
            return self._handle_collapse()
        return self._json(404, {"error": "not found"})

    def _handle_score(self):
        body = self._read_json()
        pid = body.get("policy", "clean")
        if pid not in policies.POLICIES:
            return self._json(400, {"error": "unknown policy: %r" % (pid,)})
        try:
            seed = int(body.get("seed", 1))
        except (TypeError, ValueError):
            seed = 1
        r = score_one(pid, seed=seed)
        ref = policies.reference_actions()
        r["traj"] = downsample(policies.POLICIES[pid]["fn"](ref, seed=seed))
        r["reference"] = downsample(ref)
        entry = LEDGER.append("score", {
            "policy": pid, "seed": seed,
            "verdict": r["verdict"]["label"], "score": r["score"],
        })
        r["ledger"] = {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16]}
        return self._json(200, r)

    def _handle_sweep(self):
        """Module-2 lite: ramp noise_scale, find where the verdict flips."""
        body = self._read_json()
        pid = body.get("policy", "clean")
        if pid not in policies.POLICIES:
            return self._json(400, {"error": "unknown policy: %r" % (pid,)})
        try:
            lo = float(body.get("from", 1.0))
            hi = float(body.get("to", 8.0))
            steps = max(2, min(int(body.get("steps", 8)), 12))
        except (TypeError, ValueError):
            return self._json(400, {"error": "bad sweep range"})
        if not (0.1 <= lo < hi <= 30):
            return self._json(400, {"error": "range must satisfy 0.1 <= from < to <= 30"})
        points = []
        flip_at = None
        for i in range(steps):
            ns = round(lo + (hi - lo) * i / (steps - 1), 2)
            r = score_one(pid, seed=1, noise_scale=ns)
            points.append({
                "noise_scale": ns,
                "band": r["verdict"]["band"],
                "verdict": r["verdict"]["label"],
                "mean_drift": r["score"]["mean_drift"],
                "mean_spread": r["score"]["mean_spread"],
            })
            if flip_at is None and r["verdict"]["band"] != "green":
                flip_at = ns
        entry = LEDGER.append("sweep", {"policy": pid, "flip_at": flip_at,
                                        "range": [lo, hi, steps]})
        return self._json(200, {
            "policy": pid, "points": points, "flip_at": flip_at,
            "ledger": {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16]},
        })

    def _handle_hunt(self):
        """Falsification style hunt: smallest disturbance that breaks a policy."""
        body = self._read_json()
        pid = body.get("policy", "clean")
        if pid not in policies.POLICIES:
            return self._json(400, {"error": "unknown policy: %r" % (pid,)})
        try:
            budget = max(4, min(int(body.get("budget", 24)), 40))
        except (TypeError, ValueError):
            budget = 24
        try:
            hseed = int(body.get("hunt_seed", 1))
        except (TypeError, ValueError):
            hseed = 1
        r = adversarial.hunt(pid, hunt_seed=hseed, budget=budget)
        mb = r["minimal_break"]
        entry = LEDGER.append("hunt", {
            "policy": pid, "tested": r["tested"], "counts": r["counts"],
            "holds": r["holds"],
            "minimal_break": ({k: mb[k] for k in ("params", "verdict", "band")}
                               if mb else None),
        })
        r["ledger"] = {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16]}
        return self._json(200, r)

    def _handle_dossier(self):
        """Evidence dossier: scorecard mapped to compliance clauses."""
        body = self._read_json()
        pid = body.get("policy", "clean")
        if pid not in policies.POLICIES:
            return self._json(400, {"error": "unknown policy: %r" % (pid,)})
        try:
            seed = int(body.get("seed", 1))
        except (TypeError, ValueError):
            seed = 1
        d = dossier.build(pid, seed=seed)
        dh = dossier.digest(d)
        entry = LEDGER.append("dossier", {
            "policy": pid, "seed": seed,
            "verdict": d["verdict"]["label"], "dossier_hash": dh,
        })
        d["ledger"] = {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16],
                       "dossier_hash": dh[:16]}
        return self._json(200, d)

    def _handle_pairscore(self):
        """Gap scorecard for one curated pair (real or synthetic)."""
        body = self._read_json()
        pid = body.get("pair_id", "")
        got = datasets_mod.get_pair(pid)
        if got is None:
            return self._json(400, {"error": "unknown pair_id: %r" % (pid,)})
        pair = got["pair"]
        r = gaps_mod.score_pair(pair["sim"], pair["real"])
        r["pair_id"] = pid
        r["card"] = got["card"]
        r["sim"] = downsample(pair["sim"])
        r["real"] = downsample(pair["real"])
        entry = LEDGER.append("pairscore", {
            "pair_id": pid, "verdict": r["verdict"]["label"],
            "frechet": r["score"]["frechet_sim_real"],
        })
        r["ledger"] = {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16]}
        return self._json(200, r)

    def _handle_xemb(self):
        """Cross-embodiment divergence between two pairs' executed paths."""
        body = self._read_json()
        aids = (body.get("a", ""), body.get("b", ""))
        gots = []
        for pid in aids:
            got = datasets_mod.get_pair(pid)
            if got is None:
                return self._json(400, {"error": "unknown pair_id: %r" % (pid,)})
            gots.append(got)
        frames = [g["pair"].get("frame", "") for g in gots]
        meters = ["meters" in f for f in frames]
        if meters[0] != meters[1]:
            return self._json(400, {"error": "incomparable frames: %r vs %r "
                                             "(meters never mix with abstract units)"
                                    % (frames[0], frames[1])})
        r = gaps_mod.xemb_distance(gots[0]["pair"]["real"], gots[1]["pair"]["real"])
        r["a"], r["b"] = aids
        entry = LEDGER.append("xemb", {
            "a": aids[0], "b": aids[1], "label": r["label"],
            "frechet_centered": r["frechet_centered"],
            "span_ratio": r["span_ratio"],
        })
        r["ledger"] = {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16]}
        return self._json(200, r)

    def _handle_batch(self):
        """Governance audit for an uploaded batch (alpha ratio + verdict)."""
        try:
            n = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            n = 0
        if n > gaps_mod.MAX_BODY:
            return self._json(413, {"error": "batch too large (max 3 MB)"})
        body = self._read_json()
        try:
            r = gaps_mod.batch_audit(body.get("episodes", []))
        except ValueError as exc:
            return self._json(400, {"error": str(exc)})
        r["name"] = str(body.get("name", "upload"))[:80]
        entry = LEDGER.append("batch", {
            "name": r["name"], "n": r["n"], "alpha": r["alpha"],
            "verdict": r["verdict"]["label"], "collapse_risk": r["collapse_risk"],
        })
        r["ledger"] = {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16]}
        return self._json(200, r)

    def _handle_collapse(self):
        """Model-collapse illustration (simulated, labeled, deterministic)."""
        body = self._read_json()
        try:
            seed = int(body.get("seed", 1))
        except (TypeError, ValueError):
            seed = 1
        r = gaps_mod.collapse_demo(seed=seed)
        entry = LEDGER.append("collapse", {
            "seed": seed, "label": r["verdict"]["label"],
        })
        r["ledger"] = {"seq": entry["seq"], "entry_hash": entry["entry_hash"][:16]}
        return self._json(200, r)

    def log_message(self, fmt, *args):  # quieter logs
        sys.stderr.write("verify: %s\n" % (fmt % args))


def main():
    port = int(os.environ.get("VERIFY_PORT", "8000"))
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print("Genuity Verify MVP  ->  http://127.0.0.1:%d/   (Ctrl+C to stop)" % port)
    print("Ledger: %s" % LEDGER_PATH)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped.")


if __name__ == "__main__":
    main()
