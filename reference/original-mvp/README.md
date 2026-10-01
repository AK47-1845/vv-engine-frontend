# Genuity Verify MVP · V&V / Governance Platform, Module 1

Policy in → trust scorecard out → every run hash-chained into a provenance ledger.
Built for the Wednesday CTO pitch. Stdlib-only: no installs, works offline.

## Run it

**Easiest:** double-click `START.cmd`, leave its window open, then open
**http://127.0.0.1:8000/** in a browser.

Or from PowerShell in this folder:

```powershell
& 'C:\Program Files\Python310\python.exe' backend/server.py
```

(Plain `python` may hit the Microsoft Store shim · "Python was not found" -
so use the full path above, or `py backend/server.py`.)
No server? Double-click `reports/index.html` · pre-rendered scorecards, same numbers.
To use another port: `$env:VERIFY_PORT=8123; & 'C:\Program Files\Python310\python.exe' backend/server.py`

## The 3-minute demo script

1. Hit **Compare all 4** · clean=TRUSTED, synthfed=REVIEW, drifty+playback=BLOCKED.
2. Click the **playback** card · action-sensitivity reads exactly **0.0**: a dead
   steering wheel caught from trajectory data alone.
3. Click **synthfed** · the synthetic-data-trained policy: responsive but spiky,
   lands REVIEW. "Synthetic in, governance out."
4. Run a **Sweep** on clean · watch the verdict flip as noise ramps. That's the
   breaking point insurers and auditors pay for.
5. Point at the **ledger feed** · every click above is hash-chained. `GET
   /api/ledger/verify` proves the chain. EU clock counts down to 2027-01-20.

## If the projector / Wi-Fi dies

- The server is localhost · no internet needed, ever.
- Backup: `python tests/test_scorecard.py` prints all 4 verdicts in the terminal.
- Paper backup: export scorecard JSONs beforehand (Export button) and print one.

## Layout

```
backend/   server.py (API + static) · metrics_std.py (8 Genesis §4.4 metrics)
           policies.py (4 deterministic fixtures) · ledger.py (hash chain) · adversarial.py (disturbance hunt) · dossier.py (evidence drafts)
frontend/  index.html · docs.html · compliance.html · styles.css · app.js · docs.js · compliance.js (vanilla, no framework)
tests/     test_scorecard.py (10 tests, stdlib unittest)
docs/      TECHNICAL_PROMPT.md · KNOWLEDGE_GRAPH.md · PROCEDURAL_GRAPH.md
data/      ledger.jsonl (append-only; created on first run)
```

## Honesty labels (say these out loud, don't hide them)

- Gates are **DRAFT** until Month-1 calibration on Open X-Embodiment pairs.
- Jerk/bounds rows are **proxies**, not contact-dynamics proofs (needs Isaac/Genesis sim).
- Horizon gate debounces single-frame spikes (3-step breach run) · documented
  in `metrics_std.drift_at_horizon`.
- Fixtures are synthetic by design; the engine they exercise is the real artifact.

## Tests

```powershell
python tests/test_scorecard.py
```

10 tests: discrimination, exact-0.0 sensitivity, fail-closed, determinism,
ledger tamper-evidence, stdlib-only import scan, live in-process API.
