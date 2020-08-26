from flask_restful import Resource

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
