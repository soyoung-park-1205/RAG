from langchain_ollama.llms import OllamaLLM
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.graph.message import add_messages

from preprocess import extract_keyword
from search import search_news

from util import prompt_util


class MyState(MessagesState):
    question: str
    keyword: str
    context: str
    response: str
    thread_id: str
    model_nm: str

memory = MemorySaver()
config = {"configurable": {"thread_id": "1"}}


def call_model(state):
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


# LangGraph workflow 정의
workflow = StateGraph(state_schema=MyState)
workflow.add_node("model", call_model)
workflow.add_edge(START, "model")
workflow.set_finish_point("model")
app = workflow.compile(checkpointer=memory)


def ask_model_search(origin: bool, model_nm: str, question: str):
    keyword = extract_keyword.get_main_keyword(question)

    if not origin:
        context = search_news.get_search_context(keyword)
    else:
        context = ""

    input_data = {
        "question": question,
        "keyword": keyword,
        "context": context,
        "messages": [],
        "model_nm": model_nm,
        "thread_id": "1"
    }

    final_state = None
    for event in app.stream(input_data, config, stream_mode="values"):
        final_state = event

    if final_state:
        return final_state.get("response", "")
    else:
        return "죄송합니다. 질문을 이해하지 못했어요."
