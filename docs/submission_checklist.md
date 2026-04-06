# Submission Checklist

Use this checklist before final handoff.

## Required Deliverables
- [ ] Environment setup documented (`README.md`, `requirements.txt`, `.env.example`)
- [ ] Deterministic settings defined (`RANDOM_SEED`)
- [ ] Ingestion/indexing command works (`python -m src.ingest --rebuild`)
- [ ] RAG retrieval/generation pipeline returns citations
- [ ] API endpoints work: `/`, `/chat`, `/health`
- [ ] Evaluation set included (15-30 questions)
- [ ] Evaluation run artifact included (`evaluation/eval_run_22q_final.json`)
- [ ] Evaluation report included (`evaluation/EVAL_REPORT_LATEST.md`)
- [ ] Design rationale included (`docs/design.md`)
- [ ] CI workflow included (`.github/workflows/ci.yml`)
- [ ] Deployment config included (`render.yaml`)

## Deployment Verification
- [ ] Public URL is accessible
- [ ] `GET /health` returns status JSON
- [ ] `POST /chat` returns structured payload with citations and meta

## Grader Access
- [ ] Repository shared with GitHub account `quantic-grader`
- [ ] Visibility/access verified from repository settings

## Suggested Final Commands
```bash
python -m src.ingest --rebuild
python -m uvicorn app:app --reload
python -m src.eval --base-url http://localhost:8000 --limit 22 --out evaluation/eval_run_22q_final.json
```
