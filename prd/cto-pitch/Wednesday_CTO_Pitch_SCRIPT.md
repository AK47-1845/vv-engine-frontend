# Wednesday CTO Pitch — Full Speaker Script v2
> 30 Sept. ~30 min + Q&A. Voice: humble-elite. Every number tagged.
> All [VERIFY] items resolved 28 Sept via P1/P2 Deep Research (see Story doc
> P1/P2 Verification Appendix). Nothing below is unverified except [Estimated] tags.
> Stage directions in [brackets]. Slides numbered S1–S16 (map at end).

## TRAILER (45 seconds) — S1
"Sir, thank you for your time. In the next 30 minutes I'll do three things.
First, two minutes on where I came from — so you know whose findings these are.
Second, what I did inside LTTS month by month, and the three findings that came
out of four months of research — every number tagged to a source you can check.
Third, one working demo I built from those findings last week — not slides, code
that runs. At the end I'll ask for four months of checkable work. [pause] Please
interrupt me anywhere, sir. If I'm wrong on anything, I'd rather hear it here
than carry it forward."

## ACT 0 — PRE-INTRO (2.5 min) — S2
"I'm Karthikeya, from Vizag — Kendriya Vidyalaya kid. I fell in love with
mathematics early: NTSE scholar, state rank 14 in Andhra, 97 out of 100 in the
mental-ability paper; IOQM merit certificate. JEE 99.5 percentile brought me to
Mechanical at IIT Guwahati.
At IITG I did two things. One — Tech Board, drones and robotics, where I learned
that hardware punishes every assumption software lets you get away with.
[10-sec human beat, only if room is warm: also won an Inter-IIT gold in dance —
proof I can follow choreography as well as write it.]
Two — for 18 months I tried to make AI work on real enterprise data. 200-plus
conversations with industry teams, pilots and POCs, a Kaggle competition we ran
with 46-plus teams, an Inter-IIT problem statement that reached 2,000 students
across 23 IITs. I registered a small company along the way — honestly, sir,
mostly so I could sign pilot paperwork properly. [defuses Pvt-Ltd in one line,
smile, move on] I think of those 18 months as field school: I learned how AI
actually gets deployed — mostly by failing at it.
That journey brought me to Dr. Singh's doorstep in March — and then inside LTTS.
Everything after this slide happened in your building."

## ACT 1 — WHAT I DID INSIDE (5 min, dated) — S3–S4
"March 2026 — the aerospace POC. A 300-row, 22-column seed dataset; my pipeline
returned 5,000 physics-valid rows across 92 benchmarked runs with zero physics
violations. That's the work that earned Dr. Singh's trust, and his invitation to
come inside. [look at Madhusudhan, nod]
Month one inside — I mostly listened. Your senior teams walked me through MTR
validation, part rationalization, the OCR-to-JSON-to-ML pipelines you run for
clients. I saw how a services giant actually operates — the volume, the edge
cases, the review queues.
Month two — I built something: Genuity Reconcile, a 51-test evidence engine for
those exact workflows. And Dr. Singh gave me the most valuable feedback of my
four months — your teams already do this. [pause] He was right. And I learned
my first inside-lesson: never pitch table stakes to people who set the table.
Months three and four — Dr. Singh pointed me at research instead. Where does AI
actually stand? Synthetic data? World models? Physical AI? I produced four
documents: Genesis of Physical AI, 26 pages on world-model mathematics and
failure modes; The Practice of Physical AI, 16 pages prepared for Dr. Singh on
commercial reality; a 48-page frontier-LLM evolution study; and Idea 1, an
11-page governance blueprint. [hold up / gesture at printed stack]
I removed eleven claims from my own drafts when I couldn't verify them — the
list is in the appendix of your printed copy. [one sentence, move on. Opus
red-team fix: let him DISCOVER the deletion log — discovery beats performance.]
Everything I'm about to show carries a tag — Verified, Reported, Estimated, or
Speculative. If any number lacks proof, I'll say so before you have to ask."

## ACT 2 — THREE FINDINGS (12 min) — S5–S9
"Sir, four months of research compressed into three findings. Please correct me
on any of them.

FINDING ONE — World models are real, but pre-production. [S5–S6]
The field has three schools, and conflating them is the most common strategic
error I found. The Renderer school — Sora, Genie, Cosmos — predicts pixels:
photorealistic, but seconds per frame with severe hallucination risk. The latent
JEPA school predicts abstract physics: sub-5-millisecond inference, data
efficient — under 62 hours of robot data reported. The spatial-engineered school
— occupancy grids, PINNs, Isaac-class platforms — is the only one with explicit
conservation laws and high verifiability.
And all three share five failure modes I characterized mathematically: drift
that compounds until objects pass through solid walls within minutes; an
executability gap where flawless-looking video commands shattering grasps;
silent perceptual hallucination; action marginalization where the model ignores
the operator entirely; and a sim-to-real gap the 2026 industry consensus says
cannot be fully closed. [S6: the five, one line each]
The money agrees with the math: over $5 billion into humanoid and VLA
efforts in 18 months [Verified], against under $20 million of industry-wide
production revenue [Estimated] — a 250-to-1 asymmetry. Sir, this finding
is WHY I did not come back with a world-model proposal. The field needs years
of research. I'd rather tell you that than sell you hype. [pause]

FINDING TWO — The money that IS flowing goes to the boring layer. [S7–S8]
Tier-1 production today is simulation, validation, inspection, integration —
Applied Intuition and Isaac-class platforms under ISO 26262 contracts, PINN
inspection lines, Waymo's paid trips [each cited]. Hundreds of millions in
licenses [Verified]. Meanwhile every humanoid deployment — Figure at BMW,
Apollo at Mercedes, Digit at Amazon — is a bounded, pre-production pilot
[Verified press releases, all of them].
My reading, sir: intelligence gets the headlines; verification gets the revenue.
And verification is LTTS-shaped work. [glance at Madhusudhan — shared thesis]

FINDING THREE — The regulatory clock. [S9]
On January 20, 2027 [Verified, EUR-Lex] — under four months from today — the
EU Machinery Regulation makes Notified Body assessment mandatory for
self-evolving AI in safety functions: Annex I, Part A, Item 24. And here's the
detail that matters, sir: frozen-weight systems may still self-assess — but
every over-the-air update that shifts safety behavior counts as a substantial
modification, requiring re-assessment and a new CE mark. So TÜVs will certify
the snapshot — and somebody must monitor the movie, across every update, with
Notified Body queues already at six to twelve months. In parallel, ISO's
humanoid safety standard sits as an unpublished industrial-scope draft
[Reported — publication expected late 2026/2027]. Purpose-built neural-policy
verification has no owner yet. Sir, this window is measured in months. Somebody
certifies the physical-AI age. The only question my research couldn't answer is
who — that's a decision for this room, not my documents. [humble landing]"

## ACT 3 — TEN-YEAR BETS FOR L&T (5 min, options never orders) — S10–S11
"Sir, I'm 21 and I've been inside four months — so take these as readings, not
recommendations, and please correct me. But I've been thinking about where your
parent company's world goes in the decade when robots enter every factory, site,
and facility L&T builds. If you asked me where I'd place bets:
One — a Verification practice FIRST, Q1 2027. Lowest capex, regulatory-forced,
serves your existing auto, aero, and medical clients from day one. The
deliverable I'd build toward is an Automated Safety Dossier Compiler — barrier
functions plus reachable-set proofs that output ISO 13849 / IEC 61508 dossiers
without millions of physical trials. Phase one around $2.8 million, bottom-up
in the document [Estimated].
Two — PLC alliances in Q2, once safety credentials exist: Siemens, Rockwell
bridge partnerships, plant-floor access. Around $1.3M [Estimated].
Three — synthetic data factories in Q3 — AFTER validation and access exist, not
before. Around $4.2M.
Four — a standing Center of Excellence: 250 engineers upskilled, lateral PhDs,
IIT/IISc fellowships. Around $2.5M a year.
Notice the order, sir: verify first, generate later; credentials before alliances
before factories. The industry does it backwards — models first, safety never.
That inversion is the single most expensive mistake my research found. [pause]
I'm not asking you to approve any of this today. I'm showing you I thought in
budgets, sequences, and dependencies — not in thesis chapters."

## ACT 4 — THE IMMEDIATE PROPOSAL + DEMO (8 min) — S12–S14
"Idea 1 is the platform thesis. But I didn't want to come with only paper. So
last week I built Module 1 — a trust scorecard engine for robot policies. If
given the chance, sir, this is the kind of thing I would build here. [S12]
[DEMO — 3 min, S13 on screen] Three policies, one scorecard each. A clean policy
— green across drift, horizon, sensitivity. A drifting policy — watch the
coherence horizon collapse to 0.38 and the sim-to-real distance spike. And a
playback policy that ignores its controls — action-sensitivity reads exactly
zero-point-zero. It caught a dead steering wheel from trajectory data alone.
Every metric maps to one Genesis failure mode. The Fréchet sim-to-real score is
patent vector number one in Idea 1. [pause] Nothing here is a slide, sir. It runs.
[S14] If you gave me four months, here are checkable gates — two per month,
judge me on dates:
Month 1 — scorer hardened on public Open X-Embodiment rollout pairs, plus 3
customer outreach emails sent with response tracking. If nobody wants this after
30 days of outreach, I'll tell you myself.
Month 2 — module 2: adversarial edge-case discovery in Isaac Sim, plus a first
customer response log — insurers first, sir, they hold actuarial budgets today.
Month 3 — module 3: provenance ledger prototype.
Month 4 — two provisional patent drafts with attorney review initiated, plus a
pilot proposal for ONE LTTS client asset.
If I miss, you lose nothing — the research, the code, and the drafts stay with
you. [Opus fix: underpromise in words, overdeliver in work. Provisionals, not
grants; outreach logged, not assumed.]"

## CLOSE (90 seconds) — S15
"Sir, four months ago you asked me to come inside, drop my ego, and prove my
worth. Since then I learned your business, mapped your industry's next decade,
found the one window that's open right now — and built the first module before
this meeting instead of after it. [slow down]
I'm not asking you to believe in world models. I'm asking you to believe in four
months of checkable work. Give me the chance — and I'll give you a platform,
patents, and pilots. Thank you, sir. [stop. Do not add one more sentence.]"

## Q&A OPENER — S16 (title only: "Questions — please be harsh")
"Sir, before questions — three attacks I expect, with one line each: who pays —
insurers first, they hold actuarial budgets today, then OEMs when January
regulation forces them, then TICs; why me and not internal teams — structural
arbitrage, sir, your teams can't spend four months off-P&L on a speculative bet
and I can; and Applied Intuition — they build the simulation, I score the
output: the builder can't be the auditor — rating agency, not bank. Full maps
on page 8 of Idea 1. Now please — where am I wrong?"

---

## SLIDE MAP (16 slides, 30 min)
| # | Title | Visual | Time |
|---|---|---|---|
| S1 | Trailer: findings + demo + 4-month ask | 3 icons, no text walls | 0:45 |
| S2 | Where I came from | Vizag→IITG timeline, 5 nodes | 2:30 |
| S3 | Inside: dated journey | Mar→Sept timeline, 4 rows | 2:30 |
| S4 | The 4 documents + deletion log | Doc covers + "11 claims deleted" callout | 2:30 |
| S5 | 3 schools matrix | 10-dim table (from Genesis) | 3:00 |
| S6 | 5 failure modes | 5 rows, 1 line + 1 number each | 3:00 |
| S7 | Capital vs revenue: 250:1 (>$5B vs <$20M) | 1 big ratio + corrected company table | 2:30 |
| S8 | Tier 1/2/3 production reality | 3-tier map with citations | 2:30 |
| S9 | Regulatory clock: Jan 2027 | Timeline + gap diagram | 3:00 |
| S10 | 10-year bets 1–2 | V&V + alliances, budgets | 2:30 |
| S11 | 10-year bets 3–4 | Factories + CoE, sequence logic | 2:30 |
| S12 | Module 1: trust scorecard | Architecture: policy in → report out | 1:30 |
| S13 | LIVE DEMO | Terminal + report card (backup: recording) | 3:00 |
| S14 | 4-month gated ask | 4 rows: month → gate → proof | 2:00 |
| S15 | Close: the bet | 1 line. Nothing else on slide | 1:30 |
| S16 | Questions — be harsh | 3 preempted attacks, 1 line each | Q&A |

## DELIVERY NOTES (critic pass baked in)
- Acts are modular: any interruption lands on a completed thought. Never "I'll get
  to that" — answer, then bridge back ("...which is exactly why Finding 2 matters").
- "Correct me" rhythm: invite scrutiny at the end of EVERY act. Dhurandhar trusts
  people who beg for attacks.
- Madhusudhan moments (Act 1 nod, Finding 2 glance): scripted, visible, genuine.
  He must leave feeling like the mentor who found the guy — that's your air cover.
- Pvt Ltd: exactly one line, Act 0, framed as pilot paperwork. Never again unless
  the CTO asks. If asked: "a vehicle for pilots, sir — today's proposal lives
  wherever you want it to live."
- Spinout/funding: NEVER raised by you. Idea 1 §6.3 sits in the appendix for the
  CTO to discover. If he asks "how does this live inside LTTS": ring-fenced
  vehicle on product metrics → spinout option keeps LTTS equity if Phase 2
  outgrows P&L tolerance. Deliver as HIS idea the moment his eyes light up.
- Numbers without tags don't exist. All [VERIFY] items resolved 28 Sept (P1/P2);
  anything still soft gets cut with a logged deletion (deletions are trust assets).
- Rehearse aloud 3×, timed. Record once, watch once. Cut 10% after each run.

