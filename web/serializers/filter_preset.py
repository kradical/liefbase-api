from web.models import FilterPreset, MapItemTemplate, ReliefMap

from rest_framework import serializers

class FilterPresetSerializer(serializers.ModelSerializer):
    mapItemTemplates = serializers.PrimaryKeyRelatedField(many=True, queryset=MapItemTemplate.objects.all(), source='templates')
    reliefMap = serializers.PrimaryKeyRelatedField(queryset=ReliefMap.objects.all(), source='relief_map')

    def create(self, validated_data):
        user = self.context['request'].user
        templates = validated_data.pop('templates', [])

        preset = FilterPreset.objects.create(owner=user, **validated_data)
        preset.templates = templates
        preset.save()

        return preset

    class Meta:
        model = FilterPreset
        fields = ('id', 'name', 'reliefMap', 'mapItemTemplates')
