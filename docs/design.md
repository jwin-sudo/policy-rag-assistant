# Design Documentation

## Overview
The application is a Retrieval-Augmented Generation (RAG) assistant for policy question answering. It indexes policy documents locally and uses retrieved chunks as evidence for LLM responses.

## Key Design Choices

### Embedding Model
- Choice: `sentence-transformers/all-MiniLM-L6-v2` (local HuggingFace embedding model)
- Why: zero API cost, good semantic quality for short policy chunks, reproducible local runs.

### Vector Store
- Choice: Chroma local persistent store
- Why: lightweight setup, no external infrastructure, suitable for assignment scope.

### Chunking Strategy
- Choice: heading-aware recursive chunking with overlap
- Parameters: chunk size `900`, overlap `120`
- Why: policy documents are section-structured; heading-preserving chunks improve retrieval grounding.

### Retrieval Strategy
- Choice: top-k dense retrieval (`k=5`) from Chroma
- Why: balances evidence coverage and context noise in prompt.

### Prompting Strategy
- System prompt enforces:
  - policy-only scope
  - refusal for out-of-corpus queries
  - concise response length
  - explicit source citations
- User prompt injects retrieved chunks with `doc_id` and title metadata.

### Guardrails
- Out-of-domain refusal sentence is fixed.
- Max answer word guidance is enforced in prompt.
- Citations and snippets are always returned from retrieved chunks.

## Trade-offs
- Local embeddings reduce cost but may be slower than managed APIs on low-resource machines.
- Top-k retrieval without reranking is simpler but can surface redundant chunks.
- Citation verification is currently rubric-based/manual during evaluation.

## Future Improvements
- Add optional reranker for retrieval quality.
- Add automatic groundedness/citation scoring model.
- Add prompt ablations (k, chunk size, phrasing).
- Add OCR for scanned PDFs.
