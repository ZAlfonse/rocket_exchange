from .models import Listing
from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
