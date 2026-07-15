from flask import Flask, jsonify, render_template, request
from typing import Any

app = Flask(__name__)

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

dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 12},
    {"numberOfSides": 20}
]

@app.route("/api/dices", methods=["GET", "POST"])
def handle_dices_request():
    if request.method == "GET":
        return jsonify(available_dices=dices)
    else:
        try:
            payload = request.json

            if not payload["numberOfSides"]:
                raise Exception("numberOfSides is required")
            if not payload["numberOfSides"]  > 1:
                raise Exception("numberOfSides must be greater than 1")
            
            new_dice = {"numberOfSides": payload["numberOfSides"]}

            if new_dice in dices:
                raise Exception()
            
            dices.append(new_dice)

            return {"message": "Dice created"}, 201
        
        except:
            return {"message": "An Unknown Error Occurred"}, 500