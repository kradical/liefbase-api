from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from web.models import MapItem, MapItemTemplate, ReliefMap

class MapItemSerializer(GeoFeatureModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        return MapItem.objects.create(owner=user, **validated_data)

    class Meta:
        model = MapItem
        geo_field = "point"
        fields = ('id', 'quantity', 'mapItemTemplate', 'owner', 'createdAt', 'updatedAt')
