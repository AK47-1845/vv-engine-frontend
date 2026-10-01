# Final Verification Receipt

Date: 2026-10-01. Runtime: Windows, Node 24.18.0, installed Microsoft Edge. Production origin: http://127.0.0.1:5191. No cloud deployment was performed.

| Gate | Observed Result |
| --- | --- |
| Next.js production build | PASS; all five displayed routes prerendered |
| TypeScript noEmit | PASS after final test changes |
| Pure model tests | 5 PASS |
| Production Playwright suite | 11 PASS in 39.9s at 16:38:58 IST |
| Widths | 390, 768, 1024, 1440, 1920; no measured horizontal overflow |
| Accessibility | axe WCAG 2A/AA and 2.1AA scan passed; reduced-motion path passed |
| Interactions | Three injections, reset, evidence export, ledger selection, pilot local draft, dialog Escape/focus, manual pipeline stage |
| Graphics | Nonblank/moving canvas at 1440 and 390; WebGL failure loads the real bitmap |
| Metadata | Privacy, OG image and icon routes return 200; internal anchors resolve |
| Lint | 0 errors; 2 documented no-img-element warnings |
| Desktop Lighthouse | 99 performance / 100 accessibility / 100 best practices / 100 SEO |
| Mobile Lighthouse | 77 performance / 100 accessibility / 100 best practices / 100 SEO |
| LCP | Desktop 696ms; mobile 3515ms, target missed |
| CLS | Desktop 0.000058; mobile 0.000140 |
| Sustained 60fps / physical devices | NOT VERIFIED |
| Vercel deployment | NOT PERFORMED; build configuration and instructions provided |

Scores use Lighthouse 13.5.0 with mobile default simulated throttling and the desktop configuration in `site/tests/performance.mjs`. These are local lab measurements. The initial reports remain available. Native image and visible-label advisories remain in the backlog even though aggregate accessibility/best-practice scores are 100.

Screenshots and subjective section scores are indexed in CRITIQUE.md. Public-contact, video, biography/traction approval and legal privacy details remain launch blockers. The site does not claim certification or physical safety proof.