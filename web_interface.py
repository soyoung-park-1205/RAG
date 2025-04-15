from flask import Flask, render_template, request, jsonify
import requests

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
            'llama3.2': '',
            'gemma3:1b': ''
        },
        'origin_false': {
            'llama3.2': '',
            'gemma3:1b': ''
        }
    }
    
    # Get answers with origin=True
    for model in ['llama3.2', 'gemma3:1b']:
        response = requests.get(
            'http://127.0.0.1:5000/answer',
            params={
                'question': question,
                'model': model,
                'origin': 'true'
            }
        )
        results['origin_true'][model] = response.text
    
    # Get answers with origin=False
    for model in ['llama3.2', 'gemma3:1b']:
        response = requests.get(
            'http://127.0.0.1:5000/answer',
            params={
                'question': question,
                'model': model,
                'origin': 'false'
            }
        )
        results['origin_false'][model] = response.text
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5001) 