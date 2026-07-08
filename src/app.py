from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def personalized_hello(name):
    return f"Hello, {name}"

@app.route("/dices")
def dices():
    return "Look at these beautiful dices"
