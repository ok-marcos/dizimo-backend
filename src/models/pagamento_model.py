# src/models/pagamento_model.py
from src.db import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = 'payments'
    __table_args__ = {'extend_existing': True}

    id_payment = db.Column(db.String(32), primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    status = db.Column(db.String)
    due_date = db.Column(db.DateTime)
    payment_date = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime, default=datetime.now())
    titular_id = db.Column(db.String(32), db.ForeignKey('titular.titular_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
              'id_payment': self.id_payment,
            'amount': self.amount,
            'date_created': self.date_created.strftime('%Y-%m-%d %H:%M:%S') if self.date_created else None,
            'titular_id': self.titular_id,
            'user_id': self.user_id,
            'description': self.description,
            'due_date': self.due_date.strftime('%Y-%m-%d %H:%M:%S') if self.due_date else None,
            'payment_date': self.payment_date.strftime('%Y-%m-%d %H:%M:%S') if self.payment_date else None,
        }
