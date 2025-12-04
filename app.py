import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(
        {
            "message": "Hello from CI/CD demo!",
            "version": os.environ.get("APP_VERSION", "v2"),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
