# Final Project: Embeddable AI Emotion Detection Web App

A Flask web application that detects the emotions expressed in a piece of text
using IBM Watson NLP's Emotion Predict API. The app returns scores for anger,
disgust, fear, joy, and sadness, along with the dominant emotion, and includes
error handling for blank or invalid input.

## Features

- `/emotionDetector` endpoint: accepts a `textToAnalyze` query parameter and
  returns a formatted response with all five emotion scores and the dominant
  emotion.
- Blank-input handling: submitting no text returns a clear error message
  instead of a raw exception or a nonsense score.
- Unit tests (`test_emotion_detection.py`) covering anger, joy, sadness, fear,
  and disgust dominant-emotion cases against live API responses.
- Static code analysis via pylint, with docstrings on all functions and modules.

## Project Structure
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── init.py
│   └── emotion_detection.py
├── static/
├── templates/
├── server.py
├── test_emotion_detection.py
└── README.md
## Running Locally

```bash
python3.11 server.py
```

Then visit `http://localhost:5000` or query the endpoint directly:

```bash
curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20thrilled"
```

## Running Tests

```bash
python3.11 test_emotion_detection.py
```
