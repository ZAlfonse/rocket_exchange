from .models import Listing, User
from .serializers import ListingSerializer, UserSerializer

from rest_framework import viewsets


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
