# Meta Muse Code 1.3 Contributor: Read This First

You are continuing an existing, working project. You are NOT being asked to regenerate it.

## Non-Negotiable Preservation Rules

1. Read this file, README.md, STATUS.md, ARCHITECTURE.md, FACTS_VS_PLACEHOLDERS.md and BACKLOG.md in this handoff directory before proposing an edit.
2. Read ../AGENTS.md and ../docs/ai-skills/frontend-craft/SKILL.md before frontend work.
3. Preserve `site/` (Next.js pitch site), `web/` (Vite operations console), `backend/` (Python engine/API), `reference/`, `knowledge/`, and this handoff. These are separate products/layers, not duplicate folders to delete.
4. Do not run create-next-app, create-vite, framework migrations, whole-directory replacement, global formatting, dependency upgrades or a redesign unless the user explicitly requests that change.
5. Never run `git reset --hard`, `git clean -fd`, force checkout, or overwrite existing files from an archive to fix a local issue.
6. Begin each task by stating the exact user-visible change, the files you intend to touch, and one focused test. Make one small change at a time. If more than three application source files are necessary, explain why and obtain agreement before widening the change.
7. Inspect `git status` and the existing diff before editing. Do not revert changes made by the user or another model. Commit a tested checkpoint before another feature, with the user's approval.
8. Preserve existing exports, API contracts, CSS tokens, evidence labels and test assertions. Do not make tests pass by deleting safety checks, weakening thresholds or replacing real behavior with hard-coded success.
9. Update the handoff after every meaningful verified change. Report failed tests and unverified claims plainly. Do not mark intentions as completed work.

## Why The Project Has This Shape

The user's original goal was an LTTS-facing physical-AI assurance engine based on five supplied PDFs and an earlier MVP. The original MVP was retained, its 42-test baseline passed, and typed evaluation/storage/runtime/formal/evidence mechanisms were built in Python. A light operations console was then built in `web/`.

The user subsequently changed the immediate priority to a timeboxed, dark marketing/product-story site. That separate site is `site/`. It is not a replacement for the console or backend. The site uses deterministic synthetic browser examples so it can run without credentials, hardware or backend connectivity. Never call those examples measured robot evidence.

The frontend was built from six measured reference sites, local Geist/JetBrains Mono, CSS tokens, Radix dialogs, Three.js, Motion, GSAP and Lenis. It has a robot/trace hero, failure-injection lab, evidence pipeline, ledger/report, sourced regulatory context and an honest pilot ask. Desktop gets 3D; mobile gets a lightweight live trace with optional 3D. The exact tested source and dependency locks are preserved in Git and the transfer archive.

## What Is Verified And What Is Not

Verified: production frontend build, 5 model tests, final 11/11 production browser tests at five widths, accessibility/reduced-motion scan, exports, fallback artwork, metadata, canvas pixels/motion, and the current 35-node/36-edge handoff graph.

Unfinished: mobile performance (final Lighthouse 77, LCP 3.515 s), actual pilot destination/video/public biography approval, some interaction advisories, completion/qualification of the separate console/backend, real hardware integration, calibrated thresholds, legal applicability and independent assessment. No public deployment or safety certification occurred.

Do not rewrite the site to fix the mobile score. Profile initial hydration, preserve the current visual design, and make measured small improvements. The user intends three days of incremental work, not another rebuild.

## First Session: Exact Order

1. Follow TRANSFER.md to open the portable preview or install development dependencies.
2. Confirm the source commit from the archive's TRANSFER_MANIFEST.json and inspect the Git history bundle. Keep the original transfer ZIP untouched as a recovery copy.
3. Run the relevant existing tests BEFORE editing. Capture the current UI screenshot for any frontend task.
4. Ask which single improvement the user wants. Suggested first task: mobile hydration performance without changing layout or content.
5. Read only the owner and neighboring test, patch narrowly, rerun the same check, compare screenshots, and show the diff summary.

## Ready-To-Paste Instruction

"Continue Genuity Verify without rewriting it. Read handoff/META_MUSE_START_HERE.md and handoff/STATUS.md first. Preserve site, web, backend, reference and knowledge. Do not scaffold a new app or redesign working screens. For the one change I request, identify the smallest owning file and test, make a narrow patch, run the test and inspect the diff. Ask before touching more than three application source files or changing an API, dependency, theme or architecture. Never invent safety, certification, customer or pilot claims."