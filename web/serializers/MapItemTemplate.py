from rest_framework import serializers

from web.serializers import MapItemSerializer
from web.models import MapItemTemplate, ReliefMap, MapItem

class MapItemTemplateSerializer(serializers.ModelSerializer):
    mapItems = serializers.PrimaryKeyRelatedField(queryset=MapItem.objects.all(), many=True, source='mapitem_set')

    def create(self, validated_data):
        user = self.context['request'].user
        return MapItemTemplate.objects.create(owner=user, **validated_data)

    class Meta:
        model = MapItemTemplate
        fields = ('id', 'name', 'category', 'subCategory', 'reliefMap', 'mapItems', 'owner', 'createdAt', 'updatedAt')
