# Create a python wrapper for the Pokémon API. It should take in a Pokémon name and create a Pokémon object.
# The Pokémon object should have, at a minimum, the Pokémon's name, height, and weight.

from api import PokemonAPI


poke_search = PokemonAPI()
poke_found = poke_search.get_pokemon(input("Enter pokemon name: "))
if poke_found:
    print(f'{poke_found.name} is {poke_found.height} units tall, and weighs {poke_found.weight}')

