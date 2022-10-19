
from flask import request
from flask import Flask

app = Flask(__name__)

Box = [
    {
        "name": "MyBox",
        "items": [
            {
                "name": "Toy",
                "Weight": "15m"
            }
        ]
    }
]


@app.get("/Box")  # http://127.0.0.1:5000/Box
def get_Boxes():
    return {"Box": Box}


@app.post("/Box")
def create_Box():
    request_data = request.get_json()
    new_box = {"name": request_data["name"], "items": []}
    Box.append(new_box)
    return new_box, 201


@app.post("/Box/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for box in Box:
        if box["name"] == name:
            new_item = {
                "name": request_data["name"], "Weight": request_data["Weight"]}
            box["items"].append(new_item)
            return new_item
    return {"message": "Box not found"}, 404


@app.get("/Box/<string:name>")
def get_store(name):
    for box in Box:
        if box["name"] == name:
            return box
    return {"message": "box not found"}, 404


@app.get("/Box/<string:name>/item")
def get_item_in_box(name):
    for box in Box:
        if box["name"] == name:
            return {"items": box["items"]}
    return {"message": "Box not found"}, 404
