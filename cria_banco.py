import sqlite3

connection = sqlite3.connect('banco.db')

cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis(hotel_id text PRIMARY KEY, " \
              "nome text, " \
              "estrelas real, " \
              "diaria real," \
              "cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('1', 'Apha H4', 4.3, 411.00, 'João Pessoa')"

cursor.execute(cria_tabela)

cursor.execute(cria_hotel)

connection.commit()
connection.close()
