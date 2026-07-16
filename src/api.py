from flask import Blueprint, jsonify, request

api_bp = Blueprint("api", __name__)

dices = [
    {"numberOfSides": 6},
    {"numberOfSides": 12},
    {"numberOfSides": 20}
]

@api_bp.route("dices", methods=["GET", "POST"])
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