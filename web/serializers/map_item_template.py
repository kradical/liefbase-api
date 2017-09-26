from web.serializers import MapItemSerializer
from web.models import MapItemTemplate, ReliefMap

from rest_framework import serializers


class MapItemTemplateSerializer(serializers.ModelSerializer):
    mapItems = MapItemSerializer(read_only=True, many=True, source='mapitem_set')
    reliefMap = serializers.PrimaryKeyRelatedField(queryset=ReliefMap.objects.all(), source='relief_map')
    subCategory = serializers.CharField(source="sub_category")

    def create(self, validated_data):
        user = self.context['request'].user
        return MapItemTemplate.objects.create(owner=user, **validated_data)

    class Meta:
        model = MapItemTemplate
        fields = ('id', 'name', 'category', 'subCategory', 'reliefMap', 'mapItems')
