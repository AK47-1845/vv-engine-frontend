# Genuity Verify Pitch Site

## Getting Started

Use Node 24.18.0 (the verified runtime) and the committed npm lockfile:

```powershell
npm.cmd ci
npm.cmd run dev -- --hostname 127.0.0.1 --port 5190
```

Open http://127.0.0.1:5190. Production: `npm.cmd run build`, then `npm.cmd run start -- --hostname 127.0.0.1 --port 5191`.

Tests: `npm.cmd test`, `npm.cmd run lint`, `npm.cmd run test:browser`. Browser tests use installed Edge and a running server. See ../handoff/README.md for exact measurements and current gaps.

## Deployment

Vercel root directory: `site`. Framework: Next.js. Install: `npm ci`. Build: `npm run build`. Set `NEXT_PUBLIC_SITE_URL` to the approved public origin. The application is prerendered and needs no marketing-demo API credentials. No deployment was performed during this sprint.

## Replace Before Launch

- `src/components/Actions.tsx`: actual pilot submission destination and a real 90-second demo recording. Current form produces a local, unsubmitted draft.
- `src/components/ContextSections.tsx`: approved public biography and verified pilot evidence. Never invent these.
- `src/app/privacy/page.tsx`: legal operator, privacy contact, processing and hosting details.
- `src/app/layout.tsx`: approved public metadata/origin if different from the environment configuration.

## Architecture

`src/components/Pitch.tsx` composes the story. `src/lib/demo.ts` is a pure deterministic synthetic model. `HeroScene.tsx` uses a light mobile poster/canvas and opt-in 3D; desktop uses lazy Three.js. `FailureLab.tsx` computes verdicts and SHA256 exports. `Pipeline.tsx` loads ScrollTrigger near the section. `Actions.tsx` uses Radix dialogs. Tokens live in `src/app/site.css`; section styles in `workbench.css`.

Fonts are local WOFF2 through next/font. Poster images are generated from the actual scene by `tests/make-poster.mjs`. No third-party customer logos or remote product photos are used.

Final measured Lighthouse: desktop 99/100/100/100; mobile 77/100/100/100 (performance/accessibility/best-practices/SEO). Mobile LCP 3.515 s misses the requested target. Reports and next actions are preserved outside this app in ../design-intel/ and ../handoff/.
