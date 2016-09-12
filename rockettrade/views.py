from .models import Listing
from .serializers import ListingSerializer, UserSerializer

from django.contrib.auth.models import User

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
