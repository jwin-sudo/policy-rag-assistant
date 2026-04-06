from __future__ import annotations

import re
import time
from time import sleep
from typing import Any

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from openai import OpenAI

from src.config import Settings
from src.schemas import Citation

SYSTEM_PROMPT = (
    "You are a policy assistant. Answer only with facts supported by retrieved policy context. "
    "If the answer is outside the policy corpus, reply exactly: "
    "'I can only answer questions about the provided policy corpus.' "
    "Keep responses concise and under the configured word limit. "
    "Cite policy sources in-line by doc_id and title."
)

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "to",
    "what",
    "when",
    "which",
    "who",
    "with",
}


def _normalized_terms(text: str) -> set[str]:
    terms = set(re.findall(r"[a-zA-Z0-9]+", text.lower()))
    return {t for t in terms if len(t) > 2 and t not in STOPWORDS}


def _title_terms(title: str) -> set[str]:
    return _normalized_terms(title.replace("_", " "))


class PolicyRAGService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.embeddings = HuggingFaceEmbeddings(model_name=settings.embedding_model)
        self.vectorstore = Chroma(
            collection_name="policy_corpus",
            embedding_function=self.embeddings,
            persist_directory=str(settings.vector_db_path),
        )
        self.client = None
        if settings.openrouter_api_key:
            self.client = OpenAI(
                api_key=settings.openrouter_api_key,
                base_url=settings.openrouter_base_url,
            )

    def index_ready(self) -> bool:
        try:
            return self.vectorstore._collection.count() > 0
        except Exception:
            return False

    def retrieve(self, question: str) -> list[dict[str, Any]]:
        fetch_k = max(self.settings.retrieval_fetch_k, self.settings.top_k)
        docs = self.vectorstore.similarity_search(question, k=fetch_k)

        question_terms = _normalized_terms(question)
        ranked: list[tuple[float, Any]] = []
        for idx, doc in enumerate(docs):
            text = doc.page_content
            text_terms = _normalized_terms(text[:1000])
            overlap = len(question_terms & text_terms)
            # Prefer high lexical overlap, then preserve vector rank order.
            score = (overlap * 10.0) - float(idx)
            ranked.append((score, doc))

        ranked.sort(key=lambda x: x[0], reverse=True)

        results: list[dict[str, Any]] = []
        seen_chunks: set[str] = set()
        for _, doc in ranked:
            text = doc.page_content.strip()
            if not text:
                continue

            dedupe_key = f"{doc.metadata.get('doc_id','unknown')}::{text[:220]}"
            if dedupe_key in seen_chunks:
                continue
            seen_chunks.add(dedupe_key)

            snippet = text[:380]
            prompt_text = text[: self.settings.max_context_chars]
            text_terms = _normalized_terms(text[:1000])
            overlap = len(question_terms & text_terms)
            results.append(
                {
                    "doc_id": doc.metadata.get("doc_id", "unknown"),
                    "title": doc.metadata.get("title", "Untitled"),
                    "source": doc.metadata.get("source", ""),
                    "snippet": snippet,
                    "text": prompt_text,
                    "overlap": overlap,
                }
            )

            if len(results) >= self.settings.top_k:
                break

        return results

    def _make_user_prompt(self, question: str, contexts: list[dict[str, Any]]) -> str:
        serialized = []
        for i, ctx in enumerate(contexts[: self.settings.prompt_k], start=1):
            serialized.append(
                f"[Source {i}] doc_id={ctx['doc_id']}; title={ctx['title']}\n"
                f"{ctx['text']}"
            )

        return (
            f"Question: {question}\n\n"
            f"Use only the sources below. If insufficient evidence exists, refuse. "
            f"Maximum {self.settings.max_answer_words} words.\n\n"
            + "\n\n".join(serialized)
        )

    def answer(self, question: str) -> tuple[str, list[Citation], int, bool]:
        start = time.perf_counter()
        contexts = self.retrieve(question)

        if not contexts:
            return (
                "I can only answer questions about the provided policy corpus.",
                [],
                int((time.perf_counter() - start) * 1000),
                True,
            )

        answer = ""
        if self.client is not None:
            for attempt in range(1, 4):
                try:
                    completion = self.client.chat.completions.create(
                        model=self.settings.openrouter_model,
                        extra_headers={
                            "HTTP-Referer": self.settings.openrouter_http_referer,
                            "X-Title": self.settings.openrouter_app_title,
                        },
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": self._make_user_prompt(question, contexts)},
                        ],
                        temperature=self.settings.llm_temperature,
                        max_tokens=self.settings.llm_max_tokens,
                    )
                    answer = completion.choices[0].message.content or ""
                    break
                except Exception:
                    if attempt < 3:
                        sleep(float(attempt))

        if not answer:
            # Fallback keeps endpoint stable and remains grounded in retrieved evidence.
            answer = (
                "I could not reach the model provider right now. "
                "Based on retrieved policy context: "
                f"{contexts[0]['snippet']}"
            )

        answer_lower = answer.lower()
        answer_terms = _normalized_terms(answer)

        # Prefer citations explicitly referenced by doc_id/title in generated answer text.
        referenced: list[dict[str, Any]] = []
        for ctx in contexts:
            doc_id = ctx["doc_id"]
            title_terms = _title_terms(ctx["title"])
            title_overlap = len(answer_terms & title_terms)
            if doc_id.lower() in answer_lower or title_overlap >= 2:
                referenced.append(ctx)

        citation_candidates = referenced if referenced else contexts

        citations: list[Citation] = []
        seen_docs: set[str] = set()
        for ctx in citation_candidates:
            doc_id = ctx["doc_id"]
            if doc_id in seen_docs:
                continue

            citations.append(
                Citation(
                    doc_id=doc_id,
                    title=ctx["title"],
                    source=ctx.get("source", ""),
                    snippet=ctx["snippet"],
                )
            )
            seen_docs.add(doc_id)
            if len(citations) >= self.settings.max_citations:
                break

        latency_ms = int((time.perf_counter() - start) * 1000)
        refusal = answer.strip().startswith("I can only answer questions about the provided policy corpus.")
        return answer.strip(), citations, latency_ms, refusal
