from __future__ import annotations

import random
from pathlib import Path

import numpy as np
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    openrouter_api_key: str | None = Field(default=None, alias="OPENROUTER_API_KEY")
    openrouter_model: str = Field(default="qwen/qwen3.6-plus:free", alias="OPENROUTER_MODEL")
    openrouter_base_url: str = Field(default="https://openrouter.ai/api/v1", alias="OPENROUTER_BASE_URL")
    openrouter_app_title: str = Field(default="policy-rag-assistant", alias="OPENROUTER_APP_TITLE")
    openrouter_http_referer: str = Field(default="http://localhost:8000", alias="OPENROUTER_HTTP_REFERER")

    embedding_model: str = Field(default="sentence-transformers/all-MiniLM-L6-v2", alias="EMBEDDING_MODEL")
    vector_db_dir: str = Field(default="./data/chroma", alias="VECTOR_DB_DIR")
    corpus_dir: str = Field(default="./corpus", alias="CORPUS_DIR")

    top_k: int = Field(default=5, alias="TOP_K")
    retrieval_fetch_k: int = Field(default=10, alias="RETRIEVAL_FETCH_K")
    prompt_k: int = Field(default=2, alias="PROMPT_K")
    chunk_size: int = Field(default=900, alias="CHUNK_SIZE")
    chunk_overlap: int = Field(default=120, alias="CHUNK_OVERLAP")
    random_seed: int = Field(default=42, alias="RANDOM_SEED")
    max_answer_words: int = Field(default=180, alias="MAX_ANSWER_WORDS")
    max_context_chars: int = Field(default=650, alias="MAX_CONTEXT_CHARS")
    max_citations: int = Field(default=2, alias="MAX_CITATIONS")
    llm_temperature: float = Field(default=0.0, alias="LLM_TEMPERATURE")
    llm_max_tokens: int = Field(default=220, alias="LLM_MAX_TOKENS")

    otel_enabled: bool = Field(default=False, alias="OTEL_ENABLED")
    otel_service_name: str = Field(default="policy-rag-assistant", alias="OTEL_SERVICE_NAME")
    otel_exporter_otlp_endpoint: str | None = Field(default=None, alias="OTEL_EXPORTER_OTLP_ENDPOINT")
    otel_sample_ratio: float = Field(default=1.0, alias="OTEL_SAMPLE_RATIO")

    @field_validator("otel_sample_ratio")
    @classmethod
    def clamp_otel_sample_ratio(cls, value: float) -> float:
        return min(max(value, 0.0), 1.0)

    @property
    def vector_db_path(self) -> Path:
        return Path(self.vector_db_dir)

    @property
    def corpus_path(self) -> Path:
        return Path(self.corpus_dir)


def set_global_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
