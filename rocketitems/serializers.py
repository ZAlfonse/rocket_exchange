from .models import Item, Attribute, Quality, Type, Pack, Variation, VariationAttribute
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


class AttributeSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Attribute
        fields = ('name', 'type')

    def get_type(self, obj):
        return obj.get_type_display()


class VariationAttributeSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = VariationAttribute
        fields = ('id', 'attribute')


class VariationSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    attributes = VariationAttributeSerializer(many=True)

    class Meta:
        model = Variation
        fields = ('id', 'item', 'attributes')
