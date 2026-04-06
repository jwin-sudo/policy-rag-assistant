# Evaluation Report Template

## Run Metadata
- Date:
- Evaluator:
- App version / commit:
- Embedding model:
- LLM model:
- Retriever settings (k, chunk size, overlap):
- Prompt version:

## Aggregate Results
- Total questions evaluated:
- Groundedness (%):
- Citation Accuracy (%):
- Exact Match (%) [optional]:
- Partial Match (%) [optional]:
- Latency p50 (ms):
- Latency p95 (ms):

## Per-Question Log
| Q# | Question | Groundedness (0/0.5/1) | Citation Accuracy (0/0.5/1) | Exact/Partial (opt) | Latency (ms) | Notes |
|----|----------|--------------------------|------------------------------|---------------------|--------------|-------|
| 1  |          |                          |                              |                     |              |       |
| 2  |          |                          |                              |                     |              |       |
| 3  |          |                          |                              |                     |              |       |
| 4  |          |                          |                              |                     |              |       |
| 5  |          |                          |                              |                     |              |       |
| 6  |          |                          |                              |                     |              |       |
| 7  |          |                          |                              |                     |              |       |
| 8  |          |                          |                              |                     |              |       |
| 9  |          |                          |                              |                     |              |       |
| 10 |          |                          |                              |                     |              |       |
| 11 |          |                          |                              |                     |              |       |
| 12 |          |                          |                              |                     |              |       |
| 13 |          |                          |                              |                     |              |       |
| 14 |          |                          |                              |                     |              |       |
| 15 |          |                          |                              |                     |              |       |
| 16 |          |                          |                              |                     |              |       |
| 17 |          |                          |                              |                     |              |       |
| 18 |          |                          |                              |                     |              |       |
| 19 |          |                          |                              |                     |              |       |
| 20 |          |                          |                              |                     |              |       |
| 21 |          |                          |                              |                     |              |       |
| 22 |          |                          |                              |                     |              |       |

## Metric Calculations
- Groundedness % = (sum groundedness scores / total questions) x 100
- Citation Accuracy % = (sum citation accuracy scores / total questions) x 100
- Exact Match % = (count exact matches / total questions) x 100
- Partial Match % = (count partial matches / total questions) x 100

## Required Checks
- Any hallucination in legal/security answers?
- Any citation to incorrect policy document?
- Any response with no citation despite factual claims?

## Optional Ablation Table
| Variant | Retriever k | Chunk size | Prompt version | Groundedness % | Citation Acc % | p50 (ms) | p95 (ms) | Notes |
|---------|-------------|------------|----------------|----------------|----------------|----------|----------|-------|
| Baseline |             |            |                |                |                |          |          |       |
| A        |             |            |                |                |                |          |          |       |
| B        |             |            |                |                |                |          |          |       |

## Conclusion
- Meets quality gate? (Yes/No)
- Meets latency gate? (Yes/No)
- Recommended next iteration:
