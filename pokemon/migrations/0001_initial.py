# Generated by Django 5.0.1 on 2024-02-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveBigIntegerField(verbose_name='External id')),
                ('name', models.CharField(max_length=100, verbose_name='Pokemon name')),
                ('front_default', models.URLField(verbose_name='Fron default')),
                ('is_favorite', models.BooleanField(default=False, verbose_name='Is favorite?')),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemons',
            },
        ),
    ]
