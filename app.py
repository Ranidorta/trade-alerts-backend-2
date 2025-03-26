from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

from trade_engine import generate_all_signals

# Carrega variáveis de ambiente do .env
load_dotenv()

# Instância do Flask
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "🚀 Trade Alerts Backend is Live!"}), 200


@app.route("/signals", methods=["POST"])
def signals():
    try:
        data = request.get_json()
        timeframe = data.get("timeframe", "1h")
        leverage = data.get("leverage", 1)

        signals = generate_all_signals(timeframe=timeframe, leverage=leverage)
        return jsonify({"signals": signals})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Entrypoint Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Porta padrão no Render
    app.run(host="0.0.0.0", port=port, debug=True)
