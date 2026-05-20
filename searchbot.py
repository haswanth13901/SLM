import requests
import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def ask(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "phi3:mini", "prompt": prompt, "stream": False}
    )
    return r.json()["response"]

def search(query):
    result = client.search(query, max_results=3)
    return "\n\n".join([f"{r['title']}: {r['content']}" for r in result['results']])

def main():
    print("Local Search Bot ready. Type 'quit' to exit.\n")
    while True:
        query = input("You: ").strip()
        if query.lower() in ("quit", "exit"):
            break
        if not query:
            continue
        print("Searching...")
        context = search(query)
        prompt = f"""You are a search assistant. Answer using ONLY the search results below.
Do NOT use your training data. Do NOT say your knowledge is limited.

SEARCH RESULTS:
{context}

QUESTION: {query}

Answer:"""
        print("Bot:", ask(prompt), "\n")

if __name__ == "__main__":
    main()