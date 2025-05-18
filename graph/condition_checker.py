import json

from graph.state import MyState
from util import prompt_util

from langchain_ollama.llms import OllamaLLM


def has_keyword(state: MyState):
    return state["keyword"] != ""

def is_origin(state: MyState):
    return state["origin"]

def needs_search(state: MyState):

    prompt = prompt_util.build_search_decision_prompt()

    # 프롬프트 렌더링
    prompt_str = prompt.format(
        question=state["question"]
    )

    # LLM 실행
    model = OllamaLLM(model=state["model_nm"], temperature=0.5)
    response = model.invoke(prompt_str)
    result_json = json.loads(response[response.index('{') : response.rindex('}')+1])
    return True if result_json["fit_condition"] == '1' else False


def is_relevance(state: MyState):
    prompt = prompt_util.build_doc_relevance_prompt()

    prompt_str = prompt.format(
        question=state["question"],
        document=state["context"]
    )

    # LLM 실행
    model = OllamaLLM(model=state["model_nm"], temperature=0.5)
    response = model.invoke(prompt_str)
    result_json = json.loads(response[response.index('{'): response.rindex('}') + 1])
    return True if result_json['relevance'] == 1 else False
