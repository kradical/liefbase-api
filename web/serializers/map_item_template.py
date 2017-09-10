from web.serializers import MapItemSerializer
from web.models import MapItemTemplate, ReliefMap

from rest_framework import serializers


class MapItemTemplateSerializer(serializers.ModelSerializer):
    map_items = MapItemSerializer(read_only=True, many=True, source='mapitem_set')

    def create(self, validated_data):
        user = self.context['request'].user
        return MapItemTemplate.objects.create(owner=user, **validated_data)

    class Meta:
        model = MapItemTemplate
        fields = ('id', 'name', 'category', 'sub_category', 'relief_map', 'map_items')
