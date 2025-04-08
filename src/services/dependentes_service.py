from datetime import datetime
from src.models import DependenteModel
from src.db import db


def get_dependente_by_id(dependente_id):
    return DependenteModel.query.get(dependente_id)

def get_all_dependentes():
    return DependenteModel.query.all()

def create_dependente(data):
    dependente = DependenteModel(
        dependente_id=data.get("dependente_id"),
        name=data["name"],
        sexo=data["sexo"],
        titular_id=data["titular_id"],
        tipo_dependente=data["tipo_dependente"],
        updated_at=datetime.now()
    )
    db.session.add(dependente)
    db.session.commit()
    return dependente

def update_dependente(dependente_id, data):
    dependente = DependenteModel.query.get(dependente_id)
    if dependente:
        dependente.name = data.get("name", dependente.name)
        dependente.sexo = data.get("sexo", dependente.sexo)
        dependente.titular_id = data.get("titular_id", dependente.titular_id)
        dependente.tipo_dependente = data.get("tipo_dependente", dependente.tipo_dependente)
        dependente.updated_at = datetime.now()
        db.session.commit()
    return dependente

def delete_dependente(dependente_id):
    dependente = DependenteModel.query.get(dependente_id)
    if dependente:
        db.session.delete(dependente)
        db.session.commit()
        return True
    return False
