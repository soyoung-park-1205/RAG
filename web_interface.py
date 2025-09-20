import json

from flask import Flask, render_template, request, jsonify
import requests
import time
from evaluator.evaluate import judge_answer_by_nouns
from preprocess.extract_keyword import get_main_keyword
from search.search_news import get_search_context
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_answers', methods=['POST'])
def get_answers():
    question = request.json.get('question', '')
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    results = {
        'origin_true': {
            'gemma3:1b': {'answer': '', 'time': 0, 'evaluation': {'faithfulness': False}},
            'gpt-oss:20b': {'answer': '', 'time': 0, 'evaluation': {'faithfulness': False}}
        },
        'origin_false': {
            'gemma3:1b': {'answer': '', 'time': 0, 'evaluation': {'faithfulness': False}},
            'gpt-oss:20b': {'answer': '', 'time': 0, 'evaluation': {'faithfulness': False}}
        }
    }
    
    # Get answers with origin=True
    for model in ['gemma3:1b', 'gpt-oss:20b']:
        start_time = time.time()
        response = requests.get(
            'http://localhost:15000/answer',
            params={
                'question': question,
                'model': model,
                'origin': 'true'
            }
        )
        end_time = time.time()
        answer = response.json().get('answer')
        results['origin_true'][model]['answer'] = answer
        results['origin_true'][model]['time'] = end_time - start_time
        keyword = get_main_keyword(question)
        if not keyword:
            searched_context = get_search_context(question)
        else:
            searched_context = get_search_context(keyword)
        results['origin_true'][model]['evaluation'] = {
            #'faithfulness': eval_result.get('faithfulness', 0)
            'faithfulness' : judge_answer_by_nouns(answer, searched_context)
        }
    
    # Get answers with origin=False
    for model in ['gemma3:1b', 'gpt-oss:20b']:
        start_time = time.time()
        response = requests.get(
            'http://localhost:15000/answer',
            params={
                'question': question,
                'model': model,
                'origin': 'false'
            }
        )
        end_time = time.time()
        answer = response.json().get('answer')
        results['origin_false'][model]['answer'] = answer
        results['origin_false'][model]['time'] = end_time - start_time
        keyword = get_main_keyword(question)
        if not keyword:
            searched_context = get_search_context(question)
        else:
            searched_context = get_search_context(keyword)
        results['origin_false'][model]['evaluation'] = {
            'faithfulness': judge_answer_by_nouns(answer, searched_context)
        }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5001)
