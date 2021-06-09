from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
from letters import Letters as letters

app = Flask(__name__)
api = Api(app)


class Letter(Resource):

    def get(self, id=None):
        if id == None:
            return letters, 200

        for letter in letters:
            if(letter["id"] == id):
                return letter, 200
        return "letter not found", 404

    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("letter")
        params = parser.parse_args()

        automatic_id = len(letters)

        letter = {
            "id": automatic_id,
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