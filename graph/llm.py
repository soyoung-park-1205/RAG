from graph.state import MyState
from util import prompt_util

from langchain_ollama.llms import OllamaLLM


def llm_answer(state: MyState):
    prompt = prompt_util.build_question_prompt()

    return get_lllm_answer(prompt, state)


def llm_answer_search(state: MyState):
    prompt = prompt_util.build_context_prompt()

    return get_lllm_answer(prompt, state)


def get_lllm_answer(prompt, state: MyState):
    # messages만 추출
    current_messages = state["messages"]

    prompt_str = prompt.format(
        question=state["question"],
        keyword=state.get("keyword", ""),
        context=state.get("context", ""),
        messages="\n".join([m.content for m in state["messages"]]),
    )

    # LLM 실행
    model = OllamaLLM(model=state["model_nm"], temperature=0.7)
    result = model.invoke(prompt_str)

    return {
        **state,
        "messages": [("user", state["question"]), ("assistant", result)],
        "response": result
    }
