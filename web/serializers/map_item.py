from web.models import MapItem, MapItemTemplate, ReliefMap

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class MapItemSerializer(GeoFeatureModelSerializer):
    template = serializers.PrimaryKeyRelatedField(queryset=MapItemTemplate.objects.all())

    class Meta:
        model = MapItem
        geo_field = "point"
        fields = ('id', 'quantity', 'template')
