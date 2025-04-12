import subprocess


def ask_deepseek(prompt: str):
    try:
        command = f"echo \"{prompt}\" | ollama run deepseek-coder:6.7b"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            return None

        return result.stdout.strip()

    except Exception as e:
        print("Exception:", str(e))
        return None
