# V2 ARCHITECTURE DELTAS to 05 (2026-10-03 live research; append, do not rewrite)

## A1. PAR open spec (priority raised; the billion-dollar asset)

Publish the Policy Assurance Record JSON Schema as an open spec with a
versioned changelog; ship the offline reader CLI (stdlib-only, recomputes all
hashes, exits non-zero with first-bad-pointer on any mismatch). Engine stays
paid and closed. Rule: any third party must validate a PAR with zero Genuity
contact. Conformance fixtures live in eval/corpus/par/.

## A2. Held-out gate panel service (new component)

Private seeded case bank (never served to clients, never in repo): per-release
commit (seed hash + case count) appended to ledger BEFORE scoring; reveal after
verdict with seed + cases for re-verification. Access: founder key only in V1
(document the ceremony). Metrics: panel-hit rate per gate feeds credibility
cards. Threat model note: panel exists to defeat benchmark leakage/Goodhart;
any panel content appearing in training corpora invalidates that panel version
(disclose + rotate).

## A3. External eval ingestion adapters (new package surface)

packages/sim_adapters grows an INGEST side: Isaac Lab-Arena, RoboArena,
SIMPLER/LIBERO log readers behind one ExternalEval protocol (parse -> canonical
trace + provenance note). Schemas [VERIFY] against each harness. Ship stubs +
conformance tests first; each adapter graduates only with a recorded real-log
run. Halos outputs: define the ingestion point now (do not fight NVIDIA on
sim; absorb their evidence into PAR rows where schemas allow).

## A4. Notified Body briefing view (M7 frontend addition)

Read-only dossier walkthrough route: regulation rows -> evidence pointers ->
re-verify buttons -> credibility cards -> independence register. No editing, no
scoring, no auth beyond reviewer link. This view is the artifact shown in TIC
format-feedback meetings (Oct outreach).

## A5. Credibility-card store (extends profiles + runs)

Per gate-version: card JSON (fields per 02_V2) pinned to corpus hash + code
version; CI rule: DRAFT->v1.0 transition requires a current card or the merge
fails. Bootstrap CI computation lives in packages/engine/stats (seeded,
deterministic, dependency-light). Exchangeability statements stored alongside
any conformal threshold; auto-invalidated flag if optimisation-against-gates
is detected or declared.

## A6. Retention + cyber-timing notes

Safety-decision logs: configurable retention, default 12+ months [VERIFY IES
guide]; policy test enforces minimum. Cyber provisions timing is PENDING
(possible delay to 2027-12-11): architecture must not depend on cyber-gated
features for the core wedge; EHSR 1.1.9/1.2.1(f) rows ship as monitored
placeholders, not blockers.

## A7. Release-compare pipeline (FR-34 shape)

OTA vault entries gain parent/child linkage by default; compare job runs the
same profile+seed on both weight sets and emits per-gate deltas with CIs +
candidate flag. Identical weights short-circuit to zero-delta with a hash
equality proof (cheap, and it demonstrates determinism to auditors).
