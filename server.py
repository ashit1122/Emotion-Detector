from flask import Flask, request, jsonify
from emotion_detector.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route('/predict_emotion', methods=['POST'])
def predict_emotion():
	data = request.get_json()
	text = data.get('text', '')
	
	if not text.strip():
		return jsonify({"error": "Input text is empty"}), 400
	result = emotion_predictor(text)
	return jsonify(result)

if __name__ == "__main__":
	app.run(debug=True)
