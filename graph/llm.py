from graph.state import MyState
from util import prompt_util

from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage

from langchain_ollama.llms import OllamaLLM


def call_model(state: MyState):
    # messages만 추출
    current_messages = state["messages"]
    # 새로운 질문 메시지 추가
    updated_messages = add_messages(current_messages, [HumanMessage(content=state["question"])])

    # 프롬프트 선택
    if state.get("context"):
        prompt = prompt_util.build_context_prompt()
    else:
        prompt = prompt_util.build_question_prompt()

    # 프롬프트 렌더링
    prompt_str = prompt.format(
        question=state["question"],
        keyword=state.get("keyword", ""),
        context=state.get("context", ""),
        messages="\n".join([m.content for m in state["messages"]]),
    )

    # LLM 실행
    model = OllamaLLM(model=state["model_nm"], temperature=0.7)
    result = model.invoke(prompt_str)

    # state 업데이트 (messages는 계속 쌓임)
    return {
        **state,
        "messages": updated_messages,
        "response": result
    }
