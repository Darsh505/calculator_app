from pathlib import Path

from flask import Flask, jsonify, render_template, request

from calculator import Calculator

BASE_DIR = Path(__file__).resolve().parent.parent
app = Flask(__name__, template_folder=str(BASE_DIR / "templates"))
calc = Calculator()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True) or {}
    expression = data.get("expression", "")
    result = calc.evaluate(expression)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False, use_reloader=False)
