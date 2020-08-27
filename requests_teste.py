import requests


def get_hoteis():
    # get
    get = requests.get("http://127.0.0.1:5000/hoteis")

    hoteis = get.json()['hoteis']

    for hotel in hoteis:
        print(hotel)


def get_hotel():
    get = requests.get("http://127.0.0.1:5000/hoteis/ass/")
    print(get.json())


def post_hotel():
    data = {
        "estrelas": 4.0,
        "nome": "G750",
        "diaria": 550.00,
        "cidade": "Paraiba"
    }
    post = requests.post(f"http://127.0.0.1:5000/hoteis/ass/", json=data)

    print(post.json())


def put_hotel():
    data = {
        "nome": "New",
        "estrelas": 1.0,
        "diaria": 550.00,
        "cidade": "Paraiba"
    }
    put = requests.put(f"http://127.0.0.1:5000/hoteis/bravo/", json=data)

    print(put.json())


def delete_hotel():
    delete = requests.delete("http://127.0.0.1:5000/hoteis/ass/")
    print(delete.json())


def get_usuarios():
    get = requests.get("http://127.0.0.1:5000/usuarios/1")
    print(get.json())


def delete_usuarios():
    delete = requests.delete("http://127.0.0.1:5000/usuarios/1")
    print(delete.json())


def login_usuarios():
    data = {

    }
    post = requests.post("http://127.0.0.1:5000/login/", json=data)
    print(post.json())


def logout_usuarios():
    data = {

    }
    post = requests.post("http://127.0.0.1:5000/logout/", json=data)
    print(post.json())


def cadastro_usuarios():
    data = {

    }
    post = requests.post("http://127.0.0.1:5000/logout/", json=data)
    print(post.json())
