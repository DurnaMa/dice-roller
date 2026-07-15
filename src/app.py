from flask import Flask, render_template
from typing import Any

app = Flask(__name__)

def wrap_template_rendering(template_name: str, **context: Any):
    return render_template(template_name, _author="Mahir", **context)

@app.route("/")
def home():
    return wrap_template_rendering("home.html")

@app.route("/dices")
def handle_dices():
    return wrap_template_rendering("dices.html")


@app.route("/hello")
@app.route("/hello/<string:name>")
def hello_world(name: str = None):
    return wrap_template_rendering("hello.html", _name=name)