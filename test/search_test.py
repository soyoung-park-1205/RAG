from search import search_news
from util import prompt_util
from ollama_processor import run_ollama
from preprocess import extract_keyword

if __name__ == '__main__':
    question = "잘자 고마워"
    keyword = extract_keyword.get_main_keyword(question)
    print("keyword: ", keyword)
    context = search_news.get_search_context(keyword)
    context_prompt = prompt_util.build_context_prompt()
    prompt = context_prompt.format(context=context, question=question, keyword=keyword, messages="")
    print("prompt: ", prompt)
    print("===")
    print("deepseek origin: ", run_ollama.ask_model(question, "gemma3:1b"))
    print("===")
    print("llama origin: ", run_ollama.ask_model(question, "llama3.2"))
    print("===")
    print("deepseek src answer: ", run_ollama.ask_model(prompt, "gemma3:1b"))
    print("===")
    print("llama src answer: ", run_ollama.ask_model(prompt, "llama3.2"))
