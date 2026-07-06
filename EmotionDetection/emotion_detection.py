'''Creating an emotion detection application using the Watson NLP library'''

import requests

def emotion_detector(text_to_analyze):
    '''Uses url to input defined text to watson emotion detector 
       which analyzes and outputs emotion with score'''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    my_input = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=my_input, headers=header, timeout=10)

    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None,
                'joy': None, 'sadness': None, 'dominant_emotion': None}

    if response.status_code !=200:
        return None

    formatted_response = response.json()
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions