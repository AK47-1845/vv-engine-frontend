/* LTTS Physical AI V&V console logic. Vanilla JS, no deps. */
"use strict";
const $ = (id) => document.getElementById(id);
let selected = "clean";
let lastResult = null;

async function api(path, opts) {
  const r = await fetch(path, opts);
  if (!r.ok) throw new Error("HTTP " + r.status + " on " + path);
  return r.json();
}

function setPill(ok, text) {
  const pill = document.getElementById("envPill");
  const txt = document.getElementById("envText");
  if (!pill || !txt) return;
  pill.classList.remove("ok", "bad");
  pill.classList.add(ok ? "ok" : "bad");
  txt.textContent = text;
}

function setStat(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

/* ---------- policies ---------- */
async function loadPolicies() {
  const list = await api("/api/policies");
  const box = $("policyList");
  box.innerHTML = "";
  list.forEach((p) => {
    const b = document.createElement("button");
    b.className = "policy" + (p.id === selected ? " sel" : "");
    b.innerHTML = "<b></b><span></span>";
    b.querySelector("b").textContent = p.title;
    b.querySelector("span").textContent = p.story;
    b.onclick = () => {
      selected = p.id;
      [...box.children].forEach((c) => c.classList.remove("sel"));
      b.classList.add("sel");
    };
    box.appendChild(b);
  });
}

/* ---------- scoring ---------- */
async function score() {
  const seed = parseInt($("seedInput").value || "1", 10);
  const btn = $("scoreBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Scoring…";
  try {
    const r = await api("/api/score", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({policy: selected, seed}),
    });
    lastResult = r;
    renderResult(r);
    refreshLedger();
    refreshHistory();
  } catch (e) {
    $("verdict").className = "verdict red";
    $("verdict").textContent = "Server unreachable · is it running? " + e.message;
    setPill(false, "OFFLINE");
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

async function compare() {
  const btn = $("compareBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Comparing…";
  try {
    const c = await api("/api/compare");
    const grid = $("compareGrid");
    grid.innerHTML = "";
    c.results.forEach((r) => {
      const d = document.createElement("div");
      d.className = "cmp";
      const b = document.createElement("span");
      b.className = "badge " + r.verdict.band;
      b.textContent = r.verdict.label;
      const t = document.createElement("b");
      t.textContent = r.title + " ";
      t.appendChild(b);
      const s = document.createElement("span");
      s.textContent = "drift " + r.score.mean_drift + " · sens " + r.score.action_sensitivity;
      d.appendChild(t);
      d.appendChild(s);
      d.style.cursor = "pointer";
      d.title = "Click to inspect";
      d.onclick = () => {
        lastResult = Object.assign({}, r, {reference: c.reference});
        renderResult(lastResult);
      };
      grid.appendChild(d);
    });
    // auto-inspect the most interesting one (first non-green, else clean)
    const pick = c.results.find((r) => r.verdict.band !== "green") || c.results[0];
    lastResult = Object.assign({}, pick, {reference: c.reference});
    renderResult(lastResult);
    refreshLedger();
    refreshHistory();
  } catch (e) {
    $("verdict").className = "verdict red";
    $("verdict").textContent = "Server unreachable · " + e.message;
    setPill(false, "OFFLINE");
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

function renderResult(r) {
  const v = $("verdict");
  v.className = "verdict " + r.verdict.band;
  v.innerHTML = "";
  const strong = document.createElement("span");
  strong.textContent = r.verdict.label + " · " + r.title;
  const small = document.createElement("small");
  small.textContent = r.verdict.detail + " · seed " + r.seed + " · gates DRAFT · scored live " +
    new Date().toLocaleTimeString();
  v.appendChild(strong);
  v.appendChild(small);
  $("meta").textContent = "ledger #" + (r.ledger ? r.ledger.seq : "?") +
    " · hash " + (r.ledger ? r.ledger.entry_hash : "?") + " · [Verified] recomputed live";
  const tb = $("metricTable").querySelector("tbody");
  tb.innerHTML = "";
  r.gates.forEach((g, index) => {
    const tr = document.createElement("tr");
    tr.style.animationDelay = (index * 0.05) + "s";
    const tdM = document.createElement("td"); tdM.textContent = g.metric;
    const tdV = document.createElement("td"); tdV.textContent = g.value;
    tdV.className = "num";
    const tdB = document.createElement("td");
    const badge = document.createElement("span");
    badge.className = "badge " + g.band;
    badge.textContent = g.band.toUpperCase();
    tdB.appendChild(badge);
    const tdD = document.createElement("td");
    tdD.className = "desc"; tdD.textContent = g.desc;
    tr.append(tdM, tdV, tdB, tdD);
    tb.appendChild(tr);
  });
  if (r.traj && r.reference) drawPlot(r.reference, r.traj, r.verdict.band);
  $("exportBtn").disabled = false;
}

/* ---------- plot ---------- */
function gridOn(ctx, W, H, pad) {
  ctx.strokeStyle = "rgba(255,255,255,0.055)";
  ctx.lineWidth = 1;
  ctx.beginPath();
  for (let g = 1; g < 5; g++) {
    ctx.moveTo(pad + (W - 2 * pad) * g / 5, pad);
    ctx.lineTo(pad + (W - 2 * pad) * g / 5, H - pad);
    ctx.moveTo(pad, pad + (H - 2 * pad) * g / 5);
    ctx.lineTo(W - pad, pad + (H - 2 * pad) * g / 5);
  }
  ctx.stroke();
}

function drawPlot(ref, traj, band) {
  const cv = $("plot");
  const ctx = cv.getContext("2d");
  const W = cv.width, H = cv.height;
  ctx.clearRect(0, 0, W, H);
  const all = ref.concat(traj);
  const xs = all.map((p) => p[0]), ys = all.map((p) => p[1]);
  const x0 = Math.min(...xs), x1 = Math.max(...xs);
  const y0 = Math.min(...ys), y1 = Math.max(...ys);
  const pad = 24;
  const sx = (x) => pad + ((x - x0) / ((x1 - x0) || 1)) * (W - 2 * pad);
  const sy = (y) => H - pad - ((y - y0) / ((y1 - y0) || 1)) * (H - 2 * pad);
  gridOn(ctx, W, H, pad);
  const colors = {green: "#2ea043", amber: "#d9a021", red: "#f85149"};
  const line = (pts, color, width, dash) => {
    ctx.beginPath();
    ctx.setLineDash(dash || []);
    ctx.strokeStyle = color;
    ctx.lineWidth = width;
    pts.forEach((p, i) => (i ? ctx.lineTo(sx(p[0]), sy(p[1])) : ctx.moveTo(sx(p[0]), sy(p[1]))));
    ctx.stroke();
    ctx.setLineDash([]);
  };
  line(ref, "#5b6570", 1.5, [5, 4]);           // commanded (dashed gray)
  line(traj, colors[band] || "#fff", 2, []);    // executed (verdict color)
  ctx.font = "11px ui-monospace, monospace";
  ctx.strokeStyle = "#5b6570";
  ctx.lineWidth = 2;
  ctx.setLineDash([5, 4]);
  ctx.beginPath(); ctx.moveTo(10, 12); ctx.lineTo(34, 12); ctx.stroke();
  ctx.setLineDash([]);
  ctx.fillStyle = "#8a8d91";
  ctx.fillText("commanded", 40, 16);
  ctx.strokeStyle = colors[band] || "#fff";
  ctx.beginPath(); ctx.moveTo(130, 12); ctx.lineTo(154, 12); ctx.stroke();
  ctx.fillStyle = colors[band] || "#fff";
  ctx.fillText("executed (" + band + ")", 160, 16);
}

/* ---------- sweep ---------- */
async function sweep() {
  const out = $("sweepOut");
  out.innerHTML = "<p class='muted'>Sweeping… (8 full scorecards, a few seconds)</p>";
  const btn = $("sweepBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Sweeping…";
  try {
    const r = await api("/api/sweep", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        policy: selected,
        from: parseFloat($("sweepFrom").value || "1"),
        to: parseFloat($("sweepTo").value || "8"),
        steps: 8,
      }),
    });
    out.innerHTML = "";
    const maxD = Math.max(...r.points.map((p) => p.mean_drift), 0.001);
    r.points.forEach((p) => {
      const row = document.createElement("div");
      row.className = "bar";
      const lab = document.createElement("span");
      lab.textContent = "×" + p.noise_scale;
      lab.style.width = "44px";
      const track = document.createElement("div");
      track.className = "track";
      const fill = document.createElement("div");
      fill.className = "fill " + p.band;
      fill.style.width = Math.max(4, (p.mean_drift / maxD) * 100) + "%";
      track.appendChild(fill);
      const tag = document.createElement("span");
      tag.textContent = p.verdict;
      row.append(lab, track, tag);
      out.appendChild(row);
    });
    const flip = document.createElement("p");
    flip.innerHTML = "";
    flip.textContent = r.flip_at == null
      ? "No flip in range · policy holds to ×" + $("sweepTo").value + "."
      : "Breaking point: ×" + r.flip_at + " noise · verdict flips there. [Verified]";
    out.appendChild(flip);
    refreshLedger();
    refreshHistory();
  } catch (e) {
    out.innerHTML = "<p class='muted'>Sweep failed: " + e.message + "</p>";
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

/* ---------- hunt ---------- */
async function hunt() {
  const out = $("huntOut");
  out.innerHTML = "<p class='muted'>Hunting... (33 scored trials, several seconds)</p>";
  const btn = $("huntBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Hunting…";
  try {
    const r = await api("/api/hunt", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({policy: selected, budget: 24}),
    });
    out.innerHTML = "";
    const d = document.createElement("div");
    d.className = "entry";
    if (r.holds) {
      d.textContent = "Holds across " + r.tested + " trials. No disturbance in range broke " + selected + ".";
      out.appendChild(d);
    } else {
      const m = r.minimal_break;
      const b = document.createElement("span");
      b.className = "badge " + m.band;
      b.textContent = m.verdict;
      d.appendChild(b);
      d.appendChild(document.createTextNode(" breaks at bias " + m.params.cmd_bias +
        " / cmd noise " + m.params.cmd_noise + " / actuation x" + m.params.noise_scale));
      out.appendChild(d);
      const c = document.createElement("p");
      c.className = "muted small";
      c.textContent = r.tested + " trials: " + r.counts.green + " green, " +
        r.counts.amber + " amber, " + r.counts.red + " red. Caught by: " +
        (m.red_gates.join(", ") || "amber gates") + ". Ledger #" + r.ledger.seq + ".";
      out.appendChild(c);
    }
    refreshLedger();
    refreshHistory();
  } catch (e) {
    out.innerHTML = "<p class='muted'>Hunt failed: " + e.message + "</p>";
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

/* ---------- ledger / history ---------- */
/* loadGovernance retired: the Compliance panel is static HTML now. */

async function refreshLedger() {
  try {
    const v = await api("/api/ledger/verify");
    const l = await api("/api/ledger");
    setPill(v.ok, v.ok ? "LIVE" : "CHAIN BROKEN");
    setStat("stLedger", v.checked);
    const feed = $("ledgerFeed");
    feed.innerHTML = "";
    const status = document.createElement("div");
    status.className = "entry";
    status.textContent = v.ok ? "chain verified · " + v.checked + " entries"
                              : "CHAIN BROKEN @ " + v.break_at;
    feed.appendChild(status);
    l.entries.slice(-8).reverse().forEach((e) => {
      const d = document.createElement("div");
      d.className = "entry";
      const s = document.createElement("span");
      s.className = "seq";
      s.textContent = "#" + e.seq + " " + e.kind + " ";
      const c = document.createElement("code");
      c.textContent = e.entry_hash.slice(0, 12);
      const t = document.createElement("span");
      t.className = "muted";
      t.textContent = " ← " + String(e.prev_hash).slice(0, 8);
      d.append(s, c, t);
      feed.appendChild(d);
    });
    if (!l.entries.length) feed.innerHTML = "<p class='muted'>Empty · score a policy.</p>";
  } catch (e) { setPill(false, "OFFLINE"); }
}

async function refreshHistory() {
  try {
    const h = await api("/api/history");
    const feed = $("historyFeed");
    feed.innerHTML = "";
    h.runs.slice(0, 8).forEach((e) => {
      const d = document.createElement("div");
      d.className = "entry";
      let txt = "#" + e.seq + " " + e.kind;
      const p = e.payload || {};
      if (p.policy) txt += " " + p.policy + " → " + (p.verdict || "");
      if (p.verdicts) txt += " " + Object.values(p.verdicts).join("/");
      if (p.flip_at != null) txt += " " + p.policy + " flips ×" + p.flip_at;
      if (p.pair_id) txt += " " + p.pair_id + " → " + (p.verdict || "");
      if (p.alpha != null) txt += " α=" + p.alpha + " → " + (p.verdict || "");
      d.textContent = txt + " · " + e.ts.slice(11, 19);
      feed.appendChild(d);
    });
    if (!h.runs.length) feed.innerHTML = "<p class='muted'>No runs yet.</p>";
  } catch (e) { /* server down */ }
}

function exportJSON() {
  if (!lastResult) return;
  const blob = new Blob([JSON.stringify(lastResult, null, 2)], {type: "application/json"});
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "scorecard-" + lastResult.policy + "-seed" + lastResult.seed + ".json";
  a.click();
  URL.revokeObjectURL(a.href);
}

/* ---------- dashboard evidence: real data first (ev- namespace) ---------- */
async function evApi(path, opts) {
  const r = await fetch(path, opts);
  if (!r.ok) {
    let msg = "HTTP " + r.status;
    try { msg += " " + (await r.json()).error; } catch (e) { /* keep code */ }
    throw new Error(msg + " on " + path);
  }
  return r.json();
}

function evBadge(band, text) {
  const s = document.createElement("span");
  s.className = "badge " + band;
  s.textContent = text;
  return s;
}

function evThin(traj, maxPts) {
  if (traj.length <= maxPts) return traj;
  const step = Math.ceil(traj.length / maxPts);
  return traj.filter((_, i) => i % step === 0);
}

async function evBoot() {
  const d = await evApi("/api/datasets");
  document.getElementById("evCounts").classList.remove("loading");
  document.getElementById("evCounts").textContent = d.counts.real +
    " real open-source pairs · " + d.counts.synthetic +
    " synthetic + morph pairs · scored live below";
  setStat("stReal", d.counts.real);
  setStat("stTotal", d.counts.total);
  setStat("stSamples", d.samples.length);
  const sel = document.getElementById("evPairSelect");
  sel.innerHTML = "";
  d.datasets.forEach((e) => {
    const o = document.createElement("option");
    o.value = e.id;
    o.textContent = e.label + " [" + e.kind + "]";
    sel.appendChild(o);
  });
  sel.value = "droid_pour_s1";
  const sb = document.getElementById("evSamples");
  sb.innerHTML = "";
  d.samples.forEach((s) => {
    const b = document.createElement("button");
    b.textContent = "Load " + s.id;
    b.title = s.blurb;
    b.onclick = () => evAuditSample(s.id);
    sb.appendChild(b);
    const dl = document.createElement("a");
    dl.href = "/api/sample/" + encodeURIComponent(s.id);
    dl.textContent = "file";
    dl.className = "muted small";
    sb.appendChild(dl);
  });
}

function evDraw(cv, sim, real, band) {
  const ctx = cv.getContext("2d");
  const W = cv.width, H = cv.height;
  ctx.clearRect(0, 0, W, H);
  const all = sim.concat(real);
  const xs = all.map((p) => p[0]), ys = all.map((p) => p[1]);
  const x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs);
  const y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
  const pad = 24;
  const sx = (x) => pad + ((x - x0) / ((x1 - x0) || 1)) * (W - 2 * pad);
  const sy = (y) => H - pad - ((y - y0) / ((y1 - y0) || 1)) * (H - 2 * pad);
  gridOn(ctx, W, H, pad);
  const colors = {green: "#2ea043", amber: "#d9a021", red: "#f85149"};
  const line = (pts, color, width, dash) => {
    ctx.beginPath();
    ctx.setLineDash(dash || []);
    ctx.strokeStyle = color;
    ctx.lineWidth = width;
    pts.forEach((p, i) => (i ? ctx.lineTo(sx(p[0]), sy(p[1])) : ctx.moveTo(sx(p[0]), sy(p[1]))));
    ctx.stroke();
    ctx.setLineDash([]);
  };
  line(sim, "#5b6570", 1.5, [5, 4]);
  line(real, colors[band] || "#fff", 2, []);
  ctx.font = "11px ui-monospace, monospace";
  ctx.fillStyle = "#8a8d91";
  ctx.fillText("commanded", 40, 16);
  ctx.fillStyle = colors[band] || "#fff";
  ctx.fillText("executed (" + band + ")", 160, 16);
}

async function evScore() {
  const pid = document.getElementById("evPairSelect").value;
  const btn = document.getElementById("evPairBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Scoring…";
  try {
    const r = await evApi("/api/pairscore", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({pair_id: pid}),
    });
    const v = document.getElementById("evVerdict");
    v.className = "verdict " + r.verdict.band;
    v.innerHTML = "";
    const strong = document.createElement("span");
    strong.textContent = r.verdict.label + " · " + pid;
    const small = document.createElement("small");
    small.textContent = r.verdict.detail + " · T " + r.T +
      " · scored live " + new Date().toLocaleTimeString();
    v.appendChild(strong);
    v.appendChild(small);
    document.getElementById("evMeta").textContent = "ledger #" + r.ledger.seq +
      " · hash " + r.ledger.entry_hash + " · [Verified] recomputed live";
    const tb = document.getElementById("evGates").querySelector("tbody");
    tb.innerHTML = "";
    r.gates.forEach((g, index) => {
      const tr = document.createElement("tr");
      tr.style.animationDelay = (index * 0.05) + "s";
      const tdM = document.createElement("td"); tdM.textContent = g.metric;
      const tdV = document.createElement("td"); tdV.textContent = g.value;
      tdV.className = "num";
      const tdB = document.createElement("td");
      tdB.appendChild(evBadge(g.band, g.band.toUpperCase()));
      const tdD = document.createElement("td");
      tdD.className = "desc"; tdD.textContent = g.desc;
      tr.append(tdM, tdV, tdB, tdD);
      tb.appendChild(tr);
    });
    evDraw(document.getElementById("evPlot"), r.sim, r.real, r.verdict.band);
    refreshLedger();
    refreshHistory();
  } catch (e) {
    const v = document.getElementById("evVerdict");
    v.className = "verdict red";
    v.textContent = "Score failed · " + e.message;
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

function evRender(r, src) {
  const out = document.getElementById("evOut");
  out.innerHTML = "";
  const d = document.createElement("div");
  d.className = "entry";
  d.appendChild(evBadge(r.verdict.band, r.verdict.label));
  d.appendChild(document.createTextNode(" " + r.name + ": alpha " + r.alpha +
    " (" + r.n_synthetic + "/" + r.n + " synthetic) · collapse risk " + r.collapse_risk));
  out.appendChild(d);
  const bar = document.createElement("div");
  bar.className = "bar alpha";
  const track = document.createElement("div");
  track.className = "track";
  const fill = document.createElement("div");
  fill.className = "fill " + r.verdict.band;
  fill.style.width = Math.max(2, r.alpha * 100) + "%";
  track.appendChild(fill);
  const tag = document.createElement("span");
  tag.textContent = "alpha " + r.alpha;
  bar.append(track, tag);
  out.appendChild(bar);
  const p = document.createElement("p");
  p.className = "muted small";
  p.textContent = "drift real " + r.drift_real_mean + " · drift synth " +
    r.drift_synth_mean + " · " + r.verdict.detail + " · scored live " +
    new Date().toLocaleTimeString() + " · Ledger #" + r.ledger.seq + ".";
  out.appendChild(p);
  if (src && src.episodes && src.episodes.length) {
    const first = src.episodes[0];
    const cap = document.createElement("p");
    cap.className = "small";
    cap.textContent = "first episode plotted live (" + first.id + ", T=" +
      first.sim.length + "):";
    out.appendChild(cap);
    const cv = document.createElement("canvas");
    cv.width = 640;
    cv.height = 220;
    cv.style.width = "100%";
    cv.style.background = "#0b0f13";
    cv.style.border = "1px solid rgba(255,255,255,0.08)";
    cv.style.borderRadius = "6px";
    out.appendChild(cv);
    evDraw(cv, evThin(first.sim, 220), evThin(first.real, 220), r.verdict.band);
  }
  refreshLedger();
  refreshHistory();
}

async function evAuditObj(obj, name) {
  obj.name = name;
  const r = await evApi("/api/batch", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(obj),
  });
  evRender(r, obj);
}

async function evAuditFile() {
  const f = document.getElementById("evFile").files[0];
  if (!f) {
    document.getElementById("evOut").innerHTML =
      "<p class='muted'>Pick a batch JSON file first, or load a sample below.</p>";
    return;
  }
  const btn = document.getElementById("evAuditBtn");
  const label = btn.textContent;
  btn.disabled = true;
  btn.textContent = "Auditing…";
  try {
    await evAuditObj(JSON.parse(await f.text()), f.name);
  } catch (e) {
    document.getElementById("evOut").innerHTML =
      "<p class='muted'>Audit failed: " + e.message + "</p>";
  } finally {
    btn.disabled = false;
    btn.textContent = label;
  }
}

async function evAuditSample(sid) {
  const out = document.getElementById("evOut");
  out.innerHTML = "<p class='muted'>Loading " + sid + "…</p>";
  try {
    await evAuditObj(await evApi("/api/sample/" + encodeURIComponent(sid)), sid);
  } catch (e) {
    out.innerHTML = "<p class='muted'>Sample audit failed: " + e.message + "</p>";
  }
}

/* ---------- boot ---------- */
$("scoreBtn").onclick = score;
$("compareBtn").onclick = compare;
$("sweepBtn").onclick = sweep;
$("huntBtn").onclick = hunt;
$("exportBtn").onclick = exportJSON;
document.getElementById("evPairBtn").onclick = evScore;
document.getElementById("evAuditBtn").onclick = evAuditFile;
loadPolicies().catch(() => { setPill(false, "OFFLINE"); });
evBoot().catch(() => {
  document.getElementById("evCounts").textContent =
    "Server unreachable · is it running? Start it with START.cmd, then reload.";
  setPill(false, "OFFLINE");
});
refreshLedger();
refreshHistory();
