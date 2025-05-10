from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get_answers', methods=['POST'])
def get_answers():
    question = request.json.get('question', '')
    if not question:
        return jsonify({'error': '질문이 필요합니다.'}), 400

    # /answer API 호출 (gemma3.1만)
    response = requests.get(
        'http://localhost:15000/answer',
        params={'question': question,
                'model': 'gemma3:4b',
                'origin': 'true'}
    )
    answer = response.json().get('answer', '응답 없음')

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(port=5003, debug=True)
