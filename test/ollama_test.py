import subprocess


def ask_deepseek(prompt: str) -> str:
    try:
        # echo "질문" | ollama_processor run deepseek-r1
        command = f"echo \"{prompt}\" | ollama run deepseek-coder:6.7b"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            print("오류 발생:", result.stderr)
            return "❌ 응답 실패"

        return result.stdout.strip()

    except Exception as e:
        print("예외 발생:", str(e))
        return "❌ 예외 발생"


if __name__ == "__main__":
    question = "잘자 고마워"
    answer = ask_deepseek(question)
    print("💬 DeepSeek 응답:\n", answer)
