from flask import Flask

app = Flask(__name__)

games = [
    {
        "Category":"Shooters",
        "Items":[
            {"Name":"Call Of Duty",
            "price": 40.99}
        ]
    }
]

@app.get("/games")  #http://127.0.0.1:5000/games
def get_games():
    return {"games": games}