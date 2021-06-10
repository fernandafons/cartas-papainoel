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

        if params['name'] == None or params['letter'] == None:
            return "params name and letter are mandatory!", 422

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
                if params["name"]:
                    letter["name"] = params["name"]
                if params["letter"]:
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
        for letter in letters:
            if letter["id"] == id:
                del(letters[id])
                return f"Letter with id {id} was deleted.", 200

        return "id does not exist", 404


api.add_resource(Letter, "/letters", "/letters/", "/letters/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)