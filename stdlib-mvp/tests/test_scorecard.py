"""Genuity Verify MVP - acceptance tests (stdlib unittest, no deps).

Run from the MVP folder:   python tests/test_scorecard.py
Covers TECHNICAL_PROMPT §8 criteria 1-4 fully, 2/5 via in-process live API,
plus the Evidence track: real pairs, xemb, batch alpha, collapse, registry.
"""

import ast
import json
import os
import sys
import tempfile
import threading
import unittest
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "backend"))

import adversarial  # noqa: E402
import datasets  # noqa: E402
import dossier  # noqa: E402
import gaps  # noqa: E402
import ledger as ledger_mod  # noqa: E402
import metrics_std  # noqa: E402
import policies  # noqa: E402
import server as srv  # noqa: E402

REAL_B = "droid_success_2023_07_07_fri_jul_7_09_43_39_2023"


def pair_score(pid):
    got = datasets.get_pair(pid)
    return gaps.score_pair(got["pair"]["sim"], got["pair"]["real"])


class TestDiscrimination(unittest.TestCase):
    def test_four_verdicts(self):
        got = {p: srv.score_one(p)["verdict"]["label"]
               for p in ("clean", "drifty", "playback", "synthfed")}
        self.assertEqual(got["clean"], "TRUSTED")
        self.assertEqual(got["drifty"], "BLOCKED")
        self.assertEqual(got["playback"], "BLOCKED")
        self.assertEqual(got["synthfed"], "REVIEW")

    def test_playback_sensitivity_exactly_zero(self):
        s = srv.score_one("playback")["score"]
        self.assertEqual(s["action_sensitivity"], 0.0)

    def test_fail_closed(self):
        bad = {"frechet_sim_real": 0, "mean_drift": 0, "final_drift": 0,
               "coherence_horizon_ratio": 1.0, "action_sensitivity": 9.9,
               "mean_spread": 0, "max_jerk_proxy": 0, "bound_violation_rate": 0.5}
        label, _, band = metrics_std.verdict(bad)
        self.assertEqual((label, band), ("BLOCKED", "red"))


class TestDeterminism(unittest.TestCase):
    def test_identical_bytes(self):
        a = srv.score_one("synthfed", seed=7)["score"]
        b = srv.score_one("synthfed", seed=7)["score"]
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))


class TestLedger(unittest.TestCase):
    def test_chain_and_tamper(self):
        tmp = os.path.join(tempfile.mkdtemp(), "t.jsonl")
        lg = ledger_mod.Ledger(tmp)
        lg.append("score", {"policy": "clean"})
        lg.append("score", {"policy": "drifty"})
        self.assertTrue(lg.verify()["ok"])
        # tamper: rewrite entry 0 payload in place
        with open(tmp, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        e0 = json.loads(lines[0])
        e0["payload"]["policy"] = "clean-HACKED"
        lines[0] = json.dumps(e0, sort_keys=True) + "\n"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.writelines(lines)
        v = ledger_mod.Ledger(tmp).verify()
        self.assertFalse(v["ok"])
        self.assertEqual(v["break_at"], 0)


class TestSweep(unittest.TestCase):
    def test_drifty_red_from_start(self):
        r = srv.score_one("drifty", seed=1, noise_scale=1.0)
        self.assertEqual(r["verdict"]["band"], "red")

    def test_clean_holds_at_1(self):
        r = srv.score_one("clean", seed=1, noise_scale=1.0)
        self.assertEqual(r["verdict"]["band"], "green")


class TestStdlibOnly(unittest.TestCase):
    ALLOW = {"__future__", "ast", "datetime", "hashlib", "http", "json", "math",
             "os", "random", "sys", "tempfile", "threading", "time",
             "unittest", "urllib", "importlib",
             "ledger", "metrics_std", "policies", "server", "ledger_mod",
             "adversarial", "datasets", "dossier", "gaps", "re"}

    def test_no_third_party_imports(self):
        backend = os.path.join(BASE, "backend")
        for fn in os.listdir(backend):
            if not fn.endswith(".py"):
                continue
            with open(os.path.join(backend, fn), encoding="utf-8") as fh:
                tree = ast.parse(fh.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for a in node.names:
                        self.assertIn(a.name.split(".")[0], self.ALLOW, fn)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    self.assertIn(node.module.split(".")[0], self.ALLOW, fn)


class TestHunt(unittest.TestCase):
    def test_deterministic(self):
        a = adversarial.hunt("clean", hunt_seed=3, budget=8)
        b = adversarial.hunt("clean", hunt_seed=3, budget=8)
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))

    def test_finds_break_for_clean(self):
        r = adversarial.hunt("clean", hunt_seed=1, budget=24)
        self.assertFalse(r["holds"])
        self.assertIsNotNone(r["minimal_break"])
        self.assertEqual(r["tested"], 1 + 24 + 8)

    def test_playback_fails_at_baseline(self):
        r = adversarial.hunt("playback", hunt_seed=1, budget=8)
        m = r["minimal_break"]
        self.assertEqual(m["params"], {"cmd_bias": 0.0, "cmd_noise": 0.0,
                                       "noise_scale": 1.0})


class TestDossier(unittest.TestCase):
    def test_maps_clauses(self):
        d = dossier.build("clean", seed=1)
        self.assertEqual(d["verdict"]["label"], "TRUSTED")
        for g in d["gates"]:
            self.assertTrue(g["clauses"])
        text = json.dumps(d)
        self.assertIn("2023/1230", text)
        self.assertIn("DRAFT", text)

    def test_body_deterministic(self):
        a = dossier.build("synthfed", seed=2)
        b = dossier.build("synthfed", seed=2)
        a.pop("generated_ts")
        b.pop("generated_ts")
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))


class TestRealPairs(unittest.TestCase):
    def test_pour_trusted_under_point_three(self):
        r = pair_score("droid_pour_s1")
        self.assertEqual(r["verdict"]["label"], "TRUSTED")
        self.assertLess(r["score"]["frechet_sim_real"], 0.30)

    def test_all_real_trusted(self):
        for e in datasets.list_datasets():
            if e["kind"] != "real":
                continue
            with self.subTest(e["id"]):
                self.assertEqual(pair_score(e["id"])["verdict"]["label"], "TRUSTED")

    def test_degraded_synthetic_review(self):
        r = pair_score("bias_drift_s1")
        self.assertEqual(r["verdict"]["label"], "REVIEW")
        self.assertGreater(r["score"]["frechet_sim_real"], 0.30)

    def test_dropout_is_extreme(self):
        r = pair_score("dropout_heavy_s1")
        self.assertGreater(r["score"]["frechet_sim_real"], 0.50)

    def test_rejects_traversal(self):
        self.assertIsNone(datasets.get_pair("../server"))
        self.assertIsNone(datasets.get_pair("nope-missing-id"))


class TestXemb(unittest.TestCase):
    def _real(self, pid):
        return datasets.get_pair(pid)["pair"]["real"]

    def test_self_aligned_zero(self):
        r = gaps.xemb_distance(self._real("droid_pour_s1"),
                               self._real("droid_pour_s1"))
        self.assertEqual((r["label"], r["frechet_centered"], r["span_ratio"]),
                         ("ALIGNED", 0.0, 1.0))

    def test_baseline_scale_agrees(self):
        r = gaps.xemb_distance(self._real("droid_pour_s1"), self._real(REAL_B))
        self.assertEqual(r["label"], "DIVERGED")
        self.assertEqual(r["scale_band"], "green")
        self.assertAlmostEqual(r["span_ratio"], 0.8733, places=3)

    def test_morph_scale_red(self):
        r = gaps.xemb_distance(self._real("droid_pour_s1"),
                               self._real("morph_pour_short_s1"))
        self.assertEqual(r["label"], "SEVERE")
        self.assertEqual(r["scale_band"], "red")
        self.assertAlmostEqual(r["span_ratio"], 0.5502, places=3)

    def test_symmetric_and_deterministic(self):
        a = self._real("droid_pour_s1")
        b = self._real("morph_pour_tall_s1")
        r1 = gaps.xemb_distance(a, b)
        r2 = gaps.xemb_distance(b, a)
        r3 = gaps.xemb_distance(a, b)
        for key in ("frechet_centered", "mean_drift_centered", "span_ratio",
                    "shape_band", "scale_band", "band", "label"):
            self.assertEqual(r1[key], r2[key], key)
        self.assertEqual(r1["span_a"], r2["span_b"])
        self.assertEqual(r1["span_a"], r3["span_a"])
        self.assertEqual(json.dumps(r1, sort_keys=True), json.dumps(r3, sort_keys=True))


class TestBatch(unittest.TestCase):
    def _audit(self, sid):
        return gaps.batch_audit(datasets.get_sample(sid)["episodes"])

    def test_sample_a_governed(self):
        r = self._audit("sample-a-real-pour")
        self.assertEqual((r["alpha"], r["verdict"]["label"], r["collapse_risk"]),
                         (0.0, "GOVERNED", "LOW"))

    def test_sample_b_review(self):
        r = self._audit("sample-b-mixed-batch")
        self.assertEqual((r["alpha"], r["verdict"]["label"], r["collapse_risk"]),
                         (0.6, "REVIEW", "ELEVATED"))

    def test_sample_c_blocked_high(self):
        r = self._audit("sample-c-synth-heavy")
        self.assertEqual((r["alpha"], r["verdict"]["label"], r["collapse_risk"]),
                         (0.9, "BLOCKED", "HIGH"))

    def test_sample_d_generation_slope(self):
        r = self._audit("sample-d-generations")
        self.assertEqual(r["alpha"], 0.75)
        self.assertGreater(r["generation_slope"], 0)
        self.assertEqual(len(r["generation_curve"]), 3)

    def test_rejects_garbage(self):
        with self.assertRaises(ValueError):
            gaps.batch_audit([])
        with self.assertRaises(ValueError):
            gaps.batch_audit([{"source": "maybe", "sim": [], "real": []}])
        with self.assertRaises(ValueError):
            gaps.batch_audit([{"source": "real", "sim": [[0, 0]], "real": [[0, 0]]}])


class TestCollapse(unittest.TestCase):
    def test_shows_collapse(self):
        r = gaps.collapse_demo(seed=1)
        self.assertEqual(r["verdict"]["label"], "COLLAPSE SHOWN")
        first, last = r["curve"][0], r["curve"][-1]
        self.assertGreater(first["occupied_bins"], last["occupied_bins"])
        self.assertGreater(first["variance"], last["variance"])

    def test_deterministic(self):
        a = gaps.collapse_demo(seed=1)
        b = gaps.collapse_demo(seed=1)
        self.assertEqual(json.dumps(a, sort_keys=True), json.dumps(b, sort_keys=True))


class TestRegistry(unittest.TestCase):
    def test_counts(self):
        ds = datasets.list_datasets()
        real = [d for d in ds if d["kind"] == "real"]
        self.assertEqual(len(ds), 53)
        self.assertEqual(len(real), 5)
        self.assertEqual(len(datasets.list_samples()), 4)
        self.assertEqual(len(datasets.demo_guide()), 7)

    def test_guide_targets_exist(self):
        for g in datasets.demo_guide():
            use = g["use"]
            with self.subTest(use):
                if use.startswith("Sample "):
                    letter = use.split(" ")[1].lower()
                    sid = [s["id"] for s in datasets.list_samples()
                           if s["id"].startswith("sample-%s" % letter)]
                    self.assertTrue(sid, use)
                else:
                    for pid in [p.strip() for p in use.split("+")]:
                        self.assertIsNotNone(datasets.get_pair(pid), pid)


class TestLiveAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._real = srv.LEDGER
        srv.LEDGER = ledger_mod.Ledger(os.path.join(tempfile.mkdtemp(), "live.jsonl"))
        try:
            cls.httpd = ThreadingHTTPServer(("127.0.0.1", 0), srv.Handler)
        except PermissionError:
            raise unittest.SkipTest("socket bind forbidden in this sandbox;"
                                    " live API runs on the user machine")
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        srv.LEDGER = cls._real

    def _get(self, path):
        with urllib.request.urlopen("http://127.0.0.1:%d%s" % (self.port, path)) as r:
            return r.status, r.read()

    def _post(self, path, obj):
        req = urllib.request.Request(
            "http://127.0.0.1:%d%s" % (self.port, path),
            data=json.dumps(obj).encode(), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read())

    def _post_status(self, path, obj):
        try:
            status, _ = self._post(path, obj)
            return status
        except urllib.error.HTTPError as exc:
            return exc.code

    def test_compare_four_verdicts(self):
        _, raw = self._get("/api/compare")
        body = json.loads(raw)
        labels = {r["policy"]: r["verdict"]["label"] for r in body["results"]}
        self.assertEqual(labels, {"clean": "TRUSTED", "drifty": "BLOCKED",
                                  "playback": "BLOCKED", "synthfed": "REVIEW"})
        self.assertEqual(len(body["reference"]), 50)

    def test_score_roundtrip(self):
        _, body = self._post("/api/score", {"policy": "playback", "seed": 3})
        self.assertEqual(body["score"]["action_sensitivity"], 0.0)
        self.assertEqual(body["verdict"]["label"], "BLOCKED")
        _, raw = self._get("/api/ledger/verify")
        self.assertTrue(json.loads(raw)["ok"])

    def test_frontend_serves(self):
        status, raw = self._get("/")
        self.assertEqual(status, 200)
        self.assertIn(b"LTTS Physical AI", raw)
        for route, marker in (("/docs", b"How scoring works"),
                              ("/compliance", b"Compliance timeline")):
            status, raw = self._get(route)
            self.assertEqual(status, 200)
            self.assertIn(marker, raw)
        for asset in ("/docs.js", "/compliance.js"):
            status, _ = self._get(asset)
            self.assertEqual(status, 200)

    def test_evidence_serves(self):
        status, raw = self._get("/evidence")
        self.assertEqual(status, 200)
        self.assertIn(b"Evidence, on real data", raw)
        status, raw = self._get("/evidence.js")
        self.assertEqual(status, 200)
        self.assertIn(b"auditSample", raw)
        status, raw = self._get("/assets/ltts-regular-white.png")
        self.assertEqual(status, 200)
        self.assertTrue(raw.startswith(b"\x89PNG"))

    def test_datasets_endpoint(self):
        _, raw = self._get("/api/datasets")
        body = json.loads(raw)
        self.assertEqual(body["counts"], {"total": 53, "real": 5, "synthetic": 48})
        self.assertEqual(len(body["samples"]), 4)
        self.assertEqual(len(body["guide"]), 7)

    def test_dataset_endpoint(self):
        _, raw = self._get("/api/dataset?id=droid_pour_s1")
        body = json.loads(raw)
        self.assertEqual(body["verdict"]["label"], "TRUSTED")
        self.assertTrue(len(body["sim"]) > 50)

    def test_sample_download(self):
        _, raw = self._get("/api/sample/sample-b-mixed-batch")
        body = json.loads(raw)
        self.assertEqual(len(body["episodes"]), 5)

    def test_pairscore_roundtrip(self):
        _, body = self._post("/api/pairscore", {"pair_id": "bias_drift_s1"})
        self.assertEqual(body["verdict"]["label"], "REVIEW")
        _, raw = self._get("/api/ledger/verify")
        self.assertTrue(json.loads(raw)["ok"])

    def test_xemb_roundtrip_and_frame_guard(self):
        _, body = self._post("/api/xemb", {"a": "droid_pour_s1",
                                           "b": "morph_pour_short_s1"})
        self.assertEqual(body["label"], "SEVERE")
        self.assertEqual(self._post_status("/api/xemb", {"a": "droid_pour_s1",
                                                          "b": "bias_drift_s1"}), 400)

    def test_batch_roundtrip(self):
        doc = datasets.get_sample("sample-c-synth-heavy")
        _, body = self._post("/api/batch", doc)
        self.assertEqual(body["verdict"]["label"], "BLOCKED")
        self.assertEqual(body["collapse_risk"], "HIGH")
        self.assertEqual(self._post_status("/api/batch", {"episodes": []}), 400)

    def test_collapse_roundtrip(self):
        _, body = self._post("/api/collapse", {"seed": 1})
        self.assertEqual(body["verdict"]["label"], "COLLAPSE SHOWN")
        self.assertEqual(len(body["curve"]), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
