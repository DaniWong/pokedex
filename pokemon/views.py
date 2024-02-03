from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from django.http import Http404
from pokemon.constants import AUTH_TOKEN, HEADER_AUTH

from pokemon.serializers import PokemonSerializer
from pokemon.models import Pokemon
from pokemon.services import get_or_create_pokemon


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

    def validate_auth(self):
        token_auth_provided = self.request.META.get(HEADER_AUTH, '')
        if token_auth_provided != AUTH_TOKEN:
            raise PermissionDenied
    
    def get_object(self):
        self.validate_auth()
        if self.action == 'retrieve':
            pokemon_name = self.kwargs.get('pk')
            pokemon = get_or_create_pokemon(pokemon_name)
            if not pokemon:
                raise Http404
            return pokemon
        return super().get_object()
