# Procedural Graph · build order (each node gates the next)

```
[0 DOCS: prompt+graphs] ──done──> [1 metrics_std.py] ──unit-tested──> [2 policies.py]
                                                                        │
[3 ledger.py] ◄──independent── [0]                                      │
    │                                                                   ▼
    └──────────────> [4 server.py wires 1+2+3 + serves frontend] ◄── [sensitivity probe check:
                                                                       playback EXACTLY 0.0]
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
            [5 /api/compare]  [6 /api/sweep]   [7 /api/ledger+governance]
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      ▼
                    [8 frontend: picker → verdict → plot → ledger feed]
                                      │
                                      ▼
                    [9 tests/test_scorecard.py 5/5] ──fail?──> back to lowest failing node
                                      │
                                      ▼
                    [10 LIVE server smoke: curl /api/compare + open dashboard]
                                      │
                                      ▼
                    [11 HANDOFF: README run line + URL + backup plan]
```

## Node exit criteria
1. metrics_std: frechet/drift/sensitivity/spread/jerk/bounds match verify-mvp
   formulas on a fixed fixture (spot-check 3 values by hand).
2. policies: 4 fixtures deterministic; playback ignores probe (diff exactly 0).
3. ledger: append → verify chain OK; tampered copy → verify FAILS.
4. server: stdlib only; `python -c "import ast..."` scan finds no third-party imports.
5. compare: clean=TRUSTED, drifty=BLOCKED, playback=BLOCKED(sens 0.0), synthfed=REVIEW.
6. sweep: monotone noise ↑ ⇒ verdict degrades; flip point reported.
7. governance: countdown = days until 2027-01-20; calibration status = DRAFT.
8. frontend: no framework; works with JS disabled except scoring (static copy renders).
9. tests: 5/5, stdlib unittest, no network except localhost smoke (skippable flag).
10. smoke: server boots <2s, /api/compare 200 with 4 verdicts.
11. handoff: one copy-paste start command + URL + "if projector dies" paper backup.
