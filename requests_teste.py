import requests

# get
get = requests.get("http://127.0.0.1:5000/hoteis")

hoteis = get.json()['hoteis']

for hotel in hoteis:
    print(hotel)

