# Backlog

## P0: Mobile Performance Acceptance

VERIFIED OPEN. Final Lighthouse mobile 77, LCP 3.515 s, TBT 451 ms. Target >=95 and LCP <2s is unmet. Inspect `design-intel/performance/mobile.json`, especially bootup-time, unused-javascript and render delay.

Files: `site/src/components/Hero.tsx`, `HeroScene.tsx`, `FailureLab.tsx`, `Actions.tsx`, `Pipeline.tsx`, and the page composition. First reduce initial React work and defer below-fold interactive hydration while preserving meaningful server-rendered content. Retain mobile poster/2D trace and opt-in 3D. Check actual responsive image selection at high DPR. Do not hide interactions from Lighthouse or weaken throttling.

Acceptance: production build plus all model/browser/canvas tests pass, mobile scores >=95 across repeated equivalent runs, LCP <2s, no layout shift regression, and actual screenshots remain coherent. Preserve previous reports instead of cherry-picking the best score.

## P0: Public Launch Content

Ask the user for an approved pilot destination, actual recording, public biography and any verified pilot evidence. Edit Actions.tsx, ContextSections.tsx and privacy/page.tsx. Implement real submission only after destination, privacy, retention, spam protection and authorization are defined. Until then, preserve [REPLACE] and LOCAL_DRAFT_NOT_SUBMITTED labels. No invented customer/accelerator logos.

## P1: Interaction And Visual Refinement

- Complete arrow-key/roving-focus behavior for the custom pipeline tablist, preferably with an accessible primitive. Current tabs are reachable/clickable but were not tested for every ARIA tab keyboard convention.
- Fix the Lighthouse accessible-name advisory on the header wordmark and evaluate replacing native poster img with a documented responsive Image loader without adding network-dependent transforms.
- Profile sustained animation smoothness and battery cost on real mobile hardware. Nonblank/moving canvas checks do not establish sustained 60fps.
- Reduce tiny mono labels where practical, and perform independent human visual review. The timed self-critique does not establish an award-level design score.
- Keep styles readable: the initial token/section CSS is compact. Format only touched rules; do not rewrite working layout.

## P1: Engineering Product Continuation

Preserved backend and console need their own completion/qualification sprint. Inspect `web/src/Console.tsx`, `Workbenches.tsx`, `backend/api.py` and existing tests. Finish missing governance UI, independent runtime reset workflows, calibrated evidence and operating documentation. Do not relabel the marketing page as production safety software.

## P2: Deployment And Deeper Evidence

Deploy only after user approval and public-launch gates. Run hosted checks against the actual deployment. Refresh the older graphify graph after reviewing newly added prose; the current frontend handoff graph is already separate. Optional real-artifact demo must preserve input/source qualification.