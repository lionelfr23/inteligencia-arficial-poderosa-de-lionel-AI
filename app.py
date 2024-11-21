from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Lógica para procesar el mensaje
    if "creador" in user_message.lower():
        response = "Mi creador es Lionel Edersson Aragos Illanes."
    else:
        response = generar_respuesta(user_message)

    return jsonify({"response": response})

def generar_respuesta(mensaje):
    return f"Hola, dijiste: {mensaje}. ¿En qué más puedo ayudarte?"

if __name__ == "__main__":
    app.run(debug=True)
