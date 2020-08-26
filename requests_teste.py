import requests

# get
get = requests.get("http://127.0.0.1:5000/hoteis")

print(get.json())
