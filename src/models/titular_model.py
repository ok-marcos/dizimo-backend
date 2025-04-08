from datetime import datetime
from src.db import db
from src.utils.utils import generate_uuid



class TitularModel(db.Model):
    __tablename__ = 'titular'
    __table_args__ = {'extend_existing': True}

    titular_id = db.Column(db.String(32), primary_key=True)
    numero_dizimista = db.Column(db.Integer, nullable= False)
    name = db.Column(db.String(80), nullable=False)
    sexo = db.Column(db.String(32), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = db.Column(db.DateTime)
    comunidade_id = db.Column(db.String(32), db.ForeignKey('comunidade.comunidade_id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    endereco = db.relationship('EnderecoModel', backref='titular')
    dependente = db.relationship('DependenteModel', backref='titular_relation')
    payments = db.relationship('Payment', backref='titular')

    def to_dict(self):
        return {
            'titular_id': self.titular_id,
            'numero_dizimista': self.numero_dizimista,
            'name': self.name,
            'sexo': self.sexo,
            'data_nascimento': self.data_nascimento.strftime('%Y-%m-%d'),
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'deleted_at': self.deleted_at.strftime('%Y-%m-%d %H:%M:%S') if self.deleted_at else None,
            'comunidade_id': self.comunidade_id,
            'user_id': self.user_id
        }



class EnderecoModel(db.Model):
    __tablename__ = 'endereco'
    __table_args__ = {'extend_existing': True}

    endereco_id = db.Column(db.String(32), primary_key=True, default=generate_uuid)
    titular_id = db.Column(db.String(32), db.ForeignKey('titular.titular_id'))
    cep = db.Column(db.String(32), nullable=False)
    rua = db.Column(db.String(32), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(32), nullable=False)
    cidade = db.Column(db.String(32), nullable=False)
    complemento = db.Column(db.String(32), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


    def to_dict(self):
        return {
            'endereco_id': self.endereco_id,
            'titular_id': self.titular_id,
            'cep': self.cep,
            'rua': self.rua,
            'numero': self.numero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'complemento': self.complemento,
            'updated_at': self.updated_at,
            'titular_relation': self.titular_relation.to_dict() if self.titular_relation else None
        }
        
        
class DependenteModel(db.Model):
    __tablename__ = 'dependente'
    __table_args__ = {'extend_existing': True}

    dependente_id = db.Column(db.String(32), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(32), nullable=False)
    sexo = db.Column(db.String(32), nullable=False)
    titular_id = db.Column(db.String(32), db.ForeignKey('titular.titular_id'))
    tipo_dependente = db.Column(db.String(32), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


    def to_dict(self):
        return {
            'dependente_id': self.dependente_id,
            'name': self.name,
            'sexo': self.sexo,
            'titular_id': self.titular_id,
            'tipo_dependente': self.tipo_dependente,
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }