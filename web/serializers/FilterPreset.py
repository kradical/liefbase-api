from rest_framework.serializers import CurrentUserDefault
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from web.models import FilterPreset, MapItemTemplate, ReliefMap

class FilterPresetSerializer(DynamicModelSerializer):
    mapItemTemplates = DynamicRelationField('web.serializers.MapItemTemplateSerializer', many=True)
    reliefMap = DynamicRelationField('web.serializers.ReliefMapSerializer')
    owner = DynamicRelationField('web.serializers.UserSerializer', read_only=True, default=CurrentUserDefault())

    def create(self, validated_data):
        mapItemTemplates = validated_data.pop('mapItemTemplates', [])

        preset = FilterPreset.objects.create(**validated_data)

        preset.mapItemTemplates = mapItemTemplates
        preset.save()

        return preset

    class Meta:
        model = FilterPreset
        name = 'filterPreset'
        fields = ('id', 'name', 'reliefMap', 'mapItemTemplates', 'owner', 'createdAt', 'updatedAt')
