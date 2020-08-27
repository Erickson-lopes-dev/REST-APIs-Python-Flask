from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help='the fild login cannot be left')
atributos.add_argument('senha', type=str, required=True, help='the fild senha cannot be left')


class User(Resource):
    def get(self, user_id):
        usuario = UserModel.find_user(user_id)

        if usuario:
            return usuario.json()
        return {'message': 'user not found'}, 404

    @jwt_required
    def delete(self, user_id):
        usuario = UserModel.find_user(user_id)
        if usuario:
            try:
                usuario.delete_hotel()
            except:
                return {'message': 'An internal error ocurred trying to Delete user'}, 500
            return {'message': 'user deleted'}
        return {'message': 'hotel not found'}, 404


class UserRegister(Resource):
    # / cadastro
    def post(self):
        dados = atributos.parse_args()

        # saber se o id existe ou nao
        if UserModel.find_by_login(dados['login']):
            return {"message": f"The login {dados['login']} already exists"}

        user = UserModel(**dados)
        user.save_user()
        return {"message": "user cread sucessfully"}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'acces_token': token_de_acesso}, 200

        return {'message': 'The username or passwor is incorrect'}, 401