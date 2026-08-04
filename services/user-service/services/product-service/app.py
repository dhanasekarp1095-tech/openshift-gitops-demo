from flask import Flask, jsonify
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "product-service")
APP_VERSION = os.getenv("APP_VERSION", "v1")


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": APP_NAME,
        "version": APP_VERSION
    })


@app.route("/products")
def products():
    return jsonify([
        {
            "id": 1,
            "name": "Laptop",
            "price": 75000
        },
        {
            "id": 2,
            "name": "Mouse",
            "price": 1200
        },
        {
            "id": 3,
            "name": "Keyboard",
            "price": 2500
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
