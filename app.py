from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.post("/ai/predict")
@cross_origin()
def predict():
    text = request.get_json().get("message")
    # checking if text is valid;
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)