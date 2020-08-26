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


def put_hotel(pk):
    put = requests.put("http://127.0.0.1:5000/hoteis/" + str(pk))


def delete_hotel(pk):
    delete = requests.delete("http://127.0.0.1:5000/hoteis/" + str(pk))


get_hotel(1)
