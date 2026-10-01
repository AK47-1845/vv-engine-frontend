# The_Complete_Evolution_of_Frontier_LLMs (1) (1).pdf

SHA256: 63f475718391f4b93b3851ce8344bbe2ec5e2a349035605ab99f743502e91640

## Page 1

The Complete Evolution
of Frontier LLMs

## Page 2

Contents
1 Executive Summary 4
2 Foundations: The Transformer and the First Scaling Bets (2017–2020) 7
2.1 Why Self-Attention Replaced Recurrence . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.1 Multi-Head Attention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.2 The Quadratic Cost and Positional Encoding . . . . . . . . . . . . . . . . . 7
2.2 Tokenization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 The GPT Line: 1 through 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.4 The Kaplan Scaling Laws . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 The Scaling Era and Chat Alignment (2021–2023) 10
3.1 From Raw Prediction to Aligned Assistants . . . . . . . . . . . . . . . . . . . . . . 10
3.2 GPT-4 and the Move to Mixture-of-Experts . . . . . . . . . . . . . . . . . . . . . . 10
3.2.1 How MoE Routing Works . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3 The Chinchilla Correction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.4 Anthropic, Claude, and Constitutional AI . . . . . . . . . . . . . . . . . . . . . . . 11
4 The Context-Window Race, Multimodality, and Attention Efficiency (2023–2024) 13
4.1 The Quadratic Wall . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4.2 FlashAttention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4.3 Positional Encoding, Take Two: ALiBi and RoPE . . . . . . . . . . . . . . . . . . . 13
4.3.1 Attention with Linear Biases (ALiBi) . . . . . . . . . . . . . . . . . . . . . 13
4.3.2 Rotary Position Embedding (RoPE) . . . . . . . . . . . . . . . . . . . . . . 14
4.4 KV-Caching, Grouped-Query Attention, and Ring Attention . . . . . . . . . . . . . 14
4.5 Native Multimodality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.6 Claude 3 and the “Good, Fast, Cheap” Tiering Strategy . . . . . . . . . . . . . . . 14
5 The Reasoning-Model Turn: Test-Time Compute (Late 2024–2025) 16
5.1 From Pretraining Compute to Inference Compute . . . . . . . . . . . . . . . . . . 16
5.1.1 Process Reward Models vs. Outcome Reward Models . . . . . . . . . . . . 16
5.2 Anthropic’s Transparent Alternative . . . . . . . . . . . . . . . . . . . . . . . . . . 16
5.3 DeepSeek-R1 and the Commoditization of Reasoning . . . . . . . . . . . . . . . . 16
5.3.1 Group Relative Policy Optimization (GRPO) . . . . . . . . . . . . . . . . . 17
5.4 Self-Consistency and Test-Time Search . . . . . . . . . . . . . . . . . . . . . . . . 17
6 Agentic and Tool-Using Models (2025–2026) 18
6.1 From Text Generators to Digital Actuators . . . . . . . . . . . . . . . . . . . . . . 18
6.2 The Model Context Protocol (MCP) . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.3 Long-Horizon Context Management . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.4 Multi-Agent Orchestration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
Confidential: Internal Strategy Briefing 1 September 2026

## Page 3

The Complete Evolution of Frontier LLMs CONTENTS
7 Failure Modes, Security, and Governance in Agentic Deployment 20
7.1 Hallucination and Confident Error . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.2 Prompt Injection: The Central Agentic Vulnerability . . . . . . . . . . . . . . . . . 20
7.3 Data Leakage and IP Confidentiality . . . . . . . . . . . . . . . . . . . . . . . . . 21
7.4 Sycophancy , Automation Bias, and Review Fatigue . . . . . . . . . . . . . . . . . . 21
7.5 Building an Internal Evaluation Set . . . . . . . . . . . . . . . . . . . . . . . . . . 22
8 The Current Frontier (September 2026): GPT-6 Astra vs. Claude Fable 5.1 / Mythos
5.1 23
8.1 Model Overviews . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
8.1.1 GPT-6 Astra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
8.1.2 Claude Fable 5.1 and Claude Mythos 5.1 . . . . . . . . . . . . . . . . . . . 23
8.2 Rigorous, Sourced Benchmark Comparison . . . . . . . . . . . . . . . . . . . . . . 24
8.3 Corrected Pricing Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
9 Architecture and Training: Deep-Dive Reference Tables 27
9.1 Parameter Count and Architecture Trends . . . . . . . . . . . . . . . . . . . . . . 27
9.2 Context Window Growth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
9.3 Inference Cost Trends (Flagship Tier) . . . . . . . . . . . . . . . . . . . . . . . . . 28
9.4 Post-Training Pipeline Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
9.5 Inference-Time Efficiency: Quantization and Speculative Decoding . . . . . . . . 28
10 Benchmark Integrity and Evaluation Methodology 30
10.1 Self-Reported vs. Independent Evaluation . . . . . . . . . . . . . . . . . . . . . . 30
10.2 Benchmark Contamination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
10.3 METR Time Horizons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
10.4 Practical Guidance for Reading Any Benchmark Claim in This Report . . . . . . . 31
11 Open-Weight Models and Sovereign Fallback 32
11.1 The Open-Weight Tier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
11.2 What Self-Hosting Actually Buys . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
11.3 What It Costs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
11.4 Distillation as the Bridge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
12 Practical Guidance: Which Model, When 34
12.1 Task-Type to Model Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
12.2 Pros and Cons: GPT-6 Astra vs. Claude Fable 5.1 / Opus 5 . . . . . . . . . . . . . 35
12.3 Business-Lens Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
13 LTTS-Specific Use-Case Mapping 36
13.1 Mobility Segment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
13.2 Sustainability Segment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
13.3 Tech Segment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
13.4 Cost Modelling: A Worked Example . . . . . . . . . . . . . . . . . . . . . . . . . . 37
13.5 A 90-Day Adoption Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
13.6 Risk Register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
13.7 Cross-Cutting Horizontal Use Cases . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Confidential: Internal Strategy Briefing 2 September 2026

## Page 4

The Complete Evolution of Frontier LLMs CONTENTS
14 Confidence, Caveats, and Corrections 40
14.1 Unverified or Vendor-Sourced Claims Carried Forward . . . . . . . . . . . . . . . 40
14.2 Corrections Applied in This Edition . . . . . . . . . . . . . . . . . . . . . . . . . . 40
15 Glossary 42
16 Sources 45
16.1 Sourcing Policy for This Edition . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
16.2 Foundational Papers (Primary) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
16.3 Attention and Efficiency (Primary) . . . . . . . . . . . . . . . . . . . . . . . . . . 46
16.4 Vendor Primary Sources (Announcements, System Cards, Pricing) . . . . . . . . . 46
16.5 Independent Evaluators (Primary) . . . . . . . . . . . . . . . . . . . . . . . . . . 47
16.6 Claims Retained Without a Primary Source . . . . . . . . . . . . . . . . . . . . . . 47
Confidential: Internal Strategy Briefing 3 September 2026

## Page 5

CHAPTER 1
Executive Summary
This briefing documents the architectural, operational, and commercial evolution of frontier
large language models from the 2017 Transformer paper through September 2026, focusing
on the primary dichotomy between OpenAI’s GPT lineage and Anthropic’s Claude lineage, with
reference to the DeepSeek-R1 reasoning breakthrough that reshaped the economics of the entire
field in early 2025. Over this decade, the dominant paradigm shifted three times: first from
recurrent sequence models to self-attention (2017–2019); then from static, single-pass next-token
prediction to post-training-aligned, human-preference-optimized chat models (2021–2023); and
finally from a pure pretraining-compute race to a dynamic, inference-time compute regime in
which models reason, verify , and act autonomously across tools and environments (2024–2026).
For L&T Technology Services (LTTS), this progression signals a shift from deploying models
as generic text generators toward embedding them as semi-autonomous engineering agents that
interpret computational fluid dynamics (CFD) output, generate embedded C/C++ and real-time
operating system code, review Verilog/VHDL, and identify vulnerabilities across large codebases.
The current frontier, defined by OpenAI’s GPT-6 Astra and Anthropic’s Claude Fable 5.1 (with
the restricted Claude Mythos 5.1 variant for trusted cybersecurity/biosecurity partners), offers
million-token context windows, native multimodality, and system-level computer use, at unit
economics that have compressed by roughly 80–90% in real terms since GPT-4’s 2023 debut
even as raw capability has increased by several multiples on demanding benchmarks.
Confidential: Internal Strategy Briefing 4 September 2026

## Page 6

The Complete Evolution of Frontier LLMs CHAPTER 1. EXECUTIVE SUMMARY
The Decade at a Glance
Year Landmark Why it mattered
2017 Transformer (Attention Is All
You Need)
Replaced recurrence with self-attention; made training
parallelisable across the sequence.
2018–
19
GPT-1, GPT-2, BERT Proved generative pretraining transfers; GPT -2’s staged
release set the norm of restricted frontier deployment.
2020 GPT-3, Kaplan scaling laws In-context learning emerged; scale became the strat-
egy .
2022 InstructGPT, Chinchilla, Chat-
GPT
RLHF made models usable; Chinchilla corrected the
scaling recipe; ChatGPT set the interface.
2023 GPT-4, Claude 2, Constitu-
tional AI
Sparse Mixture-of-Experts and 100K context; AI feed-
back removed the human-labelling bottleneck.
2024 GPT-4o, Claude 3 family,
FlashAttention/RoPE maturity
Native multimodality; tiered pricing; long context be-
came economically serviceable.
2024–
25
o1/o3, Claude 3.7, DeepSeek-
R1
Capability shifted to inference-time compute;
DeepSeek proved it was not a proprietary moat.
2025–
26
MCP, GPT-5, Claude 4.5 Models became tool-using agents; integration stan-
dardised.
2026 GPT-6 Astra, Claude Fa-
ble/Mythos 5.1
Million-token context, system-level computer use, and
the first government-ordered suspension of a frontier
model.
Table 1.1: Ten years of frontier model development, compressed.
How to Read This Document
Chapters 2 through 6 are the technical spine and build in order: attention, alignment, context
scaling, reasoning, and agency. Chapters 7 through 10 are the current-state assessment and
are readable standalone. Chapters 11 through 13 are the LTTS-specific recommendations, and
are the chapters to read first if the reader’s question is “what should we do on Monday.” Every
benchmark figure in this report is labelled either self-reported or independent; Chapter 10
explains why that distinction carries more weight than the numbers themselves.
What Changed in This Edition
• Source quality. The prior edition cited a number of secondary SEO/content aggregator sites
for factual claims that originate from primary sources (OpenAI system cards, Anthropic’s
newsroom, Artificial Analysis, METR). This edition re-attributes claims to primary sources
wherever they could be independently located, and explicitly flags any claim that could only
be sourced to a vendor blog or an unverified aggregator.
• The cost table. The malformed $/1M-token pricing table in Part 7 of the prior edition is
corrected below with input/output columns cleanly separated and tiered pricing for long-
context requests noted explicitly .
• The Astra-vs-Fable framing. The prior edition’s prose leaned toward describing GPT-6 Astra
as a near-universal capability ceiling. Independent benchmarking now available (Artificial
Analysis Intelligence Index v4.2, published September 4, 2026) placesClaude Fable 5.1 ahead
Confidential: Internal Strategy Briefing 5 September 2026

## Page 7

The Complete Evolution of Frontier LLMs CHAPTER 1. EXECUTIVE SUMMARY
of GPT-6 Astra on the composite index, while GPT-6 Astra remains the more token-efficient
model on agentic terminal tasks and the stronger model on spatial/CAD-adjacent benchmarks.
This is a genuine split decision, not an Astra sweep, and the report now says so in the same
breath as the claim rather than in a disconnected appendix.
• The export-control narrative. The prior edition attributed the June 2026 suspension of
Fable 5/Mythos 5 to a specific researcher at a named company discovering a safeguard bypass.
That specific attribution is not corroborated across independent reporting and is removed.
What is corroborated: Anthropic suspended global access to Fable 5 and Mythos 5 on June 12,
2026 to comply with a U.S. Department of Commerce export-control directive; the Department
lifted the relevant controls on June 30, 2026; and Anthropic restored access on July 1, 2026.
• Depth. This edition roughly triples the technical content: full derivations of scaled dot-
product and multi-head attention, FlashAttention’s tiling mechanism, RoPE’s rotation-matrix
formulation, Mixture-of-Experts routing and load-balancing, the RLHF and Constitutional AI
objective functions, DeepSeek’s Group Relative Policy Optimization (GRPO), KV-cache and
quantization mechanics for inference economics, and a new chapter on benchmark integrity
and evaluation methodology .
Three Things to Remember
1. Model selection is now continuous routing, not vendor lock-in. Because inference-time
reasoning means cost scales with how long a model “thinks,” the competitive question is
which model to route which task to, not which single model to standardize on.
2. The Model Context Protocol (MCP) is the integration layer worth standardizing on ,
independent of which underlying model wins any given benchmark cycle, because it decouples
LTTS’s tool integrations (iDriVe, CAE pipelines, ticketing systems) from any single vendor’s
API.
3. Frontier access is now conditional infrastructure.The June 2026 export-control suspension
demonstrated that a government directive can remove global API access to a flagship model
inside 72 hours. Any mission-critical workflow needs a fallback model and a contractual
understanding of data residency and access continuity .
Confidential: Internal Strategy Briefing 6 September 2026

## Page 8

CHAPTER 2
Foundations: The Transformer and the First Scaling Bets
(2017–2020)
2.1 Why Self-Attention Replaced Recurrence
Prior to 2017, sequence modeling was dominated by Recurrent Neural Networks (RNNs) and
Long Short-Term Memory (LSTM) networks. Both process tokens one at a time, carrying a hidden
state forward through the sequence. This creates two structural problems: the computation
cannot be parallelized across the sequence dimension during training (each step depends on the
previous one), and information from early tokens must survive many sequential transformations
to influence late tokens, causing gradual degradation. This is the vanishing and exploding
gradient problem.
The Transformer, introduced by Vaswani et al. inAttention Is All You Need (2017), eliminated
recurrence entirely in favor of a self-attention mechanism that lets every token attend directly
to every other token in a single parallel operation. The core operation, Scaled Dot-Product
Attention, is:
Attention(Q,K,V ) = softmax
QKT
√dk

V (2.1)
where Q (queries), K (keys), and V (values) are learned linear projections of the input
token embeddings, anddk is the dimensionality of the key vectors. The QKT term computes
a similarity score between every pair of tokens; dividing by √dk prevents these scores from
growing too large in magnitude as dimensionality increases (which would push the softmax
into a saturated, low-gradient regime); and the softmax converts the scores into a probability
distribution used to compute a weighted sum of the value vectors.
2.1.1 Multi-Head Attention
A single attention operation captures one notion of “relatedness” between tokens. The Trans-
former instead runs h attention operations in parallel, each with its own learned projection
matrices, then concatenates and linearly projects the results:
MultiHead(Q,K,V ) = Concat(head1,..., headh)WO
where head i = Attention(QWQ
i , KWK
i , VWV
i )
(2.2)
Each head can specialize. Empirically , different heads in trained Transformers learn to track
syntactic dependencies, coreference, positional offsets, or rare-token copying behavior. This gives
the model a richer representational basis than a single attention computation would permit, at a
compute cost that still scales linearly inh for fixed total dimensionality .
2.1.2 The Quadratic Cost and Positional Encoding
Self-attention’s central drawback is immediate from theQKT term: for a sequence of length n,
this produces ann×n score matrix, so both compute and memory scale asO(n2d). Doubling
Confidential: Internal Strategy Briefing 7 September 2026

## Page 9

The Complete Evolution of Frontier LLMs CHAPTER 2. FOUNDATIONS: THE TRANSFORMER AND THE FIRST SCALING BETS (2017–2020)
context length quadruples the attention compute, and this is the central bottleneck that Chapter
4 of this report addresses.
Because self-attention has no inherent sense of token order (it is permutation-equivariant),
the original Transformer injected sinusoidal positional encodings into the input embeddings:
PE (pos,2i) = sin
 pos
100002i/dmodel

, PE (pos,2i+1) = cos
 pos
100002i/dmodel

(2.3)
Using geometric progressions of sine and cosine frequencies lets the model represent both
coarse and fine-grained relative positions, and, in principle, extrapolate to sequence lengths not
seen during training, a property that later architectures (Chapter 4) improved on substantially .
The original Transformer used an encoder-decoder structure built for machine translation.
Generative language modeling instead favored decoder-only architectures with causal (trian-
gular) masking, which zeroes out attention scores for any key position after the query position,
forcing each token to attend only to its predecessors. This is what makes autoregressive, left-to-
right next-token generation well-defined.
2.2 Tokenization
Before any of this math runs, raw text is converted into discrete tokens via Byte-Pair Encoding
(BPE) or a close variant (e.g. SentencePiece unigram models). BPE starts from individual bytes or
characters and iteratively merges the most frequent adjacent pair into a new symbol, building a
vocabulary (typically 32K–200K tokens for frontier models) that balances sequence length against
embedding-table size. Tokenization choices materially affect apparent context-window capacity ,
per-language cost (languages poorly represented in the merge statistics fragment into more
tokens per word), and numerical reasoning ability (digit tokenization schemes vary significantly
across model families and affect arithmetic performance).
2.3 The GPT Line: 1 through 3
OpenAI’s Generative Pre-trained Transformer (GPT) series applied the decoder-only Transformer
at increasing scale. GPT-1 (2018) demonstrated that unsupervised generative pretraining
followed by supervised fine-tuning transferred well across downstream NLP tasks. GPT-2 (2019)
scaled to 1.5 billion parameters and a 1,024-token context window, trained on WebText, a dataset
built from outbound links on highly-upvoted Reddit posts. GPT-2 was also a socio-political
milestone: OpenAI staged the release of model weights, citing concern that a 1.5B-parameter
model could be misused for mass disinformation generation. That decision established the
now-standard industry norm of restricted frontier-model deployment rather than immediate
open-sourcing.
GPT -3 (2020) scaled to 175 billion parameters and a 2,048-token context window, trained on
roughly 300 billion tokens. Its defining property was in-context learning: the ability to perform
novel tasks from a handful of examples placed directly in the prompt, without any gradient
update. This was an emergent capability that smaller models in the same family did not exhibit
to the same degree, and it reframed language models as general-purpose few-shot learners rather
than task-specific fine-tuning targets.
2.4 The Kaplan Scaling Laws
GPT-3’s scale was theoretically justified by scaling laws published by Kaplan et al. (OpenAI,
2020), which modeled test lossL as a power-law function of computeC, parameter countN,
Confidential: Internal Strategy Briefing 8 September 2026

## Page 10

The Complete Evolution of Frontier LLMs CHAPTER 2. FOUNDATIONS: THE TRANSFORMER AND THE FIRST SCALING BETS (2017–2020)
and dataset sizeD. The headline finding was an allocation rule: as compute budgets grow, they
should be spent overwhelmingly on parameters rather than data, roughly
Noptimal∝C0.73, D optimal∝C0.27 (2.4)
This is why GPT-3 was trained on a comparatively modest 300B-token corpus relative to
its 175B-parameter size. It was following what was then believed to be the compute-optimal
frontier. As Chapter 3 covers, this conclusion was later shown to be an artifact of Kaplan et al.’s
experimental setup rather than a durable law.
Confidential: Internal Strategy Briefing 9 September 2026

## Page 11

CHAPTER 3
The Scaling Era and Chat Alignment (2021–2023)
3.1 From Raw Prediction to Aligned Assistants
A raw next-token predictor is not a well-behaved assistant: prompted with a question, it may
continue the text in any statistically plausible direction, including completing it with more
questions, hedges, or toxic continuations, because its only training objective was to predict the
next token of internet text. OpenAI’s InstructGPT (2022) addressed this with Reinforcement
Learning from Human Feedback (RLHF), a three-stage pipeline:
1. Supervised Fine-Tuning (SFT).Human labelers write ideal responses to a set of prompts; the
base model is fine-tuned on these demonstrations to learn the basic format of a helpful reply .
2. Reward Model (RM) training. The SFT model generates multiple candidate responses per
prompt; human labelers rank them by preference. These rankings train a separate reward
model to predict a scalar preference score for any (prompt, response) pair.
3. RL fine-tuning via PPO. Proximal Policy Optimization (PPO) is used to update the SFT policy
to maximize the reward model’s score.
Optimizing purely against a learned reward model risks reward hacking: the policy drifts
toward reward-model blind spots, producing fluent but degenerate or sycophantic outputs
(“mode collapse”). The RLHF objective therefore adds a Kullback-Leibler (KL) divergence penalty
that keeps the learned policyπθ close to a fixed reference policyπref (usually the SFT model):
L(θ) = Ex,y∼πθ

rϕ(x,y )

−βDKL
 
πθ(y|x)∥πref(y|x)

(3.1)
The coefficientβ trades off reward maximization against fidelity to the reference model’s
broader linguistic competence. Too small aβ produces reward hacking; too large aβ produces a
model that barely moves from its pre-RLHF behavior.
ChatGPT’s November 2022 launch is frequently described as a research breakthrough, but is
more precisely a product and distribution milestone: it wrapped the existing InstructGPT model
in a conversational, stateful interface and shipped it to hundreds of millions of users, establishing
the chat paradigm as the default way people interact with language models. The underlying
deep learning advances had shipped months earlier.
3.2 GPT-4 and the Move to Mixture-of-Experts
GPT -4 (early 2023) introduced native multimodal input and a substantially larger context window,
and is widely believed (OpenAI has not officially confirmed exact figures) to have moved from
GPT-3’s dense architecture to a sparse Mixture-of-Experts (MoE) design, persistent industry
estimates putting it at roughly 1.8 trillion total parameters across 16 experts of about 111B
parameters each, with only a small subset of experts active per token.
Confidential: Internal Strategy Briefing 10 September 2026

## Page 12

The Complete Evolution of Frontier LLMs CHAPTER 3. THE SCALING ERA AND CHAT ALIGNMENT (2021–2023)
3.2.1 How MoE Routing Works
In an MoE Transformer, each feed-forward block is replaced by a bank ofN expert feed-forward
networks and a lightweight gating (router) network. For each token, the router computes a score
for every expert and activates only the top-k (commonlyk=1 or 2):
g(x) = softmax
 
TopK(xWg,k )

, y =
X
i∈TopK
gi(x)Ei(x) (3.2)
This decouples total parameter count (which drives representational capacity) from active
compute per token (which drives inference latency and cost). A model can have trillions of
parameters while only a small fraction fire on any given forward pass. The engineering challenge
is load balancing: without a corrective term, routers tend to collapse onto a small subset of
“popular” experts, under-utilizing the rest of the network’s capacity . Standard practice adds an
auxiliary load-balancing loss that penalizes uneven token-to-expert assignment across a training
batch, encouraging the router to spread tokens roughly evenly .
3.3 The Chinchilla Correction
DeepMind’s Chinchilla paper (Hoffmann et al., 2022) overturned the Kaplan-era conclusion.
Kaplan et al.’s power-law fits had been biased by evaluating models at small scale using fixed,
sub-optimal learning-rate schedules that did not decay appropriately for larger training runs.
Re-run with properly scaled learning-rate schedules, the compute-optimal allocation looked very
different:
Noptimal∝C0.50, D optimal∝C0.50 (3.3)
i.e. parameters and training tokens should scale equally, not with parameters dominating.
The resulting rule of thumb, roughly 20 training tokens per parameter, meant that GPT-3-scale
models had been substantially under-trained relative to their size. Smaller, more data-saturated
models (Chinchilla itself, at 70B parameters trained on 1.4 trillion tokens, outperformed the
280B-parameter Gopher) could match or beat far larger, under-trained models at a fraction of
the inference cost. This single correction reshaped training-compute budgets across the industry
for the next several years.
3.4 Anthropic, Claude, and Constitutional AI
Anthropic, founded in 2021 by former OpenAI researchers including Dario Amodei and Daniela
Amodei, released the Claude 1 and Claude 2 model families in 2023, differentiating on extended
context (Claude 2 offered a 100K-token window, enabling full-document analysis well ahead of
contemporaries) and on alignment methodology .
Anthropic’s central alignment contribution, Constitutional AI (CAI), replaces much of the
human preference-labeling step in RLHF with AI-generated feedback graded against a written
constitution, a set of explicit principles the model is trained to satisfy . CAI runs in two phases:
• Supervised phase. The model generates an initial response, then critiques its own response
against the constitution, then revises it. This loop is iterated a few times to produce a
cleaned-up demonstration set for SFT.
• RL phase (RLAIF). Instead of human raters comparing response pairs, an AI evaluator model
compares pairs against constitutional principles to build a preference dataset, which trains
Confidential: Internal Strategy Briefing 11 September 2026

## Page 13

The Complete Evolution of Frontier LLMs CHAPTER 3. THE SCALING ERA AND CHAT ALIGNMENT (2021–2023)
a reward model exactly as in RLHF; PPO then optimizes the policy against this AI-derived
reward model.
The motivation is practical as well as ethical: human preference labeling at RLHF scale is
expensive, slow, and repeatedly exposes human raters to harmful content in order to grade it.
Replacing the bulk of this labeling with a rule-based AI evaluator removed a major scalability
bottleneck and let Anthropic iterate on alignment substantially faster.
Confidential: Internal Strategy Briefing 12 September 2026

## Page 14

CHAPTER 4
The Context-Window Race, Multimodality, and Attention
Efficiency (2023–2024)
4.1 The Quadratic Wall
As established in Chapter 2, standard self-attention costsO(n2d) in both compute and memory .
Doubling the context window quadruples the compute and memory footprint of the attention
layers. In practice, the binding constraint on GPUs is often not floating-point throughput but
High Bandwidth Memory (HBM) I/O: naive attention implementations materialize the fulln×n
score matrix in slow global GPU memory, and the resulting memory traffic, not the arithmetic
itself, dominates wall-clock time. Unlocking million-token context windows required a cluster of
complementary innovations.
4.2 FlashAttention
FlashAttention (Dao et al., 2022) is an IO-aware, exact (not approximate) attention algorithm.
Instead of computing and storing the fulln×n attention matrix, it tiles the computation into
blocks small enough to fit in the GPU’s ultra-fast on-chip SRAM, computing partial softmax
statistics incrementally (an “online softmax”) and never writing the full intermediate matrix
back to slow HBM. This reduces memory reads/writes from quadratic to roughly linear in
sequence length for the I/O-bound portion of the computation, yielding large real-world speedups
(commonly 2–4x) without changing the mathematical result. It is a systems optimization, not an
approximation.
4.3 Positional Encoding, Take Two: ALiBi and RoPE
Sinusoidal positional encodings extrapolate poorly beyond training-time sequence lengths. Two
alternatives became standard:
4.3.1 Attention with Linear Biases (ALiBi)
ALiBi discards learned/sinusoidal positional embeddings entirely . Instead, it adds a static, head-
specific linear penalty to the raw attention scores based on the distance between query and key
positions:
score(i,j ) = qi·kj−m·|i−j| (4.1)
wherem is a fixed, head-specific slope (geometrically spaced across heads). Nearby tokens
are penalized less than distant ones, biasing attention toward locality without any learned
position parameters. Because the bias is a simple, unbounded linear function of distance, models
trained on short sequences empirically extrapolate to much longer sequences at inference time
with limited degradation, the “train short, test long” property .
Confidential: Internal Strategy Briefing 13 September 2026

## Page 15

The Complete Evolution of Frontier LLMsCHAPTER 4. THE CONTEXT -WINDOW RACE, MULTIMODALITY , AND ATTENTION EFFICIENCY (2023–2024)
4.3.2 Rotary Position Embedding (RoPE)
RoPE instead encodes absolute position by rotating the query and key vectors in 2D sub-planes of
the embedding space by an angle proportional to position, such that the dot product between a
rotated query at positioni and a rotated key at positionj depends only on their relative offset
i−j, not their absolute positions. This directly bakes relative-position dependence into the
attention score computation itself, rather than adding it as a separate bias term, and has become
the de facto standard positional scheme in most current frontier open architectures, valued for its
clean extrapolation behavior when combined with interpolation/scaling tricks (e.g. NTK-aware
scaling, YaRN) for extending context beyond the training length.
4.4 KV-Caching, Grouped-Query Attention, and Ring Attention
During autoregressive generation, each new token’s query must attend to the keys and values of
all previous tokens. Recomputing these from scratch at every step would be wasteful; instead,
inference engines cache the key/value tensors for all previously generated tokens (the KV cache)
and only compute the new token’s own K/V pair at each step. The KV cache’s memory footprint
grows linearly with sequence length and is, in practice, the dominant memory cost for long-
context serving, often exceeding the memory used by the model weights themselves at long
context lengths. Two techniques reduce this pressure:
• Multi-Query Attention (MQA) shares a single key/value head across all query heads, and
Grouped-Query Attention (GQA) is an intermediate compromise, sharing K/V heads across
small groups of query heads. Both cut KV-cache size substantially with modest quality loss
relative to full multi-head attention.
• Ring Attention distributes a very long sequence’s KV cache and computation across multiple
GPUs arranged in a ring topology , with each device passing key/value blocks to its neighbor as
computation proceeds, allowing context lengths far beyond what a single device’s memory
could hold.
DeepSeek’s Multi-head Latent Attention (MLA), introduced with DeepSeek-V2/V3, takes a
different approach: it compresses the K/V representations into a low-rank latent vector before
caching, reconstructing full-rank keys/values on the fly , cutting KV-cache memory by an order of
magnitude relative to standard multi-head attention while preserving most of its quality. This
was a significant contributor to DeepSeek’s later cost advantages (Chapter 5).
4.5 Native Multimodality
GPT-4 Turbo (late 2023) extended the context window to 128K tokens. GPT-4o (2024) repre-
sented a deeper architectural shift: rather than bolting an independently-trained vision encoder
onto a text model and projecting its embeddings into the text token space (the prevailing ap-
proach through GPT -4), GPT -4o integrated text, audio, and vision within a single, unified network
trained end-to-end, eliminating the latency of cascaded models and letting cross-modal signal
flow directly through the primary attention layers rather than through a narrow embedding
bottleneck.
4.6 Claude 3 and the “Good, Fast, Cheap” Tiering Strategy
Anthropic’s March 2024 Claude 3 launch established a three-tier product strategy of Haiku
(fast/cheap), Sonnet (balanced), and Opus (maximum capability), which both signaled a ma-
Confidential: Internal Strategy Briefing 14 September 2026

## Page 16

The Complete Evolution of Frontier LLMsCHAPTER 4. THE CONTEXT -WINDOW RACE, MULTIMODALITY , AND ATTENTION EFFICIENCY (2023–2024)
turing enterprise pricing model and let Anthropic ship a single architecture at multiple serving
costs. Claude 3.5 Sonnet (mid-2024) briefly inverted this hierarchy, outperforming the larger
Claude 3 Opus on several benchmarks, including a reported 64% versus 38% gap on an agentic
coding evaluation. This was achieved without a full new pretraining run: Anthropic applied
improved post-training (synthetic-data-driven fine-tuning and RL) to the existing Sonnet check-
point, demonstrating that meaningful capability gains could be extracted from post-training
algorithmic improvements alone, independent of base-model scale.
Confidential: Internal Strategy Briefing 15 September 2026

## Page 17

CHAPTER 5
The Reasoning-Model Turn: Test-Time Compute (Late
2024–2025)
5.1 From Pretraining Compute to Inference Compute
Through 2024, the dominant scaling axis was pretraining compute: bigger models trained on
more data with more FLOPs. In September 2024, OpenAI’s o1 (followed by o3) introduced
a structural pivot: instead of scaling only at training time, these models scale capability at
inference time by generating an extended, hidden chain of reasoning tokens before producing a
final answer, planning, checking intermediate steps, and backtracking within a single response.
5.1.1 Process Reward Models vs. Outcome Reward Models
Standard RLHF reward models are Outcome Reward Models (ORMs): they score only the final
answer, providing a single, sparse reward signal for an entire multi-step reasoning trace. This
makes credit assignment difficult. A correct final answer reached via flawed intermediate steps is
rewarded identically to one reached soundly , and a promising partial trace that ultimately fails
gets no partial credit.
Process Reward Models (PRMs) instead score each intermediate reasoning step, providing
a dense reward signal that can guide the model through multi-step problems and penalize
specific flawed steps even within an otherwise-correct trajectory . Training a good PRM requires
step-level labels (human-annotated or, increasingly , generated by using a strong verifier model
or an executable checker), which is more expensive to collect than outcome labels but yields
substantially better credit assignment for long reasoning chains.
The exact training and search procedure behind o1/o3 remains undisclosed by OpenAI.
Widespread academic speculation suggests mechanisms resembling Monte Carlo Tree Search
(MCTS) over candidate reasoning paths, but OpenAI has not confirmed this, and it should be
treated as an informed hypothesis rather than a documented fact.
5.2 Anthropic’s Transparent Alternative
Anthropic’s response, Claude 3.7 Sonnet and the Claude 4 family, took a different design
stance: rather than hiding the reasoning trace as OpenAI does (citing competitive and safety
reasons), Anthropic exposed the intermediate reasoning tokens to developers and gave explicit
programmatic control over a thinking budget, letting an application dial reasoning depth up or
down per request. This reframed the commercial unit from a flat per-query price to a variable
cost tied to how much test-time compute a given query actually consumed, reinforcing an
industry-wide shift toward consumption-based, reasoning-depth-sensitive pricing.
5.3 DeepSeek-R1 and the Commoditization of Reasoning
DeepSeek-R1’s January 2025 release was the catalyst that forced both OpenAI and Anthropic
to compress API pricing aggressively . DeepSeek published an open-weight model that reached
Confidential: Internal Strategy Briefing 16 September 2026

## Page 18

The Complete Evolution of Frontier LLMs CHAPTER 5. THE REASONING-MODEL TURN: TEST -TIME COMPUTE (LATE 2024–2025)
frontier-competitive reasoning benchmarks using a fraction of the training compute reportedly
spent by U.S. labs, and, critically, published enough of its methodology to demonstrate that
high-quality reasoning behavior could be learned through large-scale reinforcement learning
with comparatively little human-annotated step-level supervision.
5.3.1 Group Relative Policy Optimization (GRPO)
DeepSeek’s key algorithmic contribution was Group Relative Policy Optimization (GRPO),
a variant of PPO that removes the separate learned value/critic network. For a given prompt,
GRPO samples a group ofG candidate outputs from the current policy , scores each with a (often
rule-based, e.g. “did the code execute correctly”) reward function, and computes each output’s
advantage relative to the group’s own mean and standard deviation:
Ai = ri− mean(r1,...,r G)
std(r1,...,r G) (5.1)
This sidesteps the cost and instability of training a separate value network (as standard
PPO requires) by using the group itself as the baseline, while a KL term (as in standard RLHF)
keeps the policy from drifting too far from a reference model. Combined with largely rule-based,
automatically verifiable rewards (unit tests passing, math answers matching a known solution)
rather than a learned reward model, GRPO let DeepSeek train sophisticated reasoning behavior
with substantially less human labeling infrastructure than classic RLHF. This was a major driver
of the subsequent industry-wide cost compression, since “process supervision at scale” no longer
strictly required expensive PRM label collection.
5.4 Self-Consistency and Test-Time Search
A simpler, complementary test-time technique, self-consistency or majority voting, samples
multiple independent reasoning chains for the same prompt and takes the most common final
answer. This trades additional inference compute (running the model k times) for improved
accuracy on tasks with verifiable answers, and is often combined with more sophisticated search
or verification passes in production reasoning systems as a cheap accuracy lever when task
budgets allow multiple samples.
Confidential: Internal Strategy Briefing 17 September 2026

## Page 19

CHAPTER 6
Agentic and Tool-Using Models (2025–2026)
6.1 From Text Generators to Digital Actuators
By the Claude 4.5 generation and OpenAI’s GPT-5 generation, both labs shifted primary optimiza-
tion focus from single-turn answer quality toward long-horizon agentic competence: models
that drive a browser, operate a desktop environment, call external APIs, and maintain coherent
state across hundreds or thousands of tool calls without losing track of constraints established
early in a session.
6.2 The Model Context Protocol (MCP)
Anthropic’s Model Context Protocol, an open standard built on JSON-RPC, addresses the integra-
tion problem this creates: rather than every enterprise writing bespoke, brittle API glue code for
every tool a model might need, MCP standardizes communication through three primitives:
• Tools: discrete, callable functions the model can invoke (e.g. “create a Jira ticket,” “run this
SQL query”) with defined input/output schemas.
• Resources: addressable, read-only data the model can pull into context on demand via a
URI-based request-response pattern (the client issues a ReadResourceRequest ; the server
returns structured data), avoiding the need to pre-load an entire document store into the
prompt.
• Prompts: reusable, parameterized prompt templates a server can expose to standardize how
a given tool should be invoked across different client applications.
Because MCP is a protocol rather than a proprietary SDK, an MCP server written once against
a given enterprise system (an ERP, a CAD repository, a ticketing system) can be called by any
MCP-compliant model client, from any vendor. This is the key property that lets an organization
avoid re-building its tool integrations every time it swaps or adds a model provider.
6.3 Long-Horizon Context Management
Earlier agent architectures relied on lossy compaction: as a session’s context filled up, older
turns were summarized into a shorter form to make room for new ones. This reliably degraded
performance over very long sessions, as specific constraints established early (“never touch this
file,” “the units here are millimeters, not inches”) would blur or drop out of the compressed
summary after enough compaction cycles. Current-generation architectures (from the GPT-5
line onward, and matched by Claude’s agentic tooling) instead implement forms of continuous
context caching and recurrent state carried natively through the network, preserving precise
cross-window references without repeatedly re-compressing the entire history into a single lossy
summary . This materially improves coherence on multi-day , thousand-tool-call autonomous runs
such as large codebase refactors or persistent simulation monitoring.
Confidential: Internal Strategy Briefing 18 September 2026

## Page 20

The Complete Evolution of Frontier LLMs CHAPTER 6. AGENTIC AND TOOL-USING MODELS (2025–2026)
6.4 Multi-Agent Orchestration
A parallel development is the shift from a single model handling an entire task to orchestrated
multi-agent systems: a lightweight “planner” model decomposes a task and dispatches sub-tasks
to specialized worker agents (a coding agent, a search agent, a verification agent), often running
different model tiers for different sub-tasks to balance cost against capability . This pattern, rather
than a single monolithic model call, is increasingly how production agentic systems are built,
and it is the direct motivation for Chapter 12’s task-to-model routing guidance: the unit of
deployment decision-making has moved from “which model do we standardize on” to “which
model handles which step.”
Confidential: Internal Strategy Briefing 19 September 2026

## Page 21

CHAPTER 7
Failure Modes, Security, and Governance in Agentic
Deployment
A model that can only produce text can only mislead a reader. A model that can execute shell
commands, open pull requests, and query internal systems can act on a mistake before anyone
reviews it. The shift described in the previous chapter therefore changes the risk profile of
deployment more than it changes the risk profile of the model, and this chapter is the practical
counterweight to that chapter’s enthusiasm.
7.1 Hallucination and Confident Error
Language models generate the most probable continuation, not the most truthful one. In
engineering contexts the characteristic failure is not obvious nonsense but plausible, well-
formatted, internally consistent fabrication: a POSIX flag that does not exist, a register address
off by one, a citation to a standard clause number that was never written, a material property
quoted to four significant figures from nowhere. Retrieval-augmented generation reduces this by
grounding answers in retrieved documents, but it does not eliminate it, because the model can
still misread, over-generalise, or blend a retrieved fact with a remembered one.
The only reliable mitigation in an engineering workflow is verification against a determinis-
tic oracle: compile the generated code, run the test suite, check the dimension against the CAD
model, resolve the citation against the actual standard. Where no oracle exists, the output needs
human sign-off proportional to its consequence. A useful framing for deployment decisions is
to ask what the cost of an undetected error is, and to permit autonomy only where that cost is
bounded.
7.2 Prompt Injection: The Central Agentic Vulnerability
Prompt injection is the most important security property of agentic systems and is structurally un-
solved. The mechanism is simple: a model reading untrusted content cannot reliably distinguish
between data it is meant to process and instructions it is meant to follow. A comment in a pull
request, text in a scraped web page, a line in an uploaded specification, or an entry in a returned
API payload can carry instructions that the model then executes with the full permissions of the
session.
Why This Is Not a Patchable Bug
Prompt injection is not an implementation defect in a particular model; it follows from
how instruction-following models work. Both OpenAI and Anthropic ship classifiers and
training-based mitigations that raise the difficulty considerably, and both state plainly
that these reduce rather than remove the risk. Any architecture whose security depends
on the model always correctly ignoring adversarial instructions in its context window is
Confidential: Internal Strategy Briefing 20 September 2026

## Page 22

The Complete Evolution of Frontier LLMs CHAPTER 7. FAILURE MODES, SECURITY , AND GOVERNANCE IN AGENTIC DEPLOYMENT
unsound. Security must come from the permissions surrounding the model, not from the
model’s judgement.
The defensive posture that follows is conventional security engineering:
• Least privilege on tools. An agent reviewing code needs read access to the repository, not
write access to production. Scope every MCP server’s credentials to the narrowest capability
that makes the task possible.
• Separate trusted from untrusted context. Treat any content the agent did not receive
directly from an authenticated human as data. Where an architecture must process untrusted
content, run that step in a session with no privileged tools attached.
• Human confirmation on irreversible actions. Merging, deploying, sending external email,
deleting, and spending money should require an explicit human approval step regardless of
how confident the agent is.
• Egress control. The classic injection payoff is exfiltration: instruct the agent to encode secrets
into a URL it then fetches. Restricting outbound network access from agent sandboxes to an
allowlist removes most of the value of a successful injection.
• Logging and replay. Every tool call an agent makes should be logged with its arguments, so
that an incident can be reconstructed. This is also the raw material for building the evaluation
set described in Section 7.5.
7.3 Data Leakage and IP Confidentiality
For an ER&D services firm, client IP exposure is the risk that ends contracts. Three distinct
exposures need separate controls. Training-corpus absorption is addressed by Zero Data
Retention contracting and by enterprise API tiers that contractually exclude inputs from training;
consumer tiers generally do not offer this and should be prohibited by policy for client work.
Context-window leakage occurs when a prompt assembled from multiple sources carries one
client’s data into a session serving another; this is an application architecture problem, solved
by per-client tenancy in the retrieval layer, not by the model vendor.Residency is a regulatory
rather than technical exposure, addressed by routing through Azure AI Foundry data zones,
AWS Bedrock regional endpoints, or equivalent, with the region chosen to satisfy the strictest
applicable clause in the client contract.
7.4 Sycophancy, Automation Bias, and Review Fatigue
Two human-side failure modes deserve explicit mention because they defeat otherwise sound
controls. Models trained on human preference data tend toward sycophancy: agreeing with
a stated position, validating a proposed design, and softening criticism, particularly when the
user signals confidence. An engineer who asks “this approach is correct, right?” will get a less
rigorous review than one who asks “what is wrong with this approach?”. Prompt conventions
that require the model to argue against a design are a cheap and effective countermeasure.
Automation bias is the reciprocal problem: reviewers approve machine output at a rate
that rises as the output’s historical accuracy rises, until review becomes nominal. A review step
that is always approved provides no protection. Sampling audits, where a random fraction of
Confidential: Internal Strategy Briefing 21 September 2026

## Page 23

The Complete Evolution of Frontier LLMs CHAPTER 7. FAILURE MODES, SECURITY , AND GOVERNANCE IN AGENTIC DEPLOYMENT
approved outputs is independently re-checked, are the standard control and should be budgeted
for explicitly rather than assumed.
7.5 Building an Internal Evaluation Set
The single highest-value engineering investment an ER&D firm can make in this area is a
private evaluation set drawn from its own work: several hundred real tasks with known-correct
outcomes, covering the firmware, CAE, documentation, and review workloads the firm actually
sells. Such a set is immune to the contamination problem described in Chapter 10, measures the
tasks that matter commercially rather than the tasks a benchmark author chose, and turns every
model release into a one-day procurement decision rather than a quarter-long debate. It is also
the only way to substantiate a capability claim to a client or an auditor.
Confidential: Internal Strategy Briefing 22 September 2026

## Page 24

CHAPTER 8
The Current Frontier (September 2026): GPT-6 Astra vs.
Claude Fable 5.1 / Mythos 5.1
8.1 Model Overviews
8.1.1 GPT-6 Astra
OpenAI released GPT -6 Astra on September 3, 2026, its flagship model for computer use, software
engineering, cybersecurity-adjacent work, and long-horizon agentic tasks. Verified specifications:
• Context window: 1,050,000 tokens (max input 922,000; max output 128,000 tokens).
• Knowledge cutoff: April 30, 2026.
• Reasoning effort levels: low, medium, high, xhigh, max.
• Standard pricing: $10 per million input tokens / $50 per million output tokens for requests
with input under 272,000 tokens; requests with input above 272,000 tokens bill the entire
request at a second tier ($20 input / $50–75 output depending on provider-reported figures,
with cached-read pricing roughly doubling as well). Cached input reads are discounted to
approximately $1 per million tokens at the standard tier.
• Modalities: text and image input, text output; tool support includes web search, file search,
code interpreter, hosted shell/computer use, and MCP.
• Cyber capability rating: OpenAI’s own Preparedness Framework rates Astra’s cybersecurity
capability as Critical, and the public API accordingly refuses vulnerability-discovery and
exploit-authoring requests; this capability is reserved for vetted enterprise security partners.
8.1.2 Claude Fable 5.1 and Claude Mythos 5.1
Anthropic’s flagship tier bifurcates into two models sharing one underlying checkpoint. Fable 5.1
is the safeguarded, generally available model; Mythos 5.1 removes certain safety classifiers and
is restricted to trusted partners (Project Glasswing) for defensive cybersecurity and biosecurity
research. Verified specifications for Fable 5.1:
• Context window: 1,000,000 tokens; maximum output 128,000 tokens.
• Standard pricing: $10 per million input tokens / $50 per million output tokens, matching
Astra’s standard-tier rate exactly .
• Cached input reads: approximately $0.25 per million tokens, notably cheaper than Astra’s
cached rate. Anthropic states this can cut total billed cost by roughly 25% for typical workloads
and up to roughly 45% for highly agentic, context-reuse-heavy workloads. Anthropic’s own
figures; independent validation against production workloads is limited.
Confidential: Internal Strategy Briefing 23 September 2026

## Page 25

The Complete Evolution of Frontier LLMs
CHAPTER 8. THE CURRENT FRONTIER (SEPTEMBER 2026): GPT -6 ASTRA VS. CLAUDE FABLE 5.1 /
MYTHOS 5.1
• Adaptive thinking is always enabled and cannot be fully disabled, unlike some earlier Claude
generations that allowed pure non-reasoning calls.
Corrected Timeline: The June 2026 Export-Control Suspension
Claude Fable 5 and Claude Mythos 5 (the 5.0 generation, predecessors to the 5.1
models discussed above) were first released on June 9, 2026. On June 12, 2026 ,
Anthropic suspended global access to both models to comply with a U.S. Department of
Commerce export-control directive. The Department lifted the relevant controls on
June 30, 2026, and Anthropic restored access on July 1, 2026 (Anthropic’s public
statement: anthropic.com/news/fable-mythos-access ). Multiple independent outlets
reported that the suspension followed the discovery of a technique capable of bypassing
a cybersecurity safeguard in Fable 5; the previous edition of this report additionally
attributed that discovery to a named researcher at a specific company , a detail that could
not be corroborated across independent sources and has accordingly been removed
rather than repeated. This episode is the concrete evidence behind this report’s recurring
recommendation that frontier-model access be treated as conditional infrastructure
subject to abrupt regulatory revocation, not a stable utility .
8.2 Rigorous, Sourced Benchmark Comparison
Benchmark GPT-6 Astra Claude Fable
5.1
Claude
Opus 5
Source / Notes
Terminal-Bench 4.0
(complex CLI/OS
automation)
57.9% 55.8% N/A OpenAI system card, self-
reported
OSWorld 2.0 (desk-
top GUI automa-
tion)
72.6% N/A N/A OpenAI system card, self-
reported
SWE-bench Verified
(software engineer-
ing)
N/A 95.0% (Fable
5)
N/A Anthropic, self-reported at
Fable 5 launch
SWE-bench Pro N/A 80.3% (Fable
5)
69.2%
(Opus 4.8)
Anthropic, self-reported
Artificial Analysis
Intelligence Index
v4.2 (9-benchmark
composite: GDPval-
AA v2, τ 3-Banking,
Terminal-Bench
v2.1, SciCode,
Humanity’s Last
Exam, GPQA Di-
amond, CritPt,
AA-Omniscience,
AA-LCR)
2nd place 1st place lower Artificial Analysis, inde-
pendent, Sept. 4, 2026
Confidential: Internal Strategy Briefing 24 September 2026

## Page 26

The Complete Evolution of Frontier LLMs
CHAPTER 8. THE CURRENT FRONTIER (SEPTEMBER 2026): GPT -6 ASTRA VS. CLAUDE FABLE 5.1 /
MYTHOS 5.1
Benchmark GPT-6 Astra Claude Fable
5.1
Claude
Opus 5
Source / Notes
GDP.pdf (4,592-
page multi-
document PDF
reasoning, 1,275
expert criteria)
33.2%
(leads)
lower N/A Artificial Analysis, inde-
pendent
Token efficiency on
agentic terminal
tasks
Highest
among
frontier
models
lower N/A Artificial Analysis, inde-
pendent
Table 8.1: All figures reproduced as reported by the cited source
at time of publication; “self-reported” figures have not been inde-
pendently re-run under identical scaffolding and should be treated
with corresponding caution.
KEY INSIGHT
The composite picture, once independent evaluation is weighed alongside vendor self-
reports, is a split decision, not an Astra sweep. On the independent Artificial Analysis
Intelligence Index, the closest available proxy for a broad, apples-to-apples capabil-
ity comparison, Claude Fable 5.1 leads GPT-6 Astra overall. GPT-6 Astra’s genuine,
independently-corroborated edge is token efficiency: it tends to reach a correct answer
using fewer generated tokens on agentic terminal/CLI tasks, which is exactly what drives
OpenAI’s own claim (see below) of a large effective cost advantage despite identical list
pricing. Astra also leads on the newly added GDP.pdf long-document, expert-criteria
benchmark and on OpenAI’s self-reported CAD/spatial-reasoning evaluations. Procure-
ment decisions should weight the independent composite index for general capability
and treat vendor-specific benchmarks (BenchCAD, Terminal-Bench self-reported figures)
as evidence for the specific task category they measure, not as a general capability
ranking.
Fact-Check: The “57.9% at 63% Lower Cost” Claim
OpenAI’s GPT-6 Astra launch materials state that on Terminal-Bench 4.0, Astra scores 57.9%
versus Claude Fable 5.1’s 55.8%, while achieving this at an approximately 63% lower estimated
API cost per completed task. Because both models are listed at identical $10/$50 per million-
token rates, this cost gap is not a pricing difference. It is a claim about token efficiency: Astra is
claimed to require substantially fewer generated (billed) tokens to solve the same terminal task.
This is a verified, correctly-quoted vendor claim originating from OpenAI’s own launch materials.
It has not been independently re-validated against production token-usage distributions by a
third party , and should be presented as OpenAI’s claim, not as an independently confirmed fact.
Confidential: Internal Strategy Briefing 25 September 2026

## Page 27

The Complete Evolution of Frontier LLMs
CHAPTER 8. THE CURRENT FRONTIER (SEPTEMBER 2026): GPT -6 ASTRA VS. CLAUDE FABLE 5.1 /
MYTHOS 5.1
8.3 Corrected Pricing Table
Model Input (/1M) Output (/1M) Cached Context
GPT-6 Astra (standard tier,≤272K
input)
$10.00 $50.00 ≈$1.00 1.05M
GPT-6 Astra (long-context tier,
>272K input)
$20.00 ≈$50–75 ≈$2.00 1.05M
Claude Fable 5.1 / Mythos 5.1 $10.00 $50.00 ≈$0.25 1.0M
Claude Opus 5 $5.00 $25.00 n/a 200K
GPT-5.6 Sol $4.00 $20.00 n/a 1M
GPT-5.6 Luna $0.20 $1.20 n/a varies
Claude Sonnet 5 $2.00 $10.00 n/a 1M
Claude Haiku 4.5 $1.00 $5.00 n/a 200K
Table 8.2: Corrected pricing table (replaces the malformed table in the prior edition). Figures
verified against provider pricing pages and third-party pricing trackers as of September 2026;
treat as a snapshot, not a live price. Confirm against the provider’s pricing page before budgeting.
Confidential: Internal Strategy Briefing 26 September 2026

## Page 28

CHAPTER 9
Architecture and Training: Deep-Dive Reference Tables
9.1 Parameter Count and Architecture Trends
Year Model Architecture Parameter Count Status
2019 GPT-2 Dense 1.5 Billion Officially confirmed
2020 GPT-3 Dense 175 Billion Officially confirmed
2023 GPT-4 Mixture-of-
Experts
∼1.8 Trillion
(16×111B)
Community estimate
/ leaked
2024 Claude 3 family Mixture-of-
Experts (be-
lieved)
Undisclosed Unconfirmed
2025 DeepSeek-
V3/R1
MoE + Multi-
head Latent At-
tention
671B total / 37B
active
Officially confirmed
(open weights)
2026 GPT-6 Astra “Looped trans-
formers” /
recurrent depth
Undisclosed
(>100k GPU train-
ing cluster)
Unconfirmed
Table 9.1: DeepSeek-V3/R1’s officially confirmed active-parameter figure (37B active out of 671B
total) is included as a rare, independently verifiable data point in an era where frontier labs
otherwise withhold parameter counts.
9.2 Context Window Growth
Year Model lineage Context window size
2019 GPT-2 1,024 tokens
2020 GPT-3 2,048 tokens
2023 GPT-4 / Claude 2 8,192–32,768 / 100,000 tokens
2024 GPT-4 Turbo / Claude 3 128,000 / 200,000 tokens
2026 GPT-6 Astra / Claude Fable
5.1
1,050,000 / 1,000,000 tokens
Confidential: Internal Strategy Briefing 27 September 2026

## Page 29

The Complete Evolution of Frontier LLMs CHAPTER 9. ARCHITECTURE AND TRAINING: DEEP-DIVE REFERENCE TABLES
9.3 Inference Cost Trends (Flagship Tier)
Year Flagship model Input (/1M) Output (/1M)
2023 GPT-4 (8K) $30.00 $60.00
2024 Claude 3 Opus / GPT-4 Turbo $15.00 $60.00 to $75.00
2025 Claude 4.5 Opus / GPT-5 $5.00 $25.00
2026 GPT-5.6 Sol / Claude Opus 5 $4.00 to $5.00 $20.00 to $25.00
2026 GPT-6 Astra / Claude Fable 5.1
(premium reasoning tier)
$10.00 $50.00
While the ultra-premium reasoning tier (Astra / Fable 5.1) sits at $10/$50, the standard enter-
prise baseline has compressed from roughly $30/$60 in 2023 to roughly $4/$20 in 2026, an
approximately 85% real-terms reduction at the mid tier, delivered alongside substantially higher
capability. The premium tier’s flat price is best understood not as the industry getting more
expensive, but as a new, separate SKU for maximum-capability reasoning workloads, priced
independently of the mid-tier trend.
9.4 Post-Training Pipeline Evolution
1. SFT→ RLHF (2021–2022). Human contractors write demonstrations and rank outputs;
PPO optimizes against a learned reward model. High alignment fidelity, poor cost/labeling
scalability .
2. RLAIF and Constitutional AI (2023–2024). AI evaluators replace human raters against an
explicit rule set, removing the human-labeling bottleneck and humans’ exposure to harmful
content during grading.
3. RL for reasoning (2024–2025). Reward signal moves from grading the conversational style
of a response to grading the correctness of a multi-step reasoning trace, via Process Reward
Models and, with DeepSeek’s GRPO, group-relative rule-based rewards that avoid a separate
learned value network entirely .
4. Generative verification (2026). Current pipelines increasingly have the model synthesize
code or a proof for its own intermediate claims, execute or check it in a sandbox, and use the
result as a verification signal before finalizing a response, automating the self-correction loop
that earlier generations relied on human or PRM feedback for.
9.5 Inference-Time Efficiency: Quantization and Speculative Decoding
Two further techniques matter for the unit economics discussed throughout this report, indepen-
dent of any single model’s architecture:
• Quantization reduces the numerical precision used to store and compute model weights (e.g.
from 16-bit to 8-bit or 4-bit representations, via methods such as GPTQ or AWQ), cutting
memory footprint and often increasing throughput, at a small, workload-dependent accuracy
cost. This is central to how smaller, cheaper model tiers (Haiku, Luna-class models) achieve
their aggressive per-token pricing.
Confidential: Internal Strategy Briefing 28 September 2026

## Page 30

The Complete Evolution of Frontier LLMs CHAPTER 9. ARCHITECTURE AND TRAINING: DEEP-DIVE REFERENCE TABLES
• Speculative decoding uses a small, fast “draft” model to propose several tokens ahead, which
the large target model then verifies in a single parallel pass, accepting the draft tokens that
match what it would have generated itself. Because verification is cheaper than sequential
generation, this can materially reduce end-to-end latency for the large model without changing
its output distribution, and is widely deployed in production serving stacks for reasoning-heavy
models where output length (and therefore sequential decoding steps) is the main latency
driver.
Confidential: Internal Strategy Briefing 29 September 2026

## Page 31

CHAPTER 10
Benchmark Integrity and Evaluation Methodology
This chapter is new to this edition, added because a technically complete picture of “which model
is better” is inseparable from understanding how these benchmark numbers are produced and
what their limitations are.
10.1 Self-Reported vs. Independent Evaluation
Most headline benchmark figures released alongside a new model, including several cited in
Chapter 8, are self-reported by the vendor in its own system card, under scaffolding (tool access,
prompting strategy, number of retries) the vendor controls and does not always fully disclose.
This does not make the figures false, but it does mean two vendors’ self-reported numbers on
the “same” benchmark are not automatically apples-to-apples, since minor variations in harness,
retry budget, or tool access can shift scores by several points. Independent evaluators such as
Artificial Analysis, METR, and academic groups running open benchmark harnesses apply a fixed
scaffold across all models, which is why this report weights the Artificial Analysis Intelligence
Index more heavily for general capability comparison than any single vendor’s launch-day claim.
10.2 Benchmark Contamination
Large pretraining corpora scrape enormous fractions of the public internet, which increasingly
includes prior benchmark questions and their answers, discussion of benchmark methodology ,
and even leaked test sets. A model can score well on a benchmark partly because it memorized
elements of that benchmark during pretraining, rather than because it possesses the underlying
capability the benchmark was designed to measure. Reputable evaluators mitigate this by holding
out a meaningful fraction of their test items as private, never published, and rotating them over
time; Artificial Analysis’s Intelligence Index v4.2, for instance, raised its private item share from
roughly 20% to roughly 40% specifically to counter benchmark gaming as contamination risk
grew across the industry .
10.3 METR Time Horizons
METR (a nonprofit AI evaluation organization) measures autonomous capability via a task-
completion time horizon: the length of task (measured in estimated human completion time)
at which a given model succeeds with a specified reliability threshold (e.g. 50%). METR’s data
shows this horizon roughly doubling every seven months across the 2023–2026 period. This
metric is a genuinely useful proxy for autonomous capability trends, but its translation into
real-world economic labor displacement is contested: human baseline times are estimated rather
than measured for every task, task selection may not represent the distribution of real workplace
tasks, and “50% reliability at time X” is a very different practical guarantee than the near-100%
reliability most production engineering workflows require.
Confidential: Internal Strategy Briefing 30 September 2026

## Page 32

The Complete Evolution of Frontier LLMs CHAPTER 10. BENCHMARK INTEGRITY AND EVALUATION METHODOLOGY
10.4 Practical Guidance for Reading Any Benchmark Claim in This Report
• Prefer a benchmark run by an evaluator with no commercial stake in the outcome.
• Treat any single-benchmark claim (“57.9% on Terminal-Bench 4.0”) as evidence about that
specific task category , not a general capability ranking.
• Where a vendor claims a large cost or efficiency advantage at identical list pricing (as with
Astra’s 63% claim in Chapter 8), understand this as a token-efficiency claim, and verify it
against your own production workload before budgeting against it.
• Weight composite indices (Artificial Analysis Intelligence Index) more heavily than any single
narrow benchmark for general-purpose model selection, and weight task-specific benchmarks
(BenchCAD, SWE-bench) more heavily when the procurement decision is for that specific task
category .
Confidential: Internal Strategy Briefing 31 September 2026

## Page 33

CHAPTER 11
Open-Weight Models and Sovereign Fallback
The June 2026 suspension established that access to a frontier model is a permission, not a
purchase. Any workflow whose interruption would breach a client commitment therefore needs
a fallback that does not depend on a single vendor’s continued willingness or legal ability to
serve it. This chapter is new to this edition and exists because the prior draft identified the
export-control risk without proposing a mitigation.
11.1 The Open-Weight Tier
A parallel ecosystem of open-weight models, whose parameters are downloadable and can be
run on infrastructure the operator controls, has tracked roughly 6 to 12 months behind the
closed frontier since 2024. The DeepSeek line (V3 and R1, with a confirmed 671B total and 37B
active parameter Mixture-of-Experts architecture), Meta’s Llama family , Alibaba’s Qwen line, and
Mistral’s releases are the significant entries. These models do not match Astra or Fable 5.1 on the
hardest reasoning tasks, and for a firm selling frontier capability that gap matters. For continuity ,
compliance, and cost-floor purposes, it matters much less.
11.2 What Self-Hosting Actually Buys
• Access continuity. Weights already downloaded cannot be revoked by a directive. This is the
direct answer to the export-control exposure.
• Absolute data residency. Inference on infrastructure the firm controls removes the ven-
dor from the trust boundary entirely, which is the strongest position available for defence,
aerospace, and certain medical device work.
• Fine-tuning rights. The firm can adapt a model to its own domain (RTOS idioms, a client’s
coding standard, a specific CAE toolchain’s output format) in ways closed APIs do not permit.
• A cost floor. At sufficient sustained volume, amortised GPU cost per token falls below API
pricing. The crossover point depends heavily on utilisation and is often further away than it
first appears.
11.3 What It Costs
Self-hosting replaces a variable API bill with fixed capital and operating costs, plus an engineer-
ing burden that is routinely underestimated. A serving stack must handle batching, KV-cache
management, quantisation, speculative decoding, autoscaling, and observability; this is a stand-
ing platform-engineering commitment, not a deployment. Hardware is capital-intensive and
depreciates against a rapidly moving frontier. Model quality must be re-validated on the firm’s
own evaluation set at every upgrade, since open-weight releases carry no vendor capability
guarantees.
Confidential: Internal Strategy Briefing 32 September 2026

## Page 34

The Complete Evolution of Frontier LLMs CHAPTER 11. OPEN-WEIGHT MODELS AND SOVEREIGN FALLBACK
KEY INSIGHT
The realistic posture for an ER&D firm is neither pure API consumption nor full self-
hosting, but a deliberate two-tier architecture: frontier APIs for the work that genuinely
needs frontier capability, and a maintained, tested open-weight deployment covering
the subset of workloads that are either continuity-critical or residency-constrained. The
essential discipline is that the fallback must be exercised, not merely provisioned. A
failover path that has never carried production traffic will not work on the day it is
needed.
11.4 Distillation as the Bridge
The most economically interesting use of the open tier is not as a replacement for frontier models
but as their output. A frontier model generates high-quality solutions for a narrow, repetitive
task; those solutions are verified against a deterministic oracle; the verified trajectories fine-tune
a much smaller open-weight model that then serves the task at a fraction of the cost. This is the
same synthetic-data pipeline the frontier labs use internally , applied at firm scale, and it is where
an ER&D firm’s proprietary domain data creates defensible advantage. The output is a small
model that is better than any general-purpose frontier model at one narrow thing the firm sells
repeatedly .
Confidential: Internal Strategy Briefing 33 September 2026

## Page 35

CHAPTER 12
Practical Guidance: Which Model, When
12.1 Task-Type to Model Mapping
Task Type Recommended
Model
Reasoning
Long-document anal-
ysis (standards, con-
tracts)
Claude Sonnet 5 At $2/$10 pricing, its 1M context handles large
engineering documents economically , with his-
torically strong recall and lower hallucination
rates on complex PDF ingestion.
Agentic coding & ma-
jor codebase refactors
Claude Opus 5 Strong long-horizon autonomous coding perfor-
mance at roughly half the cost of Fable 5.1 or
Astra ($5/$25).
Cost-sensitive, high-
volume classification
GPT-5.6 Luna /
Claude Haiku 4.5
Luna’s sub-$1/$2-class pricing makes high-
volume routing tasks effectively negligible in
cost; Haiku often yields faster time-to-first-token
latency .
Computer-use automa-
tion & GUI testing
GPT-6 Astra Strong on OSWorld 2.0 and Terminal-Bench;
handles OS/browser QA robustly via native
agentic tool pathways.
General-purpose agen-
tic reasoning at fron-
tier capability
Claude Fable 5.1 Leads the independent Artificial Analysis Intel-
ligence Index; best default choice when the
task category is not narrowly CAD/spatial or
terminal-automation specific.
Cybersecurity & pene-
tration testing (autho-
rized)
Claude Mythos 5.1
(or GPT-6 Astra Day-
break tier)
Both provide unrestricted cyber capability
strictly to vetted, enrolled partners; the stan-
dard public APIs of both vendors refuse this
category by design.
CAD & complex spatial
engineering
GPT-6 Astra Reports the strongest self-reported score on
OpenAI’s BenchCAD 3D-reconstruction-to-CAD-
code evaluation; treat as a vendor claim pending
independent replication.
Table 12.1: Task-to-model routing table.
Confidential: Internal Strategy Briefing 34 September 2026

## Page 36

The Complete Evolution of Frontier LLMs CHAPTER 12. PRACTICAL GUIDANCE: WHICH MODEL, WHEN
12.2 Pros and Cons: GPT-6 Astra vs. Claude Fable 5.1 / Opus 5
GPT-6 Astra: $10/$50 per million tokens
Strengths: Strong token efficiency on agentic terminal tasks; leads OpenAI’s self-reported
CAD/spatial benchmarks; leads the independent GDP.pdf long-document benchmark;
Batch/Flex pricing can roughly halve standard rates for non-urgent workloads.
Weaknesses: The “looped transformer” / recurrent-depth architecture obscures inter-
mediate reasoning steps, limiting auditability for compliance-heavy engineering use
cases; Critical-tier cybersecurity restrictions trigger refusals on legitimate edge-case engi-
neering security work outside the Daybreak partner tier; trails Claude Fable 5.1 on the
independent, composite Artificial Analysis Intelligence Index as of September 2026.
Claude Fable 5.1 ($10/$50) & Opus 5 ($5/$25)
Strengths: Leads the independent Artificial Analysis Intelligence Index v4.2; the Model
Context Protocol is the best-established open standard for enterprise tool integration;
exposed reasoning tokens support auditability for functional-safety and compliance
documentation; Opus 5 delivers a large share of flagship capability at roughly half Astra’s
cost. Cheaper cached-token pricing (~$0.25/M vs. Astra’s ~$1/M) benefits agentic,
context-reuse-heavy workloads specifically .
Weaknesses: Carries demonstrated export-control risk. The June 2026 suspension
showed U.S. government action can remove global API access to the entire Fable/Mythos
line with days’ notice; safeguards can be overly broad for legitimate defensive-security or
biomedical engineering work unless the user is specifically enrolled in the Mythos tier;
trails GPT-6 Astra on the specific CAD/spatial and long-document benchmarks where
Astra leads.
12.3 Business-Lens Takeaways
Buying the single largest model as a blanket default is no longer a coherent baseline strategy.
Because inference-time reasoning means cost tracks the compute a query actually consumes,
the routing architecture, meaning which task goes to which model tier at what reasoning-effort
setting, is the product decision, not a detail beneath it. Training foundation models from scratch
remains entirely uneconomical for an ER&D services firm; durable competitive advantage lies
in building proprietary tool integrations via MCP and in generating highly specific synthetic
evaluation and fine-tuning data for the narrow tasks (boundary conditions for CFD, firmware
register semantics, RBI-style regulatory test cases) that no general-purpose frontier model will
ever be separately optimized for.
Confidential: Internal Strategy Briefing 35 September 2026

## Page 37

CHAPTER 13
LTTS-Specific Use-Case Mapping
Given LTTS’s core ER&D business across Mobility, Sustainability, and Tech segments, client
intellectual-property confidentiality is paramount. Models should be deployed exclusively via
Zero Data Retention enterprise agreements, Microsoft Azure AI Foundry, or AWS Bedrock
VPC architectures, so that client proprietary designs are never absorbed into a vendor’s future
pretraining corpus.
13.1 Mobility Segment
For automotive and aerospace CAE, CAD layout, and simulation review, GPT-6 Astra is the
stronger current choice given its lead on spatial/CAD-adjacent evaluations, deployed via an
Azure Foundry US Data Zone for aerospace export-control compliance; its premium pricing makes
it poorly suited to batch-processing thousands of routine simulation states, where a cheaper tier
should be substituted. For embedded C/C++/RTOS and software-defined-vehicle platform work
(e.g. LTTS’s iDriVe framework),Claude Opus 5 is the better fit given its agentic coding strength
and MCP-native integration with Git and RTOS build systems, with the standing caveat that any
model in this class can hallucinate plausible-looking but non-existent POSIX/hardware interrupt
flags, so generated firmware code requires deterministic build/test verification, not just review.
For ISO 26262 functional-safety documentation, Claude Sonnet 5 offers strong cost-efficiency
($2/$10) with low hallucination rates on large text volumes and exposed reasoning tokens that
support audit trails, though it lacks Astra’s abstraction strength on genuinely novel edge-case
safety failure modes.
13.2 Sustainability Segment
For plant/process engineering and digital-oilfield data analysis, Claude Sonnet 5 is the stronger
default, given strength on unstructured PDF and tabular utility data at low latency and cost;
its vision encoder is occasionally weaker than Astra’s at resolving minute topological detail in
P&ID diagrams. Sensor data from digital oilfields may embed critical-infrastructure location
information, so Anthropic’s enterprise data-retention controls should be configured explicitly
rather than assumed. For CFD result interpretation and ESG reporting, GPT-6 Astra is the
stronger choice for synthesizing technical physics reports and generating accurate plots from
scientific data; its relative verbosity can dilute the specific formatting some ESG regulatory bodies
require, and proprietary fluid-flow geometries should be sanitized before being routed to any
external API regardless of vendor.
13.3 Tech Segment
For VLSI/semiconductor-adjacent design tasks (Verilog/VHDL, PCB layout via KiCad-style work-
flows), GPT-6 Astra demonstrates strong schematic and layout understanding; because low-level
register optimization can trigger false-positive hardware-tampering safeguards, and semiconduc-
Confidential: Internal Strategy Briefing 36 September 2026

## Page 38

The Complete Evolution of Frontier LLMs CHAPTER 13. LTTS-SPECIFIC USE-CASE MAPPING
tor client IP is especially sensitive, strict Zero Data Retention contracting via Azure is mandatory .
For MedTech regulatory documentation (FDA/CE),Claude Fable 5.1 is the stronger fit given
Anthropic’s emphasis on verifiable, auditable reasoning over creative extrapolation; costs are
high, and safety filters may occasionally trigger on benign medical-device-malfunction hypo-
theticals, so review workflows should anticipate some false-refusal handling. For infrastructure,
cloud, and cybersecurity workflows, the choice bifurcates between GPT-6 Astra (Daybreak
tier) and Claude Mythos 5.1, both requiring formal enrollment in the relevant vetted-partner
program; the standard public APIs of both vendors will refuse advanced offensive-security tasks
by design, and no live infrastructure credentials should ever be placed in a model’s context
window regardless of tier.
13.4 Cost Modelling: A Worked Example
Model pricing is quoted per token, but budgets are set per seat and per project. The bridge
between them is a small number of assumptions that should be stated explicitly rather than
buried. The illustration below uses an engineering copilot deployment; the arithmetic, not the
figures, is the transferable part.
Assumption Value Note
Engineers with active access 500 Pilot cohort, not total head-
count
Working days per year 220
Sessions per engineer per day 8 Observed copilot usage clus-
ters at 5 to 12
Input tokens per session (incl. retrieved con-
text)
25,000 Dominated by retrieved code
and documents
Output tokens per session 2,000 Reasoning models push this
higher
Cache hit rate on input 60% Realistic with a stable system
prompt and warm context
Annual input tokens 22.0 billion 500× 220× 8× 25,000
Annual output tokens 1.76 billion
Cost on Claude Sonnet 5 ($2/$10) ≈$61,600/yr Before caching
with 60% cache hits ≈$37,800/yr About $76 per engineer per
year
Cost on Claude Fable 5.1 ($10/$50) ≈$308,000/yr Five times the volume cost
Table 13.1: Illustrative cost model. Figures are arithmetic from stated assumptions, not observed
LTTS data.
Three conclusions follow, and they are robust to large changes in the assumptions. First,
input tokens dominate, because retrieval fills the context window while outputs stay short;
retrieval discipline, not output brevity, is the main cost lever. Second, prompt caching is
the highest-return engineering optimisation available, which is also why the cached-read
price gap noted in Chapter 8 (roughly $0.25 per million on Fable 5.1 against roughly $1.00 on
Astra) matters more than the identical headline rates suggest. Third, tier selection dominates
everything else: routing the same workload to a flagship rather than a mid-tier model is a
Confidential: Internal Strategy Briefing 37 September 2026

## Page 39

The Complete Evolution of Frontier LLMs CHAPTER 13. LTTS-SPECIFIC USE-CASE MAPPING
five-fold cost difference, which is the entire argument for the routing architecture recommended
throughout this report.
13.5 A 90-Day Adoption Sequence
Phase Activity Exit criterion
Days 1–30 Stand up the internal evaluation set
(Section 7.5). Select 200 to 300
real tasks across firmware, CAE, doc-
umentation, and review. Execute
ZDR contracting.
A measured baseline for two or three can-
didate models on LTTS work, not on public
benchmarks.
Days 31–60 Build two or three MCP servers
against the highest-traffic internal
tools. Deploy a copilot to one pilot
cohort with logging and egress con-
trol in place.
Tool calls logged and replayable; a mea-
sured cache hit rate; zero privileged-tool
sessions processing untrusted content.
Days 61–90 Introduce routing: mid-tier by de-
fault, flagship on escalation. Run
the first sampling audit. Provi-
sion and exercise the open-weight
fallback for one continuity-critical
workload.
A cost-per-task figure, an audited accuracy
figure, and a failover that has carried real
traffic.
Table 13.2: Sequenced so that measurement precedes scale.
13.6 Risk Register
Risk Severity Primary control
Client IP absorbed into
vendor training
Critical ZDR contracting; enterprise tiers only; consumer tiers
prohibited by policy for client work
Prompt injection via un-
trusted content
Critical Least-privilege tool scoping; egress allowlists; no privi-
leged tools in sessions processing untrusted input
Export-control or regu-
latory access loss
High Maintained and exercised open-weight fallback (Chap-
ter 11); second-vendor capability for critical paths
Hallucinated engineer-
ing artefacts reaching
deliverables
High Deterministic verification (compile, test, dimension
check); sign-off scaled to consequence
Automation bias erod-
ing review quality
Medium Budgeted sampling audits of approved output
Cost overrun from tier
misrouting
Medium Default-to-mid-tier routing; per-project token budgets;
cache hit rate monitoring
Cross-client context
leakage
High Per-client tenancy in the retrieval layer; no shared vector
stores across engagements
Table 13.3: Controls are stated as architecture, not as model behaviour, because model behaviour
is not a security boundary .
Confidential: Internal Strategy Briefing 38 September 2026

## Page 40

The Complete Evolution of Frontier LLMs CHAPTER 13. LTTS-SPECIFIC USE-CASE MAPPING
13.7 Cross-Cutting Horizontal Use Cases
For digital-twin data synthesis,Claude Opus 5 is well suited to maintaining consistent formatting
and logic across long output streams for synthetic simulation-support data, though $25/M output
pricing is expensive at the row-count scale digital twins require, favoring a ring-fenced, internally-
hosted deployment for bulk generation. For internal knowledge-base copilot use across LTTS’s
innovation labs, Claude Sonnet 5 balances $2/$10 pricing against strong MCP-native integration
into internal knowledge bases, with data training opt-outs explicitly toggled under an AWS
Bedrock deployment. For RFP and proposal drafting support, GPT-5.6 Luna or Claude Haiku
4.5 offer fast, cheap boilerplate generation suitable for a first draft that a human then edits,
provided commercial pricing data is sanitized before it is sent to any external API.
Confidential: Internal Strategy Briefing 39 September 2026

## Page 41

CHAPTER 14
Confidence, Caveats, and Corrections
This section documents unverified claims, vendor-marketing assertions, and areas of genuine
analytical uncertainty , and records what this edition changed relative to the prior draft.
14.1 Unverified or Vendor-Sourced Claims Carried Forward
• GPT-6 Astra’s Terminal-Bench cost claim.The 57.9%-at-63%-lower-cost figure is sourced
directly from OpenAI’s own launch materials and has not been independently re-run under
identical scaffolding.
• GPT-4’s parameter count. The 1.8-trillion, 16×111B MoE figure is industry consensus derived
from leaks and analyst estimates; OpenAI has never officially confirmed it.
• o1/o3/Astra internal search mechanics. Community speculation about MCTS-like search
during inference-time reasoning is a plausible hypothesis, not a documented fact; none of
OpenAI’s public materials confirm the specific algorithm.
• “Looped transformers” / recurrent depth. OpenAI’s own characterization of Astra’s archi-
tecture; the precise mathematical formulation has not been published in a peer-reviewed
setting.
• Claude Mythos vulnerability-discovery claims. Anthropic’s claim that Mythos found vulner-
abilities across “every major operating system” in internal testing appears only in promotional
materials and has not been independently corroborated by external security researchers.
14.2 Corrections Applied in This Edition
Summary of Changes from the Prior Draft
1. Replaced SEO/content-aggregator citations with primary sources (OpenAI system
cards and pricing pages, Anthropic newsroom and pricing pages, Artificial Analysis,
METR) wherever a primary source could be located.
2. Rebuilt the malformed cost table in Part 7 with clean input/output/cached-price
columns and explicit tiered-pricing notes.
3. Rebalanced the GPT-6 Astra vs. Claude Fable 5.1 narrative to state plainly , next to the
relevant claim rather than only in an appendix, that Fable 5.1 leads the independent
Artificial Analysis Intelligence Index while Astra leads on token efficiency and specific
spatial/long-document benchmarks.
4. Corrected the export-control timeline to the dates Anthropic itself has confirmed
(suspended June 12, controls lifted June 30, access restored July 1, 2026) and
Confidential: Internal Strategy Briefing 40 September 2026

## Page 42

The Complete Evolution of Frontier LLMs CHAPTER 14. CONFIDENCE, CAVEATS, AND CORRECTIONS
removed an uncorroborated attribution of the triggering discovery to a specific
researcher at a named company .
5. Added new chapters on benchmark integrity , agentic failure modes and security , and
open-weight sovereign fallback, plus a glossary , a cost model, an adoption sequence,
and a risk register, and substantially expanded the technical treatment of attention
mechanisms, MoE routing, RLHF/Constitutional AI objectives, GRPO, and inference-
time efficiency techniques throughout.
Confidential: Internal Strategy Briefing 41 September 2026

## Page 43

CHAPTER 15
Glossary
Agent
A model configured to take actions through tools across multiple turns, rather than only producing
text.
ALiBi
Attention with Linear Biases. Positional scheme that penalises attention by token distance,
enabling length extrapolation.
Attention
Mechanism computing a weighted sum of value vectors, weighted by query-key similarity .
Chinchilla scaling
The 2022 finding that parameters and training tokens should scale equally, roughly 20 tokens
per parameter.
Constitutional AI
Anthropic’s alignment method in which a written set of principles, applied by an AI evaluator,
replaces most human preference labelling.
Context window
Maximum tokens a model can attend to in one request, covering prompt, retrieved content,
reasoning, and output.
Distillation
Training a smaller model on a larger model’s verified outputs to approximate its capability at
lower cost.
FlashAttention
IO-aware exact attention algorithm that tiles computation into on-chip SRAM, avoiding material-
ising the full attention matrix.
GQA / MQA
Grouped-Query and Multi-Query Attention. Share key/value heads across query heads to shrink
the KV cache.
GRPO
Group Relative Policy Optimization. DeepSeek’s PPO variant that uses a sampled group’s own
mean as the baseline, removing the separate critic network.
Hallucination
Fluent, confident output not grounded in fact or source material.
In-context learning
Performing a new task from examples in the prompt, with no weight update.
Confidential: Internal Strategy Briefing 42 September 2026

## Page 44

The Complete Evolution of Frontier LLMs CHAPTER 15. GLOSSARY
KV cache
Stored key/value tensors for prior tokens, reused during generation. Usually the dominant
memory cost at long context.
MCP
Model Context Protocol. Open JSON-RPC standard connecting models to external tools, re-
sources, and prompts.
MLA
Multi-head Latent Attention. Compresses cached keys and values into a low-rank latent, cutting
KV-cache memory substantially .
MoE
Mixture-of-Experts. Sparse architecture routing each token to a small subset of expert sub-
networks, decoupling total parameters from active compute.
ORM / PRM
Outcome and Process Reward Models. ORMs score only the final answer; PRMs score each
intermediate reasoning step.
PPO
Proximal Policy Optimization. The reinforcement learning algorithm underlying standard RLHF.
Prompt caching
Reusing computation for a repeated prompt prefix, billed at a steep discount. The main cost
lever in retrieval-heavy workloads.
Prompt injection
Attack in which instructions embedded in content a model reads are executed as if issued by the
user.
Quantisation
Reducing numerical precision of weights and activations to cut memory and increase throughput,
at some accuracy cost.
RAG
Retrieval-Augmented Generation. Retrieving relevant documents and placing them in context
before generating.
RLHF / RLAIF
Reinforcement Learning from Human, or AI, Feedback.
RoPE
Rotary Position Embedding. Encodes position by rotating query and key vectors so attention
scores depend on relative offset.
Speculative decoding
Using a small draft model to propose tokens that the large model verifies in parallel, cutting
latency without changing output.
Test-time compute
Compute spent reasoning at inference rather than during training. The dominant scaling axis
since late 2024.
Confidential: Internal Strategy Briefing 43 September 2026

## Page 45

The Complete Evolution of Frontier LLMs CHAPTER 15. GLOSSARY
Token
The discrete unit of text a model processes, produced by byte-pair encoding or similar. Roughly
0.75 English words on average.
Transformer
The 2017 architecture, based entirely on self-attention, underlying all frontier models discussed
here.
ZDR
Zero Data Retention. Contractual commitment that inputs are neither stored nor used for
training.
Confidential: Internal Strategy Briefing 44 September 2026

## Page 46

CHAPTER 16
Sources
16.1 Sourcing Policy for This Edition
The prior edition drew a meaningful fraction of its citations from SEO and content-aggregator
blogs. The underlying figures largely checked out, but citing an aggregator for a number that
originates in an OpenAI system card or an Anthropic pricing page undermines the document’s
credibility the moment a reader clicks through. This edition applies three rules:
1. Cite the primary publisher of a figure (the lab’s own announcement, system card, pricing
page, or the independent evaluator’s own site), not a blog paraphrasing it.
2. Where a claim rests on a peer-reviewed or preprint paper, cite the paper (arXiv identifier),
not a tutorial explaining it.
3. Where only a secondary source exists for a claim, either drop the claim or state explicitly
in-text that it is uncorroborated. Several claims in the prior edition were dropped under this
rule, most notably the specific attribution of the June 2026 safeguard-bypass discovery .
16.2 Foundational Papers (Primary)
1. Vaswani et al., Attention Is All You Need, arXiv:1706.03762 (2017).
2. Radford et al., Language Models are Unsupervised Multitask Learners (GPT-2 technical report,
OpenAI, 2019).
3. Brown et al., Language Models are Few-Shot Learners (GPT-3), arXiv:2005.14165 (2020).
4. Kaplan et al., Scaling Laws for Neural Language Models, arXiv:2001.08361 (2020).
5. Hoffmann et al., Training Compute-Optimal Large Language Models (Chinchilla),
arXiv:2203.15556 (2022).
6. Ouyang et al., Training Language Models to Follow Instructions with Human Feedback (Instruct-
GPT), arXiv:2203.02155 (2022).
7. Schulman et al., Proximal Policy Optimization Algorithms, arXiv:1707.06347 (2017).
8. Bai et al., Constitutional AI: Harmlessness from AI Feedback, arXiv:2212.08073 (Anthropic,
2022).
9. Lee et al., RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback ,
arXiv:2309.00267 (2023).
10. Lightman et al., Let’s Verify Step by Step (process supervision / PRMs), arXiv:2305.20050
(OpenAI, 2023).
11. Wang et al., Self-Consistency Improves Chain of Thought Reasoning in Language Models ,
arXiv:2203.11171 (2022).
Confidential: Internal Strategy Briefing 45 September 2026

## Page 47

The Complete Evolution of Frontier LLMs CHAPTER 16. SOURCES
16.3 Attention and Efficiency (Primary)
12. Dao et al., FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness ,
arXiv:2205.14135 (2022).
13. Press et al., Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapola-
tion (ALiBi), arXiv:2108.12409 (2021).
14. Su et al., RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE),
arXiv:2104.09864 (2021).
15. Shazeer, Fast Transformer Decoding: One Write-Head is All You Need(Multi-Query Attention),
arXiv:1911.02150 (2019).
16. Ainslie et al., GQA: Training Generalized Multi-Query Transformer Models from Multi-Head
Checkpoints, arXiv:2305.13245 (2023).
17. Liu et al., Ring Attention with Blockwise Transformers for Near-Infinite Context ,
arXiv:2310.01889 (2023).
18. Shazeer et al., Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts
Layer, arXiv:1701.06538 (2017).
19. Fedus et al., Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient
Sparsity, arXiv:2101.03961 (2021).
20. Leviathan et al., Fast Inference from Transformers via Speculative Decoding, arXiv:2211.17192
(2022).
21. Frantar et al., GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transform-
ers, arXiv:2210.17323 (2022).
22. DeepSeek-AI, DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement
Learning (GRPO), arXiv:2501.12948 (2025).
23. DeepSeek-AI, DeepSeek-V3 Technical Report(Multi-head Latent Attention, MoE architecture,
confirmed 671B total / 37B active parameters), arXiv:2412.19437 (2024).
16.4 Vendor Primary Sources (Announcements, System Cards, Pricing)
24. OpenAI, GPT-6 Astra launch announcement and system card: https://openai.com/index/g
pt-6-astra/ . Source of the Terminal-Bench 4.0 (57.9%), OSWorld 2.0 (72.6%), BenchCAD,
and “63% lower estimated API cost per task” claims. All self-reported.
25. OpenAI, API model and pricing documentation: https://developers.openai.com/api/
docs/pricing . Source of $10/$50 standard-tier pricing, the 272K-token tier threshold,
cached-read pricing, and Batch discount.
26. OpenAI, Preparedness Framework and deployment safety materials: https://deployment
safety.openai.com/ . Source of Astra’s “Critical” cybersecurity capability rating and the
corresponding public-API restrictions.
27. Anthropic, Claude Fable 5 / Mythos 5 launch announcement: https://www.anthropic.com/
news/ . Source of Fable 5’s SWE-bench Verified (95.0%) and SWE-bench Pro (80.3%) figures.
Self-reported.
Confidential: Internal Strategy Briefing 46 September 2026

## Page 48

The Complete Evolution of Frontier LLMs CHAPTER 16. SOURCES
28. Anthropic, Statement on the directive to suspend Fable 5 access: https://www.anthropic.com/
news/fable-mythos-access . Primary source for the June 12 to July 1, 2026 export-control
suspension timeline.
29. Anthropic, Claude Platform pricing documentation: https://platform.claude.com/docs/e
n/about-claude/pricing . Source of Fable 5.1, Opus 5, Sonnet 5, and Haiku 4.5 per-token
rates and cached-read pricing.
30. Anthropic, Introducing the Model Context Protocol: https://www.anthropic.com/news/mod
el-context-protocol , and the MCP specification: https://modelcontextprotocol.io/sp
ecification/ . Source of the Tools / Resources / Prompts primitive descriptions.
31. Anthropic, Introducing Claude 3.5 Sonnet: https://www.anthropic.com/news/claude-3-5
-sonnet . Source of the 64% vs. 38% agentic coding comparison against Claude 3 Opus.
32. OpenAI, Learning to Reason with LLMs: https://openai.com/index/learning-to-reaso
n-with-llms/ . Primary description of the o-series inference-time reasoning approach.
16.5 Independent Evaluators (Primary)
33. Artificial Analysis, Intelligence Index (v4.1.1 and v4.2, September 2026): https://artifi
cialanalysis.ai/ . Source of the composite index ranking (Claude Fable 5.1 first, GPT-6
Astra second), the constituent nine-benchmark list, the GDP.pdf result (Astra 33.2%), the
token-efficiency finding, and the increase in the private-item share from 20% to 40%.
34. METR, Task-Completion Time Horizons of Frontier AI Models : https://metr.org/time-h
orizons/ , and Kwa et al., Measuring AI Ability to Complete Long Tasks , arXiv:2503.14499
(2025). Source of the seven-month time-horizon doubling figure and its stated methodological
limitations.
16.6 Claims Retained Without a Primary Source
The following are flagged because no primary source exists; they are reported as estimates or as
vendor assertions, not as established fact.
• GPT-4’s 1.8T / 16×111B parameter count. Analyst and leak-derived consensus only; never
confirmed by OpenAI. No citable primary source exists.
• “Looped transformer” / recurrent-depth architecture for GPT-6 Astra. OpenAI’s own
characterization; no peer-reviewed formulation published.
• MCTS-style search in o1/o3/Astra training or inference. Research-community hypothesis;
explicitly unconfirmed by OpenAI.
• Claude Mythos operating-system vulnerability claims. Appear in Anthropic promotional
material; not independently replicated by external security researchers.
Confidential: Internal Strategy Briefing | September 2026
Confidential: Internal Strategy Briefing 47 September 2026
