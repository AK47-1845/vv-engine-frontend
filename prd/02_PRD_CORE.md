# GENUITY VERIFY: Production PRD Core
Version 1.0, 2026-10-03. Companion: 01_CONTEXT_BRIEF.md (read first), 03_MASTER_PROMPT.md
(operating contract), 04_DEEP_RESEARCH_PROMPTS.md. Approx: 5.2k tokens this file.

Status: PRD CORE (locked skeleton). Meta Spark 1.3 contributor expands each module into a
buildable spec (tasks + tests + acceptance runs) WITHOUT changing locked decisions,
scope exclusions, or honesty labels. Anything marked [VERIFY] or [DECISION] needs the
founder, not a guess.

## 1. Vision, users, why we win

Vision: the independent verification layer for the physical-AI age. World-model builders,
robot OEMs, synthetic-data vendors, insurers, and TICs all run through Genuity Verify
before anything touches production hardware. Policy in, evidence out: scorecards,
edge-case catalogues, provenance ledgers, compliance dossiers. North Star: number of
policies scored with evidence packs an external party (insurer, OEM reliability lead,
Notified Body) accepts as input to a real decision.

Personas: (P1) Validation engineer at OEM/Tier-1: uploads rollouts, triages red gates,
exports evidence for sign-off. (P2) Insurer analyst: consumes Robot Risk Passports
(per-policy risk scores + drift numbers) to price liability. (P3) TIC auditor: reviews
machine-readable technical files + re-runs verifications. (P4) Founder/operator: runs
demos, tracks gates, files provisionals. Phase 1 serves P1+P4 directly; P2/P3 consume
exports (no multi-tenant portal until Beta).

Why this wins (one paragraph for accelerators, all defensible): regulation creates the
customer (Jan 20 2027 mandatory NB assessment + OTA re-assessment rule), incumbents
cannot own it (OEM self-cert conflict; services P&L J-curve; TIC hardware DNA), no funded
pure-play competitor exists, the wedge is math depth (Frechet degradation, collapse
governance, bounded proofs, adversarial discovery) not sim scale, and every output is
evidence an auditor already demands (Art 10/12/14/15 map). Moat compounds via accepted
evidence formats + embedded CI/CD + calibration data network effects.

## 2. Goals, non-goals, success metrics

Goals (production V1): (G1) Score any uploaded trajectory rollout set against versioned
gate profiles with deterministic, reproducible verdicts. (G2) Discover breaking
disturbances via seeded adversarial hunt with refine step. (G3) Maintain tamper-evident
provenance for every run, dataset, and decision (hash-chained, verifiable by third
party). (G4) Export auditor-shaped evidence: scorecard JSON + human report + dossier
draft mapped to Machinery Reg/AI Act/ISO rows. (G5) Calibrate gates on real OXE pairs
so DRAFT labels can be lifted per gate with recorded evidence.

Non-goals (V1): no robot actuation or live control; no certified-safety claims; no
multi-tenant SaaS billing/SSO (demo auth + RBAC skeleton only); no full-VLA formal
proofs (bounded sub-policy queries only); no hosted public leaderboard (local scoring
first); no mobile app.

Success metrics: M1 exit = 42/42 MVP tests + OXE calibration runs logged + gate
thresholds versioned v1.0; M2 exit = hunt finds seeded breaks in <=50 trials on 3/3
fixture families + adversarial catalogue export; M3 exit = ledger verifies 1000-entry
chain + ratio-drift alarm fires on synthetic test; M4 exit = 2 provisional drafts +
1 pilot proposal + dossier accepted as "usable format" by 1 external reviewer
[DECISION: who]. Product-level: p95 score latency <30s for 10k-step rollouts on
reference laptop; zero false TRUSTED on the 4-fixture + OXE regression set
(false REVIEW/BLOCKED allowed, false TRUSTED is a sev-1).

## 3. Module map (7 modules = 7 patent vectors; Blueprint 5.2 architecture)

M1 Degradation scorer [EXISTS in MVP, harden]: sim-to-real divergence (discrete
Frechet base), drift-at-horizon curves, action sensitivity, spread, executability
proxies, bounds. Inputs: reference + observed trajectories + gate profile version.
Outputs: per-gate measurements + bands + verdict + evidence refs. Done when: OXE
calibration lifts DRAFT on >=5 gates with recorded runs.

M2 Runtime executability guard [MVP has proxies; build middleware]: PINN-loss +
inequality checks over action chunks (friction limits, torque/velocity envelopes,
singularity distance); HALT/flag on violation; never actuates (supervisory only).
Done when: seeded invariant violations caught in <=1 chunk latency on fixtures +
override-latency log format frozen for Art 14 mapping.

M3 Bounded-behavior verifier [MVP has Z3 stubs in claude formal.py; extend]:
bounded NN queries (exact rational, timeouts, UNKNOWN-tolerant) on scoped
sub-policies + safety filters; CBF dh/dt >= -alpha(h) checks; reachable-set
interface (alpha-beta-CROWN adapter; Marabou/Lean 4 as roadmap adapters with
stubs). Done when: 3 documented bounded proofs on toy sub-policies + UNKNOWN
rate reported, never hidden.

M4 Adversarial scenario engine [MVP has seeded hunt; scale up]: parameter search
over lighting/friction/mass/sensor-noise (+ Isaac/Genesis adapter interface;
local noise-model backend first, sim adapters as Phase 2). Outputs edge-case
catalogue (params + failing gate + severity + replay). Done when: finds all
seeded breaks + catalogue exports as auditor artifact.

M5 Cross-embodiment benchmark [MVP has gaps.py start; productize]: OXE pair
registry (RLDS reader for a pinned subset), centered-Frechet + span ratio with
strict same-frame guard (400 on cross-frame), batch alpha audit
(GOVERNED<=0.5/REVIEW<=0.8/BLOCKED). Done when: 10 OXE pairs scored end to end
with frame/IN SUFFICIENT handling proven (missing timing => INSUFFICIENT).

M6 Provenance ledger [MVP has hash chain; harden + extend]: append-only JSONL,
per-entry sha256 chaining, /verify endpoint, dataset cards (generator version +
verifier + pass rate), sample fingerprinting, ratio enforcement as build
parameter with drift alarms, re-anchor cadence tracking. Done when: 3rd-party
re-verification script passes on exported chain + alarm demo on synthetic drift.

M7 Compliance mapping engine [MVP has dossier.py draft; rebuild on P2 map]:
template-driven dossier compiler: scores/bounds/proofs/ledger excerpts ->
Machinery Reg Annex IV technical-file shape, AI Act Art 10/12/14/15 rows, ISO
10218 5.3.5 OTA checklist rows, 25785-1 placeholder rows (draft-aware, never
cited as requirements). OTA vault: weight-file registry + checksums + regression
gate (in-ODD = checksum + log; out-of-ODD = SUBSTANTIAL-MODIFICATION flag).
Done when: 1-click dossier export validates against a published JSON schema +
founder walkthrough with 1 external reviewer logged.

Build order: M1 harden -> M4 scale + M6 harden (parallel-safe) -> M5 productize ->
M2 middleware -> M7 compiler -> M3 extend. Rationale: revenue-adjacent evidence
first (score, hunt, ledger, dossier), deep math (bounds/proofs) last.

## 4. Functional requirements (testable; P0 = V1 blocker, P1 = V1 should, P2 = Beta)

Upload/score (M1/M5): FR-1 (P0) Accept rollout upload (JSON/CSV/RLDS-subset) with
schema validation; reject mismatched lengths/dims, non-finite values, unit-less
traces with itemized errors. FR-2 (P0) Score against a NAMED gate-profile version;
profiles immutable once published (new version = new id). FR-3 (P0) Return
per-gate measurement + threshold + band + verdict + evidence pointers in one
scorecard JSON (schema-published). FR-4 (P0) Missing required evidence yields
INSUFFICIENT for that gate, never PASS. FR-5 (P0) Verdict precedence:
any BLOCKED => BLOCKED; else any REVIEW/INSUFFICIENT => REVIEW; else TRUSTED.
FR-6 (P1) Batch score N policies and rank by worst-gate margin. FR-7 (P1) OXE
pair ingestion for the pinned subset with provenance recorded per pair.

Hunt (M4): FR-8 (P0) Seeded disturbance hunt (cmd bias/noise, actuation noise,
sensor noise, friction/mass where backend supports) with deterministic refine
around breaks; seed + full param log in output. FR-9 (P0) Hunt ledger-logs every
trial (params hash + outcome). FR-10 (P1) Local noise backend AND sim-adapter
interface (Isaac/Genesis) behind one HuntBackend protocol; sim adapters may ship
as documented stubs with recorded manual runs.

Ledger/provenance (M6): FR-11 (P0) Append-only hash-chained JSONL for runs,
reviews, uploads, hunts, dossier generations; /verify recomputes and reports
first-bad-index or OK + head hash. FR-12 (P0) Machine-readable dataset card per
scored dataset (generator id/version, verifier id, pass rate, real/synthetic
counts, alpha). FR-13 (P0) Ratio enforcement: profile declares max synthetic
fraction; exceeding it BLOCKs the dataset gate with the measured fraction shown.
FR-14 (P1) Fingerprint registry: synthetic sample ids recorded so audits can
recompute fractions later. FR-15 (P1) Re-anchor tracking: dataset age vs cadence
surfaced as REVIEW when stale.

Guards/proofs (M2/M3): FR-16 (P0) Executability guard evaluates action chunks
against inequality envelopes + PINN-loss proxy; violations HALT the evaluated
chunk with the violated invariant named. FR-17 (P1) Bounded verifier answers
scoped queries with PROVEN/VIOLATED/UNKNOWN + bounds + timeout record; UNKNOWN
never renders as pass. FR-18 (P2) CBF/reachability adapters behind one interface
with at least one worked toy proof end to end.

Dossier/OTA (M7): FR-19 (P0) One-click evidence export: scorecard JSON + human
HTML report + dossier JSON, all cross-linked by content hash. FR-20 (P0) Dossier
rows map to regulation rows (Machinery Annex IV items, AI Act Art 10/12/14/15,
10218 5.3.5 checklist) with per-row status + evidence pointer + "draft mapping,
human review required" banner. FR-21 (P1) OTA vault: register weight files
(sha256 + version + parent), run regression gates on update, emit checksum
record or SUBSTANTIAL-MODIFICATION flag with the breached boundary named.
FR-22 (P1) 25785-1 rows ship as clearly-marked DRAFT placeholders (standard
unpublished; no clause text reproduced).

Console (frontend): FR-23 (P0) Dashboard: run scorer on fixtures/uploads/samples,
compare view, sweep widget, ledger feed with verify button. FR-24 (P0) Gate drill
down: click a failed gate => exact trace interval + measurement + threshold +
evidence source on one screen (the memorable interaction). FR-25 (P0) Trajectory
replay with dark workspace + failed-interval highlighting. FR-26 (P1) Evidence
page: corpus table + pair scorer + upload + collapse illustration (labeled
simulation). FR-27 (P1) Docs + compliance pages with live widgets (score buttons,
verify buttons, dossier generation). FR-28 (P0) No page may render a passing
verdict for missing evidence; INSUFFICIENT states are first-class UI.

Admin/integration: FR-29 (P0) Token auth (demo + RBAC skeleton: operator/reviewer/
admin; reviews require reviewer+). FR-30 (P1) GENERATOR/VERIFIER adapter interface
for the founder's proprietary synthetic library (generate/verify + dataset card
I/O; stub implementation + conformance tests). FR-31 (P2) CI hook shape: POST
run + poll + verdict badge JSON (design the contract; reference client optional).

## 5. Non-functional requirements

- Determinism: identical inputs + profile + seed = byte-identical scorecard JSON
  (modulo timestamps, which live outside the hashed canonical body). Tested.
- Fail-closed: every error path (timeout, OOM-guard, sim missing, partial data)
  degrades to REVIEW/BLOCKED/INSUFFICIENT, never TRUSTED. Tested per module.
- Performance budgets (reference laptop): score <=30s p95 for 10k-step rollouts;
  hunt <=50 trials default cap with early stop; ledger verify streaming (no full
  load); UI first render <2s on desktop (mobile perf is a known backlog: track,
  do not fake).
- Offline-first core: scoring + ledger + reports work with zero network (MVP
  heritage). Sim adapters degrade to local backend with a banner.
- Security: no secrets in repo; tokens hashed at rest; uploads size-capped +
  type-sniffed; audit log of auth + review actions; dependency pinning + vuln
  scan in CI.
- Honesty UX: DRAFT gates badged; proxies labeled "proxy, not proof"; synthetic
  fixtures labeled; collapse illustration labeled simulation; ledger labeled
  tamper-evident (not immutable/attested).
- Compatibility: Windows-first run (START.cmd parity), Linux CI; Python 3.10+
  backend; Node 24 console/pitch site; ports 8000 (MVP engine), 5190/5191 (site).

## 6. Architecture (extend, do not rewrite)

- Monorepo: engine/ (scoring core: port MVP metrics_std + gaps patterns into
  typed, tested package; numpy allowed here, stdlib-only MVP kept as
  reference + offline fallback), server/ (FastAPI service: extend claude
  backend/api.py route map; SQLAlchemy store, sqlite default, postgres path),
  ledger/ (hash chain lib shared by server + CLI), console/ (extend Vite ops
  console; pitch site stays separate), sim_adapters/ (HuntBackend protocol +
  local backend + Isaac/Genesis stubs), dossier/ (template compiler + JSON
  schemas), eval/ (regression corpus: 4 fixtures + OXE subset + seeded hunts).
- Data flow: upload -> validate -> canonicalize (hash pinned) -> score (gates on
  unrounded values) -> verdict -> ledger append -> export (JSON+HTML+dossier).
  Every artifact carries input hash + profile version + code version.
- Ledger: JSONL append-only, sha256 chain, head hash API; export/import with
  re-verify script a third party can run without our stack.
- Frontend: console routes Dashboard/Replay/Evidence/Docs/Compliance/Ledger;
  pitch site untouched except honest placeholders. Shared design tokens;
  reduced-motion + a11y gates in CI (axe).
- CI gates per merge: unit + regression suites green, determinism check (run
  twice, diff canonical bodies), no-new-unlabeled-proxy scan (grep honesty
  labels), lint + typecheck, build pitch site.
- Environments: local-first (START.cmd / npm dev); staging = same stack on a
  second port; no public deploy without founder sign-off + placeholder audit.

## 7. Data model (core entities; extend claude store.py, do not fork it)

- Policy(id, name, version, embodiment_id, kind [uploaded/fixture/oxe], created,
  hashes). Embodiment(id, name, dof, frames, units). Dataset(id, card JSON:
  generator id/version, verifier id, pass rate, real/synthetic counts, alpha,
  fingerprint refs, created, reanchor_cadence). Trace(id, dataset_id, frames:
  t/cmd/act/obs, units, frame_id, hash). GateProfile(id, version, gates[]:
  {metric, green/amber thresholds, required_evidence[]}, status [draft/v1.0],
  calibrated_on). Run(id, policy_id, dataset_id, profile_id, seed, started,
  scorecard JSON, verdict, ledger_index). Scorecard(run_id, per_gate:
  {measurement, threshold, band, evidence_refs[]}). Review(id, run_id, reviewer,
  role, decision [approve/reject/needs-work], note, ledger_index). EvidencePack
  (id, run_ids[], dossier JSON, report HTML, export hash, ledger_index).
  LedgerEntry(index, ts, kind, payload_hash, prev_hash, entry_hash).
  OTARelease(id, policy_id, weight_sha256, parent_sha256, regression_run_id,
  verdict [IN-ODD/SUBSTANTIAL-MODIFICATION]).
- Invariants: profiles immutable; runs pin profile+input+code versions; ledger
  append-only (no update/delete endpoints, ever); reviews append-only (a rejection
  never deletes the run).

## 8. API surface (REST; keep claude route map, add the missing)

Keep: healthz/readyz/config, auth demo/login/logout/session, workspace,
datasets, embodiments, profiles, runs + reviews + export, experiments,
transfers, proofs, runtime + telemetry + reset, audit + audit/verify,
evidence/verify, records, standards, knowledge, admin users, tokens.
Add for V1: POST /api/uploads (rollout ingest + validation report);
POST /api/hunts + GET /api/hunts/{id} (seeded hunt + trials log);
GET /api/hunts/{id}/catalogue (edge-case export); POST /api/dossiers
(compile from run_ids + template version); GET /api/dossiers/{id}/rows
(regulation-mapped rows); POST /api/ota/releases + GET verdict;
GET /api/gates/regression (fixture + OXE suite status); POST /api/verify/chain
(third-party chain check on upload). Auth: bearer tokens (demo seeder for local);
reviews + dossier finalize require reviewer+ role. Errors: itemized validation
failures (field, rule, value hash, hint); never stack traces to clients.

## 9. Metrics/gates catalog (formulas locked; thresholds draft until OXE)

- G1 drift_at_horizon: max_t<=H ||pred_t - true_t|| with 3-step breach debounce;
  report full drift-vs-horizon curve. Draft: green <0.15m, amber <0.5m @H.
- G2 discrete_frechet: Eiter-Mannila DP over ref vs observed EE paths
  (same-frame enforced). Draft bands from fixture spread; OXE calibration sets v1.0.
- G3 action_sensitivity: E[||T(z,a) - T(z,shuffle(a))||^2] via dynamics probe
  (NOT seed shuffle); playback must read 0.0 exactly (regression-pinned).
- G4 rollout_spread: inter-seed variance sigma^2_seed + reconstruction residual
  E_recon where encoder available; report both, never blended.
- G5 executability: inequality envelopes (torque/velocity/friction bounds,
  singularity margin mu(q)) + jerk proxy; LABEL: proxy until sim-backed.
- G6 bounds/jerk: |jerk| + workspace-bound checks; same proxy label.
- G7 dataset_alpha: synthetic_fraction vs profile max; breach BLOCKs dataset gate.
- G8 transfer (pairs only): centered-Frechet + span ratio, same-frame guard,
  400 + INSUFFICIENT on cross-frame or missing timing.
- Precedence: BLOCK > REVIEW/INSUFFICIENT > TRUSTED. Calibration plan per gate:
  method + corpus + date + analyst recorded in profile version notes; DRAFT badge
  lifts ONLY with that record. [DECISION: founder approves each v1.0 threshold.]

## 10. Milestones (4-month gated plan; 2 gates/month; judge on dates)

- M1: (a) scorer hardened on pinned OXE subset + v1.0 thresholds proposed with
  calibration records; (b) 3 customer outreach emails sent + response log started.
  Proof: regression suite green incl. OXE pairs; outreach log file.
- M2: (a) M4 hunt scaled (local backend + sim-adapter interface + stubs) with
  catalogue export; (b) insurer response log (any reply counts, logged verbatim).
  Proof: seeded-break demo + catalogue JSON + log.
- M3: (a) M6 ledger hardened (streaming verify, cards, ratio alarms, re-anchor
  tracking) + third-party re-verify script; (b) M7 dossier compiler v0 with
  schema-validated export. Proof: external re-verify run + sample dossier.
- M4: (a) 2 provisional patent drafts (vectors 1+6) with attorney review
  initiated [DECISION: counsel]; (b) 1-client pilot proposal for one named asset.
  Proof: drafts + proposal doc + outreach response summary.
- Kill rule (founder-honest): if M1 outreach + M2 log show zero pull after 60
  days, report it plainly and propose the pivot (insurer-data product vs OEM-tool
  vs TIC-license) with evidence. Never hide a dead market.

## 11. Risks and mitigations (top 8)

- R1 Zero customer pull: mitigate with outreach gates in M1/M2 + kill rule above.
- R2 Applied Intuition Dana encroachment: mitigate with complementary positioning
  (rating agency), TIC/auditor channel they cannot own (conflict), depth over
  scale. Track Dana releases quarterly [VERIFY].
- R3 TIC build-in-house: mitigate with JV-on-standards + insurer-first revenue
  that does not need TICs. Precedents file maintained (NORD/Rheinland/AIQURIS).
- R4 Model-maker makes scorer obsolete: accepted; scorer is one module of seven,
  ledger/dossier/OTA layers persist regardless of generator quality.
- R5 Formal-methods overclaim: mitigated by bounded scope + UNKNOWN-tolerant UX +
  forbidden "proven safe" language (CI grep).
- R6 Sim adapters unavailable (no GPU/Isaac on founder laptop): local backend is
  the shippable default; sim runs recorded manually until automation lands.
- R7 Regulatory drift (25785-1 text changes, Omnibus delegated acts): mapping
  layer isolates change; quarterly review task; never cite draft clauses.
- R8 Founder bandwidth (solo builder): module order puts demoable evidence first;
  each milestone ends with a runnable artifact + one-page proof, never vibes.

## 12. Open questions for the founder (decision-only; max 8, no fishing)

- Q1: Approve v1.0 gate thresholds after OXE calibration? (per gate, dated)
- Q2: Name the Month-4 pilot asset + client? (M4 needs ONE named target)
- Q3: Patent counsel engaged for provisionals 1+6? (month to start)
- Q4: /privacy page fate + pitch-site placeholder approvals (bio/traction/video/
  contact)? (blocks any public deploy)
- Q5: Which OXE subset to pin for calibration? (size vs download pain)
- Q6: Proprietary library adapter priority: Tier-3 generator first, verifier
  first, or both together?
- Q7: Insurer vs OEM vs TIC for the first 3 outreach emails? (order matters)
- Q8: Postgres cutover trigger: at Beta start, or stay sqlite through pilots?
