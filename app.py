from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/system/health")
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route("/")
def hello():
    return "こんにちは、jsonify！"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)