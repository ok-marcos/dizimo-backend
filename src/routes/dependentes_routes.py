
from flask import request
from flask_restful import Resource
from src.services.dependentes_service import delete_dependente, get_all_dependentes, get_dependente_by_id, create_dependente, update_dependente
class DependenteResource(Resource):
    def get(self, dependente_id=None):
        if dependente_id:
            dependente = get_dependente_by_id(dependente_id)
            if dependente:
                return dependente.to_dict(), 200
            else:
                return {"message": "Dependente não encontrado"}, 404
        else:
            dependentes = get_all_dependentes()
            return [dep.to_dict() for dep in dependentes], 200

    def post(self):
        data = request.get_json()
        new_dependente = create_dependente(data)
        return new_dependente.to_dict(), 201

    def put(self, dependente_id):
        data = request.get_json()
        updated_dependente = update_dependente(dependente_id, data)
        if updated_dependente:
            return updated_dependente.to_dict(), 200
        else:
            return {"message": "Dependente não encontrado"}, 404

    def delete(self, dependente_id):
        deleted = delete_dependente(dependente_id)
        if deleted:
            return '', 204
        else:
            return {"message": "Dependente não encontrado"}, 404


def initialize_routes_dependente(api):
    api.add_resource(DependenteResource, '/dependente', '/dependente/<string:dependente_id>')
