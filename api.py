import requests


class PokemonStats:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height


class PokemonAPI:
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    def get_pokemon(self, name):
        poke_stat = requests.get(self.base_url + name)
        if poke_stat:
            data = poke_stat.json()
            name = data['name']
            height = data['height']
            weight = data['weight']
            pokemon = PokemonStats(name, height, weight)
            return pokemon
        else:
            print('Pokemon not found')
