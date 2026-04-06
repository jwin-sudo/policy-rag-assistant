# Success Metrics for Policy RAG Assistant

This document defines required success metrics for evaluating the policy assistant.

## 1. Evaluation Scope
The assistant is expected to answer policy questions using retrieved context from the corpus and provide supporting citations.

## 2. Required Information-Quality Metrics
### 2.1 Groundedness (required)
Definition: Percentage of answers that are fully supported by retrieved evidence and contain no unsupported or contradictory claims.

Formula:
Groundedness % = (Number of fully grounded answers / Total evaluated answers) x 100

Scoring rubric per answer:
- 1.0: Every factual claim is supported by retrieved context.
- 0.5: Mostly supported, but includes minor unsupported detail.
- 0.0: Contains unsupported or contradicted claims.

Recommended pass threshold:
- Minimum: 85%
- Target: 92%+

### 2.2 Citation Accuracy (required)
Definition: Percentage of answers where cited sources correctly point to the specific policy passage(s) backing each key claim.

Formula:
Citation Accuracy % = (Number of answers with correct citations / Total evaluated answers) x 100

Scoring rubric per answer:
- 1.0: Citations correctly map to all key claims.
- 0.5: Some claims are correctly cited, others vague or mismatched.
- 0.0: Citations missing, incorrect, or misleading.

Recommended pass threshold:
- Minimum: 85%
- Target: 95%+

### 2.3 Exact Match / Partial Match (optional)
Definition: Agreement between model answer and short gold answer.

Formula:
- Exact Match % = exact answer matches / total
- Partial Match % = answers that are directionally correct but incomplete / total

Use this as a secondary metric, since policy answers can be phrased in multiple valid ways.

## 3. Required System Metrics
### 3.1 Latency (required)
Definition: Time from user request received to final answer returned.

Report:
- p50 latency across 10 to 20 queries
- p95 latency across 10 to 20 queries

Recommended pass threshold:
- p50 <= 2.5s
- p95 <= 6.0s

### 3.2 Optional system diagnostics
- Retrieval latency (vector search only)
- Generation latency (LLM only)
- Token usage per request

## 4. Secondary Retrieval Quality Metrics (optional but useful)
- Context Precision@k: proportion of retrieved chunks that are relevant
- Context Recall@k: whether at least one relevant chunk is retrieved
- Citation Coverage: % of claims in an answer that have explicit citation support

## 5. Overall Release Gates
A candidate configuration is considered acceptable if all are true:
- Groundedness >= 85%
- Citation Accuracy >= 85%
- p95 latency <= 6.0s
- No critical hallucination in security/privacy/legal topics

## 6. Common Failure Categories to Track
- Unsupported policy claim
- Wrong policy source cited
- Correct source but wrong section
- Missing exception/condition in policy rule
- Stale policy version conflict

## 7. Evaluation Run Size and Frequency
- Minimum benchmark set size: 15 to 30 questions
- Recommended default: 20 questions
- Run before each major prompt, retriever, or chunking change
