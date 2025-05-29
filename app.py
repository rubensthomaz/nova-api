from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Respostas simples como exemplo
respostas_online = {
    "quem descobriu o brasil": [
        "Foi Pedro Álvares Cabral, uai!",
        "Quem descobriu o Brasil foi Cabral, lá em 1500."
    ],
    "que dia é hoje": [
        "Uai, eu não sei o dia exato agora, mas posso te ajudar com outras coisas!",
        "Se quiser saber a data, pode me perguntar de novo mais tarde!"
    ]
}

@app.route("/responder", methods=["POST"])
def responder():
    dados = request.get_json()
    mensagem = dados.get("mensagem", "").lower()

    if mensagem in respostas_online:
        return jsonify({"resposta": random.choice(respostas_online[mensagem])})
    else:
        return jsonify({"resposta": "Ainda tô aprendendo isso também lá na nuvem, mas um dia chego lá!"})

if __name__ == "__main__":
    app.run()
