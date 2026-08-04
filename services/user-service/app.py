from flask import Flask, jsonify
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask application
app = Flask(__name__)

# Environment variables
APP_NAME = os.getenv("APP_NAME", "user-service")
APP_VERSION = os.getenv("APP_VERSION", "v1")


@app.route("/health", methods=["GET"])
def health():
    logger.info("Health endpoint called")
    return jsonify({
        "status": "UP",
        "service": APP_NAME,
        "version": APP_VERSION
    })


@app.route("/user", methods=["GET"])
def get_user():
    logger.info("User endpoint called")
    return jsonify({
        "id": 101,
        "name": "John Doe",
        "email": "john@example.com",
        "department": "Engineering"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
