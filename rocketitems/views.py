from .models import Item, Quality, Type
from .serializers import ItemSerializer, QualitySerializer, TypeSerializer

from rest_framework import viewsets


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class QualityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rarities to be viewed or edited
    """
    queryset = Quality.objects.all().order_by('sort')
    serializer_class = QualitySerializer
