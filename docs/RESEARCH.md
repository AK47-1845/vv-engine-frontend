# Research And Source Register

Reviewed 2026-10-01. This register distinguishes source content, implemented methods, and unresolved claims. Public references are read for methodology and design; no proprietary interface, assets, marketing statistics, or full standards text is copied into the application.

## Supplied Sources

All five PDFs were text-extracted with page boundaries and SHA256, then read in the source extraction pass: Genesis (26 pages), Idea 1 (11), Physical AI (16), Strategic Blueprint (13), Frontier LLMs (48). See `knowledge/source-manifest.json` and `knowledge/source-text/`. The frontier document's opening page needs visual review. Text review does not imply that every diagram was visually inspected.

- Strategic Blueprint, pages 9-10: seven modules and explicit limitation against full-VLA formal-verification claims.
- Genesis: drift, hallucination, physical inconsistency, action insensitivity, uncertainty, and data collapse motivate separate observability layers, not one invented trust percentage.
- Idea 1: invention areas are design proposals. Filing status and freedom to operate remain unverified.
- Physical AI and Frontier LLMs: research context, not proof of safety or support for proprietary vendor claims.

## Corrections From The Existing MVP

1. The original test suite contains 42 tests, not the 10 reported by its README; all 42 passed in the baseline run.
2. DROID `sim` is commanded end-effector XY, not a simulator rollout. The imported fields omit Z, orientation, gripper and torques. Native timestamps are not established by the staged pair. Derivative gates must remain missing unless genuine timing is provided.
3. DROID source metadata describes FR3; the public DROID project describes its general platform as Franka Panda. Preserve the original metadata and do not infer an exact hardware configuration from general project documentation.
4. Genesis and MVP use opposite alpha conventions. The new contract uses explicit `real_samples`, `synthetic_samples`, and `synthetic_fraction`.
5. Morph traces are synthetic geometric transformations, not cross-robot validation.
6. Recursive histogram resampling illustrates distribution degradation; it does not establish collapse of a trained model.
7. A locally consistent hash chain is tamper-evident relative to its retained head. It is not immutable storage or independent attestation.

## Public Research And Engineering Sources

| Source | Reviewed Surface | Use And Limit |
| --- | --- | --- |
| [DROID](https://droid-dataset.github.io/) / [paper](https://arxiv.org/abs/2403.12945) | Official project, abstract, data/method overview | Recorded-trajectory adapter and provenance. No new model training or reproduction claimed. |
| [Open X-Embodiment](https://robotics-transformer-x.github.io/) / [paper](https://arxiv.org/abs/2310.08864) | Official project, cross-robot data and results overview | Embodiment-specific contracts. Reported transfer results do not establish transfer for this application. |
| [Z3](https://github.com/Z3Prover/z3) | Official repository and Python binding documentation | Bounded small-network queries with exact rational semantics, timeout and unknown outcomes. Not whole-VLA or floating-point execution verification. MIT dependency. |
| [SciPy Wasserstein distance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html) | API reference linked for the chosen library function | Descriptive drift diagnostic; not an automatically calibrated detector. |
| [Model collapse paper](https://www.nature.com/articles/s41586-024-07566-y) | Article landing page access redirected to publisher authentication | Full paper not retrieved in this pass. No claim to reproduce its experiments. Follow-up literature review required. |

## Design References

- [Applied Intuition](https://www.appliedintuition.com/): physical-AI validation workflow and domain framing; no assets or product claims copied.
- [Patronus](https://www.patronus.ai/): evaluation/simulation evidence workflow. Its current public positioning differs from the older source pitch; company claims remain attributed.
- [Vercel React skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices): request parallelism, lean client payloads, lazy heavy visualization, derived state, deferred filtering. MIT source.
- [Baseline UI](https://github.com/ibelick/ui-skills/blob/main/skills/baseline-ui/SKILL.md): accessible primitives, explicit loading/error states, tabular numerals, reduced motion and restrained effects. Used as guidance, not wholesale copied code.
- Supplied Scrollcraft: interview-first design and rendered verification. Its cinematic landing-page format is deliberately not applied to an operations console.

## Regulatory Register

| Reference | Dated Finding | Application Treatment |
| --- | --- | --- |
| [Commission machinery page](https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en) | Mandatory application from 20 January 2027; specific AI-powered safety and conformity provisions | Machinery Regulation mappings are draft evidence links, not legal opinions or CE certificates. |
| [EUR-Lex 2023/1230](https://eur-lex.europa.eu/eli/reg/2023/1230/oj) | Full legal text extraction failed in this pass | Exact Annex I Part A applicability and clause interpretation require legal/assessor verification. Do not claim every AI robot mandates the same route. |
| [ISO/TC 299 catalogue](https://www.iso.org/committee/5915511/x/catalogue/) | ISO/CD 25785-1, stage 30.60, under development; dynamically stable industrial mobile robots | Corrects the source AWI label. A draft is not a certifiable harmonized requirement. No unpublished clauses invented. |
| Same ISO catalogue | ISO 10218-1:2025 and 10218-2:2025 published | Scope-specific evidence mapping; copyrighted standard text not reproduced. |
| [Commission AI Act page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Retrieved page updated 3 August 2026 describes phased dates and changed high-risk timing | No universal AI Act countdown. Mark product-specific timing and amended law as legal-review-required. |

## Intellectual Property

The seven invention areas are not proof of patent novelty, ownership, validity, filing or clearance. No exhaustive patent search or attorney FTO opinion has been performed. Public, standard methods and appropriately licensed libraries are used. Before commercialization, map specific intended claims to patent families, jurisdictions, legal status and counsel's written opinion. Do not show a "patented" badge or patent counts based on placeholders in the supplied blueprint.