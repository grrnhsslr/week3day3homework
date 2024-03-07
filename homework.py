# Create a python wrapper for the Pokémon API. It should take in a Pokémon name and create a Pokémon object.
# The Pokémon object should have, at a minimum, the Pokémon's name, height, and weight.

from api import PokemonAPI

pokemon = PokemonAPI()
charizard_stats = pokemon.get_pokemon('charizard')
bulb_stats = pokemon.get_pokemon('bulbasaur')
print(charizard_stats.name)
print(charizard_stats.weight)
print(charizard_stats.height)
print(bulb_stats.name)
print(bulb_stats.weight)
print(bulb_stats.height)
