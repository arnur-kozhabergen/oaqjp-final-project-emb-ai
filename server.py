"""Serve real Watson predictions. Static analysis: python3 -m pylint server.py."""
from flask import Flask, render_template, request
from requests import RequestException
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the unmodified course-provided application interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze submitted text and display real scores or an honest error message."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    try:
        result = emotion_detector(text_to_analyze)
    except RequestException:
        return "Emotion service unavailable. Please try again later.", 503
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
