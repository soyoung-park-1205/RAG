from util import file_util
from search import search_news
from util import prompt_util
from ollama_processor import run_ollama
from preprocess import extract_keyword


if __name__ == '__main__':
    questions = file_util.read_lines("data/test.txt")
    for question in questions:
        """ get main keywords """
        keyword = extract_keyword.get_main_keyword(question)
        print(f"=====\n{question} -> {keyword}")
        """ get search result context """
        context = search_news.get_search_context(keyword)
        """ get prompt """
        prompt = prompt_util.build_context_prompt(context, question, keyword)
        print("deepseek origin: ", run_ollama.ask_model(question, "deepseek-r1:1.5b"))
        print("===")
        print("llama origin: ", run_ollama.ask_model(question, "llama3.2"))
        print("===")
        print("deepseek src answer: ", run_ollama.ask_model(prompt, "deepseek-r1:1.5b"))
        print("===")
        print("llama src answer: ", run_ollama.ask_model(prompt, "llama3.2"))
