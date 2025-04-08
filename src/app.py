import os
import sys
from flask import Flask, jsonify, make_response
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
from flask_migrate import Migrate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///clients.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')

CORS(app)

from src.db import db

db.init_app(app)

migrate = Migrate(app, db)

jwt = JWTManager(app)
api = Api(app)

from src.models import User, Payment, TitularModel, ComunidadeModel, EnderecoModel, DependenteModel

from src.routes.user_route import initialize_user_routes
from src.routes.payment_routes import initialize_payment_routes
from src.routes.titular_routes import initialize_routes_titular
from src.routes.protected_route import initialize_protected_routes
from src.routes.comunidade_route import initialize_routes_comunidade
from src.routes.dependentes_routes import initialize_routes_dependente

initialize_user_routes(api)
initialize_payment_routes(api)
initialize_routes_titular(api)
initialize_protected_routes(api)
initialize_routes_comunidade(api)
initialize_routes_dependente(api)

@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "type": str(type(e).__name__),
        "message": str(e)
    }
    print("ERROR:", response)
    return make_response(jsonify(response), 500)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
