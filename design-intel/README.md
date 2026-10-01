# Design Intelligence

VERIFIED research capture: 2026-10-01. Six URLs were opened by standalone Playwright at 1440x960 and 390x844. `observations.json` preserves computed CSS and resolved URLs; `screenshots/` preserves the actual captures. Run `node design-intel/probe.mjs` from the project root. The probe uses the existing console's Playwright dependency and installed Edge.

## Measured Samples

| Site | Desktop H1 / line | Mobile H1 / line | Sampled button duration / easing | Observed spacing |
| --- | --- | --- | --- | --- |
| Linear | 64 / 64 px | 38 / 41.8 px | 100 ms / cubic-bezier(.25,.46,.45,.94) | 72px header token; 32px heading side padding; 12px button sides |
| Stripe | 48 / 55.2 px | 34 / 35.02 px | 240-300 ms / cubic-bezier(.45,.05,.55,.95), mobile (.25,1,.5,1) | Per-element padding recorded in JSON; no universal spacing scale inferred |
| Palantir | H1 not available at initial desktop sample | 30 / 36 px | Mobile 250 ms / ease-in-out | Initial dynamic loading limits sample completeness |
| Anduril | H1 not available in sampled DOM | H1 not available | Mobile sampled 0 ms | Media-led page; no invented typography values |
| Figure | 28 / 31.08 px | 20 / 22.2 px | 300 ms / ease-in-out | Product-first full-width imagery and small supporting type |
| Godly -> Recent | 16 / 22.4 px | 16 / 22.4 px | Mobile 120 ms / cubic-bezier(.2,0,0,1) | Redirected gallery; not an inspected Awwwards winner |

These are specific computed elements at capture time, not exhaustive design-system specifications. Animations/loading may affect dynamic pages. Screenshots are private reference evidence, not licensed site assets.

## Adopted Patterns

1. Instrument hierarchy: large literal category, small mono provenance, and reserved signal color. Implement with self-hosted grotesk/mono tokens and explicit evidence labels.
2. Product as scene: show the actual system state, unframed, instead of a decorative illustration card. Implement a Three.js articulated arm and measured trajectory.
3. Consequence-driven interaction: change an input and expose the failed gate, event and verdict in the same tool. Keep deterministic computations separate from animation.
4. Evidence as a change of ground: a light report section creates a deliberate visual pause in a dark technical story. Preserve ordinary document hierarchy.
5. Narrow claims: render source links, missing prerequisites and prototype status where decisions occur. Do not borrow another company's credibility.

## Avoid

Unlicensed logos, invented statistics, repeated three-card sections, decorative spheres, arbitrary risk percentages, illegible microcopy, autoplay without pause, dark renders with invisible products, page-length padding that adds no information, fake contact submission, and a "certified" stamp on a demonstration.