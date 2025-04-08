import json
from flask import Response, jsonify
from src.models import ComunidadeModel as Comunidade
from src.db import db

def get_all_comunidades():
    return [comunidade.to_dict() for comunidade in Comunidade.query.all()]

def get_comunidade_by_id(comunidade_id):
    comunidade = Comunidade.query.get_or_404(comunidade_id)
    return comunidade.to_dict()

def get_comunidade_by_nome(nome):
    nome = Comunidade.query.filter_by(nome=nome).first()
    return nome

def create_comunidade(data):
    nome_result = get_comunidade_by_nome(data['nome'])
    
    if nome_result is not None:
        data = {'Error': 'Comunidade já cadastradata!',
                'id': nome_result.comunidade_id,
                'nome': nome_result.nome}
        return data, 400
    else:
        new_comunidade = Comunidade(
            nome = data['nome'],
            user_id = data['user_id']
        )
        db.session.add(new_comunidade)
        db.session.commit()
        return new_comunidade.to_dict(), 201

def update_comunidade(comunidade_id, data):
    comunidade = Comunidade.query.get_or_404(comunidade_id)
    comunidade.nome = data['nome']
    db.session.commit()
    return comunidade.to_dict()

def delete_comunidade(comunidade_id):
    comunidade = Comunidade.query.filter_by(comunidade_id=comunidade_id).first()
    if comunidade is not None:
        db.session.delete(comunidade)
        db.session.commit()
        return {'Message': 'Comunidade removida com sucesso!'}, 200
    else:
        return {'Message': 'Comunidade não encontrada!'}, 404
