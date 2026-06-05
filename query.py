import os

from dotenv import load_dotenv
from groq import Groq

from retrieve import retrieve

load_dotenv()

GROQ_MODEL = "llama-3.3-70b-versatile"
TOP_K      = 5

_groq = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM_PROMPT = """You are a Teamfight Tactics (TFT) guide assistant.
Answer the user's question using ONLY the information in the provided documents.
Do not use any knowledge from your training data.
If the documents do not contain enough information to answer, respond with exactly:
"I don't have enough information on that topic based on my sources."
Do not speculate or add information beyond what the documents state."""


def ask(question: str, k: int = TOP_K) -> dict:
    chunks = retrieve(question, k=k)

    context = "\n\n---\n\n".join(c["text"] for c in chunks)

    # Source attribution is pulled from retrieval results — not left to the LLM
    sources = list(dict.fromkeys(c["source"] for c in chunks))

    user_prompt = f"Documents:\n{context}\n\nQuestion: {question}"

    response = _groq.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_prompt},
        ],
    )

    return {
        "answer":  response.choices[0].message.content.strip(),
        "sources": sources,
    }


def main():
    test_queries = [
        "How much interest will I get if I have 50 gold saved?",
        "If I am playing for a 3 cost reroll composition, what level should I be rolling my gold?",
        "Is it better to have my carries placed in the front of the board or back of the board?",
    ]

    print("=== TFT RAG Pipeline — Grounded Generation Test ===\n")

    for question in test_queries:
        print("=" * 70)
        print(f"QUESTION: {question}\n")
        result = ask(question)
        print(f"ANSWER:\n{result['answer']}\n")
        print(f"SOURCES: {', '.join(result['sources'])}")
        print()


if __name__ == "__main__":
    main()
