# Local AI Search Bot

A locally running AI search bot built on a budget laptop — no GPU, no expensive hardware. Designed to squeeze maximum capability out of limited resources.

## Hardware Context

This project was built and runs on:

- **CPU:** Intel Core i7-10510U @ 1.80GHz (4 cores, 8 threads)
- **RAM:** 8GB (no dedicated GPU)
- **OS:** Windows 11 Home

No cloud compute. No GPU. Just a mid-range laptop running a full AI search pipeline.

## What It Does

Ask it anything — current news, today's weather, live sports scores, recent events. It searches the web in real time and uses a local AI model to summarize and answer in plain English.

## How It Works — Architecture

```
User Question
      ↓
Tavily Search API (real-time web search)
      ↓
Top 3 search results fetched as context
      ↓
Context + Question injected into prompt (RAG)
      ↓
phi3:mini model reasons over the context
      ↓
Answer returned via Gradio UI or terminal
```

## RAG — Retrieval Augmented Generation

This project implements RAG at its core. Instead of relying on the model's training data (which has a knowledge cutoff), the bot:

1. **Retrieves** — Tavily fetches live, relevant web results for every query
2. **Augments** — search results are injected directly into the model prompt as context
3. **Generates** — phi3:mini answers strictly based on that retrieved context

This means the bot can answer questions about today's news, live scores, current weather, and recent events — things a standard local model cannot do.

## Tech Stack

| Component | Tool | Purpose |
|---|---|---|
| Local LLM | Ollama + phi3:mini | AI reasoning engine |
| Real-time search | Tavily API | Live web retrieval |
| UI | Gradio | Browser-based chat interface |
| Terminal version | Python | Lightweight CLI interface |
| Secret management | python-dotenv | Keeps API keys out of GitHub |

## Why phi3:mini

Chosen specifically for this hardware:

- Only 2.3GB RAM usage — fits comfortably in 8GB
- Q4 quantized — optimized for CPU inference
- Fast enough for real conversations on CPU
- Microsoft's most efficient small model

Larger models (7B+) were tested and were too slow for practical use on this hardware.

## Features

- Real-time web search on every query via Tavily
- RAG pipeline — model never relies on stale training data
- Gradio web UI — runs in browser at localhost:7860
- Terminal mode — lightweight CLI version
- Fully local — your questions never leave your machine (except for search)
- API keys secured via .env file

## Setup

### Prerequisites
- Python 3.10+
- Ollama installed from ollama.com

### Installation

```bash
# Pull the model
ollama pull phi3:mini

# Clone the repo
git clone https://github.com/haswanth13901/SLM.git
cd SLM

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your Tavily API key
echo TAVILY_API_KEY=your-key-here > .env
```

### Run

**Browser UI:**
```bash
python app.py
```
Open http://127.0.0.1:7860 in your browser.

**Terminal version:**
```bash
python searchbot.py
```

## Project Structure

```
SLM/
├── .env                  # API keys (gitignored)
├── .gitignore
├── app.py                # Gradio UI entry point
├── searchbot.py          # Terminal version
├── requirements.txt
├── README.md
└── tests/
    └── test.py           # API connection test
```

## Key Learnings

- Running LLMs efficiently on CPU-only hardware
- Implementing RAG from scratch without frameworks
- Prompt engineering to override model knowledge cutoff
- Connecting local models to live web data
- Building a full AI application end to end on a budget machine
