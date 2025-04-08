from datetime import datetime
from src.db import db
from src.utils.utils import generate_uuid

class ComunidadeModel(db.Model):
    __tablename__ = 'comunidade'
    __table_args__ = {'extend_existing': True}

    comunidade_id = db.Column(db.String(32), primary_key=True, default=generate_uuid)
    nome = db.Column(db.String(80), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    titulares = db.relationship('TitularModel', backref='comunidade_relation')

    def to_dict(self):
        return {
            'comunidade_id': self.comunidade_id,
            'nome': self.nome,
            'updated_at': self.updated_at.strftime("%m/%d/%Y, %H:%M:%S")
        }
