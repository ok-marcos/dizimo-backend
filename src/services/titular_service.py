from src.models import TitularModel as Titular
from datetime import datetime
from src.db import db
import uuid


def get_all_clients():
    return [client.to_dict() for client in Titular.query.all()]


# def get_client_by_id(titular_id):

#     client = Titular.query.get_or_404(titular_id)
#     return client.to_dict()

def get_client_by_id(titular_id):
    # Consulta o titular pelo ID
    titular = db.session.query(Titular).filter_by(titular_id=titular_id).first()
    
    if not titular:
        return None

    # Converte o titular para dicionário, incluindo dependentes
    titular_data = titular.to_dict()
    titular_data['dependentes'] = [dependente.to_dict() for dependente in titular.dependente]

    return titular_data
def get_client_by_cpf(cpf):
    client = Titular.query.get_or_404(cpf)
    return client.to_dict()


def get_client_by_numero_dizimista(numero_dizimista):
    client = Titular.query.get_or_404(numero_dizimista)
    return client.to_dict()


def create_titular(data):
    new_titular = Titular(
        titular_id = str(uuid.uuid4()),
        numero_dizimista=data['numero_dizimista'],
        name=data['nome'],
        telefone=data['telefone'],
        sexo=data['sexo'],
        data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date(),
        cpf=data['cpf'],
        email=data['email'],
        comunidade_id=data['comunidade_id'],
        user_id = data['user_id']
    )
    db.session.add(new_titular)
    db.session.commit()
    #TODO lista_numeros_dizimista[1:1000] numeros_usados_ordenados[1,2,100,300] numeros_que_podemos_usar[diferenca entre eles]
    #TODO fazer verificacao de numero de dizimista e cpf
    return new_titular.to_dict()

def update_client(titular_id, data):
    client = Titular.query.get_or_404(titular_id)
    client.nome = data['nome']
    client.email = data['email']
    client.telefone = data['telefone']
    db.session.commit()
    return client.to_dict()

def delete_client(titular_id):
    client = Titular.query.get_or_404(titular_id)
    db.session.delete(client)
    db.session.commit()
    return '', 204
