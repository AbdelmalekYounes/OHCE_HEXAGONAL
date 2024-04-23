from flask import Flask, request, jsonify
from domain.ohce import OHCE, Language

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    lang = request.headers.get('Accept-Language', 'English')
    language = Language(lang)
    ohce = OHCE(language)
    input_text = request.json.get('input')
    
    if input_text.lower() == 'exit':
        farewell = ohce.language.goodbye()
        return jsonify({'response': farewell})
    
    response = ohce.analyze_string(input_text)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
