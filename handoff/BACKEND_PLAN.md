# Backend Boundary

VERIFIED: A backend already exists in ../backend/; this sprint preserves it. The new marketing site must finish before any backend expansion.

Existing files cover strict trace schemas, unit-aware metrics, SQL persistence, audit chains, evidence ZIPs, scoped Z3 checks, and supervisory runtime leases. Inspect the actual API source before relying on endpoint names.

VERIFIED FRONTEND CONTRACT: `site/src/lib/demo.ts` emits sample index, intended/observed 3D position, drift, agreement and corroboration. `assessDemo()` returns `schema`, `evidenceKind`, `failure`, `samples`, `gates`, `verdict`, `decision`, `passing`, `description`, `qualification`. This is not the backend trace schema or a physical simulator. Its five pure tests passed.

Pilot request: no server submission without an approved destination and privacy/retention policy. Offer local brief export or an explicit unconfigured state.

Production gates remain authentication configuration, rate/resource limits, operational review, calibration, hardware qualification, independent evidence review and legal applicability.

## Existing API Surfaces Inspected

VERIFIED FROM SOURCE, not newly exercised in this sprint: `backend/api.py` exposes `/healthz`, `/readyz`, `/api/config`, auth/session/logout, `/api/workspace`, dataset/embodiment/profile creation, runs and independent reviews, experiments, transfers, proofs, runtime session/telemetry/reset, audit/verify, evidence export/verify, standards, knowledge, user administration and scoped tokens. Read the actual Pydantic models and authorization dependencies before integrating.

Earlier engineering test receipts are separate from the new frontend acceptance. To reproduce the backend: from project root run `uv sync`, `uv run pytest`, and `uv run uvicorn backend.api:create_app --factory --host 127.0.0.1 --port 8180`. These launch instructions are source-derived; this frontend sprint did not newly qualify them on a clean deployment.

Future connection: create an explicit adapter from a backend Trace/assessment to the marketing view model, retain `evidence_kind`, missing-gate states, source hashes and limitations. Do not substitute toy thresholds for calibrated profiles. Never call the runtime endpoint an actuator safety controller.