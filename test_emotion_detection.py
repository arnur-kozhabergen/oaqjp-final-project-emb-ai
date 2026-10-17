"""Validate the five required emotions against the live Watson NLP service."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test the required course examples using genuine API responses."""

    def test_joy(self):
        """Recognize the required joyful statement."""
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

    def test_anger(self):
        """Recognize the required angry statement."""
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

    def test_disgust(self):
        """Recognize the required disgusted statement."""
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"],
            "disgust",
        )

    def test_sadness(self):
        """Recognize the required sad statement."""
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

    def test_fear(self):
        """Recognize the required fearful statement."""
        self.assertEqual(
            emotion_detector("I am really afraid that this will happen")["dominant_emotion"],
            "fear",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
