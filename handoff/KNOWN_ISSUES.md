# Known Issues

- VERIFIED OPEN: Mobile Lighthouse performance 77, LCP 3.515 s and TBT 451 ms miss the requested bar. Desktop 99; both other categories 100. Reports are in design-intel/performance/. Hardware/load variability exists; do not report the earlier 81 as the final result.
- VERIFIED OPEN: Pilot destination, demo recording, verified public biography and pilot traction are placeholders. The form downloads locally and does not submit.
- VERIFIED OPEN: ESLint passes with two no-img-element warnings in HeroScene.tsx and RobotScene.tsx. Locally generated responsive WebPs are intentional, but delivery remains measurable improvement work.
- VERIFIED ADVISORY: Lighthouse reports a visible-label/accessibility-name mismatch on the wordmark. It did not reduce its aggregate accessibility score but should still be repaired.
- UNVERIFIED: Sustained 60fps, physical-device energy use, every tablist keyboard convention, hostile-browser security testing and hosted Vercel performance. Do not infer these from local tests.
- UNVERIFIED: Existing console's remaining governance screens may be incomplete. They are preserved and outside this frontend-first sprint.
- VERIFIED FIXED: Initial install/terminal conflict; local-font path; paper-label contrast; effect-state lint errors; fallback-image readiness race. See frontend-craft/lessons.md.
- VERIFIED: No public deployment or independent hardware/safety certification took place.