from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import Settings, set_global_seed


def _clean_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _parse_html(path: Path) -> str:
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    return _clean_text(soup.get_text("\n"))


def _parse_text(path: Path) -> str:
    return _clean_text(path.read_text(encoding="utf-8", errors="ignore"))


def _parse_pdf(path: Path) -> str:
    loader = PyPDFLoader(str(path))
    pages = loader.load()
    return _clean_text("\n\n".join(page.page_content for page in pages))


def _load_single(path: Path) -> Document | None:
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        content = _parse_text(path)
    elif suffix in {".html", ".htm"}:
        content = _parse_html(path)
    elif suffix == ".pdf":
        content = _parse_pdf(path)
    else:
        return None

    title = path.stem.replace("_", " ")
    return Document(
        page_content=content,
        metadata={
            "doc_id": path.name,
            "title": title,
            "source": str(path),
        },
    )


def load_documents(corpus_dir: Path) -> list[Document]:
    docs: list[Document] = []
    for path in sorted(corpus_dir.rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            continue
        doc = _load_single(path)
        if doc and doc.page_content:
            docs.append(doc)
    return docs


def chunk_documents(docs: Iterable[Document], chunk_size: int, chunk_overlap: int) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n# ", "\n## ", "\n### ", "\n\n", "\n", " ", ""],
    )
    chunks = splitter.split_documents(list(docs))
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i
    return chunks


def build_index(settings: Settings, rebuild: bool = False) -> tuple[int, int]:
    set_global_seed(settings.random_seed)
    settings.vector_db_path.mkdir(parents=True, exist_ok=True)

    docs = load_documents(settings.corpus_path)
    chunks = chunk_documents(docs, settings.chunk_size, settings.chunk_overlap)

    embeddings = HuggingFaceEmbeddings(model_name=settings.embedding_model)
    vectorstore = Chroma(
        collection_name="policy_corpus",
        embedding_function=embeddings,
        persist_directory=str(settings.vector_db_path),
    )

    if rebuild:
        try:
            vectorstore.delete_collection()
        except Exception:
            pass
        vectorstore = Chroma(
            collection_name="policy_corpus",
            embedding_function=embeddings,
            persist_directory=str(settings.vector_db_path),
        )

    if not rebuild:
        try:
            vectorstore.delete_collection()
            vectorstore = Chroma(
                collection_name="policy_corpus",
                embedding_function=embeddings,
                persist_directory=str(settings.vector_db_path),
            )
        except Exception:
            pass

    vectorstore.add_documents(chunks)

    return len(docs), len(chunks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build local vector index for policy corpus")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild index from scratch")
    args = parser.parse_args()

    settings = Settings()
    doc_count, chunk_count = build_index(settings, rebuild=args.rebuild)
    print(f"Indexed documents: {doc_count}")
    print(f"Indexed chunks: {chunk_count}")


if __name__ == "__main__":
    main()
