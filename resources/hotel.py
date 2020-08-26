from flask_restful import Resource, reqparse

from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id': '1',
        'estrelas': '4',
        'nome': 'homelandia',
        'diaria': 400.00,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': '2',
        'estrelas': '5',
        'nome': 'bravo',
        'diaria': 500.00,
        'cidade': 'Minas Gerais'
    },
    {
        'hotel_id': '3',
        'estrelas': '3',
        'nome': 'H4',
        'diaria': 300.00,
        'cidade': 'Rio de Janeiro'
    },
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    # cria um objeto para receber da requisição os dados
    argumentos = reqparse.RequestParser()
    # campos que devera pegar os dados
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('cidade')
    argumentos.add_argument('diaria')

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(self, hotel_id)

        if hotel:
            return hotel
        return {'message': 'hotel not found'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel id "{hotel_id}" already exists.'}, 400

        # criar construtor
        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()

    def put(self, hotel_id):
        hotel = Hotel.find_hotel(self, hotel_id)

        dados = Hotel.argumentos.parse_args()

        hotel_object = HotelModel(hotel_id, **dados)

        novo_hotel = hotel_object.json()

        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200

        hoteis.append(novo_hotel)

        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]

        return {'message': 'Hotel deleted'}
