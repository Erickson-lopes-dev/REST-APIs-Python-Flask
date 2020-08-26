class HotelModel:
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