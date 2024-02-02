from django.db import models


class Pokemon(models.Model):
    external_id = models.PositiveBigIntegerField(verbose_name="External id")
    name = models.CharField(max_length=100, verbose_name="Pokemon name")
    front_default = models.URLField(verbose_name="Front default")
    is_favorite = models.BooleanField(verbose_name="Is favorite?", default=False)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"

    def __str__(self) -> str:
        return self.name
