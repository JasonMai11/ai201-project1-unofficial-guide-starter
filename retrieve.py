import chromadb
from sentence_transformers import SentenceTransformer

CHROMA_DIR = "chroma_db"
COLLECTION = "tft_guides"
MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K      = 5

# Initialized once at import time — reused across all retrieve() calls
_model      = SentenceTransformer(MODEL_NAME)
_client     = chromadb.PersistentClient(path=CHROMA_DIR)
_collection = _client.get_collection(name=COLLECTION)


def retrieve(query: str, k: int = TOP_K) -> list:
    embedding = _model.encode([query]).tolist()
    results   = _collection.query(query_embeddings=embedding, n_results=k)

    return [
        {
            "id":       results["ids"][0][i],
            "source":   results["metadatas"][0][i]["source"],
            "text":     results["documents"][0][i],
            "distance": results["distances"][0][i],
        }
        for i in range(len(results["ids"][0]))
    ]


def main():
    eval_queries = [
        {
            "question": "How much interest will I get if I have 50 gold saved?",
            "expected": "5 gold from interest",
        },
        {
            "question": "Is it better to have my carries placed in the front of the board or back of the board?",
            "expected": "Depends — ranged carries perform better at the bottom",
        },
        {
            "question": "If I am playing for a 3 cost reroll composition, what level should I be rolling my gold?",
            "expected": "Level 7",
        },
        {
            "question": "If I am playing for a fast 9 composition, how much gold should I be saving?",
            "expected": "Save 50 gold and use the remaining (while staying above 50) to level to 9",
        },
        {
            "question": "What item is flexible to put on any unit?",
            "expected": "Twisted Fate Gloves — guarantee two random items each round",
        },
    ]

    print("=== TFT RAG Pipeline — Retrieval Evaluation ===\n")

    for entry in eval_queries:
        query    = entry["question"]
        expected = entry["expected"]
        chunks   = retrieve(query)

        print("=" * 70)
        print(f"QUERY:    {query}")
        print(f"EXPECTED: {expected}")
        print(f"TOP-{TOP_K} RESULTS:")
        for rank, chunk in enumerate(chunks, 1):
            print(f"\n  [{rank}] source={chunk['source']}  distance={chunk['distance']:.4f}")
            print(f"       {chunk['text'][:300]}...")
        print()


if __name__ == "__main__":
    main()
