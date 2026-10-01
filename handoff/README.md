# Start Here

VERIFIED: The user requested a 60-minute frontend-first sprint on 2026-10-01, starting 15:44:24 IST. Feature work stops at 16:42:24 IST; final deadline 16:44:24 IST.

Genuity Verify is a physical-AI verification, validation and governance project. The original source corpus, Python backend and Vite operations console already exist. The current sprint adds a separate Next.js marketing/product-story site. Do not rewrite or replace working backend/console code.

## Reading Order

1. STATUS.md and CONTINUATION_PROMPT.md.
2. FACTS_VS_PLACEHOLDERS.md and ASSUMPTIONS.md.
3. DESIGN_BRIEF.md and ARCHITECTURE.md.
4. BACKLOG.md and KNOWN_ISSUES.md.
5. ../docs/ai-skills/frontend-craft/SKILL.md when created.

## Current State

VERIFIED at minute 49: The complete Next.js pitch site is running at http://127.0.0.1:5190 and its production build at http://127.0.0.1:5191. Hero, failure injection, pipeline, evidence/report preview, why-now, founder/build status, pilot draft and video placeholder are implemented. The older console remains at 5180 and original MVP at 8123.

VERIFIED: production build, final TypeScript, five model tests, and the final consolidated production browser suite (11/11). Coverage includes five responsive widths, accessibility/reduced motion, keyboard dialogs, exports, real WebGL fallback, nonblank/moving canvas and metadata. The fallback image-readiness race is repaired and passed in the final full run.

VERIFIED final Lighthouse: desktop 99/100/100/100; mobile 77/100/100/100. Mobile LCP 3.515 s and TBT 451 ms do NOT meet the requested performance bar. Both CLS values are below 0.0002. No public deployment occurred.

## Exact Next Action

Read BACKLOG.md P0. Profile mobile hydration before changing the visual design. Retain the lightweight mobile hero and split below-fold interactive hydration. Do not chase scores by excluding the real interactions or altering the test to desktop throttling.

## Run And Verify

From the project root using Node 24.18.0:

```powershell
npm.cmd --prefix site ci
npm.cmd --prefix site run dev -- --hostname 127.0.0.1 --port 5190
```

In another terminal:

```powershell
npm.cmd --prefix site run build
npm.cmd --prefix site test
npm.cmd --prefix site run lint
npm.cmd --prefix site run test:browser
node site/tests/capture.mjs
```

For performance: start `npm.cmd --prefix site run start -- --hostname 127.0.0.1 --port 5191`, then `node site/tests/performance.mjs`. Do not rebuild .next while the owned production server is serving it; stop/restart that process. Browser tools use installed Edge. An active Node 24 is required for direct TypeScript model tests.

Vercel root directory is `site`; see ../README.md. Public-launch placeholders and legal/privacy details must be approved first. No secrets or backend credentials are required for this frontend.

The current frontend graph is knowledge-graph.json. The older ../graphify-out/ snapshot covers original source research and early backend structure; it was not refreshed for this sprint and must not be treated as the current frontend map.