# Progressive Graphics

Problem: Desktop 3D can consume a mobile page's entire startup budget.

Use server-discoverable local imagery and a small live canvas first. In `HeroScene.tsx`, subscribe to viewport state with useSyncExternalStore; desktop or explicit user action enables the lazy Three.js scene. Keep screenshot-generated WebP fallbacks at explicit dimensions. The canvas and telemetry must read the same trace model.

Measure on a production server with unchanged Lighthouse throttling. Record both baseline and final values. A score improvement is not acceptance if it still misses the target. Pause offscreen work, respect reduced motion, and clean up graphics resources.

Pitfalls: conditionally rendering a dynamic import without actually splitting heavy code, loading desktop scroll libraries on mobile, testing only canvas existence, using a generic stock poster, and cherry-picking a faster run.