from rest_framework import serializers

from web.models import ReliefMap, Membership, MapItemTemplate
from web.serializers import MapItemTemplateSerializer

class ReliefMapSerializer(serializers.ModelSerializer):
    mapItemTemplates = serializers.PrimaryKeyRelatedField(queryset=MapItemTemplate.objects.all(), many=True, source='mapitemtemplate_set')

    def create(self, validated_data):
        user = self.context['request'].user
        reliefMap = ReliefMap.objects.create(owner=user, **validated_data)

        Membership.objects.create(type='admin', memberable=reliefMap, user=user)

        return reliefMap

    class Meta:
        model = ReliefMap
        fields = ('id', 'name', 'description', 'mapItemTemplates', 'public', 'owner', 'createdAt', 'updatedAt')
