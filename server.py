"""
Server module for the Emotion Detector application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze the emotion of the given text and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    # Handle blank entry - dominant_emotion is None
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant}."
    )

    return response

@app.route("/")
def render_index_page():
    """
    Render the index page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
