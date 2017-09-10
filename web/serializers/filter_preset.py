from web.models import FilterPreset, MapItemTemplate, ReliefMap
from web.serializers import MapItemTemplateSerializer

from rest_framework import serializers


class FilterPresetSerializer(serializers.ModelSerializer):
    templates = MapItemTemplateSerializer(read_only=True, many=True)
    relief_map = serializers.PrimaryKeyRelatedField(queryset=ReliefMap.objects.all())

    def create(self, validated_data):
        user = self.context['request'].user
        return FilterPreset.objects.create(owner=user, **validated_data)

    class Meta:
        model = FilterPreset
        fields = ('id', 'name', 'relief_map', 'templates')
