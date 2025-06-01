import unittest
from emotion_detector.emotion_detector import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
	def test_valid_input(self):
		result=emotion_predictor("I am happy today!")
		self.assertIn("emotion", result)
		self.assertIn(result["emotion"],["joy","sadness","anger","fear","disgust"])
		self.assertTrue(all(e in result for e in ["joy","sadness","anger","fear","disgust"]))
	def test_empty_input(self):
		result=emotion_predictor("")
		self.assertIn("error",result)
		self.assertEqual(result["error"], "Input text is empty")
if __name__== "__main__":
	unittest.main()

