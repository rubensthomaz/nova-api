from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# Carrega a chave da OpenAI da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/responder", methods=["POST"])
def responder():
    dados = request.get_json()
    mensagem = dados.get("mensagem", "")

    # Tenta gerar resposta pelo ChatGPT
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é a Nova, uma assistente virtual mineira, divertida e acolhedora."},
                {"role": "user", "content": mensagem}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        conteudo = resp.choices[0].message.content.strip()
    except Exception:
        conteudo = "Poxa, tive um problema interno. Tenta de novo mais tarde!"

    return jsonify({"resposta": conteudo})

# Rota opcional para teste via GET
@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem":"Nova API está no ar!"})

if __name__ == "__main__":
    app.run()
