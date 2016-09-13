from .models import Item, Quality, Type, Pack
from rest_framework import serializers


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name',)


class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality
        fields = ('name', 'sort')


class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = ('name', 'release_date')


class ItemSerializer(serializers.ModelSerializer):
    quality = QualitySerializer()
    type = TypeSerializer()
    pack = PackSerializer()

    class Meta:
        model = Item
        fields = ('id', 'name', 'quality', 'type', 'pack', 'platform_restrictions')
