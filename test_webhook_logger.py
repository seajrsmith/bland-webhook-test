from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
logs = []

@app.route('/test-webhook', methods=['POST'])
def test_webhook():
    payload = request.json
    logs.append({
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "payload": payload
    })
    print("Received payload:", payload)
    return jsonify({"status": "received", "payload": payload}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
