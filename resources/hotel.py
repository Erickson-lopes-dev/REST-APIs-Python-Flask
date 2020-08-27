from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required


class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    # cria um objeto para receber da requisição os dados
    argumentos = reqparse.RequestParser()
    # campos que devera pegar os dados
    argumentos.add_argument('nome', type=str, required=True, help="the fild 'nome' cannot be left name")
    argumentos.add_argument('estrelas', type=float, required=True, help="the fild 'estrelas' cannot be left name")
    argumentos.add_argument('cidade', type=str, required=True)
    argumentos.add_argument('diaria', type=float, required=True)

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        if hotel:
            return hotel.json()
        return {'message': 'hotel not found'}, 404

    @jwt_required
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel id "{hotel_id}" already exists.'}, 400

        # criar construtor
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to safe hotel'}, 500
        return hotel.json()

    @jwt_required
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            # atualiza
            hotel_encontrado.update_hotel(**dados)
            # salva a alteração
            try:
                hotel_encontrado.save_hotel()
            except:
                return {'message': 'An internal error ocurred trying to update hotel'}, 500
            return hotel_encontrado.json(), 200

        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()

        return hotel.json(), 201

    @jwt_required
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An internal error ocurred trying to Delete hotel'}, 500
            return {'message': 'Hotel deleted'}
        return {'message': 'hotel not found'}, 404
