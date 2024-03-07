# Create a python wrapper for the Pokémon API. It should take in a Pokémon name and create a Pokémon object.
# The Pokémon object should have, at a minimum, the Pokémon's name, height, and weight.

import requests


class Pokemon:
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    def __init__(self):
        self.weight = None
        self.height = None
        self.name = None

    def get_pokemon(self, name):
        poke_stat = requests.get(self.base_url + name)
        if poke_stat:
            data = poke_stat.json()
            self.name = data['name']
            self.height = data['height']
            self.weight = data['weight']
        else:
            print('Pokemon not found')


pokemon1 = Pokemon()
pokemon1.get_pokemon(input('Enter pokemon name: '))
print(f'{pokemon1.name} is your Pokemon, it weighs {pokemon1.weight}, and is {pokemon1.height} units tall')

pokemon2 = Pokemon()
pokemon2.get_pokemon('bulbasaur')
print(f'{pokemon2.name} is your Pokemon, it weighs {pokemon2.weight}, and is {pokemon2.height} units tall')
