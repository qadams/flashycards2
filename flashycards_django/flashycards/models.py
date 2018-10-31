from __future__ import unicode_literals
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User, Group
from django.contrib import admin
import base64

# Create your models here.
class Deck(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=True)
    # is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "deck"

class DeckAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Flashcard(models.Model):
    # parentDeck = models.ForeignKey(Deck, on_delete=models.CASCADE, blank=True, null=True)
    term = models.TextField(max_length=50)
    definition = models.TextField(max_length=250)
    def __str__(self):
        return self.term
    class JSONAPIMeta:
        resource_name = "flashcard"

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id',)
