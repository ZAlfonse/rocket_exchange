from .models import Listing, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
