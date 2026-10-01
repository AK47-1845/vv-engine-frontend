# Start Here: Durable Project Context

## Latest Priority: 2026-10-01 Frontend Sprint

The user changed the immediate deliverable to a 60-minute frontend-first Next.js marketing/product-story site. Read `handoff/README.md` and `handoff/STATUS.md` first. The site is in `site/`, separate from the preserved `web/` console and `backend/`. Final mobile performance remains below target; public launch placeholders and hardware qualification remain open. The earlier checkpoint below is historical, not the current completion state.

## User Goal

Build a substantial Genuity Verify physical-AI verification, validation, and governance application for an LTTS CTO demonstration and future deployment. Preserve source grounding, a knowledge graph, procedural graphs, design decisions, and a practical operations guide.

## Confirmed Decisions

- New work belongs in this `claude bro` project; original archives and PDFs are preserved.
- Precision engineering console: light main interface with a dark replay workspace.
- Support uploaded/API evaluation and clearly scoped live integration contracts.
- No real hardware, cloud deployment target, authentication provider, or calibration evidence has been provided.
- Safety and compliance claims must remain narrower than the evidence supporting them.

## Resume Order

1. Read this file, `docs/BRIEF.md`, and `docs/DECISIONS.md` when present.
2. Read `docs/VERIFICATION.md` and `docs/OPERATIONS.md` when present for actual tested capabilities and remaining deployment gates.
3. Query `graphify-out/graph.json` and inspect `knowledge/source-manifest.json` for source lineage.
4. Read the current implementation and tests before making changes. The graph is a map, not executable truth.
5. Update decision records, verification results, procedural graphs, and this checkpoint after each meaningful milestone.

## Current Checkpoint

Source preparation completed. Five PDFs, 114 pages; page 1 of the frontier-LLM document has little extractable text and needs visual review. PDF text extraction is not a review of all diagrams. Original MVP and Scrollcraft reference sources were selectively extracted without bundled dependencies, secret environment files, or large binaries.

Known MVP risk: metric functions use `zip` and assume compatible trajectory lengths/dimensions. New ingestion must reject mismatched, non-finite, malformed, or unit-incompatible traces before evaluation. Thresholds in the original MVP are draft, not calibrated safety limits.

This file records observable facts, decisions, implementation status, and next actions. It does not contain private model reasoning or invented execution history.