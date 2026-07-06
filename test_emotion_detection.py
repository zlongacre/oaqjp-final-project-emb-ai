from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        dominant = max(result, key=result.get)
        self.assertEqual(dominant, 'joy')

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        dominant = max(result, key=result.get)
        self.assertEqual(dominant, 'anger')

    def test_digust(self):
        result = emotion_detector("I feel disgusted just hearing this")
        dominant = max(result, key=result.get)
        self.assertEqual(dominant, 'disgust')

    def test_sadness(self):
        result = emotion_detector("Iam so sad about this")
        dominant = max(result, key=result.get)
        self.assertEqual(dominant, 'sadness')

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        dominant = max(result, key=result.get)
        self.assertEqual(dominant, 'fear')

if __name__ == '__main__':
    unittest.main()