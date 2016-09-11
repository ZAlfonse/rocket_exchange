from .models import Item, Rarity, Category
from .serializers import ItemSerializer, RaritySerializer, CategorySerializer

from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RarityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rarities to be viewed or edited
    """
    queryset = Rarity.objects.all().order_by('rank')
    serializer_class = RaritySerializer
