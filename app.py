from flask import Flask, jsonify
from flask_restful import Api

from blacklist import BLACKLIST
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager

app = Flask(__name__)
# Cria na Raiz
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'segreDinho'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)

jwt = JWTManager(app)


# http://127.0.0.1:5000/hoteis
# antes da primeira requirição
@app.before_first_request
def cria_banco():
    banco.create_all()


# verifica se o id esta na blacklist
@jwt.token_in_blacklist_loader
def verificar_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidade():
    return jsonify({"message": "You have been logged out. "})


api.add_resource(Hoteis, '/hoteis/')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>/')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
