import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

CHUNKS_FILE = Path("chunks.json")
CHROMA_DIR  = "chroma_db"
COLLECTION  = "tft_guides"
MODEL_NAME  = "all-MiniLM-L6-v2"


def main():
    print("=== TFT RAG Pipeline — Embedding + Vector Store ===\n")

    # Step 1 — Load chunks
    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    print(f"Loaded {len(chunks)} chunks from {CHUNKS_FILE}.\n")

    # Step 2 — Generate embeddings
    print(f"Loading embedding model '{MODEL_NAME}'...")
    model = SentenceTransformer(MODEL_NAME)
    texts = [c["text"] for c in chunks]
    print("Generating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)

    # Step 3 — Load into ChromaDB
    print(f"\nConnecting to ChromaDB at '{CHROMA_DIR}'...")
    client     = chromadb.PersistentClient(path=CHROMA_DIR)
    try:
        client.delete_collection(name=COLLECTION)
    except Exception:
        pass
    collection = client.create_collection(name=COLLECTION)

    collection.upsert(
        ids        = [c["id"]     for c in chunks],
        embeddings = embeddings.tolist(),
        documents  = [c["text"]   for c in chunks],
        metadatas  = [{"source": c["source"]} for c in chunks],
    )
    print(f"Collection '{COLLECTION}' now has {collection.count()} entries.\n")

    # Step 4 — Smoke-test retrieval
    print("--- Smoke Test: 'how does economy work in TFT' ---")
    results = collection.query(
        query_embeddings=model.encode(["how does economy work in TFT"]).tolist(),
        n_results=3,
    )
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        print(f"\n[{meta['source']}]")
        print(doc[:200] + "...")
    print()


if __name__ == "__main__":
    main()
