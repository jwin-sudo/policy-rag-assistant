from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from src.config import Settings, set_global_seed
from src.rag import PolicyRAGService
from src.schemas import ChatMeta, ChatRequest, ChatResponse, HealthResponse

settings = Settings()
set_global_seed(settings.random_seed)

app = FastAPI(title="Policy RAG Assistant", version="0.1.0")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

rag_service = PolicyRAGService(settings)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", index_ready=rag_service.index_ready())


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "Policy RAG Assistant"},
    )


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    if not settings.openrouter_api_key:
        raise HTTPException(status_code=500, detail="OPENROUTER_API_KEY is not configured")

    if not rag_service.index_ready():
        raise HTTPException(status_code=503, detail="Vector index is empty. Run ingestion first.")

    answer, citations, latency_ms, refusal = rag_service.answer(payload.question)
    return ChatResponse(
        question=payload.question,
        answer=answer,
        citations=citations,
        meta=ChatMeta(
            latency_ms=latency_ms,
            model=settings.openrouter_model,
            top_k=settings.top_k,
            refusal=refusal,
        ),
    )
