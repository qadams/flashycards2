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
    # #push_live method was taken from online from the github user, highfivecode
    # def getNumCards(self):
    #     num = self.card_set.count()
	#     return '%s' %(self.num)
    # def push_live(modeladmin, request, queryset):
    #     rows_updated = queryset.update(is_active=True)
    #     if rows_updated == 1:
    #         message_bit = "A deck was"
    #     else:
    #         message_bit = "%s decks were" % rows_updated
    #     modeladmin.message_user(request, "%s successfully marked as active." % message_bit)
    # list_display = ('name' ,'is_active', 'getNumCards')
    # list_filter=('is_active',)
    # search_fields = ['name', 'description']
    # actions = [push_live]
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
