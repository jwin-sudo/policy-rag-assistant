# Design and Evaluation

## 1. System Design and Architecture Decisions

### Project Goal
The system is a policy-focused Retrieval-Augmented Generation (RAG) assistant that answers user questions using only an internal policy corpus and returns citations for traceability.

### High-Level Architecture
1. Ingestion and indexing pipeline
2. Retrieval layer over embedded document chunks
3. Generation layer constrained by policy-only guardrails
4. Web/API interface for chat and health checks
5. Evaluation pipeline for quality and latency reporting

### Technology Choices and Rationale

#### Backend framework
- Choice: FastAPI
- Why: simple API development, clear endpoint structure, lightweight deployment, and good fit for assignment scope.

#### Embeddings
- Choice: sentence-transformers/all-MiniLM-L6-v2 (local model)
- Why: no per-request API cost, solid semantic retrieval quality for short policy chunks, reproducible local runs.

#### Vector store
- Choice: Chroma (local persistent store)
- Why: low operational overhead, no managed infrastructure required, fast setup for local development and grading.

#### LLM provider and model
- Choice: OpenRouter with qwen/qwen3.6-plus:free
- Why: free-tier availability and practical quality/latency balance for assignment constraints.

#### Document processing and chunking
- Choice: heading-aware recursive chunking with overlap
- Parameters: chunk size 900, overlap 120
- Why: policy files are section-based; preserving structural boundaries improves retrieval grounding and reduces context fragmentation.

#### Retrieval strategy
- Choice: dense top-k retrieval with fetch_k and prompt_k controls, plus overlap-based reranking and deduplication
- Why: improves evidence relevance while limiting prompt noise and unnecessary token usage.

#### Prompting and guardrails
- Design:
  - system instruction restricts answers to policy corpus
  - explicit refusal when evidence is insufficient or outside scope
  - concise response target
  - citation expectation embedded in answer behavior
- Why: enforces groundedness and assignment-aligned safety behavior.

### Operational Design Notes
- Deterministic settings and consistent configs were used for reproducible evaluation runs.
- API behavior includes health reporting and structured metadata (latency, model, retrieval settings, refusal flag) for observability.
- Optional OpenTelemetry tracing is available behind an environment flag for low-risk incremental observability in staging/production.

### Trade-offs
- Local embeddings reduce cost but increase cold-start and CPU workload.
- Simpler reranking is easier to maintain but less precise than dedicated cross-encoder rerankers.
- Citation scoring currently includes manual rubric checks, which are transparent but labor-intensive.

## 2. Evaluation Approach and Results

### Evaluation Objectives
The evaluation measured:
1. Groundedness: whether answers are supported by corpus evidence
2. Citation accuracy: whether cited sources correctly support the answer
3. Optional match quality: exact or partial agreement with expected answer
4. Performance: end-to-end latency distribution

### Evaluation Setup
- Benchmark set: 22 policy QA prompts spanning HR, security, privacy, change management, continuity, and support operations.
- Scoring rubric:
  - Groundedness score per item (1.0, 0.5, 0.0)
  - Citation accuracy score per item (1.0, 0.5, 0.0)
  - Optional exact/partial match tagging
- Run configuration:
  - Retriever: k=5, fetch_k=10, prompt_k=2
  - Chunking: 900/120
  - Embedding model: sentence-transformers/all-MiniLM-L6-v2
  - LLM: qwen/qwen3.6-plus:free (OpenRouter)

### Aggregate Results (Latest 22-Question Run)
- Groundedness: 100.0%
- Citation Accuracy: 90.9%
- Exact Match (optional): 86.4%
- Partial Match (optional): 13.6%
- Latency p50: 14,955 ms
- Latency p95: 25,271 ms

### Interpretation
- The system met quality gates for groundedness and citation accuracy.
- Retrieval and citation-filtering improvements significantly reduced irrelevant citations.
- Remaining quality gap is mostly occasional extra citation noise rather than unsupported answers.

### Limitations and Next Improvements
1. Add a lightweight reranker to further improve citation precision.
2. Add per-claim citation alignment to tighten attribution.
3. Run controlled ablation comparisons for k and prompt_k to optimize latency/quality trade-offs.

## 3. Conclusion
The current RAG implementation satisfies assignment requirements for design clarity, evidence-grounded answering, citation behavior, and benchmark reporting. The evaluation indicates strong factual grounding with citation quality above the target threshold, while highlighting clear next steps for further precision and performance tuning.
