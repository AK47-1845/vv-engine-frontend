# Genuity Verify

> **Public demo:** https://ak47-1845.github.io/vv-engine-frontend/ — pre-rendered
> trust scorecards, screenshots, and run instructions. No login, no install.
> The interactive console runs locally (see below); the demo page shows real
> output captured from it.

**New here? Start with the zero-install MVP:** [`stdlib-mvp/`](stdlib-mvp/) runs
the V&V scorecard on 4 deterministic policies with Python stdlib only —
`START.cmd`, open http://127.0.0.1:8000/, done. Product spec and architecture
live in [`prd/`](prd/) (PRD + CTO pitch).

**Moving computers or handing off to Meta Muse?** Read `handoff/TRANSFER.md` and `handoff/META_MUSE_START_HERE.md`. The verified transfer ZIP includes a ready-to-preview website, full source and Git history. `OPEN-WEBSITE.cmd` opens the frozen preview without npm installation; Node.js is required.

Physical-AI verification, validation and governance. This repository contains a Next.js pitch site, an existing Vite operations console, a Python engineering backend, and the source/decision history behind them.

**Start with `handoff/README.md`.** The latest user request was a 60-minute frontend-first sprint. The pitch site is implemented; safety-critical production qualification and public-launch placeholders remain open.

## Pitch Site

From this project root, using Node 24 (tested: 24.18.0):

```powershell
npm.cmd --prefix site ci
npm.cmd --prefix site run dev -- --hostname 127.0.0.1 --port 5190
```

Production:

```powershell
npm.cmd --prefix site run build
npm.cmd --prefix site run start -- --hostname 127.0.0.1 --port 5191
```

Current previews: http://127.0.0.1:5190 (development), http://127.0.0.1:5191 (production). These processes last only while their terminals remain running.

## Verify

```powershell
npm.cmd --prefix site test
npm.cmd --prefix site run lint
npm.cmd --prefix site run test:browser
node site/tests/capture.mjs
node site/tests/performance.mjs
```

Browser tests use installed Microsoft Edge. The site must be running on 5190; Lighthouse uses production port 5191. `SITE_URL` overrides test targets. Evidence lives under `design-intel/build-shots/` and `design-intel/performance/`.

## Deploy

In Vercel, select **Root Directory: site**, framework **Next.js**, install `npm ci`, build `npm run build`. Set `NEXT_PUBLIC_SITE_URL` to the approved HTTPS domain. No backend keys are required for the pitch site. No public deployment was performed.

Before a public launch: replace the pilot-contact destination and demo video in `site/src/components/Actions.tsx`, approve the biography/traction text in `ContextSections.tsx`, finalize `site/src/app/privacy/page.tsx`, and address the mobile-performance backlog. The current pilot form downloads an unsubmitted local draft; it does not email or store personal data remotely.

## Other Surfaces

- `backend/`: existing FastAPI/SQLAlchemy evaluation and governance implementation. `uv run pytest` runs its tests. Hardware, PostgreSQL deployment, operational resilience and full production qualification remain separate gates.
- `web/`: existing React/Vite console. `npm.cmd --prefix web run build`. Preserved, not declared complete by the marketing sprint.
- `reference/`: supplied MVP and Scrollcraft reference copies. Original archives/PDFs remain outside this project in the parent folder.
- `knowledge/`, `graphify-out/`: earlier source extraction and graph snapshot. The current frontend graph is `handoff/knowledge-graph.json`.
- `docs/ai-skills/frontend-craft/`: reusable frontend workflow, tokens and lessons.

This is an engineering evidence product, not a certification body. Synthetic examples and draft gates must never be relabeled as physical safety proof, customers, pilots, revenue or certified compliance.