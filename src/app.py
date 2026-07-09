from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def hello_world(name: str = None):
    return render_template("hello.html", _name=name)

#@app.route("/<name>")
# def personalized_hello(name):
#     return render_template("hello.html", _name=name)

@app.route("/dices")
def dices():
    return "Look at these beautiful dices"
