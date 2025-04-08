from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return jsonify(message="This is a protected route")

def initialize_protected_routes(api):
    api.add_resource(ProtectedResource, '/protected')
