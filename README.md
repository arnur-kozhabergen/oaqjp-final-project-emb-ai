# Final project

Watson NLP Emotion Detector, developed for the Coursera Developing AI Applications with Python and Flask final project. Based on the official IBM starter repository.

The EmotionDetection package calls the genuine Watson EmotionPredict service, returns anger, disgust, fear, joy, sadness and the dominant emotion, and handles HTTP 400 with None values. The Flask application serves the provided interface and displays an explicit error for invalid input.

Run: install requests, flask and pylint, then python server.py (port 5000). Run the five live service tests with python -m unittest -v test_emotion_detection. Run static analysis with python -m pylint server.py. The Watson service must be reachable; predictions are never replaced with sample values.

The original course-provided templates/index.html and static/mywebscript.js are preserved. This is a student demonstration, not a clinical emotion assessment.
