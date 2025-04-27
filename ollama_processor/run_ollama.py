import requests


def ask_model(prompt: str, model_nm: str):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model_nm, "prompt": prompt, "stream": False}
        )
        return response.json()["response"]
    except Exception as e:
        print("Exception:", str(e))
        return None

