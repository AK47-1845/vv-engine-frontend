---
name: frontend-craft
description: "Use when building, reviewing, or extending the Genuity Verify marketing frontend: research-grounded visual design, evidence-first interactions, responsive screenshots, accessibility and honest performance verification."
---

# Frontend Craft

1. Read `handoff/README.md`, `STATUS.md` and `FACTS_VS_PLACEHOLDERS.md` before editing. Preserve the working console and backend.
2. Inspect a bounded set of live references. Save desktop/mobile screenshots and computed CSS under `design-intel/`. Distinguish measured values from inference and failed captures.
3. Write the product journey and one visual concept before building. Genuity uses a near-black test instrument, cyan signal, and contrasting evidence paper. Do not use gradient blobs, generic glass cards or invented customer logos.
4. Keep tokens centralized in `site/src/app/site.css`. Use Geist and JetBrains Mono through `next/font/local`. Use explicit responsive type steps and zero tracking. Use compact type for instruments, large type only for real section headings.
5. Use Next.js App Router, TypeScript, Tailwind tokens and Radix dialog primitives. Use Lucide icons. Lazy-load Three.js. Let Lenis own smooth scrolling and GSAP ScrollTrigger own pipeline progress. Use Motion only for local state transitions.
6. Keep the demonstration model pure and deterministic. Label every trace/result as synthetic. Never promote a browser mock into hardware, safety, traction, certification or calibrated evidence.
7. Give each control a complete outcome: selected, busy, success, error, reset and export where appropriate. Never imply that a pilot request was sent when it was only downloaded.
8. After a substantive edit run the cheapest focused behavior/type/build check. Inspect real screenshots at 1440 and 390. Run all five target widths before acceptance.
9. Score hierarchy, type, spacing, motion, originality and polish honestly. Scores are subjective, not certifications. Fix the largest issue first. Use two passes for hero/demo and one for secondary sections in a timed sprint.
10. Verify keyboard focus, dialog semantics, reduced motion, canvas pixels/movement, console errors, viewport overflow, internal links and a production build. Measure Lighthouse on a production server and report the exact configuration; do not promise 95 without a result.
11. Update `lessons.md`, handoff status, graph, known issues and next actions after meaningful checkpoints. Do not describe nonexistent files or unrun checks as complete.

## Quality Gate

- Literal first-viewport product/category signal and a visible hint of the next section.
- No text/scene overlap, clipped controls, invented metrics or contact destinations.
- Real static fallback for unavailable WebGL; no endless loading state.
- All public assets local or licensed with attribution.
- Production build passes; measured results and remaining launch gates documented.