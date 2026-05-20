import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3:mini",
        "prompt": "Hello! What can you do?",
        "stream": False
    }
)

print(response.json()["response"])