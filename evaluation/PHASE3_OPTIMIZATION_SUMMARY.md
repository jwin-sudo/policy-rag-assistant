# Phase 3 Optimization Summary

Date: 2026-04-05

## What Was Optimized
1. Retrieval quality
- Added lexical-overlap reranking on top of vector search.
- Added chunk deduplication to reduce repeated evidence.
- Added stopword-filtered overlap scoring for better relevance.

2. Prompt efficiency
- Added prompt context cap (`MAX_CONTEXT_CHARS`) to reduce payload size.
- Added configurable number of contexts included in prompt (`PROMPT_K`).

3. Generation controls
- Added configurable `LLM_TEMPERATURE` and `LLM_MAX_TOKENS`.
- Added model-call retry handling for transient upstream failures.
- Added grounded fallback response if provider is unavailable.

4. Citation quality
- Prefer unique source docs in returned citations.
- Limit citation count (`MAX_CITATIONS`) with overlap-based filtering.

## Benchmark Artifacts
- Baseline: `evaluation/eval_run_10q.json`
- Optimization pass 1: `evaluation/eval_run_10q_opt.json`
- Optimization pass 2: `evaluation/eval_run_10q_opt_v2.json`

## Latency Comparison (10-query runs)
- Baseline: answered 10/10, p50=12817 ms, p95=29439 ms
- Pass 1: answered 10/10, p50=10318 ms, p95=30923 ms
- Pass 2: answered 10/10, p50=12591 ms, p95=24826 ms

## Interpretation
- p50 improved best in pass 1 (~19.5% better than baseline).
- p95 improved best in pass 2 (~15.7% better than baseline).
- Stability remained 10/10 answered for all compared runs.

## Recommended Runtime Defaults
For lower tail latency while preserving citation precision:
- `TOP_K=5`
- `RETRIEVAL_FETCH_K=12`
- `PROMPT_K=3`
- `MAX_CONTEXT_CHARS=750`
- `MAX_CITATIONS=4`
- `LLM_TEMPERATURE=0.0`
- `LLM_MAX_TOKENS=260`

## Next Optimization Ideas
1. Add optional reranker model to improve citation accuracy further.
2. Add dynamic context budget by question complexity.
3. Run full 20-22 question benchmark and complete manual groundedness/citation scoring.
