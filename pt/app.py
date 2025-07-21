import json
from flask import Flask, request, jsonify
from secure_logger import get_logger

app = Flask(__name__)
logger = get_logger()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    logger.info(json.dumps(data)) 
    return jsonify({"message": "Data received"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
