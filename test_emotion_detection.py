import unittest
import EmotionDetection as e

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        cases = {
            'I am glad this happened': 'joy',
            'I am really mad about this': 'anger',
            'I feel disgusted just hearing about this': 'disgust',
            'I am so sad about this': 'sadness',
            'I am really afraid that this will happen' :'fear'
        }

        for key, value in cases.items():
            dominant_emotion = e.emotion_detector(key)['dominant_emotion']
            self.assertEqual(dominant_emotion, value)

unittest.main()