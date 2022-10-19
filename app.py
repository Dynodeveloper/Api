
from urllib import request
from flask import Flask

app = Flask(__name__)

games = [
    {
        "Category": "Shooters",
        "Items": [
            {"Name": "Call Of Duty",
             "price": 40.99}
        ]
    }
]


@app.get("/games")  # http://127.0.0.1:5000/games
def get_games():
    return {"games": games}


@app.post("/games")
def create_category():
    request_data = request.get_json()
    new_category = {"Name": request_data["Name"], "Items": []}
    games.append(new_category)
    return new_category, 201


@app.post("/games/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for game in games:
        if game["name"] == name:
            new_item = {
                "name": request_data["name"], "price": request_data["price"]}
            game["items"].append(new_item)
            return new_item
    return {"message": "Game not found"}, 404


@app.get("/games/<string:name>")
def get_game(name):
    for game in games:
        if game["name"] == name:
            return game
    return {"message": "Game not found"}, 404
