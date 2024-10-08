import requests, json

# Emotion Prediction function from the Watson NLP library
def emotion_detector(text_to_analyse):
    # URL for the AI progam
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set up Headers for parse
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Set up json under myobj to analyze the text for parse
    myobj = {"raw_document": { "text": text_to_analyse}}
    # Create response object for json parsing
    response = requests.post(url, json=myobj, headers=header)
    # Parse the requested API
    formatted_response = json.loads(response.text)
    # Determin what type of emotion the text is giving
    if response.status_code == 200:
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]
    # Return the response of the emotion and it's rating
        return {
            'anger': emotion_predictions ['anger'],
            'disgust': emotion_predictions ['disgust'],
            'fear': emotion_predictions ['fear'],
            'joy': emotion_predictions ['joy'],
            'sadness': emotion_predictions ['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        return None