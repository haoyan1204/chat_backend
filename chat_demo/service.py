from flask import Flask, jsonify, request, Response
from api_demo import chat

app = Flask(__name__)

# chat interface，now use zhipuai interface
@app.route('/chat', methods=['post'])
def set_response():
    if request.is_json:
        data = request.get_json()

        question = data.get('question', '')

        response = {
            "message": chat(question)
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 8200
    app.run(ip, port, debug=True)