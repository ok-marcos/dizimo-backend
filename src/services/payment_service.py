from src.models import User, TitularModel, Payment
from src.db import db
import uuid


def get_all_payments():
    return [payment.to_dict() for payment in Payment.query.all()]

def get_payment_by_id(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        return payment.to_dict()
    else:
        return None

def create_payment(data):
    client = TitularModel.query.get(data['titular_id'])
    print(client)
    user = User.query.get(data['user_id'])
    print(user)
    if not client or not user:
        raise ValueError('Client or User not found')
    

    payment = Payment(
        id_payment = str(uuid.uuid4()),
        amount=data['amount'],
        titular_id=data['titular_id'],
        user_id=data['user_id'],
        description=data['description']    )

    print(payment)
    db.session.add(payment)
    db.session.commit()
    return payment.to_dict()

def update_payment(payment_id, data):
    payment = Payment.query.get(payment_id)
    if payment:
        payment.amount = data['amount']
        payment.description = data.get('description')
        payment.client_id = data['client_id']
        payment.user_id = data['user_id']
        db.session.commit()
        return payment.to_dict()
    else:
        return None

def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        db.session.delete(payment)
        db.session.commit()
        return True
    else:
        return False


def get_payments_by_titular_id(titular_id):
    try:
        payments = Payment.query.filter_by(titular_id=titular_id).all()
        return [payment.to_dict() for payment in payments]
    except Exception as e:
        print(f"Error fetching payments by titular_id {titular_id}: {e}")
        return None