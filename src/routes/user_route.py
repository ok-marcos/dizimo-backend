from flask_restful import Resource
from flask import request, jsonify, make_response
from src.models import User
from src.db import db
from flask_jwt_extended import create_access_token
from src.services.users_service import authenticate_user, create_user

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if User.query.filter_by(username=username).first():
            return {'message': 'Username already exists'}, 400

        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return {'id': new_user.id, 'username': new_user.username}, 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = authenticate_user(data['username'], data['password'])
            access_token = create_access_token(identity=user['id'])
            
            # Retorna o token e o ID do usuário no login
            return make_response(jsonify(token=access_token, user_id=user['id']), 200)
        except ValueError as e:
            return make_response(jsonify({'message': str(e)}), 400)

def initialize_user_routes(api):
    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserLogin, '/login')
