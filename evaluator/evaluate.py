import json
from ollama.run_ollama import ask_model
from util.prompt_util import build_judge_prompt


def judge_result(question, answer, context, model_nm):
    evaluate_prompt = build_judge_prompt()
    prompt = evaluate_prompt.format(question = question,
                                    context = context,
                                    answer = answer)
    print("judge prompt: ", prompt)
    response = ask_model(prompt, model_nm)
    print(response)
    if not response.startswith("{"):
        response = response[response.index("{") : response.index("}") + 1]
    return response
