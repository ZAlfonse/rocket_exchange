from .models import Listing, ListingItem, User
from rocketitems.serializers import VariationSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'steam_persona', 'steam_profile', 'steam_avatar'
        )


class ListingItemSerializer(serializers.ModelSerializer):
    variation = VariationSerializer()

    class Meta:
        model = ListingItem
        fields = (
            'name', 'quantity', 'price', 'value', 'variation'
        )


class ListingSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    buyer = UserSerializer()
    listing_items = ListingItemSerializer(many=True)

    status = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = (
            'status', 'created', 'edited',
            'closed', 'listing_items', 'seller', 'buyer'
        )

    def get_status(self, obj):
        return obj.get_status_display()
