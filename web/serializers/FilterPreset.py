from rest_framework import serializers

from web.models import FilterPreset, MapItemTemplate, ReliefMap

class FilterPresetSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        mapItemTemplates = validated_data.pop('mapItemTemplates', [])

        preset = FilterPreset.objects.create(owner=user, **validated_data)
        preset.mapItemTemplates = mapItemTemplates
        preset.save()

        return preset

    class Meta:
        model = FilterPreset
        fields = ('id', 'name', 'reliefMap', 'mapItemTemplates', 'owner', 'createdAt', 'updatedAt')
