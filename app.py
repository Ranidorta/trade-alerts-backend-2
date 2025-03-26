from flask import Flask, jsonify
from trade_engine import generate_all_signals

app = Flask(__name__)

@app.route('/generate-signals')
def generate_signals():
    results = generate_all_signals()
    return jsonify(results)

if __name__ == '__main__':
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
