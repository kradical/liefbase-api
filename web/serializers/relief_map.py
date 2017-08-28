from web.serializers import MapItemSerializer

from web.models import ReliefMap

from rest_framework import serializers


class ReliefMapSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
    map_items = MapItemSerializer(read_only=True, many=True, source='get_map_items')

    class Meta:
        model = ReliefMap
        fields = ('id', 'name', 'description', 'owner', 'map_items')
