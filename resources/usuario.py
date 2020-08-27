from flask_restful import Resource

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
