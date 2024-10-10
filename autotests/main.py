import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3d73e2e1b998b388cc175a0e81f0371c'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Барабашка",
    "photo_id": 620 
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)

print(response_create.text)

body_update = {
    "pokemon_id": "49591",
    "name": "Барабашка2",
    "photo_id": 618
}

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)

print(response_update.text)

body_add_pokeball = {
    "pokemon_id": "49591",
    "name": "Барабашка2",
    "photo_id": 618
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)


print(response_add_pokeball.text)