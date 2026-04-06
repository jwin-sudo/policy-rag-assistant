# AI Tooling

## Tools Used
- GitHub Copilot Chat in VS Code for implementation support, debugging, and refactoring.
- Built-in terminal workflows (pip, uvicorn, git, and CI checks) to validate AI-generated changes in a real environment.

## How I Used AI in This Project
- Scaffolded and iterated core components for ingestion, retrieval, generation, API endpoints, and evaluation scripts.
- Used AI assistance to diagnose CI failures and dependency/import issues (for example, LangChain deprecations and import-time initialization problems).
- Generated and refined project documentation, including setup instructions and evaluation reporting structure.
- Used AI to speed up repetitive tasks (boilerplate, schema shaping, config wiring) while manually reviewing architecture and behavior decisions.

## What Worked Well
- Rapid prototyping of end-to-end features (FastAPI routes, RAG service flow, evaluation pipeline).
- Fast root-cause analysis for runtime and CI errors when logs were available.
- Helpful code suggestions for migration updates and cleanup when package APIs changed.
- Strong productivity gains for documentation drafting and consistency across files.

## What Did Not Work Well
- Some generated code initially assumed package APIs that were deprecated or version-mismatched, requiring manual fixes.
- AI suggestions occasionally overfit to generic patterns and needed project-specific constraints to be reliable.
- Citation quality and retrieval tuning still required iterative manual testing; AI alone was not enough to guarantee quality targets.
- Performance/latency optimization required empirical benchmarking rather than one-shot AI suggestions.

## Practical Workflow That Helped
1. Use AI to draft or patch code quickly.
2. Immediately run local checks (import/start/eval) and inspect logs.
3. Keep only validated changes; revise prompts or code where behavior diverges.
4. Document final decisions and metrics after measured runs.

## Summary
AI tooling significantly accelerated development and debugging, but best results came from combining AI-assisted coding with manual review, reproducible tests, and benchmark-driven iteration.
