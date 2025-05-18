from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph

from graph.retriever import add_main_keyword, add_naver_news_search, empty_node
from graph.condition_checker import has_keyword, is_origin, needs_search, is_relevance
from graph.llm import llm_answer, llm_answer_search

from graph.state import MyState


memory = MemorySaver()
config = {"configurable": {"thread_id": "1"}}

# LangGraph workflow 정의
workflow = StateGraph(state_schema=MyState)
workflow.add_node("needs_search", empty_node)
# retriever - extract keyword
workflow.add_node("extract_keyword", add_main_keyword)
# retriever (NAVER search API)
workflow.add_node("naver_searcher", add_naver_news_search)
workflow.add_node("relevance_check", empty_node)
# call LLM
workflow.add_node("llm_answer", llm_answer)
workflow.add_node("llm_answer_search", llm_answer_search)

# check origin
workflow.add_conditional_edges(START,
   is_origin,
   {
       False : "llm_answer",
       True : "needs_search"
   }
)
# decision to use searched context
workflow.add_conditional_edges("needs_search",
    needs_search,
    {
        False : "llm_answer",
        True : "extract_keyword"
     }
)
# has keyword -> search, no keyword -> LLM
workflow.add_conditional_edges(
    "extract_keyword",
    has_keyword,
    {
        False : "llm_answer",
        True : "naver_searcher"
     }
)
workflow.add_edge("naver_searcher", "relevance_check")
# relevance check
workflow.add_conditional_edges(
    "relevance_check",
        is_relevance,
           {
               False : "llm_answer",
               True: "llm_answer_search"
           })

workflow.set_finish_point("llm_answer")
workflow.set_finish_point("llm_answer_search")
app = workflow.compile(checkpointer=memory)

print(app.get_graph(xray=True).draw_mermaid())

def ask_model_search(origin: bool, model_nm: str, question: str):
    input_data = {
        "question": question,
        "messages": [],
        "model_nm": model_nm,
        "thread_id": "1",
        "origin": origin
    }

    final_state = None
    for event in app.stream(input_data, config, stream_mode="values"):
        final_state = event
    if final_state:
        return final_state.get("response", "")
    else:
        return "죄송합니다. 질문을 이해하지 못했어요."
