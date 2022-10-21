
from flask import request
from flask import Flask

app = Flask(__name__)

Boxes = [
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


@app.get("/Boxes")  # http://127.0.0.1:5000/Box  #obtain data
def get_Boxes():
    return {"Boxes": Boxes}


@app.post("/Boxes")   #create a new Box
def create_Box():   #def a function
    request_data = request.get_json()  #obtain data of a json file
    
    new_box = {"name": request_data["name"], "items": []} #create a box based oi the info on "request data"
    Boxes.append(new_box) #append the new box to the principal collection
    return new_box, 201  #message of success


@app.post("/Boxes/<string:name>/item")    #create a new item
def create_item(name):   #def a function
    request_data = request.get_json() #save data of json in a variable
    for box in Boxes:   #create a for on the  box collection
        if box["name"] == name: #condition to the creation of an item
            new_item = {
                "name": request_data["name"], "Weight": request_data["Weight"]} #creation of the item based on the json data
            box["items"].append(new_item)  #append the new item to the box
            return new_item   # show the box data withe the new item
    return {"message": "Box not found"}, 404  #error message in case the box dosnt exist


@app.get("/Boxes/<string:name>")  #get the data of a especific box
def get_store(name):   #def a function with the box name as a parameter
    for box in Boxes:   #a for into the box collection
        if box["name"] == name:   # in case that the name of the box existe
            return box            # show the box data
    return {"message": "box not found"}, 404  #error message if the box dosnt exist 


@app.get("/Boxes/<string:name>/item") # get the items of a box
def get_item_in_box(name):   #function with the box name as a parameter
    for box in Boxes:   # for to the box collection
        if box["name"] == name:   #if the box name is correct
            return {"items": box["items"]}    #show the items inside 
    return {"message": "Box not found"}, 404   #error messsage in case the box dsnt exist
