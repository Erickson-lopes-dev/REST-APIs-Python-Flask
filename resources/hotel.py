from flask_restful import Resource

hoteis = [
    {
        'hotel_id': 1,
        'estrelas': '4',
        'nome': 'homelandia',
        'diaria': 400.00,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 2,
        'estrelas': '5',
        'nome': 'bravo',
        'diaria': 500.00,
        'cidade': 'Minas Gerais'
    },
    {
        'hotel_id': 3,
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
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'hotel not found'}, 404

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
