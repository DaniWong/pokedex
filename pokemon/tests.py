from django.test import TestCase

from rest_framework.test import APIClient

from pokemon.models import Pokemon
from pokemon.services import PokemonApi


class PokemonSearchTestCase(TestCase):
    def setUp(self):
        Pokemon.objects.create(
            name="pikachu",
            external_id='1',
            front_default='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
            is_favorite=False
        )

    def test_search_pokemon_in_db(self):
        client = APIClient()
        pokemon_to_search = 'pikachu'
        url = f'/pokedex/pokemon/{pokemon_to_search}/'
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get('name'), pokemon_to_search)

    def test_search_pokemon_in_api(self):
        pokemon_to_search = 'snorlax'
        pokemon = PokemonApi().get_pokemon(pokemon_to_search)
        self.assertTrue(pokemon)

    def test_mark_pokemon_as_favorite(self):
        client = APIClient()
        pokemon_to_search = 'pikachu'
        url = f'/pokedex/pokemon/{pokemon_to_search}/'
        response = client.patch(url, {'is_favorite': True})
        self.assertEqual(response.status_code, 200)
        response = client.get(url)
        data = response.json()
        self.assertTrue(data.get('is_favorite'))
