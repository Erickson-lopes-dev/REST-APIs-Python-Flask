from flask_restful import Resource, reqparse

from models.usuario import UserModel


class User(Resource):

    def get(self, user_id):
        usuario = UserModel.find_user(user_id)

        if usuario:
            return usuario.json()
        return {'message': 'user not found'}, 404

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
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help='the fild login cannot be left')
        atributos.add_argument('senha', type=str, required=True, help='the fild senha cannot be left')

        dados = atributos.parse_args()

        # saber se o id existe ou nao
        if UserModel.find_by_login(dados['login']):
            return {"message": f"The login {dados['login']} already exists"}

        user = UserModel(**dados)
        user.save_user()
        return {"message": "user cread sucessfully"}, 201
