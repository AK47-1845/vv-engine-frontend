# GENUITY VERIFY: Full-Context Brief for Meta Spark 1.3 Contributor
Version 1.0, 2026-10-03. Companion files: 02_PRD_CORE.md, 03_MASTER_PROMPT.md, 04_DEEP_RESEARCH_PROMPTS.md.
Paste guide: 00_README_PASTE_GUIDE.md. Approx: 7.3k tokens this file.

This file exists because the full source corpus (5 research docs, 100+ pages; 4 external
research packs; 2 codebases) cannot be uploaded to the model. Everything below is distilled
from those primary sources. Numbers use the founder's verification tags: [Verified] =
primary source/audit; [Reported] = trade press/company claim; [Estimated] = modeled with
stated method; [Speculative] = judgment call. Any number here WITHOUT a tag must be
treated as unverified. Never upgrade a tag without a new primary source.

Rule zero for the model: never invent traction, customers, pilots, revenue, certifications,
or benchmark wins. The product must visibly label draft gates, proxy metrics, and synthetic
fixtures as such. This honesty discipline is the brand.

## 1. Mission in one paragraph

Build Genuity Verify, an independent Verification and Validation (V&V) engine for the
physical-AI age: whoever builds world models, deploys physical-AI robots, or trains on
synthetic data gets scored by us. The platform ingests robot policies/trajectories/datasets
and outputs red/amber/green trust scorecards, adversarial edge-case catalogues, tamper-evident
provenance ledgers, and auditor-ready compliance dossiers. First money comes from insurers
(actuarial robotics data), then OEMs (regulatory-forced sign-off), then TICs (licensed audit
tooling). The forcing function is EU Machinery Regulation 2023/1230, mandatory Jan 20, 2027
[Verified, EUR-Lex]: self-evolving safety AI needs third-party assessment, and every
safety-shifting OTA update re-opens the file. Tagline the model must internalize: TICs
certify the SNAPSHOT (hardware, once); we monitor the MOVIE (neural behavior, continuously).

## 2. Founder and voice

Karthikeya Adari, IIT Guwahati Mech 2023-27, founder of Genuity IO, currently inside LTTS
Bangalore on an external semester. He spent 4 months inside LTTS: won trust with an
aerospace synthetic-data POC, got redirected from building to research, produced the 4
research documents, then built Module 1 (trust scorecard) before the Sept 30 CTO pitch.
Voice for any user-facing text: humble-elite. Findings-first, invite correction, dates and
checkable gates over adjectives. Banned: "you should", "obviously", "trust me", flexing
the Pvt Ltd. Product text follows the same voice: state what was measured, how, and what
remains unproven.

## 3. Research synthesis (corrected numbers only)

### 3.1 The macro frame (Genesis Part 1 + Practice doc, P1-corrected)

- The bottleneck moved: public text exhausts ~2027-2028 [Estimated]; frontier compute is
  power-capped (gigawatt scale), growth slowing ~10x/yr toward 3-4x/yr by 2028 [Estimated].
  Next capability comes from proprietary physics-verified synthetic data, not bigger
  pretraining runs.
- Four epochs: supervised discriminative, autoregressive pretraining, test-time reasoning,
  embodied physical AI (now). Each epoch absorbed the last; the 4th is where marginal
  capability lives.
- The Humanoid Capital Trap: >$5.0B into humanoid/VLA in 18 months [Verified] vs <$20M
  industry-wide unconstrained production revenue [Estimated] = 250:1 asymmetry. (Old
  $3.2B/160:1 figures are DEAD, superseded by P1 audit.)
- Corrected company table [Verified unless noted]: Figure AI ~$1.9-2.0B raised, $39B
  (Sept 2025), <$10M realized / $100M+ contracted; Skild ~$1.7B raised, $14B (Jan 2026
  SoftBank), revenue undisclosed (est. <$10M); Physical Intelligence ~$1.07B raised,
  $5.6B (Nov 2025 CapitalG), <$5M; Wayve ~$1.3B raised, $4.8B post (Series C May 2024),
  NOT $7.8B; Applied Intuition $15B (June 2025) + $150-200M ARR [Reported]; Patronus
  $50M Series B June 25 2026, ~$70M total, customers incl. CARIAD, MongoDB; LTTS cap
  ~$4.0B (Rs 34,012 Cr, BSE/NSE late-Sept 2026), NOT $6B.
- Production reality tiers: Tier 1 cash flowing = sim/validation/inspection/integration
  (Applied Intuition, Isaac-class under ISO 26262, Waymo 500k+/wk by 2026 [Verified]);
  Tier 2 bounded pilots = Figure at BMW Spartanburg (Aug 2024), Apollo at Mercedes
  (Mar 2024), Digit at Amazon/GXO, Stretch at DHL [all Verified press]; Tier 3 lab =
  zero-shot assembly, domestic generalists [Speculative].
- Hardware truth: humanoid MTBF <50h continuous multi-joint actuation [Verified];
  BOM $100-250k/unit [Estimated]; target $30-50k needs planar drives, stamped
  gearboxes, custom ASICs. MTBF milestones: 500h single-shift, 2000h+ multi-shift.
- Software VLA multiples >1000x ARR will compress as OpenPI/SmolVLA mature: models
  commoditize, verification is the durable layer.

### 3.2 The three world-model schools (Genesis Part 2)

Never conflate them; school mismatch to use case is the field's most common error.
- Renderer school (Sora, Genie 1/2, Oasis, Gen-3, Cosmos-render): pixel
  diffusion/autoregressive video. Photorealistic, seconds/frame, high hallucination
  risk, poor verifiability (no ground truth on learned physics). Best for human-facing
  sim/content. TRL: high commercial, low industrial trust.
- Latent/JEPA school (V-JEPA/I-JEPA, DreamerV3, TD-MPC2): energy-based latent
  prediction, no pixels. <62h real robot data reported for SOTA zero-shot planning,
  sub-5ms inference feasible, low hallucination, moderate verifiability. Best for
  safety-critical robotic control. TRL: medium, rising fast.
- Spatial/Engineered school (Tesla occupancy nets, NVIDIA Cosmos/Isaac, MIT/Stanford
  Genesis sim): 3D/4D voxel occupancy + PINN constraints, explicit conservation laws,
  metric geometry output. Medium data efficiency (sim-bootstrapped), low-medium
  latency, high verifiability. Best for industrial digital twins and AV perception.
  TRL: medium-high in AV, nascent elsewhere.
- Formal substrate: POMDP M = <S,A,O,T,E,R,gamma>; encoder/transition/decoder
  zt -> zhat(t+1) ~ That(zhat|zt,at) -> ohat(t+1); planning = value over imagined
  latent rollouts V_pi(zt). Pearl's ladder: text models stuck at Rung I
  (association P(Y|X)); control needs Rung II intervention (P(Y|do(u))) and Rung III
  counterfactuals. Deploying Rung-I models on Rung-II tasks is a category error.
- No shared world-model leaderboard exists [Verified]. Vendor SOTA claims are
  provisional marketing. Our scorecard can become the de-facto standard.

### 3.3 The five failure modes with math (Genesis Part 2; the product's scoring spine)

Each mode below maps to one or more MVP gates (mapping in brackets).

- FM1 Compounding autoregressive drift: E[||zhat_T - z_T||] <= O(T * eps).
  Per-step latent error eps compounds over horizon T. Models stay coherent for
  MINUTES not hours; objects pass through walls. Product: drift_at_horizon gate
  with measured drift-vs-horizon curves, not single-point demos. Demand hours-long
  evidence. [MVP: drift_at_horizon with 3-step breach debounce]
- FM2 Executability gap: perceptual losses (LPIPS/SSIM) carry zero information
  about contact dynamics (F_contact = mu * F_N). Flawless-looking video can command
  shattering grasps. Product: PINN-constrained checks + certified-simulator
  cross-checks, never perceptual similarity alone. [MVP: executability_proxy
  (bounds/jerk proxy only, HONESTLY LABELED, needs Isaac/Genesis sim for proofs)]
- FM3 Perceptual hallucination: z_q(x) = argmin_k ||E(x) - e_k||^2. OOD inputs
  (unfamiliar tool, steam, sensor noise) collapse to nearest codebook token,
  silently corrupting the rollout from step one. Product: reconstruction residual
  E_recon(x) = ||x - D(E(x))||^2 gating (E_recon > tau) + OOD bounds. [MVP: partial
  via rollout_spread; full OOD module is Month-2 work]
- FM4 Action marginalization: E[||That(z,a) - That(z,shuffle(a))||^2] -> 0.
  Action sensitivity test: if shuffling actions barely changes prediction, the model
  ignores control input (dead steering wheel playing back a plausible tape).
  Hardest to detect externally. [MVP: action_sensitivity, playback fixture reads
  EXACTLY 0.0]
- FM5 Sim-to-real gap: D_real != D_sim. 2026 industry consensus: synthetic data
  cannot fully replace real data for robotics. Winning strategy is hybrid: synthetic
  for volume + rare edges, real data retained to validate safety. Any vendor
  claiming to have CLOSED the gap is disqualified on that claim alone.
  [MVP: discrete_frechet sim-vs-real end-effector path distance = patent vector 1]

Compute/latency note: kHz control loops cannot tolerate seconds/frame generation;
this favors engineered/targeted platforms over general simulators in deployment.
Convergence view: generative for human-facing sim, latent for safety-critical
control, engineered constraints for factory-floor trust. Evaluate deployments on
right-school-for-right-job, never on demo impressiveness.

### 3.4 Synthetic data doctrine (Genesis Part 3; the governance spine)

- Four tiers, each with its verifier: T1 model-generated reasoning traces (tree
  search, self-play, compiler-verified execution); T2 statistically grounded tabular
  (copulas, DP-GANs, KS-test validation); T3 simulated spatial telemetry (3DGS,
  NeRFs, Isaac rollouts); T4 formally verified data (Lean 4, Coq, SMT, ASIC-grade
  formal methods). Match tier to cost-of-being-wrong.
- Model collapse law. REPLACE (Shumailov et al., Nature 2024): recursive training
  on unfiltered self-output drives lim(n->inf) Var[X_n] = 0; tails (the safety
  edge cases) die first. ACCUMULATE-AND-FILTER (Gerstgrasser et al. 2024):
  D(n+1) = alpha * D_real + (1-alpha) * {x ~ G | Verifier(x) = TRUE}. This
  equation is the single most important governance constraint in the product:
  every dataset must state its alpha and its verifier like a financial statement
  states its accounting method. MVP contract uses explicit real_samples,
  synthetic_samples, synthetic_fraction (alpha conventions differ across sources;
  never assume).
- Curation beats volume: 1000 physics-verified synthetic trajectories beat 1M
  unverified rollouts. GRPO advantage A_i = (r_i - mean(r)) / std(r): groups of
  candidate trajectories graded by a programmatic verifier (unit test OR
  physics-collision check), portable from code reasoning to physical reasoning.
- PINN loss: L_total = L_data + lambda_pinn * ||du/dt + N[u] - f||^2. The
  differential-operator penalty forces generated imagination to obey governing
  equations. PINNs AUGMENT certified FEM/CFD simulators; they never replace them.
- Uncertainty diagnostics (log independently, never blend): reconstruction
  residual E_recon (aleatoric/input-level) + inter-seed denoising variance
  sigma^2_seed (epistemic/model-confidence). Spikes mark blind spots for human or
  formal review.
- Closed-loop flywheel: telemetry -> calibration -> generation -> deployment ->
  logging -> back to telemetry. Each component commoditizes; the closed loop does
  not. Durable position lives in the loop.
- Four MVP provenance controls (all four ship in the ledger module): dataset cards
  (generating model version + verifier + pass rate, machine-readable);
  fingerprinting (tag synthetic samples so future audits can measure fractions);
  ratio enforcement (alpha is a BUILD parameter; silent drift toward synthetic =
  replace-collapse in slow motion); periodic re-anchoring (refresh D_real on fixed
  cadence; six-month-old telemetry is stale calibration).
- Risk surface: bias amplification, verification cost, provenance-tracking failure.
  No standardized measure of AI-generated internet fraction exists: unvetted public
  data = unquantified collapse risk. Verifiably human, pre-2023 data is a defensive
  asset. Any pipeline that cannot state ratio + verifier + provenance is incomplete
  by definition.

### 3.5 The seven-row evaluation framework (Genesis 4.4; Module 1's checklist)

Every world-model/synthetic-data claim is tested on: (1) school identification
(Renderer/Latent/Spatial vs use case); (2) long-horizon consistency (measured drift
at increasing horizons, hours not minutes); (3) executability proof (tested vs real
or certified-sim contact dynamics, not LPIPS/SSIM); (4) collapse governance
(stated alpha + verifier identity per dataset, refuse otherwise); (5) uncertainty
exposure (E_recon + seed variance at inference time, or hidden); (6) sim-to-real
honesty (claims of closing the gap are disqualifying; demand stated hybrid ratio);
(7) benchmark provenance (shared standardized leaderboard vs self-reported
internal). A platform that cannot answer all seven with specifics has not earned
safety-critical deployment. Worked illustration (robot arm + new part variant):
low-hundreds real examples -> Spatial/Engineered school (PINN contact) ->
thousands of verified synthetic grasps at fixed alpha + residual monitoring ->
generalization at fraction of real-trial cost with auditable trust per decision.

## 4. Commercial engine (Idea 1 + Blueprint + P3/P4, corrected; speculative TAM is DEAD)

- Structural conflict (the moat's legal half): VLA builders are paid to ship, so a
  builder-owned verifier is paid to pass. Boeing 737 MAX = the self-certification
  parable. Independent validation must come from an independent party. This locks
  OEMs out of the V&V layer permanently. Same logic extends to ER&D firms that
  build AND validate for the same OEM: role split required (services firm does
  deployment/integration/channel; verification IP + evidence sit behind an
  information firewall in a separate entity).
- Snapshot-vs-movie (the one-liner): TUVs certify the SNAPSHOT (hardware, once,
  e.g. Mornine CE-MD/CE-RED/EN 18031 Sept 26 2025 [Verified]); we monitor the MOVIE
  (continuous neural behavior across OTA updates). Every safety-shifting OTA update
  = substantial modification = re-assessment + new CE. Static certs decay on every
  release; continuous verification compounds.
- Margin rewrite: ER&D services ~15-17% EBIT, linear headcount scaling, labor-moat.
  V&V SaaS targets 30-40% EBIT at scale, annual SaaS + per-certification fees,
  compute scaling, CI/CD-embedded moat. Adjacent proof: Applied Intuition 80%+
  gross margins, $150-200M ARR [Reported].
- GTM order (P3-ranked, Opus-endorsed): (1) INSURERS first, fastest cash: Munich Re
  aiSure/Mosaic, Autonomy Insurance (Robot Health Passport telemetry API), Relm,
  Swiss Re research. They demand telemetry + MTBF + sim-validation records and pay
  $150-500k/engagement on 2-4 month cycles [Estimated] for a "Robot Risk Passport"
  (our scorecard as actuarial input). (2) OEMs on regulatory pull: Figure,
  Apptronik, Agility, 1X, Boston Dynamics + Chinese OEMs needing CE marks;
  Automated Safety Dossier Compiler; $500k-1.5M/engagement [Estimated], 4-6 month
  cycles. (3) TICs for credibility + permanence: TUV SUD (AIQCP, AIQURIS venture,
  AI Risk Navigator, ISO/IEC 42001), TUV Rheinland (NVIDIA collab, Fennec/ASAP
  qualified tools), Intertek (CFR early audits), SGS/BV/DNV; license the ML-native
  layer or JV on standard definitions; $250-750k + fees [Estimated], 6-12 month
  cycles. Pilot-economics Year-1 case replaces TAM slides: 3 engagements x
  $150k-1.5M. The 1.5M-units/$2.25-3.75B TAM stays [Speculative] context ONLY.
- Applied Intuition ($15B June 2025 [Verified]; Dana July 2026 "Android for every
  moving machine"; Vehicle OS, SDS incl. Japan, Copilot; customers incl. TRATON,
  Stellantis, Toyota/Porsche/VW, HUMAIN, DoD, HII, Northrop, Komatsu,
  Heidelberg; EpiSci acquired): complementary, NOT competitive. Rating agency, not
  bank. They sell simulation TO OEMs; we score OEM output FOR regulators/insurers.
  If they ever build the audit layer, Boeing conflict eats them too. Their DNA
  remains wheels-on-roads + sim scale; formal neural-policy proofs + humanoid
  kinematics + TIC bridge is our wedge. Window narrows as Dana generalizes.
- No funded pure-play competitor exists for humanoid neural-policy V&V (double
  edged). Adjacent only: Patronus (software agents, no physics), Credo (~$41M,
  software GRC + EU AI Act Policy Packs), Holistic (~$20M, bias/fairness),
  Galileo ABSORBED by Cisco Apr 2026 (the "Galileo pattern" proves infra giants buy
  this layer). Research-only: generator-verifier frameworks, neural posterior
  estimation, robotics post-training protocols (done in-house at Figure/PI, not
  sold). Survival line for "why has nobody built it": the customer does not exist
  yet; Jan 2027 regulation creates it. Pre-positioning is cheap now, expensive in
  Q2 2027.
- TIC licensing precedents that kill "TICs build in-house": Applied Intuition
  suite qualified by TUV NORD (ISO 26262); TUV Rheinland x NVIDIA + Fennec/ASAP
  (T2 qualified tools); TUV SUD AIQURIS venture. TICs already license third-party
  verification software.
- Open tooling the platform must interoperate with (all downloadable offline):
  Open X-Embodiment (Apache 2.0, RLDS, 60+ embodiments, multi-TB); Isaac Sim/Lab
  (free individual, ~25GB, RTX 3070+; locomotion + domain randomization);
  MuJoCo/MJX (academic manipulation re-scoring); Genesis sim (Apache 2.0, ~5-10GB,
  multi-physics + Nyx renderer). Standard 2026 loop: train Isaac Lab ->
  re-score MuJoCo/MJX -> deploy hardware (Real2Sim2Real).
- LTTS roadmap context (Phase 1 $2.8M V&V practice Q1 2027 with Automated Safety
  Dossier Compiler: CBF dh/dt >= -alpha(h) + reachable sets R(T;X0) subset C via
  alpha-beta-CROWN -> ISO 13849/IEC 61508 dossiers; Phase 2 $1.3M PLC alliances;
  Phase 3 $4.2M synthetic factories; CoE $2.5M/yr). Durable domain moat: Jacobian
  singularity manipulability mu(q) = sqrt(det(J*J^T)) -> 0 demands DLS filtering
  pure-ML teams cannot build; EtherCAT/Profinet <1ms jitter; Cat 4/PLe dual-channel
  interlocks.

## 5. Regulatory clock (P1/P2; legal-review-required, never legal opinions)

- EU Machinery Regulation 2023/1230: applies mandatorily Jan 20, 2027, no grace
  period [Verified, EUR-Lex]. Annex I Part A Item 24 two-tier test: (1) AI performs
  a safety function (task-only AI like inspection is OUT, Module A self-assessment);
  (2) it is SELF-EVOLVING post-shipment (adapts weights/logic on field data).
  Self-evolving safety AI = mandatory Notified Body assessment. Frozen-weight
  safety systems may self-assess under Module A IF harmonized standards cover all
  EHSRs. VLA foundation policies ARE self-evolving: that is the trigger.
- Routes (Art 25): Module A internal production control (non-safety/frozen only,
  immediate); Module B+C type-examination + type conformity (6-12 mo); Module H
  full quality assurance incl. QMS audit (9-14 mo); Module G unit verification for
  bespoke cells (4-8 mo/unit). NB queues already 6-12 months and lengthening.
- OTA rule (Art 3(16)/18): safety-shifting updates = substantial modification =
  updater becomes manufacturer = full re-assessment + updated technical file + new
  CE BEFORE deployment. This is the legal spine of snapshot-vs-movie and of the
  OTA vault module.
- EHSRs that shape product: 1.1.9 protection against corruption (cyber interference
  resistance; post-market software faults must not hazard); 1.2.1 safety/reliability
  of control systems (ML controls must not exceed designed performance boundaries;
  real-time adaptation bounded by functional safety controllers).
- EU AI Act (2024/1689) intersection: Art 6(1) dual test (safety component + third-
  party assessment route) triggers high-risk under BOTH acts for VLA safety
  functions. Art 43(2): single NB assesses machinery EHSRs + AI Act Ch.III s.2
  together (no dual filing). Omnibus dates: embedded Annex-I AI duties Aug 2, 2028
  (delegated acts fold AI requirements into Machinery Reg); standalone Annex-III
  high-risk Dec 2, 2027. Never imply 2026/27 AI-Act enforcement.
- Auditor artifact map (each row = a platform module): Art 10 dataset governance
  (lineage logs, diversity matrices, bias reports) -> provenance ledger; Art 15
  robustness (OOD reports, adversarial logs, noise bounds) -> edge-case module;
  Art 14 human oversight (safety-cage design, override latency logs, state
  diagrams) -> CBF/RTA dossier; Art 12 traceability (black-box log spec, retention
  protocol) -> telemetry ledger; Art 15(4)/IEC 62443 cyber (weight-signing logs,
  secure boot, RBAC) -> OTA vault. Founder line: "I build what auditors already
  demand."
- ISO 10218:2025 (Feb 2025): "cobot" term eliminated (collaboration = application
  property); Class I/II risk mapping to PL/SIL; section 5.3.5 = parameter locks +
  crypto checksums + restart on ML-weight updates (the OTA vault's normative hook).
- ISO/CD 25785-1 (TC 299/WG 12, stage ~30.60): UNPUBLISHED industrial-only draft,
  publication expected late 2026/2027. Never cite clauses as requirements. Draft
  direction: STO invalidated as safe state for balancing machines (cutting torque
  = uncontrolled fall = projectile hazard); fallback modes under discussion:
  Active Balance Recovery (counter-stepping), Controlled Energy-Loss Crouch
  (lower CoG), Directional Fall Containment (fall away from humans); metrics move
  to whole-body dynamic impact energy, HIC, peak impulse, momentum transfer.
  Product implication: fall-mitigation simulation + dynamic impact scoring module.
- Mornine tri-module precedent (Sept 26, 2025 [Verified]): CE-MD (structure,
  electrical, e-stop, functional safety incl. dual-channel encoders) + CE-RED
  (2014/53/EU EMC/radio incl. Wi-Fi 6/5G) + EN 18031-1/-2:2024 (secure boot,
  encrypted OTA, key storage, LiDAR/RGB-D anti-intercept). First humanoid to
  verify both EN 18031 parts. Hardware-only gap stands: neural policy + OTA
  behavior unverified = our wedge.
- Deployment framing: 0-2yr AGVs/mobile manipulators (ROI now), 3-5yr fenced
  humanoid pilots, 5yr+ unconstrained (needs MTBF >2000h).

## 6. What already exists in code (build ON this, never rewrite blindly)

Two codebases exist. The model must read the actual code before changing it.

A. MVP OF VV governance platform (stdlib-only Python, zero-install, runs offline):
- backend/server.py (API + static, :8000): compare/score endpoints, hunt, dossier,
  ledger verify, evidence/pair scoring, upload + 1-click samples, collapse curve.
- backend/metrics_std.py: drift_at_horizon (3-step debounce), discrete_frechet,
  action_sensitivity, rollout_spread, executability_proxy, band, verdict, gates.
  8 Genesis-4.4-inspired gates; verdicts TRUSTED/REVIEW/BLOCKED, fail-closed
  (worst gate decides).
- backend/policies.py (4 deterministic fixtures: clean/drifty/playback/synthfed),
  ledger.py (sha256 hash-chained JSONL), adversarial.py (seeded falsification hunt
  over cmd/actuation noise + refine, ledger-logged), dossier.py (9-clause evidence
  dossier mapped to EU/ISO, hashed + logged), datasets.py + gaps.py (53-pair corpus:
  45 synth + 5 real DROID Franka pour eps + 3 morphs; xemb centered-Frechet + span
  ratio with frame guard; batch alpha audit GOVERNED/REVIEW/BLOCKED).
- frontend/ (vanilla, Meta-flat style, no framework): index (dashboard + hunt),
  docs.html (full manual + live score buttons + sweep widget), compliance.html
  (Item 24, OTA rule, bridge map, live ledger verify + dossier button),
  evidence.html (corpus table, pair scorer, upload, collapse curve). Left sidebar
  nav. LTTS-white console branding.
- tests/test_scorecard.py + test_frontend.py (42 tests green per baseline; README
  says 10, README is stale): discrimination, exact-0.0 sensitivity, fail-closed,
  determinism, ledger tamper-evidence, stdlib-import scan, live API, frontend
  audits. Run: START.cmd -> http://127.0.0.1:8000/.
- HONESTY LABELS (carry forward): gates are DRAFT until OXE calibration; jerk/bounds
  are PROXIES not contact proofs; fixtures synthetic by design (engine is the
  artifact); morphs are synthetic proxies not cross-robot validation; hash chain is
  tamper-evident vs retained head, NOT immutable storage/attestation; DROID sim =
  commanded EE XY (no Z/orientation/gripper/torques/timestamps), so derivative gates
  stay missing without genuine timing.

B. hi bro/claude bro = Genuity Verify (production-aspiration stack; MVP preserved
under reference/):
- backend/ (FastAPI + SQLAlchemy + Pydantic): api.py routes incl. healthz/readyz,
  config, auth demo/login/logout/session, workspace, datasets CRUD, embodiments,
  profiles, runs CRUD + reviews + export, experiments, transfers, proofs, runtime
  sessions + telemetry + reset, audit + audit/verify, evidence/verify,
  records, standards, knowledge, admin users, tokens CRUD. engine.py: canonical
  fingerprinting, default_profile, discrete_frechet (numpy), derivative w/
  timestamps, gate_status, evaluate, compare_embodiments. schemas.py: strict
  contracts (finite values, equal lengths/dims, timestamps, provenance). store.py,
  service.py, evidence.py, formal.py (bounded Z3 queries, exact rational, timeouts,
  UNKNOWN outcomes; NOT whole-VLA), fixtures.py, runtime.py, catalog.py, config.py.
- web/ (React/Vite ops console, preserved): precision console, dark replay
  workspace. site/ (Next.js 16 pitch site, dev 5190/prod 5191): Hero/RobotScene
  (three.js), FailureLab (failure injection, 5 model tests), Pipeline, Evidence,
  ContextSections, Actions; 11/11 Playwright green incl. axe; Lighthouse desktop
  99/mobile 77 (mobile <2s LCP BLOCKED); /privacy 404 (page deleted, owner call).
- tests/: test_api, test_assurance, test_engine, test_store. design-intel/ (shots,
  perf), knowledge/ (source manifest + SHA256 + extracted text), graphify-out/,
  tools/ (preview.mjs :5192 static server, package_transfer.py with CRC/SHA256/
  git-bundle receipt), docs/ai-skills/frontend-craft/.
- Ports: 5190 dev, 5191 prod, 5192 frozen preview. Runbook in README.

## 7. Locked engineering decisions (non-negotiable)

- Evidence before verdict: strict bounded typed inputs; missing evidence =
  INSUFFICIENT never PASS; BLOCK wins; draft-profile pass != release eligible.
- Frames/timing preserved: versioned gate profiles; physical derivatives from
  provided timestamps only; no silent truncation, auto-alignment, or invented
  sample periods; transfer comparison removes translation explicitly, keeps scale.
- Layered verification: trajectory, perception corroboration, lineage, contact
  inequalities, bounded NN queries are separate layers with separate evidence.
  No module claims full-VLA or full-robot safety. Blueprint 5.3: verify where
  bounds are tractable, guard the rest at runtime, stress all of it adversarially.
- Operational product: precision console + dark replay, source-linked results,
  real backend workflows. No cinematic marketing pages in the console. No invented
  deployments/telemetry/stats/badges. Live middleware is SUPERVISORY: never claims
  to replace certified safety controllers or to actuate equipment.
- Deterministic core: canonical hashes, seeded fixtures, gates on unrounded values,
  inputs + profile versions pinned to every result. Scenarios explicitly synthetic.
- Regulations: dated source-linked mappings, explicit applicability, human review.
  Dossiers are evidence compilations, never legal opinions or CE certificates.
- Style: no em dashes anywhere in chat or product; tabular numerals; reduced-motion
  guards; explicit loading/error states.

## 8. IP: 7 invention vectors (design proposals; NO filing, NO FTO yet)

1. Sim-to-real degradation via discrete Frechet mapping (policy-independent;
   LIVE in MVP as a metric). 2. Cryptographic provenance + ratio enforcement
   ledger in dataset cards (anti-collapse). 3. Runtime executability-loss guard
   (PINN loss on action chunks, halt on invariant violation). 4. Bounded
   reachability proofs (Lean 4 + Marabou/alpha-beta-CROWN on scoped sub-policies;
   full-VLA formal proof explicitly OUT of claim). 5. Cross-embodiment latent
   degradation benchmark (zero-shot transfer scoring). 6. Adversarial physical
   edge-case generation (lighting/friction/mass search for hallucination
   boundaries). 7. Compliance translation engine (scores/bounds/proofs ->
   Machinery Reg + 25785-1 risk-assessment structure). Roadmap: provisionals for
   vectors 1+6 first; FTO review on Frechet + formal pipelines before any
  "patented" language (currently FORBIDDEN in product).

## 9. Proprietary assets (context, not uploads)

- The founder holds a proprietary synthetic-data library (private, not shared
  here). The model must design a clean GENERATOR/VERIFIER ADAPTER INTERFACE
  (generate(params) -> batch + dataset card; verify(batch) -> pass/fail + report)
  so the library plugs in later as a Tier-3 generator + verifier without
  architectural rework. Never ask the founder to paste the library; design the
  seam and move on.
- Secondary libraries (ratio enforcer, OOD monitor, OTA vault client) get built
  alongside later; the PRD must reserve their module slots and API shapes now.

## 10. Explicitly OUT of scope for the model

- No hardware builds, no robot actuation, no safety-controller replacement claims.
- No legal opinions, no CE marks, no "certified/compliant/patented" badges.
- No invented customers, pilots, revenue, traction, or benchmark victories.
- No rewriting the working pitch site or MVP wholesale; extend and harden.
- No unbounded formal-verification claims; bounded + reported + UNKNOWN-tolerant.
- [VERIFY] tag required on every new external fact the model introduces.
