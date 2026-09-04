"""
Módulo del servidor Flask para la aplicación Detección de Emociones.
Proporciona endpoints para la interfaz de usuario y el análisis de texto.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """
    Renderiza la página principal index.html del proyecto.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analiza el texto recibido como argumento en la URL y devuelve los
    resultados de las emociones procesadas o un mensaje de error si la entrada es inválida.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get("dominant_emotion")

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
