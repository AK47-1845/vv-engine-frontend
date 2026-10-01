"""Pre-render static scorecard HTML · no-server fallback + paper backup.

Uses the REAL scoring engine (metrics_std + policies), so numbers match the
live console byte-for-byte (seed 1). Double-click reports/index.html.

Run from MVP folder:  python backend/export_static.py
"""

import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import metrics_std
import policies

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = os.path.join(BASE, "reports")

CSS = """body{margin:0;background:#0e1216;color:#e9e6df;font:14px/1.5 'Segoe UI',system-ui,sans-serif}
.wrap{max-width:900px;margin:0 auto;padding:24px 20px}
h1{font-size:20px;margin:0 0 4px}h2{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#98a1ab;margin:20px 0 8px}
.muted{color:#98a1ab}.small{font-size:12px}a{color:#d9a021}
.panel{background:#151b22;border:1px solid #28303b;border-radius:6px;padding:16px;margin:12px 0}
.verdict{font-size:17px;font-weight:700;padding:12px 14px;border-radius:6px;border:1px solid #28303b}
.verdict small{display:block;font-size:12px;font-weight:400;color:#98a1ab}
.verdict.green{background:#12261a;border-color:#3fa34d;color:#8fdc99}
.verdict.amber{background:#2b2110;border-color:#e0aa2e;color:#f0c35c}
.verdict.red{background:#2c1518;border-color:#d05252;color:#ef9a9a}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{border-bottom:1px solid #28303b;padding:7px 8px;text-align:left}
th{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:#98a1ab}
td:nth-child(2){font-family:ui-monospace,Consolas,monospace;text-align:right;white-space:nowrap}
td.desc{color:#98a1ab;font-size:12px}
.badge{font:700 10px ui-monospace,monospace;padding:2px 8px;border-radius:10px}
.badge.green{background:#1d4d25;color:#8fdc99}.badge.amber{background:#4d3a10;color:#f0c35c}.badge.red{background:#5a1f24;color:#ef9a9a}
svg{width:100%;height:auto;background:#0b0f13;border:1px solid #28303b;border-radius:6px}
.card{display:block;text-decoration:none;color:#e9e6df}
.card:hover{border-color:#d9a021}.mono{font-family:ui-monospace,Consolas,monospace}"""

COLORS = {"green": "#3fa34d", "amber": "#e0aa2e", "red": "#d05252"}


def svg_plot(ref, traj, band, w=640, h=300):
    pts = ref[::2] + traj[::2]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    pad = 30

    def X(x):
        return pad + (x - x0) / ((x1 - x0) or 1) * (w - 2 * pad)

    def Y(y):
        return h - pad - (y - y0) / ((y1 - y0) or 1) * (h - 2 * pad)

    def pl(points):
        return " ".join("%.1f,%.1f" % (X(p[0]), Y(p[1])) for p in points)

    return (
        '<svg viewBox="0 0 %d %d">'
        '<polyline points="%s" fill="none" stroke="#5b6570" stroke-width="1.5"'
        ' stroke-dasharray="5 4"/>'
        '<polyline points="%s" fill="none" stroke="%s" stroke-width="2"/>'
        '<line x1="10" y1="14" x2="34" y2="14" stroke="#5b6570" stroke-width="2"'
        ' stroke-dasharray="5 4"/>'
        '<text x="40" y="18" fill="#98a1ab" font-size="11" font-family="monospace">'
        "commanded</text>"
        '<line x1="130" y1="14" x2="154" y2="14" stroke="%s" stroke-width="2"/>'
        '<text x="160" y="18" fill="%s" font-size="11" font-family="monospace">'
        "executed (%s)</text></svg>"
        % (w, h, pl(ref[::2]), pl(traj[::2]), COLORS[band], COLORS[band],
           COLORS[band], band)
    )


def card_page(pid, title, story, score, gates, verdict, plot):
    label, detail, band = verdict
    rows = "".join(
        "<tr><td>%s</td><td>%s</td>"
        '<td><span class="badge %s">%s</span></td>'
        '<td class="desc">%s</td></tr>'
        % (g["metric"], g["value"], g["band"], g["band"].upper(), g["desc"])
        for g in gates
    )
    return """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Scorecard · %s</title><style>%s</style></head><body><div class="wrap">
<p><a href="index.html">← all scorecards</a></p>
<h1>Trust Scorecard · %s</h1>
<p class="muted small">%s · static export (not ledger-chained) · seed 1 · gates DRAFT</p>
<div class="verdict %s">%s · %s<small>%s</small></div>
<h2>Evidence</h2><div class="panel"><table>
<tr><th>Metric</th><th>Value</th><th>Gate</th><th>What it measures</th></tr>%s</table></div>
<h2>Paths</h2>%s
<p class="muted small">Fail-closed: worst gate decides. Jerk/bounds rows are proxies,
not contact-dynamics proofs. Numbers identical to the live console (same engine, seed 1).</p>
</div></body></html>""" % (title, CSS, title, story, band, label, title, detail, rows, plot)


def main():
    os.makedirs(REPORTS, exist_ok=True)
    ref = policies.reference_actions()
    probed_actions = policies.probe_actions(ref)
    days_left = (datetime.date(2027, 1, 20) - datetime.date.today()).days
    summaries = []
    for pid, meta in policies.POLICIES.items():
        fn = meta["fn"]
        pred = fn(ref, seed=1)
        probed = fn(probed_actions, seed=1)
        seeds = [fn(ref, seed=s) for s in range(5)]
        score = metrics_std.score_policy(pid, pred, ref, probed, seeds)
        verdict = metrics_std.verdict(score)
        plot = svg_plot(ref, pred, verdict[2])
        html = card_page(pid, meta["title"], meta["story"], score,
                         metrics_std.gates(score), verdict, plot)
        path = os.path.join(REPORTS, "scorecard-%s.html" % pid)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        summaries.append((pid, meta["title"], meta["story"], verdict, score))
        print("%s -> %s (%s)  %s" % (pid, verdict[0], verdict[2], path))
    cards = "".join(
        '<a class="card panel" href="scorecard-%s.html">'
        '<span class="badge %s">%s</span> <b>%s</b>'
        '<br><span class="muted small">%s</span>'
        '<br><span class="mono small muted">drift %s · sens %s · frechet %s</span></a>'
        % (pid, v[2], v[0], title, story, s["mean_drift"],
           s["action_sensitivity"], s["frechet_sim_real"])
        for pid, title, story, v, s in summaries
    )
    index = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Genuity Verify · static scorecards</title><style>%s</style></head><body><div class="wrap">
<h1>Genuity Verify · Module 1 scorecards (static)</h1>
<p class="muted">EU Machinery Reg clock: <b style="color:#d9a021">T-%d days → 2027-01-20</b>
· gates DRAFT · live console: <span class="mono">python backend/server.py</span></p>
%s
<p class="muted small">Same engine as the live server, seed 1. Static pages are not
ledger-chained; the live console chains every run. Jerk/bounds rows are proxies.</p>
</div></body></html>""" % (CSS, days_left, cards)
    ipath = os.path.join(REPORTS, "index.html")
    with open(ipath, "w", encoding="utf-8") as fh:
        fh.write(index)
    print("index -> %s" % ipath)


if __name__ == "__main__":
    main()
