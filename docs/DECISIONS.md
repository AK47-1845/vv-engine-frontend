# Engineering Decisions

## 001: Evidence Before Verdict

Accepted. Inputs are strict, bounded and explicitly typed. Missing required evidence produces INSUFFICIENT, not PASS. BLOCK takes precedence. A passing draft profile does not confer release eligibility. Checked by `tests/test_engine.py`.

## 002: Preserve Frames And Timing

Accepted. Coordinate frames, units and dimensions must match a versioned gate profile. Physical derivatives use provided timestamps. No implicit truncation, automatic frame alignment or invented DROID sample period. Geometric transfer comparison removes translation explicitly and preserves scale.

## 003: Layered Verification

Accepted. Trajectory, perception corroboration, data lineage, contact inequalities and bounded neural-controller queries have different assumptions and evidence. No single module claims full VLA or robot safety. Follow Strategic Blueprint section 5.3.

## 004: Operational Product

Accepted by user interview. Light precision console, dark spatial replay, compact typography, source-linked results, real backend workflows. No cinematic marketing landing page. No invented deployments, telemetry, pass statistics or certification badges.

## 005: Deterministic Core And Traceable Changes

Accepted. Canonical input/profile/result hashes and seeded stress fixtures make results reproducible. Gates evaluate unrounded values. Original inputs and profile versions remain associated with each result. Scenarios are explicitly synthetic.

## 006: Persistent Context Is Evidence, Not Memory Magic

Accepted. `CONTEXT.md`, source manifests, source text, semantic graph fragments, code graph, decisions, procedural diagrams and actual verification receipts comprise the handoff. Graph inference is labeled; token accounting is unavailable, not zero-cost. Future agents must verify current code against tests.