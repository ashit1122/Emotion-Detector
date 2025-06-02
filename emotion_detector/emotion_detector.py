def emotion_predictor(text):
    if not text.strip():
        # Return error and status code 400 for empty input
        return {"error": "Input text is empty"}, 400

    emotions = {
        "joy": 0.7,
        "sadness": 0.1,
        "anger": 0.05,
        "fear": 0.1,
        "disgust": 0.5
    }

    dominant_emotion = max(emotions, key=emotions.get)
    result = {"emotion": dominant_emotion}
    result.update(emotions)

    # Return result and status code 200 for success
    return result, 200
