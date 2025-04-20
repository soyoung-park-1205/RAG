from flask import Flask, render_template, request, jsonify
import requests
import time

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
            'llama3.2': {'answer': '', 'time': 0},
            'gemma3:1b': {'answer': '', 'time': 0}
        },
        'origin_false': {
            'llama3.2': {'answer': '', 'time': 0},
            'gemma3:1b': {'answer': '', 'time': 0}
        }
    }
    
    # Get answers with origin=True
    for model in ['llama3.2', 'gemma3:1b']:
        start_time = time.time()
        response = requests.get(
            'http://localhost:5000/answer',
            params={
                'question': question,
                'model': model,
                'origin': 'true'
            }
        )
        end_time = time.time()
        results['origin_true'][model]['answer'] = response.text
        results['origin_true'][model]['time'] = end_time - start_time
    
    # Get answers with origin=False
    for model in ['llama3.2', 'gemma3:1b']:
        start_time = time.time()
        response = requests.get(
            'http://localhost:5000/answer',
            params={
                'question': question,
                'model': model,
                'origin': 'false'
            }
        )
        end_time = time.time()
        results['origin_false'][model]['answer'] = response.text
        results['origin_false'][model]['time'] = end_time - start_time
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5001)