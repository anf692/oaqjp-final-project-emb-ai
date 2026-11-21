
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    response = (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
