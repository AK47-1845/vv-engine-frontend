# Critique Rubric

Score each dimension 1-10. A 9 means no material issue observed under the tested conditions, not universal perfection.

- Hierarchy: product/category understood immediately; one primary next action.
- Typography: deliberate sizes/weights, readable secondary data, no clipping.
- Spacing: coherent grid, stable dimensions, no incoherent overlap.
- Motion: state-dependent, controllable, reduced-motion equivalent available.
- Originality: domain-specific instrument, not a recolored generic template.
- Polish: complete controls, evidence labels, hover/focus/error states, consistent assets.

Run `node site/tests/capture.mjs` against the active site. Inspect the generated hero desktop/mobile screenshots, not old paths. Canvas checks must show nonzero colored pixels and actual frame change. The final suite must add 768,1024,1920 widths and interaction checks. Save test/Lighthouse receipts and state remaining gaps explicitly. Use at most two visual passes for hero and demo during the timeboxed sprint.