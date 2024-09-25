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
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector
    dominant_emotion = emotion_detector(text_to_analyze)
    
    # If the input is blank return a status code of 400
    if dominant_emotion is None:
        return "Input is invalid! Try again."
    # Return the formatted output of the application
    else:
        return f"For the given statement, the system response is {dominant_emotion}."

# Route for the HTML page
@app.route("/")
def render_index_page():
    '''This code renders the HTML page desired

    '''
    return render_template('index.html')

# Code to render the application and launch it on the appropriate localhost:5000
if __name__ == "__main__":
    app.run(host="localhost", port=5000)