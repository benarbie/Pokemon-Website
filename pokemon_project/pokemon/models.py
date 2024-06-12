from django.db import models
import json

class Pokemon(models.Model):
    TYPES = [
        ('NORMAL', 'NORMAL'), ('FIRE', 'FIRE'), ('WATER', 'WATER'),
        ('GRASS', 'GRASS'), ('ELECTRIC', 'ELECTRIC'), ('ICE', 'ICE'),
        ('FIGHTING', 'FIGHTING'), ('POISON', 'POISON'), ('GROUND', 'GROUND'),
        ('FLYING', 'FLYING'), ('PSYCHIC', 'PSYCHIC'), ('BUG', 'BUG'),
        ('ROCK', 'ROCK'), ('GHOST', 'GHOST'), ('DRAGON', 'DRAGON'),
        ('DARK', 'DARK'), ('STEEL', 'STEEL'), ('FAIRY', 'FAIRY')
    ]

    entry = models.IntegerField()
    name = models.CharField(max_length=20, unique=True)
    type1 = models.CharField(max_length=20, choices=TYPES)
    type2 = models.CharField(max_length=20, choices=TYPES, null=True, blank=True)
    images = models.JSONField()
    sprite = models.ImageField()
    # Stats
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    spattack = models.IntegerField()
    spdefense = models.IntegerField()
    speed = models.IntegerField()
    total = models.IntegerField()
    # Type Effectiveness
    fourx = models.JSONField(default=list, null=True, blank=True)
    twox = models.JSONField(default=list, null=True, blank=True)
    onex = models.JSONField(default=list, null=True, blank=True)
    halfx = models.JSONField(default=list, null=True, blank=True)
    zerox = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.name