from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

letters = [{
    "id": 0,
    "name": "Maria",
    "letter": "Dear St. Claus, I would like a bike this year. Thanks!"
},
{
    "id": 1,
    "name": "Fernanda",
    "letter": "Dear St. Claus, I would like a doll this year. Thanks!"
},
{
    "id": 2,
    "name": "Carla",
    "letter": "Dear St. Claus, I would like a computer this year. Thanks!"
},
]

class Letter(Resource):

    def get(self, id=None):
        if id == None:
            return letters, 200

        for letter in letters:
            if(letter["id"] == id):
                return letter, 200
        return "letter not found", 404

    
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("letter")
        params = parser.parse_args()

        for letter in letters:
            if(id == letter["id"]):
                return f"letter with id {id} already exists", 400

        letter = {
            "id": int(id),
            "name": params["name"],
            "letter": params["letter"]
        }

        letters.append(letter)
        return letter, 201


    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("letter")
        params = parser.parse_args()

        for letter in letters:
            if(id == letter["id"]):
                letter["name"] = params["name"]
                letter["letter"] = params["letter"]
                return letter, 200
        
        letter = {
            "id": id,
            "name": params["name"],
            "letter": params["letter"]
        }
        
        letters.append(letter)
        return letter, 201


    def delete(self, id):
        global letters
        letters = [letter for letter in letters if letter["id"] != id]
        return f"Letter with id {id} is deleted.", 200


api.add_resource(Letter, "/letters", "/letters/", "/letters/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)