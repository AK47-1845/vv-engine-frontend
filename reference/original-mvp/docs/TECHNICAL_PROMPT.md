# Technical Prompt · V&V / Governance Platform MVP
> Self-written. This is the prompt I would have fed a code LLM. I am executing it directly instead.

## 1. Objective
A working Module-1 trust-scorecard engine for robot policies, wrapped as a
governance console a CTO can click through live: policy in, red/amber/green
report out, every run hash-chained into an append-only provenance ledger.

## 2. Non-negotiable constraints
- **Stdlib only.** Python 3.10 http.server + pure-Python math. No numpy, no pip,
  no venv. Reason: sandbox has no numpy, venv ensurepip is broken, and the
  Wednesday demo must survive dead Wi-Fi.
- **Deterministic.** All policies seeded (`random.Random`). Same seed = same
  scorecard, byte for byte. Canned compare-all endpoint doubles as backup.
- **Honest labeling.** Jerk/bounds rows are PROXIES (not contact-dynamics
  proofs). Thresholds are DRAFT until calibrated on Open X-Embodiment data.
  Every number the UI shows carries a [Verified/Reported/Estimated] tag or a
  DRAFT badge. Nothing silently authoritative.
- **Fail-closed.** Worst gate decides the verdict. Unknown metric = BLOCKED.

## 3. Architecture (one process)
```
browser  <--http:8000-->  backend/server.py  (API + static frontend/)
                               |  |  |
              metrics_std.py  policies.py  ledger.py
                         data/ledger.jsonl (append-only, hash-chained)
```
- `metrics_std.py`: 8 Genesis §4.4 metrics, pure Python. Trajectory = list of
  [x, y], T=200, D=2.
- `policies.py`: 4 deterministic fixtures. Policies are functions of
  (actions, seed) so the sensitivity probe is dynamics-based, NOT the Day-1
  seed-shuffle proxy (that flaw is fixed here · see §5).
- `ledger.py`: append-only JSONL, each entry hash-linked to previous
  (sha256 over canonical JSON). Accumulate-not-replace.
- `server.py`: stdlib BaseHTTPRequestHandler. REST JSON + serves frontend/.
- `frontend/`: plain HTML/CSS/vanilla JS. No framework, no build step.

## 4. API contract
| Method | Path | Body | Returns |
|---|---|---|---|
| GET | / | - | dashboard |
| GET | /api/policies | - | 4 fixtures + descriptions |
| POST | /api/score | {policy, seed?} | scorecard + gates + verdict + ledger_id |
| GET | /api/compare | - | all 4 scorecards + downsampled trajectories |
| POST | /api/sweep | {policy, from, to, steps} | noise→verdict flip curve (Module-2 lite) |
| GET | /api/ledger | - | hash chain (verify endpoint: /api/ledger/verify) |
| GET | /api/governance | - | EU 2027-01-20 countdown, tag legend, calibration status |
| GET | /api/history | - | scored runs this session |
| POST | /api/hunt | {policy, budget?} | falsification style disturbance hunt plus ledger entry |
| POST | /api/dossier | {policy, seed?} | evidence dossier with clause mapping plus ledger entry |
| GET | /docs | - | static how-it-works page (sidebar shell) |
| GET | /compliance | - | static compliance timeline page (sidebar shell) |

## 5. The sensitivity fix (Day-1 flaw, fixed)
OLD (weak): sensitivity = distance between seed=1 and seed=999 rollouts.
Clean policies scored near-zero through no fault of their own.
NEW (dynamics-based): policies consume an explicit action sequence.
Probe = step offset added to second-half actions. Sensitivity =
E[||T(a) − T(a+probe)||²] / E[||T(a)||²]. Playback ignores actions →
exactly 0.0. Responsive policies → large. This is a real control-response
test, not a seed lottery.

## 6. Policy fixtures (the demo narrative)
1. `clean` · tracks commands + small noise → TRUSTED (green).
2. `drifty` · random-walk error compounds → BLOCKED on drift/horizon.
3. `playback` · replays fixed tape, ignores controls → BLOCKED, sensitivity 0.0.
4. `synthfed` · synthetic-data-trained profile (higher spread, responsive):
   the "synthetic data in → governance out" use case → REVIEW (amber).

## 7. Gates (DRAFT · Month-1 calibrates on OXE)
Same 8 rules as verify-mvp/report.py. Labeled DRAFT in UI and API.
Two metrology upgrades vs Day-1, both documented in code: (a) sensitivity is a
dynamics probe, not seed-shuffle (§5); (b) horizon breach requires 3 consecutive
over-threshold steps (debounced transients · `metrics_std.drift_at_horizon`).

## 8. Acceptance criteria (must all pass before handoff)
1. `python tests/test_scorecard.py` · 5/5 green (discrimination + determinism +
   ledger chain verifies + sweep finds a flip + API smoke).
2. `GET /api/compare` returns 4 verdicts: clean=TRUSTED, drifty=BLOCKED,
   playback=BLOCKED with sensitivity exactly 0.0, synthfed=REVIEW.
3. Same POST /api/score twice → identical metric bytes, two ledger entries.
4. Ledger tamper test: flip one byte in a copy → /api/ledger/verify reports break.
5. Dashboard loads at 127.0.0.1:8000, scores a policy on click, draws paths.
6. Cold start on his machine: `cd` in + one `python` command, no installs.

## 9. Explicitly NOT in this MVP
No physics sim (Isaac/Genesis), no real OXE data, no auth, no DB, no framework.
Those are Months 1-4. This MVP proves: metrics discriminate, ledger is
tamper-evident, UI tells the story in 3 minutes.
