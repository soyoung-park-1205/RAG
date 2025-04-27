from langchain_ollama.llms import OllamaLLM

from preprocess import extract_keyword
from search import search_news

from util import prompt_util


def ask_model(origin: bool, model_nm: str, question: str):
    model = OllamaLLM(model=model_nm, temperature=0.7)

    """ get main keywords """
    keyword = extract_keyword.get_main_keyword(question)
    if not origin:
        prompt = prompt_util.build_context_prompt()
        context = search_news.get_search_context(keyword)
        chain = prompt | model

        response = chain.invoke({
            "keyword": keyword,
            "context": context,
            "question": question
        })
    else:
        response = model.invoke(question)

    return response
