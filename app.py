from flask import Flask, render_template, request, jsonify
from langchain_community.llms import Ollama

app = Flask(__name__)
llm = Ollama(model="llama3")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']

    try:
        response = ""
        for chunk in llm.stream(prompt, stop=['']):
            response += chunk

        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': f"An error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
