from flask import Flask, render_template, request
import EmotionDetection as e

app = Flask('Emotion Detection')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/emotionDetector')
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = e.emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    output = f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is <b>{dominant_emotion}<b>"
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    