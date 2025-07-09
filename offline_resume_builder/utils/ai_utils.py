

import requests

def query_llama3(prompt, system_msg=None):
    """
    Sends a prompt to the locally running LLaMA 3 model using Ollama API
    and returns the response content.
    """
    payload = {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": system_msg or "You are an expert resume assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/chat", json=payload)
        result = response.json()
        return result["message"]["content"]
    except Exception as e:
        return f"[AI Error] {e}"
