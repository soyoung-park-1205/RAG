from preprocess import extract_keyword
from graph.state import MyState
from search import search_news


def add_main_keyword(state: MyState):
    keyword = extract_keyword.get_main_keyword(state["question"])
    state["keyword"] = keyword
    return state


def add_naver_news_search(state: MyState):
    state["context"] = search_news.get_search_context(state["keyword"])
    return state
