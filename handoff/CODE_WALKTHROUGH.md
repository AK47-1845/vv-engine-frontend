# Code Walkthrough For Incremental Continuation

Read the owning file and its existing test before making a change. This is an orientation map, not permission to refactor every module.

## Pitch Site: site/

- `src/app/page.tsx` renders `components/Pitch.tsx`, which orders the whole story. Change section order only when requested.
- `src/app/layout.tsx` owns local fonts, metadata and CSS imports. Fonts come from locked local packages, not runtime Google requests.
- `src/app/site.css` owns the visual tokens/base/hero; `workbench.css` owns the lab, pipeline, report and secondary sections. Preserve the established cyan/neutral/semantic palette and responsive dimensions.
- `src/lib/demo.ts` is the pure synthetic model. `sampleTrace` computes intended/observed positions; `assessDemo` derives gates and verdicts. Do not substitute these toy thresholds for backend calibration.
- `Hero.tsx` owns playback and sample timing. `HeroScene.tsx` selects lightweight mobile rendering or lazy 3D. `RobotScene.tsx` owns Three.js geometry, animation and cleanup. Visual geometry is schematic, not a dynamics simulation.
- `FailureLab.tsx` owns failure-selection/evaluation presentation, actual SHA256 calculation and browser export. Keep selected/applied states distinct so transitions cannot display stale evidence.
- `Pipeline.tsx` owns four-stage narrative state. CSS pins the section; ScrollTrigger updates stages only on desktop. Mobile/reduced-motion users can select stages directly.
- `Evidence.tsx` renders synthetic ledger selection and the light dossier. Its JSON export is an example, not an issuing-instance signature.
- `Actions.tsx` uses Radix for accessible dialogs. The pilot form ONLY downloads an unsubmitted local JSON draft. Do not add remote transmission without approved requirements.
- `ContextSections.tsx` contains sourced regulatory context, founder/build status and honest placeholders. Never invent traction to remove a placeholder.
- `next.config.ts` has an opt-in static export for transfer. Normal development remains Next.js. With `GENUITY_STATIC_EXPORT=1`, Next emits the export into `.next-transfer/`.

## Engineering Backend: backend/

- `schemas.py`: strict Pydantic contracts for finite values, equal path lengths/dimensions, timestamps, provenance, profiles, embodiments and telemetry. Reject invalid evidence rather than coercing it silently.
- `engine.py`: deterministic trajectory metrics, per-gate statuses, worst-condition precedence and canonical hashes. Missing required evidence is not a pass. Draft profiles never confer release eligibility. Tests: `tests/test_engine.py`.
- `fixtures.py`: explicitly synthetic deterministic failure cases. They exercise the engine; they are not real robot performance.
- `store.py`: SQLAlchemy tenant records, atomic record/audit writes, sequence/head locking, integrity checks and session lookup. SQLite is the local implementation; PostgreSQL deployment qualification remains pending. Tests: `tests/test_store.py`.
- `service.py`: connects datasets/profiles/runs, review independence, stress sweeps, geometric transfer, proofs, runtime sessions and export. DROID import preserves missing timestamps and dropped axes.
- `runtime.py`: bounded supervisory decision lease. Stale/replayed/unsafe telemetry produces HOLD; incidents latch. No actuator commands or certified control loop are implemented.
- `formal.py`: Z3 exact-rational affine/ReLU box queries for small scoped networks. VERIFIED_BOX does not prove floating-point execution, closed-loop stability or entire VLA safety.
- `evidence.py`: qualified ZIP export, member hashes, issuing-instance HMAC and bounded verification. Internal integrity differs from independent origin/attestation. Tests for runtime/formal/evidence: `tests/test_assurance.py`.
- `api.py`: FastAPI endpoints, authentication, role checks, CSRF/origin/body/resource boundaries and service orchestration. Tests: `tests/test_api.py`. Read the actual endpoint/dependency before integrating a new UI.
- `config.py`: environment guards and local instance settings. Production forbids demo auth and requires a proper secret/HTTPS origin. Do not copy local secrets into a new machine's source tree.

## Operations Console: web/

`src/Console.tsx` is the application shell; `api.ts` owns HTTP calls; `types.ts` carries contracts; `Replay.tsx` and `Scene.tsx` own replay; `Workbenches.tsx` owns added specialist workspaces; CSS is local to this application. `vite.config.ts` proxies the API to loopback 8180 and serves the console on 5180. Do not merge the dark pitch-site theme into this intentionally light operations interface.

## Verification Ladder

1. For a pure demo-model change: run `npm.cmd --prefix site test`.
2. For frontend changes: run its type/build check, then the matching Playwright test and compare existing screenshots.
3. For backend changes: run the owning test module first, then relevant API tests. Do not weaken missing-evidence, tenant, replay or audit assertions.
4. For a transfer/build change: build the static export and run browser tests with `SITE_URL=http://127.0.0.1:5192` against `node tools/preview.mjs`.
5. Record what passed, what failed and what was not run. Keep a small diff and an intact Git recovery point.