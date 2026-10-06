/* Docs page live widgets. Calls the real scoring engine. Vanilla JS, no deps. */
"use strict";

async function postJSON(path, obj) {
  const r = await fetch(path, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(obj),
  });
  if (!r.ok) throw new Error("HTTP " + r.status);
  return r.json();
}

function downServer(out, err) {
  out.innerHTML = "";
  const p = document.createElement("p");
  p.className = "muted small";
  p.textContent = "Server unreachable (" + err.message + "). Start it with START.cmd, then reload this page.";
  out.appendChild(p);
}

async function scoreLive(policy, outId, btn) {
  const out = document.getElementById(outId);
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Scoring...";
  try {
    const r = await postJSON("/api/score", {policy: policy, seed: 1});
    out.innerHTML = "";
    const d = document.createElement("div");
    d.className = "entry";
    const b = document.createElement("span");
    b.className = "badge " + r.verdict.band;
    b.textContent = r.verdict.label;
    d.appendChild(b);
    d.appendChild(document.createTextNode(" " + r.title + " "));
    const s = document.createElement("span");
    s.className = "muted small";
    s.textContent = "drift " + r.score.mean_drift + " · sens " + r.score.action_sensitivity +
      " · frechet " + r.score.frechet_sim_real + " · ledger #" + r.ledger.seq;
    d.appendChild(s);
    out.appendChild(d);
    const hint = document.createElement("p");
    hint.className = "muted small";
    hint.textContent = "Open the Dashboard and press Score for the full card with the path plot.";
    out.appendChild(hint);
  } catch (e) {
    downServer(out, e);
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

async function sweepLive(outId, btn) {
  const out = document.getElementById(outId);
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Sweeping...";
  try {
    const r = await postJSON("/api/sweep", {policy: "clean", from: 1, to: 8, steps: 8});
    out.innerHTML = "";
    const maxD = Math.max.apply(null, r.points.map((p) => p.mean_drift).concat([0.001]));
    r.points.forEach((p) => {
      const row = document.createElement("div");
      row.className = "bar";
      const lab = document.createElement("span");
      lab.textContent = "x" + p.noise_scale;
      lab.style.width = "44px";
      const track = document.createElement("div");
      track.className = "track";
      const fill = document.createElement("div");
      fill.className = "fill " + p.band;
      fill.style.width = Math.max(4, (p.mean_drift / maxD) * 100) + "%";
      track.appendChild(fill);
      const tag = document.createElement("span");
      tag.textContent = p.verdict;
      row.appendChild(lab);
      row.appendChild(track);
      row.appendChild(tag);
      out.appendChild(row);
    });
    const flip = document.createElement("p");
    flip.className = "muted small";
    flip.textContent = r.flip_at == null
      ? "No flip in range. The clean policy holds to noise x8."
      : "Breaking point: noise x" + r.flip_at + ". The verdict flips there. Ledger #" + r.ledger.seq + ".";
    out.appendChild(flip);
  } catch (e) {
    downServer(out, e);
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

document.querySelectorAll("[data-score]").forEach((btn) => {
  btn.addEventListener("click", () => scoreLive(btn.dataset.score, btn.dataset.out, btn));
});
const swBtn = document.getElementById("sweepLiveBtn");
if (swBtn) swBtn.addEventListener("click", () => sweepLive("sweepLiveOut", swBtn));

/* engine status pill */
(async () => {
  const pill = document.getElementById("envPill");
  const txt = document.getElementById("envText");
  if (!pill || !txt) return;
  try {
    const r = await fetch("/api/ledger/verify");
    const v = await r.json();
    const ok = r.ok && v.ok;
    pill.classList.add(ok ? "ok" : "bad");
    txt.textContent = ok ? "LIVE" : "CHAIN BROKEN";
  } catch (e) {
    pill.classList.add("bad");
    txt.textContent = "OFFLINE";
  }
})();
