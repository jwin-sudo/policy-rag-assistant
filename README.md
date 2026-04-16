# Policy RAG Assistant

Policy RAG web application for answering questions from an internal policy corpus with evidence-backed citations.

## Features
- Multi-format ingestion (`.md`, `.txt`, `.html`, `.pdf`)
- Deterministic chunking with overlap
- Local embeddings (HuggingFace sentence-transformers)
- Local vector database (Chroma)
- FastAPI endpoints:
	- `GET /` web chat UI
	- `POST /chat` answer with citations and snippets
	- `GET /health` service/index health
- Evaluation runner with latency metrics (p50/p95)
- Optional OpenTelemetry tracing (feature-flagged)
- CI pipeline via GitHub Actions

## Repository Structure
```text
policy-rag-assistant/
	app.py
	requirements.txt
	render.yaml
	corpus/
	evaluation/
	docs/
		design.md
	src/
		config.py
		ingest.py
		rag.py
		schemas.py
		eval.py
	templates/
		index.html
```

## 1. Environment and Reproducibility

### Prerequisites
- Python 3.11+

### Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Determinism
The project uses a fixed random seed via `RANDOM_SEED` in `.env` (default: `42`) for deterministic chunking/eval behavior.

## 2. Configure Environment Variables

Required:
- `OPENROUTER_API_KEY`

Common defaults are already provided in `.env.example`:
- `OPENROUTER_MODEL`
- `OPENROUTER_BASE_URL`
- `EMBEDDING_MODEL`
- `VECTOR_DB_DIR`
- `CORPUS_DIR`
- `TOP_K`, `CHUNK_SIZE`, `CHUNK_OVERLAP`
- Optional telemetry: `OTEL_ENABLED`, `OTEL_SERVICE_NAME`, `OTEL_EXPORTER_OTLP_ENDPOINT`, `OTEL_SAMPLE_RATIO`

## 3. Build the Vector Index

```bash
python -m src.ingest --rebuild
```

Expected output:
- Number of indexed documents
- Number of indexed chunks

## 4. Run the Web Application

```bash
uvicorn app:app --reload
```

Open:
- `http://localhost:8000/` for chat UI
- `http://localhost:8000/health` for health JSON

## 5. API Usage

### POST `/chat`
```bash
curl -X POST http://localhost:8000/chat \
	-H "Content-Type: application/json" \
	-d '{"question":"What is the patch deadline for critical vulnerabilities?"}'
```

Response contains:
- `question`
- `answer`
- `citations[]` with `doc_id`, `title`, `source`, `snippet`
- `meta` with `latency_ms`, `model`, `top_k`, and `refusal`

## 6. Evaluation

Question set and scoring templates are in `evaluation/`.

Run eval:
```bash
python -m src.eval --base-url http://localhost:8000 --limit 22 --out evaluation/eval_run_22q_final.json
```

This reports:
- Answered count
- Latency p50 and p95
- Per-question outputs for groundedness/citation scoring

Latest artifacts:
- `evaluation/eval_run_22q_final.json`
- `evaluation/EVAL_REPORT_LATEST.md`
- `evaluation/SUCCESS_METRICS.md`

## 6.1 Observability (OpenTelemetry)

Telemetry is disabled by default. To enable it:

```bash
export OTEL_ENABLED=true
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4318/v1/traces"
```

Optional settings:
- `OTEL_SERVICE_NAME` (default: `policy-rag-assistant`)
- `OTEL_SAMPLE_RATIO` (default: `1.0`)

When enabled, spans are emitted for:
- `chat.request`
- `rag.retrieve`
- `rag.llm_call`
- `rag.citation_select`

## 7. CI/CD

GitHub Actions workflow: `.github/workflows/ci.yml`

On push/PR it:
1. Installs dependencies
2. Runs import/build check (`import app`)

## 8. Deployment (Render)

Render blueprint is included in `render.yaml`.

Steps:
1. Connect repo to Render.
2. Set `OPENROUTER_API_KEY` in Render environment variables.
3. Deploy using `render.yaml`.

### Deployment Verification Checklist
After deployment, verify the following:
1. `GET /health` returns `{"status":"ok", ...}`.
2. `GET /` loads the chat UI.
3. `POST /chat` returns `question`, `answer`, `citations[]`, and `meta`.

Example:
```bash
curl -X POST https://<your-render-url>/chat \
	-H "Content-Type: application/json" \
	-d '{"question":"What is the patch deadline for critical vulnerabilities?"}'
```

## 9. Design Rationale

See `docs/design.md` for decisions on:
- embedding model
- chunking strategy
- retrieval top-k
- prompt/guardrail structure
- vector store choice

## Notes
- This assistant is intentionally corpus-bounded for safer policy Q&A.
- For best accuracy, rebuild index after corpus changes.

## 10. Submission Checklist
1. Repository contains setup/run instructions and `.env.example`.
2. Corpus and ingestion/indexing pipeline are present and reproducible.
3. Endpoints implemented and working: `/`, `/chat`, `/health`.
4. Evaluation artifacts committed:
	- `evaluation/EVAL_QUESTIONS.md`
	- `evaluation/eval_run_22q_final.json`
	- `evaluation/EVAL_REPORT_LATEST.md`
5. CI workflow present in `.github/workflows/ci.yml`.
6. Render deployment config present in `render.yaml`.
7. Design rationale documented in `docs/design.md`.
8. Share repository access with GitHub account `quantic-grader`.
