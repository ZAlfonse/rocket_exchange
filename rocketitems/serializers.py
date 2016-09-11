from .models import Item, Rarity, Category
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'rarity', 'category', 'platform_restrictions')


class RaritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rarity
        fields = ('id', 'name', 'rank')
