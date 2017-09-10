from web.serializers import MapItemSerializer
from web.models import MapItemTemplate, ReliefMap

from rest_framework import serializers


class MapItemTemplateSerializer(serializers.ModelSerializer):
    mapitem_set = MapItemSerializer(read_only=True, many=True)

    class Meta:
        model = MapItemTemplate
        fields = ('id', 'name', 'category', 'sub_category', 'relief_map', 'mapitem_set')
