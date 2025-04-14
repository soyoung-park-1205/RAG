from flask import request, Flask
from rag import search_news
from util import prompt_util
from preprocess import extract_keyword
from ollama.run_ollama import ask_model

app = Flask(__name__)


@app.route("/answer", methods=['GET'])
def get_answer():
    origin = request.args.get("origin", 'false').lower() == 'true'
    model_nm = request.args.get("model", '')
    question = request.args.get("question", '')
    if origin:
        prompt = question
    else:
        """ get main keywords """
        keyword = extract_keyword.get_main_keyword(question)
        """ get search result context """
        context = search_news.get_search_context(keyword)
        """ get prompt """
        prompt = prompt_util.build_context_prompt(context, question, keyword)
    return ask_model(prompt, model_nm)


if __name__ == "__main__":
    app.run()
