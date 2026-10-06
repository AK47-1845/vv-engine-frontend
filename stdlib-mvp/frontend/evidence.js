/* Evidence page logic: corpus, pair scoring, xemb, batch upload, collapse. Vanilla JS. */
"use strict";
const $ = (id) => document.getElementById(id);
let ALL = [];

async function api(path, opts) {
  const r = await fetch(path, opts);
  if (!r.ok) {
    let msg = "HTTP " + r.status;
    try { msg += " " + (await r.json()).error; } catch (e) { /* keep code */ }
    throw new Error(msg + " on " + path);
  }
  return r.json();
}

function now() {
  return new Date().toLocaleTimeString();
}

function badge(band, text) {
  const s = document.createElement("span");
  s.className = "badge " + band;
  s.textContent = text;
  return s;
}

function shortSource(src) {
  if (!src) return "-";
  if (src.indexOf("http") === 0) {
    const m = src.match(/droid_raw\/[\d.]+\/([^/]+)\/(success|failure)\/([\d-]+)\/([^/]+)/);
    if (m) return "DROID " + m[1] + " " + m[3] + " " + m[4].replace(/_/g, " ");
    return "public URL (see card)";
  }
  return src;
}

function thin(traj, maxPts) {
  if (traj.length <= maxPts) return traj;
  const step = Math.ceil(traj.length / maxPts);
  return traj.filter((_, i) => i % step === 0);
}

/* ---------- corpus + selects + guide ---------- */
async function boot() {
  const d = await api("/api/datasets");
  ALL = d.datasets;
  document.getElementById("envPill").classList.add("ok");
  document.getElementById("envText").textContent = "LIVE";
  $("corpusCounts").classList.remove("loading");
  $("corpusCounts").textContent = d.counts.real + " real open-source pairs · " +
    d.counts.synthetic + " synthetic + morph pairs · " + d.counts.total + " total · " +
    d.samples.length + " upload-ready samples";
  const tb = $("corpusTable").querySelector("tbody");
  tb.innerHTML = "";
  ALL.filter((e) => e.kind === "real").forEach((e) => {
    const tr = document.createElement("tr");
    const tds = [e.label, "REAL", String(e.T), shortSource(e.source)].map((t) => {
      const td = document.createElement("td");
      td.textContent = t;
      return td;
    });
    tds[1].appendChild(document.createTextNode(" "));
    const go = document.createElement("button");
    go.textContent = "Score";
    go.onclick = () => { $("pairSelect").value = e.id; scorePair(); };
    const tdB = document.createElement("td");
    tdB.appendChild(go);
    tds.forEach((td) => tr.appendChild(td));
    tr.appendChild(tdB);
    tb.appendChild(tr);
  });
  const syn = ALL.filter((e) => e.kind !== "real").length;
  const tr = document.createElement("tr");
  const td = document.createElement("td");
  td.colSpan = 5;
  td.className = "muted";
  td.textContent = "+ " + syn + " synthetic + morph pairs in the picker below (documented degradation stack).";
  tr.appendChild(td);
  tb.appendChild(tr);
  ["pairSelect", "xembA", "xembB"].forEach((sid) => {
    const sel = $(sid);
    sel.innerHTML = "";
    ALL.forEach((e) => {
      const o = document.createElement("option");
      o.value = e.id;
      o.textContent = e.label + " [" + e.kind + "]";
      sel.appendChild(o);
    });
  });
  $("pairSelect").value = "droid_pour_s1";
  $("xembA").value = "droid_pour_s1";
  const other = ALL.filter((e) => e.kind === "real" && e.id !== "droid_pour_s1")[0];
  $("xembB").value = other ? other.id : "morph_pour_short_s1";
  const gb = $("guideTable").querySelector("tbody");
  gb.innerHTML = "";
  d.guide.forEach((g) => {
    const tr2 = document.createElement("tr");
    [g.demo, g.use, g.expect, g.why].forEach((t) => {
      const td2 = document.createElement("td");
      td2.textContent = t;
      tr2.appendChild(td2);
    });
    gb.appendChild(tr2);
  });
  const sb = $("sampleBtns");
  sb.innerHTML = "";
  d.samples.forEach((s) => {
    const b = document.createElement("button");
    b.textContent = "Load " + s.id;
    b.title = s.blurb;
    b.onclick = () => auditSample(s.id);
    sb.appendChild(b);
    const dl = document.createElement("a");
    dl.href = "/api/sample/" + encodeURIComponent(s.id);
    dl.textContent = "file";
    dl.className = "muted small";
    dl.title = "Download " + s.id + ".json, then upload it above for the live show";
    sb.appendChild(dl);
  });
}

/* ---------- shared path plot ---------- */
function drawOn(cv, sim, real, band, labelA, labelB) {
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
  ctx.fillText(labelA || "commanded", 40, 16);
  ctx.fillStyle = colors[band] || "#fff";
  ctx.fillText((labelB || "executed") + " (" + band + ")", 160, 16);
}

/* ---------- pair scoring ---------- */
async function scorePair() {
  const pid = $("pairSelect").value;
  $("pairScoreBtn").disabled = true;
  try {
    const r = await api("/api/pairscore", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({pair_id: pid}),
    });
    const v = $("pairVerdict");
    v.className = "verdict " + r.verdict.band;
    v.innerHTML = "";
    const strong = document.createElement("span");
    strong.textContent = r.verdict.label + " · " + pid;
    const small = document.createElement("small");
    small.textContent = r.verdict.detail + " · T " + r.T + " · gates DRAFT · scored live " + now();
    v.appendChild(strong);
    v.appendChild(small);
    $("pairMeta").textContent = "ledger #" + r.ledger.seq + " · hash " +
      r.ledger.entry_hash + " · [Verified] recomputed live";
    const tb = $("pairGates").querySelector("tbody");
    tb.innerHTML = "";
    r.gates.forEach((g, index) => {
      const tr = document.createElement("tr");
      tr.style.animationDelay = (index * 0.05) + "s";
      const tdM = document.createElement("td"); tdM.textContent = g.metric;
      const tdV = document.createElement("td"); tdV.textContent = g.value;
      tdV.className = "num";
      const tdB = document.createElement("td");
      tdB.appendChild(badge(g.band, g.band.toUpperCase()));
      const tdD = document.createElement("td");
      tdD.className = "desc"; tdD.textContent = g.desc;
      tr.append(tdM, tdV, tdB, tdD);
      tb.appendChild(tr);
    });
    drawOn($("pairPlot"), r.sim, r.real, r.verdict.band);
  } catch (e) {
    $("pairVerdict").className = "verdict red";
    $("pairVerdict").textContent = "Score failed · " + e.message;
  } finally {
    $("pairScoreBtn").disabled = false;
  }
}

/* ---------- xemb ---------- */
async function xemb() {
  const out = $("xembOut");
  out.innerHTML = "<p class='muted'>Comparing…</p>";
  $("xembBtn").disabled = true;
  try {
    const r = await api("/api/xemb", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({a: $("xembA").value, b: $("xembB").value}),
    });
    out.innerHTML = "";
    const d = document.createElement("div");
    d.className = "entry";
    d.appendChild(badge(r.band, r.label));
    d.appendChild(document.createTextNode(" Frechet " + r.frechet_centered +
      " · span ratio " + r.span_ratio + " (shape " + r.shape_band +
      ", scale " + r.scale_band + ", n=" + r.n + ")"));
    out.appendChild(d);
    const c = document.createElement("p");
    c.className = "muted small";
    c.textContent = r.a + "  vs  " + r.b + " · DRAFT bands · scored live " +
      now() + " · Ledger #" + r.ledger.seq + ".";
    out.appendChild(c);
  } catch (e) {
    out.innerHTML = "<p class='muted'>Compare failed: " + e.message + "</p>";
  } finally {
    $("xembBtn").disabled = false;
  }
}

/* ---------- batch upload + samples ---------- */
function driftBars(out, episodes) {
  const maxD = Math.max.apply(null, episodes.map((e) => e.mean_drift).concat([0.001]));
  episodes.forEach((e) => {
    const row = document.createElement("div");
    row.className = "bar";
    row.style.display = "flex";
    row.style.alignItems = "center";
    row.style.gap = "6px";
    const lab = document.createElement("span");
    lab.textContent = (e.source === "real" ? "R " : "S ") + e.id.slice(0, 18);
    lab.style.width = "170px";
    lab.style.overflow = "hidden";
    lab.style.textOverflow = "ellipsis";
    lab.style.whiteSpace = "nowrap";
    const track = document.createElement("div");
    track.className = "track";
    track.style.flex = "1";
    track.style.height = "10px";
    track.style.background = "#0b0f13";
    track.style.borderRadius = "3px";
    track.style.overflow = "hidden";
    const fill = document.createElement("div");
    fill.style.height = "100%";
    fill.style.width = Math.max(2, (e.mean_drift / maxD) * 100) + "%";
    fill.style.background = e.source === "real" ? "#2ea043" : "#d9a021";
    track.appendChild(fill);
    const tag = document.createElement("span");
    tag.textContent = e.mean_drift;
    row.append(lab, track, tag);
    out.appendChild(row);
  });
}

function renderBatch(r, src) {
  const out = $("batchOut");
  out.innerHTML = "";
  const d = document.createElement("div");
  d.className = "entry";
  d.appendChild(badge(r.verdict.band, r.verdict.label));
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
    r.drift_synth_mean + " · " + r.verdict.detail + " · scored live " + now() +
    " · Ledger #" + r.ledger.seq + ".";
  out.appendChild(p);
  if (r.generation_curve && r.generation_curve.length > 1) {
    const g = document.createElement("p");
    g.className = "small";
    g.textContent = "generation drift: " + r.generation_curve.map((c) =>
      "g" + c.generation + "=" + c.mean_drift).join(" -> ") +
      " (slope " + r.generation_slope + ")";
    out.appendChild(g);
  }
  const h = document.createElement("p");
  h.className = "small";
  h.textContent = "per-episode drift, straight from your file (R = real, S = synthetic):";
  out.appendChild(h);
  driftBars(out, r.episodes);
  if (src && src.episodes && src.episodes.length) {
    const first = src.episodes[0];
    const cap = document.createElement("p");
    cap.className = "small";
    cap.textContent = "first episode plotted live (" + first.id + ", " +
      (first.source || "?") + ", T=" + first.sim.length + "):";
    out.appendChild(cap);
    const cv = document.createElement("canvas");
    cv.width = 640;
    cv.height = 240;
    cv.style.width = "100%";
    cv.style.background = "#0b0f13";
    cv.style.border = "1px solid rgba(255,255,255,0.08)";
    cv.style.borderRadius = "6px";
    out.appendChild(cv);
    drawOn(cv, thin(first.sim, 220), thin(first.real, 220), r.verdict.band,
      "commanded", "executed");
  }
}

async function auditBatchObj(obj, name) {
  obj.name = name;
  const r = await api("/api/batch", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(obj),
  });
  renderBatch(r, obj);
}

async function auditUpload() {
  const f = $("batchFile").files[0];
  const out = $("batchOut");
  if (!f) {
    out.innerHTML = "<p class='muted'>Pick a batch JSON file first, or load a sample below.</p>";
    return;
  }
  $("batchBtn").disabled = true;
  try {
    const text = await f.text();
    await auditBatchObj(JSON.parse(text), f.name);
  } catch (e) {
    out.innerHTML = "<p class='muted'>Audit failed: " + e.message + "</p>";
  } finally {
    $("batchBtn").disabled = false;
  }
}

async function auditSample(sid) {
  const out = $("batchOut");
  out.innerHTML = "<p class='muted'>Loading " + sid + "…</p>";
  try {
    const doc = await api("/api/sample/" + encodeURIComponent(sid));
    await auditBatchObj(doc, sid);
  } catch (e) {
    out.innerHTML = "<p class='muted'>Sample audit failed: " + e.message + "</p>";
  }
}

/* ---------- collapse ---------- */
async function collapse() {
  const out = $("collapseOut");
  out.innerHTML = "<p class='muted'>Running…</p>";
  $("collapseBtn").disabled = true;
  try {
    const r = await api("/api/collapse", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({seed: 1}),
    });
    out.innerHTML = "";
    const d = document.createElement("div");
    d.className = "entry";
    d.appendChild(badge(r.verdict.band, r.verdict.label));
    d.appendChild(document.createTextNode(" " + r.verdict.detail + " · " + r.note));
    out.appendChild(d);
    const maxV = Math.max.apply(null, r.curve.map((c) => c.variance));
    r.curve.forEach((c) => {
      const row = document.createElement("div");
      row.className = "bar";
      const lab = document.createElement("span");
      lab.textContent = "gen " + c.generation;
      lab.style.width = "52px";
      const track = document.createElement("div");
      track.className = "track";
      const fill = document.createElement("div");
      fill.className = "fill " + (c.diversity_retained < 0.5 ? "red" : "amber");
      fill.style.width = Math.max(2, (c.variance / maxV) * 100) + "%";
      track.appendChild(fill);
      const tag = document.createElement("span");
      tag.textContent = "var " + c.variance;
      row.append(lab, track, tag);
      out.appendChild(row);
    });
    const c = document.createElement("p");
    c.className = "muted small";
    c.textContent = "simulated just now · " + now() + " · Ledger #" + r.ledger.seq + ".";
    out.appendChild(c);
  } catch (e) {
    out.innerHTML = "<p class='muted'>Run failed: " + e.message + "</p>";
  } finally {
    $("collapseBtn").disabled = false;
  }
}

/* ---------- boot ---------- */
$("pairScoreBtn").onclick = scorePair;
$("xembBtn").onclick = xemb;
$("batchBtn").onclick = auditUpload;
$("collapseBtn").onclick = collapse;
boot().catch((e) => {
  $("corpusCounts").textContent = "Server unreachable · is it running? " + e.message;
  document.getElementById("envPill").classList.add("bad");
  document.getElementById("envText").textContent = "OFFLINE";
});
