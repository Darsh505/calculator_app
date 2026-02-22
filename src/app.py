from flask import Flask, request, jsonify, render_template
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["post"])
def calculate():
    data =nrequest.get_json()
    expresion = data.get("expression", "")
    result = calc.evaluate(expression)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)