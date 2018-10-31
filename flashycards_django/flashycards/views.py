from rest_framework import viewsets
from models import Flashcard, Deck
from serializers import FlashcardSerializer, DeckSerializer

class FlashcardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Flashcard to be CRUDed.
    """
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

class DeckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Deck to be CRUDed.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
