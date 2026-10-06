# Wednesday Deck — Full Content Spec (16 slides)
> Render target: whoever builds the .pptx (you/Antigravity) follows this exactly.
> Every number tagged. Sources in S-speaker-notes. Design: dark, 1 idea/slide.

## S1 — Trailer (0:45)
Title: "Four months inside LTTS: findings, one demo, one ask"
3 icons with 1 line each: "Where I came from + dated inside-journey" / "3 findings,
every number sourced" / "Module 1, working — then a 4-month gated ask."
Footer: "Please interrupt. If I'm wrong anywhere, I'd rather hear it here."

## S2 — Where I came from (2:30)
Timeline, 5 nodes: Vizag KV (math: NTSE AP-14, MAT 97/100, IOQM) → JEE 99.5 →
IITG Mech (Tech Board drones) → 18 months enterprise AI attempts (200+ convos,
Kaggle comp 46+ teams, Inter-IIT PS 2,000 students / 23 IITs) → "registered a
small company to sign pilot paperwork" → "March 2026: Dr. Singh's doorstep."
Speaker: Act 0 script. Warm, fast, zero flex.

## S3 — Inside: dated journey (2:30)
4-row table: Mar–Apr POC (300→5,000 rows, 92 runs, 0 violations) → Month 1
listening (MTR, part-rationalization, OCR→JSON→ML) → Month 2 Reconcile
(51 tests) + "your teams already do this" lesson → Months 3–4 research (4 docs).
Speaker: Act 1 script. Nod at Madhusudhan on the lesson row.

## S4 — The 4 documents + deletion log (2:30)
4 doc covers with page counts: Genesis 26pp / Practice 16pp (for Dr. Singh) /
Frontier-LLM 48pp / Idea 1 11pp. Callout box: "11 claims deleted from my own
drafts when unverifiable — list in your printed appendix."
Speaker: one sentence on deletions, then taxonomy tags intro.

## S5 — Three schools matrix (3:00)
Genesis 10-dim table, condensed: Renderer (Sora/Genie/Cosmos: photoreal, slow,
severe hallucination) / JEPA-latent (sub-5ms, data-efficient, control-grade) /
Spatial-engineered (occupancy + PINNs, verifiable, industrial trust).
Takeaway line: "Each won a different axis. Conflating them is the field's
most common strategic error."

## S6 — Five failure modes (3:00)
5 rows, 1 line + 1 number each: drift (coherent minutes, not hours) /
executability gap (LPIPS-plausible, Coulomb-wrong) / perceptual hallucination
(silent OOD corruption) / action marginalization (ignores the wheel) /
sim-to-real gap (D_real ≠ D_sim, hybrid wins per 2026 consensus).

## S7 — Capital vs revenue: 250:1 (2:30)
One giant ratio: ">$5B in [Verified] vs <$20M production revenue [Estimated]."
Corrected company table: Figure $39B/<$10M · Skild $14B/rev undisclosed ·
Pi $5.6B/<$5M · Wayve $4.8B · Applied Intuition $15B + $150–200M ARR.
Line: "Intelligence gets headlines. Verification gets revenue."

## S8 — Tier 1/2/3 production reality (2:30)
Tier 1 (cash flowing): sim/validation/inspection/integration + Waymo 500k+/wk
[Verified 2026]. Tier 2 (bounded pilots): BMW/Mercedes/Amazon/DHL [all Verified
press]. Tier 3 (lab): zero-shot assembly, domestic generalists [Speculative].
Line: "Verification is LTTS-shaped work."

## S9 — Regulatory clock (3:00)
Timeline bar: TODAY (Sept 30) → Jan 20, 2027 [Verified, EUR-Lex]: mandatory
Notified Body assessment for self-evolving safety AI (Annex I Part A Item 24).
Callouts: frozen weights may self-assess — BUT every safety-shifting OTA update
= substantial modification → re-assessment + new CE (Art 3(16)/18) · NB queues
already 6–12 months · ISO 25785-1 unpublished industrial draft [Reported].
Line: "TÜVs certify the snapshot. Somebody must monitor the movie."

## S10 — 10-year bets 1–2 (2:30)
Bet 1: V&V practice Q1-2027 — Safety Dossier Compiler (CBF + reachable sets →
ISO 13849/IEC 61508 dossiers), ~$2.8M [Estimated, bottom-up]. Bet 2: PLC
alliances Q2 (Siemens/Rockwell), ~$1.3M. Header: "My readings — please correct
me." Rationale line: "Lowest capex, regulatory-forced, serves existing clients."

## S11 — 10-year bets 3–4 (2:30)
Bet 3: synthetic data factories Q3 (AFTER validation + access), ~$4.2M. Bet 4:
CoE baseline — 250 engineers, lateral PhDs, IIT/IISc fellowships, ~$2.5M/yr.
Sequence banner: "Verify first, generate later — the industry does it backwards."

## S12 — Module 1: trust scorecard (1:30)
Architecture diagram: policy + rollouts IN → 8 Genesis-§4.4 metrics (drift,
horizon, Fréchet, sensitivity, spread, jerk-proxy, bounds) → red/amber/green
report card OUT. Badges: "Runs today" · "Patent vector #1 inside" · "Fail-closed:
worst gate decides."

## S13 — LIVE DEMO (3:00)
Screen: terminal run + 3 report cards side by side. clean = TRUSTED (green) ·
drifty = BLOCKED (horizon collapse, Fréchet spike) · playback = BLOCKED
(action-sensitivity exactly 0.0 — dead steering wheel caught). Backup: screen
recording + printed cards. Speaker: Act 4 demo narration. Line: "Nothing here
is a slide. It runs."

## S14 — 4-month gated ask (2:00)
4 rows × (month → 2 gates → proof): M1 scorer+OXE + 3 outreach emails tracked ·
M2 edge-case module + insurer response log · M3 provenance ledger prototype ·
M4 2 provisional drafts + 1-client pilot proposal. Footer: "Judge me on dates.
If I miss, research + code + drafts stay with you."

## S15 — Close: the bet (1:30)
 ONE line centered: "I'm not asking you to believe in world models — I'm asking
you to believe in four months of checkable work." Nothing else on the slide.
Speaker: 90-sec close, then stop. Do not add one more sentence.

## S16 — Questions: be harsh (Q&A)
3 preempted attacks, 1 line each: who pays (insurers → OEMs → TICs) · why me
(structural arbitrage, 4 months off-P&L) · Applied Intuition (rating agency,
not bank — builder can't be auditor). Opener: "Where am I wrong?"

---

## WEDNESDAY CHECKLIST
Print: 4 docs tabbed (Idea 1 + Physical AI REGENERATED with corrections — do
not print stale PDFs) · 1-page scorecard handout (clean vs playback cards) ·
this story in your head, not on slides.
Demo kit: laptop + reports/*.html + terminal run rehearsed + screen recording +
printed card screenshots (projector-proof). Deterministic seeds only.
Proof packet: P1/P2 verification appendix (shows diligence if probed) · TIC
precedents (TÜV NORD/AI, Rheinland/NVIDIA+Fennec, AIQURIS) · auditor artifact
map (Art 10/12/14/15 → modules).
Monday–Tuesday: customer-signal sprint (1 warm response = pitch transforms) ·
Idea 1 + Physical AI regen with all corrections · rehearse aloud 3× timed,
record once, cut 10% each run · dry-run demo 5× (record backup Tuesday night).
Morning-of: arrive early, test projector + clicker, printouts stacked, water,
breathe. Trailer first. Correct-me rhythm. Stop after "thank you, sir."
