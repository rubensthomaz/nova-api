from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Simulação de respostas como seu arquivo JSON local
respostas = {
    "oi": ["Oi, tudo bem?", "E aí, uai!", "Oi sô! Como posso ajudar?"],
    "como você está?": ["Tô bão demais da conta!", "Tô aqui firme e forte!"],
    "qual seu nome?": ["Eu sou a Nova, uai!", "Me chamo Nova, sua assistente mineira."],
}

@app.route("/nova", methods=["POST"])
def conversar():
    dados = request.get_json()
    mensagem = dados.get("mensagem", "").lower()

    if mensagem in respostas:
        resposta = random.choice(respostas[mensagem])
    else:
        resposta = "Ainda tô aprendendo isso, mas quero muito te entender."

    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run()
