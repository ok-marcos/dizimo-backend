from flask import request, jsonify
from flask_restful import Resource
from src.services.comunidade_service import get_all_comunidades, get_comunidade_by_id, create_comunidade, update_comunidade, delete_comunidade

class ComunidadeResource(Resource):
    def get(self, comunidade_id=None):
        if comunidade_id:
            return get_comunidade_by_id(comunidade_id)
        else:
            return get_all_comunidades()
    
    def post(self):
        data = request.get_json()
        new_comunidade, status_code = create_comunidade(data)
        return new_comunidade, status_code
    
    def put(self, comunidade_id):
        data = request.get_json()
        updated_client = update_comunidade(comunidade_id, data)
        return updated_client
    
    def delete(self, comunidade_id):
        delete_result, status_code = delete_comunidade(comunidade_id)
        return delete_result, status_code

def initialize_routes_comunidade(api):
    api.add_resource(ComunidadeResource, '/comunidade', '/comunidade/<string:comunidade_id>')
