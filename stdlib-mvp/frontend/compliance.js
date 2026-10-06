/* Compliance page live evidence. Vanilla JS, no deps. */
"use strict";

async function getJSON(path) {
  const r = await fetch(path);
  if (!r.ok) throw new Error("HTTP " + r.status);
  return r.json();
}

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

async function verifyLive() {
  const out = document.getElementById("verifyLiveOut");
  const btn = document.getElementById("verifyLiveBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Verifying...";
  try {
    const v = await getJSON("/api/ledger/verify");
    out.innerHTML = "";
    const d = document.createElement("div");
    d.className = "entry";
    const b = document.createElement("span");
    b.className = "badge " + (v.ok ? "green" : "red");
    b.textContent = v.ok ? "VERIFIED" : "BROKEN";
    d.appendChild(b);
    d.appendChild(document.createTextNode(" " + (v.ok
      ? "chain intact across " + v.checked + " entries."
      : "break at sequence " + v.break_at + ": " + v.reason)));
    out.appendChild(d);
  } catch (e) {
    downServer(out, e);
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

async function sampleLive() {
  const out = document.getElementById("sampleLiveOut");
  const btn = document.getElementById("sampleLiveBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Scoring...";
  try {
    const r = await postJSON("/api/score", {policy: "clean", seed: 1});
    const blob = new Blob([JSON.stringify(r, null, 2)], {type: "application/json"});
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "evidence-scorecard-clean-seed1.json";
    a.click();
    URL.revokeObjectURL(a.href);
    out.innerHTML = "";
    const d = document.createElement("div");
    d.className = "entry";
    const b = document.createElement("span");
    b.className = "badge " + r.verdict.band;
    b.textContent = r.verdict.label;
    d.appendChild(b);
    d.appendChild(document.createTextNode(" clean policy scored and downloaded. Ledger #" + r.ledger.seq + "."));
    out.appendChild(d);
  } catch (e) {
    downServer(out, e);
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

async function dossierLive() {
  const out = document.getElementById("dossierLiveOut");
  const btn = document.getElementById("dossierLiveBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Generating...";
  try {
    const r = await postJSON("/api/dossier", {policy: "clean", seed: 1});
    const blob = new Blob([JSON.stringify(r, null, 2)], {type: "application/json"});
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "dossier-clean-seed1.json";
    a.click();
    URL.revokeObjectURL(a.href);
    const n = r.gates.reduce((t, g) => t + g.clauses.length, 0);
    out.innerHTML = "";
    const d = document.createElement("div");
    d.className = "entry";
    const b = document.createElement("span");
    b.className = "badge " + r.verdict.band;
    b.textContent = r.verdict.label;
    d.appendChild(b);
    d.appendChild(document.createTextNode(" dossier generated: clean policy, " + n +
      " clause mappings, hash " + r.ledger.dossier_hash + ", ledger #" + r.ledger.seq + "."));
    out.appendChild(d);
  } catch (e) {
    downServer(out, e);
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

document.getElementById("verifyLiveBtn").addEventListener("click", verifyLive);
document.getElementById("sampleLiveBtn").addEventListener("click", sampleLive);
document.getElementById("dossierLiveBtn").addEventListener("click", dossierLive);

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
