import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configura tu clave de API de OpenAI
openai.api_key = "TU_API_KEY_AQUÍ"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Llama a OpenAI para obtener una respuesta
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # O usa "gpt-4" si tienes acceso
            messages=[
                {"role": "system", "content": "Eres un asistente útil y amable."},
                {"role": "user", "content": user_message},
            ],
        )
        bot_response = response["choices"][0]["message"]["content"]
    except Exception as e:
        bot_response = "Lo siento, ocurrió un error al procesar tu solicitud."

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
