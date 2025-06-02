"""Flask app for emotion detection API."""

from flask import Flask, request, jsonify
from emotion_detector.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route('/predict_emotion', methods=['POST'])
def predict_emotion():
<<<<<<< HEAD
=======
    """
    Handle POST request to predict emotion from text input.
    Returns JSON with emotions or error.
    """
>>>>>>> 5d9e71f (Add error handling and validation, update tests)
    data = request.get_json()
    text = data.get('text', '')

    result, status_code = emotion_predictor(text)
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)
