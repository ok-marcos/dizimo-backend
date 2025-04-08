from flask import request, jsonify
from flask_restful import Resource
from src.services.titular_service import get_all_clients, get_client_by_id, create_titular, update_client, delete_client
from src.models import TitularModel
from src.db import db


class TitularResource(Resource):
    def get(self, titular_id=None):
        if titular_id:
            client = get_client_by_id(titular_id)
            if client:
                return client, 200
            else:
                return {"message": "Titular não encontrado"}, 404
        else:
            clients = get_all_clients()
            return clients, 200
    
    def post(self):
        data = request.get_json()
        new_client = create_titular(data)
        return new_client, 201
    
    def put(self, titular_id):
        data = request.get_json()
        update_titular = update_client(titular_id, data)
        return update_titular
    
    def delete(self, titular_id):
        delete_client(titular_id)
        return '', 204

def initialize_routes_titular(api):
    api.add_resource(TitularResource, '/titular', '/titular/<string:titular_id>')
    
