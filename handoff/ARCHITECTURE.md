# Architecture

VERIFIED: ../backend/ contains the Python service; ../web/ is a React 19/TypeScript/Vite 8 operations console. ../knowledge/ and ../graphify-out/ preserve source context. ../reference/ holds unchanged reference copies.

PLANNED, NOT YET IMPLEMENTED: A separate Next.js App Router application serves the pitch site. Components use typed deterministic demonstration fixtures and do not send pilot contact details anywhere without an explicitly configured destination. Existing backend remains separate and is not bundled into the public site.

Exact commands, component tree, animation ownership, and dependency versions will be updated once installed and verified.