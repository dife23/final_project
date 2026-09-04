import json
import requests


def emotion_detector(text_to_analyze):
  url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
  headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  myobj = {"raw_document": {"text": text_to_analyze}}

  response = requests.post(url, json=myobj, headers=headers)

  # Convertir la respuesta de texto a un diccionario Python
  formatted_response = json.loads(response.text)

  # Extraer el diccionario de emociones
  emotions = formatted_response["emotionPredictions"][0]["emotion"]

  # Obtener los puntajes individuales
  anger_score = emotions["anger"]
  disgust_score = emotions["disgust"]
  fear_score = emotions["fear"]
  joy_score = emotions["joy"]
  sadness_score = emotions["sadness"]

  # Encontrar la emoción con la puntuación más alta
  dominant_emotion = max(emotions, key=emotions.get)

  # Devolver el diccionario con la estructura requerida
  return {
      "anger": anger_score,
      "disgust": disgust_score,
      "fear": fear_score,
      "joy": joy_score,
      "sadness": sadness_score,
      "dominant_emotion": dominant_emotion,
  }