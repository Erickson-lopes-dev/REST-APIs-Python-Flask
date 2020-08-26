import requests


def get_hoteis():
    # get
    get = requests.get("http://127.0.0.1:5000/hoteis")

    hoteis = get.json()['hoteis']

    for hotel in hoteis:
        print(hotel)


def get_hotel(pk):
    get = requests.get("http://127.0.0.1:5000/hoteis/" + str(pk))
    print(get.json())


def post_hotel():
    data = {
        "estrelas": "5",
        "nome": "G750",
        "diaria": "500.00",
        "cidade": "Paraiba"
    }
    post = requests.post(f"http://127.0.0.1:5000/hoteis/5/", json=data)

    print(post.json())


def delete_hotel(pk):
    delete = requests.delete("http://127.0.0.1:5000/hoteis/" + str(pk))


post_hotel()

get_hoteis()



