import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_obj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    res = requests.post(url, json=input_obj, headers=header)

    if res.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    res_dict = json.loads(res.text)

    anger_score = res_dict['emotionPredictions'][0]['emotion']['anger']
    disgust_score = res_dict['emotionPredictions'][0]['emotion']['disgust']
    fear_score = res_dict['emotionPredictions'][0]['emotion']['fear']
    joy_score = res_dict['emotionPredictions'][0]['emotion']['joy']
    sadness_score = res_dict['emotionPredictions'][0]['emotion']['sadness']

    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    dominant_emotion = list(output.keys())[0]
    for key, value in output.items():
        if value > output[dominant_emotion]:
            dominant_emotion = key

    output['dominant_emotion'] = dominant_emotion

    return output