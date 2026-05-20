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
    context = "\n\n".join([f"{r['title']}: {r['content']}" for r in result['results']])
    sources = "\n".join([f"- {r['title']}: {r['url']}" for r in result['results']])
    return context, sources

def search_and_ask(query):
    context, sources = search(query)
    prompt = f"""You are a polite and professional search assistant.
            Using the search results below, provide a clear and concise answer in 2-3 sentences.
            Be formal, accurate, and straight to the point.
            Do not add unnecessary explanations or contradict the search results.


SEARCH RESULTS:
{context}

QUESTION: {query}

Direct answer:"""
    
    answer = ask(prompt)
    full_response = f"{answer}\n\n---\n📚 Sources:\n{sources}"
    return full_response

demo = gr.Interface(
    fn=search_and_ask,
    inputs=gr.Textbox(label="Ask anything", placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Answer"),
    title="Local Search Bot",
    description="Powered by phi3:mini + Tavily — real-time search with source citations"
)

demo.launch()