from sql_alchemy import banco


class HotelModel(banco.Model):
    # nome da tabela
    __tablename__ = 'hoteis'

    horel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estralas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diara = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'estrelas': self.estrelas,
            'nome': self.nome,
            'diaria': self.diara,
            'cidade': self.cidade
        }
