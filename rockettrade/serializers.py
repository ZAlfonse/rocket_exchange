from .models import Listing, Offer, User
from rocketitems.serializers import VariationSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'steam_persona', 'steam_profile', 'steam_avatar'
        )


class OfferSerializer(serializers.ModelSerializer):
    bidder = UserSerializer()
    items = VariationSerializer(many=True)

    class Meta:
        model = Offer
        fields = (
            'created', 'edited', 'items', 'seller', 'bidder'
        )


class ListingSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    buyer = UserSerializer()
    status = serializers.SerializerMethodField()

    items = VariationSerializer(many=True)

    class Meta:
        model = Listing
        fields = (
            'status', 'created', 'edited',
            'closed', 'items', 'seller', 'buyer'
        )

    def get_status(self, obj):
        return obj.get_status_display()
