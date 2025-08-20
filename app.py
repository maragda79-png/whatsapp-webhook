from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def verify():
    token = "EL_TEU_TOKEN_DE_VERIFICACIÓ"  # Canvia-ho pel que configures a Meta
    challenge = request.args.get("hub.challenge")
    verify_token = request.args.get("hub.verify_token")

    if verify_token == token:
        return challenge
    return "Error de verificació", 403

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Missatge rebut:", data)
    return "OK", 200
