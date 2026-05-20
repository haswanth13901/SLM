import gradio as gr
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

def search_and_ask(query):
    context = search(query)
    prompt = f"""You are a search assistant. Answer using ONLY the search results below.
Do NOT use your training data. Do NOT say your knowledge is limited.
Use the search results directly to answer accurately.

SEARCH RESULTS:
{context}

QUESTION: {query}

Answer based strictly on the search results above:"""
    return ask(prompt)

demo = gr.Interface(
    fn=search_and_ask,
    inputs=gr.Textbox(label="Ask anything", placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Answer"),
    title="Local Search Bot",
    description="Powered by phi3:mini + Tavily — running locally with real-time search"
)

demo.launch()