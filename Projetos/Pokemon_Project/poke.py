import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data


pokemon_name = 4
pokemon_info = get_pokemon_info(pokemon_name)

try:
    if pokemon_name:
        print(f'Name: {pokemon_info["name"]}')
        print(f'Id: {pokemon_info["id"]}')
        print(f'Height: {pokemon_info["height"]}')
        print(f'Weight: {pokemon_info["weight"]}')

except TypeError:
    print('Digite corretamente')