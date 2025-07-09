import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def query_mistral(prompt: str, system_prompt: str = None):
    payload = {
        "model": "mistral",  
        "prompt": prompt,
        "stream": False,
    }
    if system_prompt:
        payload["system"] = system_prompt

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return f"[ERROR] Unable to contact Mistral model: {e}"
