from web.models import MapItem, MapItemTemplate, ReliefMap

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class MapItemSerializer(GeoFeatureModelSerializer):
    template = serializers.PrimaryKeyRelatedField(queryset=MapItemTemplate.objects.all())

    def create(self, validated_data):
        user = self.context['request'].user
        return FilterPreset.objects.create(owner=user, **validated_data)

    class Meta:
        model = MapItem
        geo_field = "point"
        fields = ('id', 'quantity', 'template')
