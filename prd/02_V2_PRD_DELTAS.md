# V2 PRD DELTAS to 02_PRD_CORE (2026-10-03 live research; append, do not rewrite)
Numbering continues the v1 PRD (FR-32+, G9+, R9+). Overlays win on conflict.

## Principles (locked)

- P-1: safety gates are NON-COMPENSATORY. Task success never offsets a safety
  breach. Report success and safety metrics separately, no blend (FR-33).
- P-2: no gate lifts DRAFT without a current credibility card (FR-32).
- P-3: release-over-release is first-class (FR-34). Every OTA-era verdict needs
  a parent/child delta with CI.
- P-4: held-out panel (FR-37). Private, seeded, commit-reveal in ledger. Open
  benchmarks leak into training; the panel must not.
- P-5: independence rules (FR-41). Diagnostics + failure localisation yes;
  reward signals, tuning, auto-fix no. Flat fee per pack, never pass-contingent.

## New requirements (testable; tests in the Test column are the acceptance bar)

- FR-32 (P0): Gate Credibility Card per gate (fields: gate id + version, corpus
  hash, n, FP/FN counts, calibration bins, rollout types, transfer error,
  search-hit count, date, analyst). TEST: CI fails if DRAFT lifts without one.
- FR-33 (P0): success vs safety metrics reported separately, no blend. TEST: a
  perfect-success run cannot raise a BLOCKED safety gate.
- FR-34 (P0): release-over-release compare of parent/child weights: per-gate
  delta with CI + SUBSTANTIAL-MODIFICATION candidate flag. TEST: seeded
  regression detected; identical releases give zero delta.
- FR-35 (P0): every gate reports independent rollout count + seeded bootstrap
  CI; below-minimum-n yields INSUFFICIENT. TEST: garbage + tiny-n inputs.
- FR-36 (P1): adversarial hunt aimed at OUR OWN scorer to find wrongly-TRUSTED
  outcomes (false positives under search; robotics has not published this:
  first-mover). TEST: zero hits on regression set; any hit becomes a sev-1 test.
- FR-37 (P1): held-out panel with commit-reveal in ledger. TEST: reveal verifies
  commitment; clients cannot request seeds.
- FR-38 (P0): PAR open JSON Schema + offline reader CLI recomputing hashes.
  TEST: runs with no network on a third-party machine.
- FR-39 (P1): applicability worksheet: ML safety function? self-evolving after
  shipment? frozen-weight OTA? Records answers + implied route (Part A 5/6,
  substantial modification, out of scope). States no legal conclusion. TEST:
  banner "human and legal review required" present.
- FR-40 (P1): property-margin gate: STL/LTLf-style spec returns signed
  satisfaction margin, spec hash-pinned. TEST: deterministic; proxy label when
  state is estimated.
- FR-41 (P1): independence register per run (builder, funder, relationship),
  exported in PAR. TEST: ledger-logged.
- FR-42 (P1): ingestion adapter stubs for external eval outputs (Isaac
  Lab-Arena, RoboArena, SIMPLER/LIBERO logs); schemas [VERIFY]. TEST:
  conformance tests per adapter.
- FR-43 (P2): configurable retention for safety-decision logs, default 12+
  months [VERIFY, IES guide]. TEST: policy test.

## New gates

- G9 property_margin (P1): signed STL/LTLf satisfaction margin, spec pinned.
- G10 time-to-success distribution (P2).
- G11 fall/impact placeholder aligned to unpublished 25785-1 direction (P2,
  DRAFT, no clause text). Pull property-margin scoring into M1/M4 scope; keep
  Z3 and alpha-beta-CROWN last in M3.

## M7 additions

Add Annex I Part A items 5/6 rows + EHSR 1.2.1(f) row; relabel AI Act rows as
"reference mapping, expected to fold into Machinery Reg"; add Notified Body
briefing view (read-only dossier walkthrough for an auditor).

## New risks (append to R1-R8)

R9 YC/market crowding (24 robotics cos S26; differentiate vs named adjacents).
R10 Halos locks the TIC on-ramp (answer: cross-stack evidence + ingest Halos).
R11 "self-evolving" legal scope ambiguity (answer: FR-39 both-readings build).
R12 robotics insurance market small + early (answer: OEM-pays flip).
R13 benchmark leakage + Goodhart (answer: held-out panel).
R14 naming/trademark collisions (answer: PAR; CI grep for Passport).
R15 cyber-provision timing (answer: do not build wedge on cyber).
R16 Dana adds independent-looking reports (answer: independence proof + register).

## Resequence (dates drive; 4-month plan ends after both deadlines)

- Week of Oct 5: apply patches; send 3 outreach messages (EU OEM; insurtech
  evidence buyer; TIC format feedback); start log.
- By Oct 20: evidence pack v0 on fixtures + 5 OXE pairs, credibility cards v0.
- By Oct 26: YC draft using ONLY logged facts; submit before Nov 2.
- November: PAR spec v0.1, release-over-release diff, commit-reveal panel v0.
- Dec 11: YC decision; applicability worksheet reviewed by 1 external expert;
  named-pilot proposal.
- Kill rule extends: zero replies from all 3 outreach targets by Nov 30 =
  report plainly (same honesty rule as v1 kill clause).

## PAR rename instruction (mechanical, CI-enforced)

Replace "Passport"/"Risk Passport" with "Policy Assurance Record (PAR)"
everywhere in product, docs, and pitch. Rationale: RobotCare trademark.
Grep must fail the build on "Passport" (case-insensitive) outside this note.

## Verifier credibility basis (arXiv 2609.09250, 2026-09-08; survey of ~150
verifiers: no free checker; cheaper/earlier/denser verdicts are less credible;
robotics has not run search-based metrics: first-mover opening)

Card fields per gate: id + version, corpus hash, n, FP/FN counts, calibration
bins, rollout types, transfer error, search-hit count, date, analyst. Status
today: rollout counts yes; error rates yes on fixtures (OXE needs labels);
rollout types yes; human agreement needs labelling; calibration partial;
transfer via M5; proxy-gain-under-training needs design now; search FPs via
FR-36. Conformal thresholds allowed ONLY with explicit exchangeability
statement; mark invalid if a policy was optimised against our gates.
