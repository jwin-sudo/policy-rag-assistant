from __future__ import annotations

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(min_length=3, max_length=2000)


class Citation(BaseModel):
    doc_id: str
    title: str
    source: str
    snippet: str


class ChatMeta(BaseModel):
    latency_ms: int
    model: str
    top_k: int
    refusal: bool


class ChatResponse(BaseModel):
    question: str
    answer: str
    citations: list[Citation]
    meta: ChatMeta


class HealthResponse(BaseModel):
    status: str
    index_ready: bool
