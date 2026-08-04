from flask import Flask, jsonify
import requests
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Local Docker URLs (we'll change these with Helm later)
USER_SERVICE_URL = os.getenv(
    "USER_SERVICE_URL",
    "http://user-service:5000"
)

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://product-service:5000"
)


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "order-service"
    })


@app.route("/orders")
def orders():

    user = requests.get(
        f"{USER_SERVICE_URL}/user",
        timeout=5
    ).json()

    products = requests.get(
        f"{PRODUCT_SERVICE_URL}/products",
        timeout=5
    ).json()

    return jsonify({
        "orderId": 1001,
        "customer": user,
        "products": products,
        "totalProducts": len(products),
        "status": "CONFIRMED"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
