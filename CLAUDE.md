# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is CodePath AI201 Project 1 — a RAG (Retrieval-Augmented Generation) pipeline called "The Unofficial Guide." The domain is Team Fight Tactics (TFT) strategy/climbing guides. The pipeline answers player questions by retrieving relevant chunks from collected web documents and generating grounded answers via an LLM.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `GROQ_API_KEY` (free key at https://console.groq.com — no credit card required).

## Pipeline Architecture

Five sequential stages:

1. **Document Ingestion** — fetch/load source documents into `documents/`
2. **Chunking** — split text into ~500-character chunks with ~100-character overlap
3. **Embedding + Vector Store** — embed chunks with `sentence-transformers` (`all-MiniLM-L6-v2`), store in ChromaDB (`chroma_db/` — gitignored)
4. **Retrieval** — top-k similarity search against ChromaDB for a user query
5. **Generation** — pass retrieved chunks as context to Groq LLM; system prompt must enforce grounding (model answers only from retrieved context)

## Key Decisions from `planning.md`

- Chunk size: 500 chars, overlap: 100 chars
- Embedding model: `sentence-transformers` `all-MiniLM-L6-v2`
- LLM: Groq API (configured via `GROQ_API_KEY`)
- UI: Gradio or Streamlit (uncomment the relevant line in `requirements.txt` when ready)
- PDF support: uncomment `pdfplumber` in `requirements.txt` if any source documents are PDFs

## Source Documents

13 TFT guides (URLs in `planning.md`) covering: beginner fundamentals, economy management, leveling strategy, unit positioning, item usage, and meta comps. Place scraped/downloaded content in `documents/`.

## Evaluation

Five test questions are defined in `planning.md` with expected answers. Run these through the completed pipeline to measure retrieval quality and response accuracy before submitting.
