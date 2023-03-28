from flask_restful import Resource

class Heritability(Resource):
    def get(self):
        return "Heritability"