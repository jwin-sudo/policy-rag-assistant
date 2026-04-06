# Evaluation Report (Latest Run)

## Run Metadata
- Date: 2026-04-05
- Evaluator: James Nguyen
- App version / commit: local working tree
- Embedding model: sentence-transformers/all-MiniLM-L6-v2
- LLM model: qwen/qwen3.6-plus:free (OpenRouter)
- Retriever settings (k, fetch_k, prompt_k): k=5, fetch_k=10, prompt_k=2
- Chunking: chunk_size=900, overlap=120
- Prompt/version: optimized citation-filtering (`src/rag.py`)
- Raw run artifact: evaluation/eval_run_22q_final.json

## Aggregate Results (22 Questions)
- Groundedness (%): 100.0
- Citation Accuracy (%): 90.9
- Exact Match (%) [optional]: 86.4
- Partial Match (%) [optional]: 13.6
- Latency p50 (ms): 14955
- Latency p95 (ms): 25271

## Manual Scoring Notes
- Groundedness scoring used the rubric in `evaluation/SUCCESS_METRICS.md`.
- Citation accuracy improved substantially after citation filtering to answer-referenced sources.
- Most questions now return exactly one citation, typically the expected source document.
- A few items still include a second citation where attribution is broader than necessary.

## Quality Gate Check
- Groundedness gate (>=85%): PASS
- Citation Accuracy gate (>=85%): PASS
- Latency reported (p50/p95 over >=10 queries): PASS

## Final Assessment
The app meets the assignment's required evaluation criteria for answer quality and system metrics on the current benchmark.

## Remaining Improvements (Optional)
1. Add lightweight reranker to further reduce occasional secondary citation noise.
2. Add per-claim citation extraction to map each claim to one exact passage.
3. Run ablation table (`k=3` vs `k=5`, `prompt_k=2` vs `3`) and append to report.
