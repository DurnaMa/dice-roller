from flask import render_template
from typing import Any

from . import create_app
from .api import dices
app = create_app()


def wrap_template_rendering(template_name: str, **context: Any):
    return render_template(template_name, _author="Mahir", **context)

@app.route("/")
def home():
    return wrap_template_rendering("home.html")

@app.route("/dices")
def handle_dices():
    return wrap_template_rendering("dices.html", _dices=dices)


@app.route("/hello")
@app.route("/hello/<string:name>")
def hello_world(name: str = None):
    return wrap_template_rendering("hello.html", _name=name)
