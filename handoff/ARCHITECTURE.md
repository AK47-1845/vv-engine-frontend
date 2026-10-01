# Architecture

VERIFIED: ../backend/ contains the Python service; ../web/ is a React 19/TypeScript/Vite 8 operations console. ../knowledge/ and ../graphify-out/ preserve source context. ../reference/ holds unchanged reference copies.

VERIFIED IMPLEMENTATION: `site/` is a separate Next.js App Router application. It has no calls to the engineering API and requires no backend credentials. The pilot form only downloads a local JSON draft.

## Component Tree

```text
site/src/app/layout.tsx: local fonts, metadata, global CSS
site/src/app/page.tsx -> components/Pitch.tsx
	SmoothMotion: desktop-only Lenis + GSAP ticker
	Hero -> HeroScene -> RobotScene (desktop or opt-in)
										 -> poster + 2D trace (mobile)
	FailureLab -> lib/demo.ts -> RobotScene + gates + SHA256 export
	Pipeline -> near-viewport GSAP ScrollTrigger + manual accessible tabs
	Evidence -> lib/demo.ts -> selectable ledger + report JSON export
	ContextSections -> sourced regulation, founder/build status, FAQ
	Actions -> Radix pilot/video dialogs -> local draft download
```

## Important Files

- `site/src/lib/demo.ts`: pure trace/assessment functions; explicit synthetic qualification. Tested by `site/tests/demo.test.mjs`.
- `site/src/app/site.css`: tokens, type, base layout, hero and responsive rules.
- `site/src/app/workbench.css`: lab, pipeline, light report, company and legal styles.
- `site/src/app/privacy/page.tsx`: implementation-specific privacy notice with legal placeholders.
- `site/src/app/opengraph-image.tsx`, `icon.tsx`: local generated share image and icon.
- `site/public/robot-poster.webp`, `robot-poster-mobile.webp`: generated from the actual scene, not stock/licensed customer imagery.
- `site/tests/site.spec.ts`: five widths, injection/reset/download, pilot keyboard flow, accessibility, reduced motion, links, metadata, WebGL failure and short-height geometry.
- `site/tests/capture.mjs`: canvas pixels, actual frame changes and hero screenshots.
- `site/tests/performance.mjs`: production Lighthouse reports; mobile default simulated throttling, desktop explicit desktop configuration.
- `design-intel/`: reference CSS, screenshots, build evidence and performance receipts. Not served publicly by Next.

## State And Motion Ownership

Hero owns playback and a synthetic sample index; pose and labels share the sample function. Dialog trees are memoized to avoid live-telemetry rerenders. HeroScene uses useSyncExternalStore for viewport state. RobotScene owns its WebGL resources and animation frame lifecycle, stops rendering offscreen/hidden and respects reduced motion.

FailureLab owns selected/applied disturbance and evaluation state. The 750ms presentation interval does not run physics or call a backend. Motion animates the verdict change. Pipeline uses CSS sticky layout; ScrollTrigger changes the active stage on desktop only. Tabs remain the reduced-motion/mobile path. Lenis never activates on mobile/reduced-motion.

## Verified Versions

Node 24.18.0; Next 16.3.8; React/React DOM 19.2.8; TypeScript 5.9.3; Tailwind 4.3.3; Three.js 0.186.1; GSAP 3.15.0; Lenis 1.3.26; Motion 12.43.0; Radix Dialog 1.1.23; Lucide 1.49.0; Playwright 1.63.0; axe 4.13.0; Lighthouse 13.5.0; font packages 5.3.0. The lockfile is authoritative.

## Build And Deploy

Exact commands are in README.md. Vercel root `site`, npm ci, npm run build. Set NEXT_PUBLIC_SITE_URL to the approved HTTPS origin. The production routes are prerendered. The Python backend is not deployable to Vercel merely by deploying this site.