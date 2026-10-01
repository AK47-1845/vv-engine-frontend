# Handoff Knowledge Graph

VERIFIED:

- User source PDFs -> reviewed text and source manifest -> physical-AI requirements.
- backend -> evaluation, provenance and governance mechanisms.
- web -> existing operations console -> backend API.
- handoff -> continuation instructions -> preserves existing work.

PLANNED: Separate pitch site -> deterministic demonstration fixtures -> illustrative product story. No marketing mock is production evidence.

## Current Frontend Map

VERIFIED file relationships are mirrored in knowledge-graph.json. All graph paths must exist; graph edges must resolve to node IDs.

```mermaid
flowchart TD
	Page[Next.js page] --> Pitch[Pitch composition]
	Pitch --> Hero
	Hero --> HeroScene[Responsive hero scene]
	HeroScene --> Mobile[Poster and lightweight canvas]
	HeroScene --> Robot[Lazy Three.js robot]
	Hero --> Demo[Pure synthetic trace model]
	Robot --> Demo
	Pitch --> Lab[Failure lab]
	Lab --> Demo
	Lab --> Export[Qualified JSON export]
	Pitch --> Pipeline[Evidence pipeline]
	Pipeline --> Scroll[Desktop ScrollTrigger or manual tabs]
	Pitch --> Ledger[Ledger and report]
	Ledger --> Demo
	Pitch --> Actions[Radix dialogs]
	Actions --> Draft[Local pilot draft, not submitted]
	Tests[Model and browser tests] --> Pitch
	Lighthouse --> Receipt[Measured reports]
```

## Procedural Graph

```mermaid
flowchart LR
	Sources[Read source facts and placeholders] --> Inspect[Inspect current files and references]
	Inspect --> Edit[Small scoped edit]
	Edit --> Check[Focused behavior or type check]
	Check --> Browser[Real browser workflow and screenshots]
	Browser --> Build[Production build]
	Build --> Measure[Lighthouse on production server]
	Measure --> Record[Record actual scores and gaps]
	Record --> Handoff[Update status, graph and continuation]
	Handoff --> Commit[Local Git checkpoint]
```

No edge from the pitch site to the engineering backend claims a live integration. `demo-model -> engine` is explicitly an illustrative mock relationship, not formula equivalence. The old graphify snapshot is retained as historical source context.