# Verification Trace

Problem: A deep-tech hero needs to show what is actually being verified.

Implementation: `site/src/components/RobotScene.tsx` renders an articulated industrial arm, explicit task envelope and deterministic cyan path. `site/src/lib/demo.ts` defines sample positions and failure perturbations. Use fixed scene dimensions, lazy import and local fonts. Pause when offscreen or the document is hidden.

Pitfalls: An attractive path is not a physical-dynamics simulation. Keep synthetic qualification visible. Camera framing must be responsive; a desktop offset is wrong on mobile. Check canvas pixels and exact geometry, not only presence of a canvas element. Provide a real bitmap fallback.