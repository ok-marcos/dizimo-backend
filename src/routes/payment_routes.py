from flask import request, jsonify
from flask_restful import Resource
from src.services.payment_service import get_all_payments, get_payment_by_id, create_payment, get_payments_by_titular_id, update_payment, delete_payment

class PaymentResource(Resource):
    def get(self, payment_id=None):
        titular_id = request.args.get('titular_id')
        
        if payment_id:
            payment = get_payment_by_id(payment_id)
            if payment:
                return jsonify(payment)
            else:
                return {'message': 'Payment not found'}, 404
        elif titular_id:
            payments = get_payments_by_titular_id(titular_id)
            if payments:
                return jsonify(payments)
            else:
                return {'message': 'No payments found for this titular_id'}, 404
        else:
            return jsonify(get_all_payments())

    def post(self):
        data = request.get_json()
        try:
            new_payment = create_payment(data)
            return new_payment, 201
        except ValueError as e:
            return {"message": str(e)}, 400
        except Exception as e:
            return {"message": "Erro interno do servidor"}, 500

    def put(self, payment_id):
        data = request.get_json()
        updated_payment = update_payment(payment_id, data)
        if updated_payment:
            return jsonify(updated_payment)
        else:
            return {'message': 'Payment not found'}, 404

    def delete(self, payment_id):
        if delete_payment(payment_id):
            return '', 204
        else:
            return {'message': 'Payment not found'}, 404

def initialize_payment_routes(api):
    api.add_resource(PaymentResource, '/payments', '/payments/<int:payment_id>')
