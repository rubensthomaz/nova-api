from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "Fale comigo!"})

@app.route("/responder", methods=["POST"])
def responder():
    dados = request.get_json()
    mensagem = dados.get("mensagem", "").lower()

    if "dia" in mensagem:
        hoje = datetime.now().strftime("%A, %d de %B de %Y")
        return jsonify({"resposta": f"Hoje é {hoje}."})

    if "hora" in mensagem:
        hora = datetime.now().strftime("%H:%M")
        return jsonify({"resposta": f"Agora são {hora}."})

    return jsonify({"resposta": "Ainda estou aprendendo isso, mas quero muito te entender."})
