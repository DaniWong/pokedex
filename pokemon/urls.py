from rest_framework import routers
from pokemon.views import PokemonViewSet

app_name = 'pokemon'

router = routers.SimpleRouter()
router.register(r'pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = router.urls
