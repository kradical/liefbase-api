from web.serializers import MapItemTemplateSerializer

from web.models import ReliefMap

from rest_framework import serializers


class ReliefMapSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
    map_item_templates = MapItemTemplateSerializer(read_only=True, many=True, source='mapitemtemplate_set')

    def create(self, validated_data):
        user = self.context['request'].user
        return FilterPreset.objects.create(owner=user, **validated_data)

    class Meta:
        model = ReliefMap
        fields = ('id', 'name', 'description', 'owner', 'map_item_templates')
