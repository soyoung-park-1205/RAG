import json
from flask import request, Flask

<<<<<<< HEAD
from chain.langchain_service import ask_model_search
=======
from graph.langgraph_service import ask_model_search
>>>>>>> master


app = Flask(__name__)

memory_pool = {}

@app.route("/answer", methods=['GET'])
def get_answer():
    origin = request.args.get("origin", 'false').lower() == 'true'
    model_nm = request.args.get("model", '')
    question = request.args.get("question", '')
    response = ask_model_search(origin, model_nm, question)
    response = json.loads(response[response.index('{') : response.rindex('}')+1])
    return response


if __name__ == "__main__":
    app.run('0.0.0.0', port=15000)
