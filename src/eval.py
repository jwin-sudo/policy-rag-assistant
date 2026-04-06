from __future__ import annotations

import argparse
import json
import re
import statistics
import time
from pathlib import Path

import requests


def parse_questions(eval_file: Path) -> list[dict[str, str]]:
    text = eval_file.read_text(encoding="utf-8")
    pattern = re.compile(
        r"\d+\. Question: (?P<question>.*?)\nGold answer: (?P<gold>.*?)\nExpected source: (?P<source>.*?)(?:\n\n|$)",
        re.DOTALL,
    )
    items: list[dict[str, str]] = []
    for match in pattern.finditer(text):
        items.append(
            {
                "question": match.group("question").strip(),
                "gold": match.group("gold").strip(),
                "source": match.group("source").strip(),
            }
        )
    return items


def run_eval(base_url: str, questions: list[dict[str, str]], limit: int) -> dict:
    outputs = []
    latencies = []

    for idx, item in enumerate(questions[:limit], start=1):
        resp = None
        for attempt in range(1, 4):
            try:
                resp = requests.post(
                    f"{base_url}/chat",
                    json={"question": item["question"]},
                    timeout=120,
                )
                if resp.status_code == 200:
                    break
            except requests.RequestException:
                resp = None

            if attempt < 3:
                time.sleep(1.0 * attempt)

        if resp is None or resp.status_code != 200:
            detail = "No response from /chat endpoint"
            if resp is not None:
                try:
                    detail = resp.json().get("detail", resp.text)
                except Exception:
                    detail = resp.text
            outputs.append(
                {
                    "id": idx,
                    "question": item["question"],
                    "error": detail,
                    "groundedness": None,
                    "citation_accuracy": None,
                }
            )
            continue

        payload = resp.json()
        latency_ms = payload.get("meta", {}).get("latency_ms", 0)
        latencies.append(latency_ms)
        outputs.append(
            {
                "id": idx,
                "question": item["question"],
                "gold": item["gold"],
                "expected_source": item["source"],
                "answer": payload.get("answer", ""),
                "citations": payload.get("citations", []),
                "latency_ms": latency_ms,
                "groundedness": "manual",
                "citation_accuracy": "manual",
            }
        )

    p50 = int(statistics.median(latencies)) if latencies else 0
    if not latencies:
        p95 = 0
    elif len(latencies) == 1:
        p95 = latencies[0]
    else:
        p95 = int(statistics.quantiles(latencies, n=100)[94])

    return {
        "total": len(outputs),
        "answered": len(latencies),
        "latency_p50_ms": p50,
        "latency_p95_ms": p95,
        "results": outputs,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Policy RAG evaluation set")
    parser.add_argument("--base-url", default="http://localhost:8000")
    parser.add_argument("--eval-file", default="evaluation/EVAL_QUESTIONS.md")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--out", default="evaluation/eval_run.json")
    args = parser.parse_args()

    questions = parse_questions(Path(args.eval_file))
    report = run_eval(args.base_url, questions, args.limit)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Saved report to {out_path}")
    print(f"Answered: {report['answered']} / {report['total']}")
    print(f"Latency p50: {report['latency_p50_ms']} ms")
    print(f"Latency p95: {report['latency_p95_ms']} ms")


if __name__ == "__main__":
    main()
