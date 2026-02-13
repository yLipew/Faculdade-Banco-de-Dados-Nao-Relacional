from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("Minha primeira atividade rodando no Docler!")


@app.route("/saude")
def saude():
    return jsonify({"Saude": "Ok"})

@app.route("/soma")
def soma():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"Resultado": a + b})
    except ValueError:
        return jsonify({"ERRO": "Parâmetros inválidos"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
