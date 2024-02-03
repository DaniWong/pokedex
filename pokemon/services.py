from typing import Optional
import requests

from pokemon.models import Pokemon

class PokemonApi(object):

    def __init__(self) -> None:
        self.version = "v2"
        self.base_url = "https://pokeapi.co/api"
        self.pokemon_url = f"{self.base_url}/{self.version}"
    
    def get_pokemon(self, name: str) -> Optional[dict]:
        url = f"{self.pokemon_url}/pokemon/{name.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None


def get_or_create_pokemon(pokemon_name: str) -> Optional[Pokemon]:
    if pokemon_name.isnumeric():
        pokemon_found_in_db = Pokemon.objects.filter(external_id=pokemon_name).first()
    else:
        pokemon_found_in_db = Pokemon.objects.filter(name=pokemon_name).first()
    if not pokemon_found_in_db:
        pokemon_found_in_api = PokemonApi().get_pokemon(pokemon_name)
        if not pokemon_found_in_api:
            return None
        pokemon_id = pokemon_found_in_api.get('id')
        pokemon_name = pokemon_found_in_api.get('name')
        pokemon_sprites = pokemon_found_in_api.get('sprites', {})
        front_default = pokemon_sprites.get('front_default')
        new_pokemon_in_db = Pokemon(
            name=pokemon_name, 
            front_default=front_default, 
            external_id=pokemon_id
        )
        new_pokemon_in_db.save()
        return new_pokemon_in_db
    return pokemon_found_in_db
