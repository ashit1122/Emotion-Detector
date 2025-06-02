def validate_output(output):
    expected_emotions = {"joy", "sadness", "anger", "fear", "disgust"}

    if "emotion" not in output:
        return False, "Missing 'emotion' key."

    if not expected_emotions.issubset(output.keys()):
        return False, "Some emotion scores are missing."

    for emotion in expected_emotions:
        score = output.get(emotion)
        if not isinstance(score, (float, int)):
            return False, f"Score for '{emotion}' is not a number."
        if score < 0 or score > 1:
            return False, f"Score for '{emotion}' is out of range (0-1)."

    dominant = output["emotion"]
    highest_score_emotion = max(expected_emotions, key=lambda e: output[e])
    if dominant != highest_score_emotion:
        return False, f"Dominant emotion '{dominant}' does not match highest score emotion '{highest_score_emotion}'."

    return True, "Output is valid."
