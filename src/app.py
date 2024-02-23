import os
import random

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

numbers_list = []


def generate_numbers(max_number: int = 100):
    numbers_list = list(range(1, max_number + 1))
    random.shuffle(numbers_list)
    return numbers_list


@app.route("/", methods=["GET"])
def index():
    return jsonify({"reset game": "/reset", "get your number": "/get"}), 200


@app.route("/reset", methods=["GET"])
def reset():
    global numbers_list
    max_number = int(request.args.get("max", 100))
    numbers_list = generate_numbers(max_number)
    return jsonify({"message": f"reset: max {max_number}"}), 200


@app.route("/get", methods=["GET"])
def get():
    global numbers_list
    if not numbers_list:
        return jsonify({"message": "No more numbers. Please reset."}), 200
    your_number = numbers_list.pop()
    return jsonify({"number": your_number}), 200


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )


if __name__ == "__main__":
    app.run(debug=True)
