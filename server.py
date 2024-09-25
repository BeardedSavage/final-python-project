from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Application creation
app = Flask("Emotion Detection")

# Route for Emotion Detection
@app.route("/emotionDetector")
def emotion_app():
    '''This code will recieve the text from the HTML interface and
        transfer it's output using the emotion_detector function.
    '''
    # Retrieve the text to analyse
    text_to_analyse = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector
    response = emotion_detector(text_to_analyse)

    # Extract the type of emotions and it's rating
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']
    
    # Return the formatted output of the application
    return f"For the given statement, the system response is 'anger': {anger} 'disgust': {disgust} 'fear': {fear} 'joy': {joy} 'sadness': {sadness} 'dominant emotion': {dominant}."

# Route for the HTML page
@app.route("/")
def render_index_page():
    '''This code renders the HTML page desired

    '''
    return render_template('index.html')

# Code to render the application and launch it on the appropriate localhost:5000
if __name__ == "__main__":
    app.run(host="localhost", port=5000)