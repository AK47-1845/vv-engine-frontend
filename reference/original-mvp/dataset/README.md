# Dataset: paired sim vs real trajectories

One scenario, two versions of the truth. Every pair holds the SAME task
executed two ways: a clean `sim` tracking line and a degraded `real` line.
Scoring lives in backend/gaps.py (pair scorecards, cross-embodiment,
batch alpha audits). This folder COLLECTS plus stages upload samples.

## Layout

```
dataset/
  generate.py     deterministic pair generator (stdlib only, rerunnable)
  validate.py     format and provenance integrity check
  manifest.json   index of every pair (written by generate.py)
  scenarios/
    <id>/
      pair.json   {id, T, dt, fields, frame, sim: [[x,y]..], real: [[x,y]..]}
      card.json   {id, scenario, seed, T, description, source, generator,
                   license, sim_params, real_params}
  samples/        upload-ready batch files (see below)
  tools/
    convert_droid_ep.py  first DROID episode adapter (kept for record)
    fetch_droid_more.py  honest-discovery fetcher for episodes 2-5
    make_samples.py      builds samples/ + morph pairs (rerunnable)
```

Coordinate frames: synthetic pairs use abstract 2D workspace units, bounds
+/-2, dt 0.05s, T usually 200 (long_horizon 400). Real captures + morphs
use meters in the Franka base frame at native rate (dt not asserted).

## Scenarios (15, each x3 seeds = 45 pairs)

reach_straight, reach_curve, pick_place, wipe_raster, insert_push,
circle_trace, figure_eight, hesitant_operator, dropout_heavy, bias_drift,
latency_lag, aggressive_fast, cautious_slow, contact_slide, long_horizon.

Real side degradation stack (exact values on each card): bias ramp,
Gaussian noise, dropout spikes, time lag, contact stick.

## Real captures (5)

All DROID raw success episodes, Franka FR3, BAIR lab, AUTOLab pour
session 2023-07-07 (09:42, 09:43, 09:53, 10:04, 10:09). sim = commanded
EE xy, real = actual EE xy, meters, native rate, no smoothing.
Raw .h5 files kept in _incoming/. Discovery: public GCS listing of the
known day-folder (no guessed URLs); converter: tools/fetch_droid_more.py.
Mean commanded-vs-actual error 1.5-3.8 cm. All 5 score TRUSTED.

## Morph pairs (3, SYNTHETIC)

morph_pour_short_s1 (0.55x), morph_pour_tall_s1 (1.40x),
morph_pour_narrow_s1 (0.50x/1.00x aspect): droid_pour_s1 replayed on
variant arm geometries. Honestly labeled synthetic cross-kinematic
proxies for the xemb endpoint. Real OXE WidowX/RT-1 pairs plug into
the same endpoint in Month 1. Built by tools/make_samples.py.

## Upload samples (4, in samples/)

vv-batch/1 format: {id, blurb, episodes[{id, source, generation,
sim, real}]}. Served at /api/sample/<id> and loadable in one click
on the Evidence page:
sample-a-real-pour (alpha 0.0, GOVERNED), sample-b-mixed-batch
(alpha 0.6, REVIEW), sample-c-synth-heavy (alpha 0.9, BLOCKED +
collapse HIGH), sample-d-generations (gen ladder, collapse curve).

## Provenance policy (strict)

Every card MUST carry source, license, and seed. Synthetic pairs say
source synthetic/generator. Public real captures say source:url plus the
original license, and their card documents every transform applied
(resample, smoothing, axis mapping). Nothing enters without a card.
validate.py enforces this.

## How public real captures slot in

1. Put the capture under scenarios/<name>/ as pair.json + card.json
   in the same schema (sim may be a documented derived reference).
2. Run `python validate.py`. Zero failures required.
3. Append the entry to manifest.json (or regenerate it).

## Regen

`python generate.py` rewrites all synthetic pairs deterministically
(same bytes every run), then `python validate.py` must report 0 bad.
`python tools/make_samples.py` rebuilds samples/ + morphs the same way.
