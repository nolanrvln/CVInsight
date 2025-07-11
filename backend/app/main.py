from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/api/test", methods=["GET"])
def test_route():
    return jsonify({"message": "Test route is working!"})

if __name__ == "__main__":
    app.run(debug=True)