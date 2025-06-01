def emotion_predictor(text):
	if not text.strip():
		return {"error": "Input text is empty"}
	emotions={
		"joy": 0.7,
		"sadness": 0.1,
		"anger": 0.05,
		"fear": 0.1,
		"disgust": 0.5}
	return emotions

