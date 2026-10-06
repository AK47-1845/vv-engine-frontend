# GENUITY VERIFY: Architecture Blueprint (production, deploy-tomorrow grade)
Version 1.0, 2026-10-03. Expands 02_PRD_CORE.md section 6. Decisions here are
LOCKED unless the founder reopens them. Approx: 8k tokens.

## 0. Design thesis (read first)

Sellable-tomorrow B2B means: runs on THEIR machine (air-gap friendly),
evidence a stranger can re-verify without our stack, every number traceable to
inputs + code version, and failure behavior a safety engineer respects
(fail-closed, INSUFFICIENT-first, UNKNOWN-tolerant). No cloud dependency, no
K8s, no magic. Boring deployment, exotic math. That contrast IS the product.

## 1. System topology

Local-first, pilot-deployable on one box (reference: Windows laptop i7/16GB;
Linux VPS identical via compose):

- engine service (FastAPI, :8000): scoring, hunts, ledger, dossiers, OTA vault,
  auth, uploads. sqlite default (WAL mode), postgres via one env var.
- console (Vite build, served by engine service as static): Dashboard, Replay,
  Evidence, Docs, Compliance, Ledger. No separate Node process in production.
- pitch site (Next.js, :5191): marketing/proof surface only. Zero product
  dependency on it; it may be down while the product runs.
- file store: ./data/{uploads,traces,corpora,evidence,ledger.jsonl} (owner:
  operator; backup = copy the folder). No S3 in V1 (adapter interface only).
- All state the product needs lives in ./data + sqlite. Delete ./data = factory
  reset. Document this; auditors love it.

## 2. Repo layout (concrete; map existing code, do not fork)

- apps/server/ <- hi bro/claude bro/backend (extend route map per PRD section 8)
- apps/console/ <- hi bro/claude bro/web (extend per FR-23..28)
- apps/site/ <- hi bro/claude bro/site (pitch; hands off except placeholders)
- packages/engine/ <- NEW typed core ported from MVP backend/metrics_std.py +
  gaps.py (numpy allowed; pure functions; zero I/O; 100% of gate math lives here)
- packages/ledger/ <- NEW hash-chain lib (append, verify-stream, export/import)
  used by server AND a standalone re-verify CLI (single file, stdlib-only, so a
  third party runs it with no install)
- packages/dossier/ <- NEW template compiler + JSON schemas + regulation-row map
- packages/sim_adapters/ <- HuntBackend protocol + local backend + Isaac/Genesis
  stubs (documented manual-run procedure until automation)
- reference/mvp/ <- MVP OF VV governance platform FROZEN (offline fallback +
  behavior oracle for regression parity tests)
- eval/corpus/ <- 4 fixtures + pinned OXE subset + seeded-hunt goldens
- infra/ <- START.cmd (+ .ps1), docker-compose.yml, systemd + nssm service files,
  backup/restore scripts, admin guide
- Contracts in packages/*/contract/*.json (JSON Schema, versioned, additive-only)

## 3. Frozen interface contracts (semver; additive-only; every payload carries
input_hash + profile_version + code_version; timestamps OUTSIDE hashed bodies)

- Scorecard: {run_id, verdict, per_gate[{metric, measurement, threshold, band,
  evidence_refs[]}], inputs_hash, profile_version, code_version, created}.
- GateProfile: {id, version, status[draft|v1.0], gates[{metric, green, amber,
  required_evidence[]}], calibrated_on{method, corpus, date, analyst}}.
  Immutable once published; v1.0 needs founder sign + calibration record.
- DatasetCard: {generator{id,version}, verifier{id}, pass_rate, real_count,
  synthetic_count, alpha, fingerprint_ref, created, reanchor_cadence}.
- HuntCatalogue: {hunt_id, seed, backend, trials[{params_hash, params, outcome}],
  breaks[{params, failing_gate, severity, replay_ref}]}.
- Dossier: {pack_id, run_ids[], rows[{regulation_ref, status, evidence_pointer,
  mapping_version}], banner: "draft mapping, human review required",
  export_hash}. Regulation refs are dated strings, never legal conclusions.
- LedgerEntry: {index, ts, kind, payload_hash, prev_hash, entry_hash}.
  Genesis entry pins code_version + profile_versions in use.
- Error envelope: {error, field?, rule?, value_hash?, hint?, run_id?}. Itemized
  validation failures; never stack traces; fail-closed verdict attached when the
  call was a scoring call.

## 4. Determinism + data flow rules

Flow: upload -> validate (itemized) -> canonicalize (sorted keys, unrounded
floats, units+frames pinned) -> score (gates on raw values) -> verdict
(precedence locked) -> ledger append -> export (JSON+HTML+dossier cross-linked
by content hash). Seeds: every stochastic step takes an explicit seed recorded
in output; default seed fixed and documented. Float policy: compute in f64,
round ONLY for display, hash the unrounded canonical body. Regression rule:
eval/corpus goldens re-run on every merge; byte-diff on canonical bodies fails
the build (timestamps excluded by construction).

## 5. Deployment: sellable tomorrow (two options, no cloud required)

Option A local (demo + air-gap audits): double-click START.cmd -> engine :8000
(+ console static) with preflight checks (python, sqlite, ./data writable) and
a server.log. Uninstall = delete folder. This is the artifact you carry into
an insurer/TIC meeting on a laptop.
Option B single box (pilot): docker-compose up (api + volume for ./data +
optional postgres profile) or native service (systemd unit / nssm) + backup
script (nightly ./data snapshot + ledger head hash to append-only log).
Buyer handover kit: versioned zip (code + pinned deps + eval corpus + sample
evidence packs + re-verify CLI + admin guide + calibration records). Release
process: tag -> CI green -> bundle + sha256 + changelog -> transfer receipt
(existing package_transfer.py pattern). No public SaaS, no signup, no telemetry
calling home in V1 (auditors and insurers read that as a feature).

## 6. Security + auth model

Demo tokens for local (documented, single admin seed on first boot, rotation
command). RBAC skeleton enforced server-side: operator (run/score/upload),
reviewer (approve/reject/finalize dossier), admin (users/tokens/config).
Tokens hashed at rest (sha256 + salt). Uploads: size caps, extension + magic
sniffing, quarantine dir, never executed. Auth + review + export actions all
ledger-logged. Secrets via env only; CI secret-scan + pip/npm audit on every
merge. Rate-limit scoring endpoints (slowloris-grade: modest, documented).

## 7. Testing strategy (pyramid with teeth)

- Unit (engine): every gate incl. exact pins (playback sensitivity == 0.0),
  verdict precedence matrix, canonicalization vectors. Bar: 85%+ on engine.
- Property: determinism (run twice, diff), seed sweep (same seed same catalogue),
  fuzz uploads (garbage/empty/mismatched -> INSUFFICIENT/BLOCKED, never TRUSTED,
  never 500).
- Regression: eval/corpus (4 fixtures + OXE subset + seeded hunts) byte-compared
  to goldens; ledger tamper test (flip one byte -> verify reports exact index).
- Parity: new engine vs frozen MVP reference on fixtures (same verdicts or a
  documented, founder-approved reason).
- API: auth matrix (role x endpoint), validation envelopes, quota paths.
- Frontend: axe clean, Playwright flows (score fixture -> drill failed gate ->
  export pack -> verify ledger), reduced-motion + keyboard pass.
- Release: START.cmd smoke on clean Windows VM path + compose smoke; pitch site
  build; placeholder audit (no lorem/None/undefined in shipped UI).

## 8. CI/CD + environments

GitHub Actions per PR: lint + typecheck (py + ts), pytest, determinism check,
honesty-label grep (fail on new unlabeled proxy/proof language + forbidden
strings: certified/compliant/patented), frontend tests, pitch build. Release:
tag -> bundle + sha256 + changelog + transfer receipt. Environments: local
(START.cmd), staging (same stack, second port, scrubbed data), pilot box
(compose). No auto-deploy anywhere; every release is a signed handoff.

## 9. Observability (no PII, ever)

Structured logs (run_id on every scoring line; durations; gate outcomes as
codes not blobs). /healthz (liveness) + /readyz (sqlite + ledger + corpus
present + disk headroom). Ledger doubles as the audit trail. Console status
pill reflects readyz. Log retention documented; evidence retained per profile
policy (default: runs 90d, packs 1yr, ledger forever).

## 10. What stands out (protect these 5 in code; they are the demo)

1. Gate drill-down: click red gate -> exact trace interval + measurement +
   threshold + source on one screen. Nobody else shows the wound this fast.
2. Stranger re-verify: third party checks our evidence with a one-file stdlib
   script, no install, no account. Trust without trust-us.
3. Honesty system: DRAFT badges, proxy labels, INSUFFICIENT-first UX. Inverts
   the industry's demo-driven lying; reviewers remember it.
4. OTA story in-product: weight registry + checksums + SUBSTANTIAL-MODIFICATION
   flags. Snapshot-vs-movie, clickable.
5. Deterministic evidence: same inputs = byte-identical pack. Auditors can
   re-run history. This is the sentence that closes pilots.

## 11. Objections, answered in product (what people get mad about)

- "Prove it on MY data" -> upload path + OXE pairs + batch rank, 5-minute answer.
- "Who calibrates your gates?" -> calibration records on every v1.0 threshold,
  method + corpus + date + analyst, shipped with the profile.
- "Formal proofs or it didn't happen" -> bounded scope page: what is proven,
  on what sub-policy, with UNKNOWN rates published. Honesty beats overclaim.
- "Does it work offline / on-prem?" -> yes: core is offline-first, single-box
  deploy, no telemetry home. Say it on slide one of the pilot deck.
- "We already have Isaac/sims" -> we are not a sim; we are the layer that
  scores sims, hunts their blind spots, and compiles the dossier. Adapter, not
  replacement.
- "Why not our internal team?" -> structural conflict (they ship, we score) +
  4-month head start + evidence formats their auditors already accept.
- "Single founder risk" -> deterministic artifacts + docs + tests any engineer
  can run; escrow-able codebase; LTTS relationship as continuity backstop.

## 12. Build sequence (concrete; per-module specs follow as 06_Mx_SPEC files)

- M1 harden (weeks 1-2): port MVP metrics to packages/engine typed + tests;
  OXE subset pinned + scored; profiles v1.0 proposed with calibration records;
  console drill-down wired to real runs. Demo: upload -> red gate -> interval.
- M4 scale + M6 harden (weeks 3-5): HuntBackend protocol + local backend +
  catalogue export; ledger lib + re-verify CLI + cards + ratio alarms.
  Demo: seeded break found + third-party verify on a foreign machine.
- M5 productize (weeks 5-6): pair registry + frame guards + batch alpha audit.
  Demo: 10 OXE pairs, cross-frame 400 shown live (a feature, not a bug).
- M2 middleware (weeks 7-8): chunk guard + envelope checks + override-latency
  log format. Demo: seeded violation halts chunk with named invariant.
- M7 compiler (weeks 8-10): dossier templates + schemas + OTA vault + regression
  gates. Demo: 1-click pack for a scored policy, schema-validated.
- M3 extend (weeks 10-12): bounded queries + toy proofs + UNKNOWN reporting.
  Demo: PROVEN/VIOLATED/UNKNOWN on 3 scoped queries, rates on screen.
Each module spec file will carry: file-by-file tasks, tests, fixtures,
acceptance runs, honesty labels, and its demo script.
