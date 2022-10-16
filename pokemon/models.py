from email.policy import default
from queue import Empty
from re import T
from xmlrpc.client import DateTime
from django.db import models


class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = 'WA'
        GRASS = 'GR'
        GHOST = 'GH'
        STEEL = 'ST'
        FAIRY = 'FA'
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30,choices=PokemonType.choices, default="WATER")
    hp = models.PositiveBigIntegerField
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_lenght=30 , default=Empty , blank = True)
    name_ar = models.CharField(max_lenght=30 , default=Empty , blank = True)
    name_jp = models.CharField(max_lenght=30 , default=Empty , blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name



