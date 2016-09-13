from .models import Listing, User
from rocketitems.serializers import ItemSerializer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username'
        )


class ListingSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    buyer = UserSerializer()
    item = ItemSerializer()

    status = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = (
            'status', 'quantity', 'price',
            'created', 'edited', 'closed',
            'item', 'seller', 'buyer'
        )

    def get_status(self, obj):
        return obj.get_status_display()
