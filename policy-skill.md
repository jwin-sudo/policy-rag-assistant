Use free or zero-cost options when possible e.g., OpenRouter’s free tier
(https://openrouter.ai/docs/api-reference/limits), Groq
(https://console.groq.com/docs/rate-limits), or your own paid API keys if you have them.
For embedding models, free-tier options are available from Cohere, Voyage,
HuggingFace and others
Complete the following steps to fully develop, deploy, and evaluate your application:
1. Environment and Reproducibility
○
Create a virtual environment (e.g., venv, conda).
○
List dependencies in requirements.txt (or environment.yml).
○
Provide a README.md with setup + run instructions.
○
Set fixed seeds where/if applicable (for deterministic chunking or
evaluation sampling).
2. Ingestion and Indexing
○
Parse & clean documents (handle PDFs/HTML/md/txt).
○
Chunk documents (e.g., by headings or token windows with overlap).
○
Embed chunks with a free embedding model or a free-tier API.
○
Store the embedded document chunks in a local or lightweight vector
database (e.g. Chroma or optionally a cloud-hosted vector store like
Pinecone, etc.)
Store vectors in a local/vector DB or cloud DB (e.g., Chroma, Pinecone, etc.)
3. Retrieval and Generation (RAG)
To build your RAG pipeline you may use frameworks such as LangChain to
handle retrieval, prompt chaining, and API calls, or implement these
manually.
Implement Top-k retrieval with optional re-ranking.
○
○
○
© 2025 Quantic Holdings, Inc. All rights reserved. 6/23/21 2
AI Engineering Project
○
Build a prompting strategy that injects retrieved chunks (and
citations/sources) into the LLM context.
○
Add basic guardrails:
■ Refuse to answer outside the corpus (“I can only answer about our
policies”),
■ Limit output length,
■ Always cite source doc IDs/titles for answers.
4. Web Application
○
Students can use Flask, Streamlit or alternative for the Web app. LangChain
is recommended for orchestration, but is optional.
○
Endpoints/UI:
■ / - Web chat interface - text box for user input
■ /chat - API endpoint that receives user questions (POST) and returns
model-generated answers with citations and snippets (link to source
and show snippet).
■ /health - returns simple status via JSON.
5. Deployment (Optional)
○
For production hosting use Render or Railway free tiers; students may
alternatively use any other free-tier providers of their choice.
○
Configure environment variables (e.g. API keys, model endpoints, DB
related etc.).
○
Ensure the app is publicly accessible at a shareable URL
○
If you do not deploy your application to production or staging, it must run
and be demoed locally
6. CI/CD
○
○
Minimal automated testing is suﬃcient for this assignment (a build/run
check, optional smoke test).
Create a GitHub Actions workflow that on push/PR:
■ Installs dependencies,
■ Runs a build/start check (e.g., python -m pip install -r
requirements.txt and python -c "import app" or pytest -q if you add
tests),
■ Optional: On success in main, deploy to your host (Render/Railway
action or via webhook/API).
7. Evaluation of the LLM Application
○
Provide a small evaluation set of 15–30 questions covering various policy
topics (PTO, security, expense, remote work, holidays, etc.). Report:
■ Answer Quality (required):
1. Groundedness: % of answers whose content is factually
consistent with and fully supported by the retrieved
© 2025 Quantic Holdings, Inc. All rights reserved. 6/23/21 3
AI Engineering Project
evidence—i.e., the answer contains no information that is
absent or contradicted in the context.
2. Citation Accuracy: % of answers whose listed citations
correctly point to the specific passage(s) that support the
information stated—i.e., the attribution is correct and not
misleading.
3. Exact/Partial Match (optional): % of answers that exactly or
partially match a short gold answer you provide.
■ System Metrics (required):
1. Latency (p50/p95) from request to answer for 10–20 queries.
■ Ablations (optional): compare retrieval k, chunk size, or prompt
variants.
8. Design Documentation
○
Briefly justify design choices (embedding model, chunking, k, prompt
format, vector store).