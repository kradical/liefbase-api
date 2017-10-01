from rest_framework.serializers import CurrentUserDefault
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from web.models import ReliefMap, Membership, MapItemTemplate

class ReliefMapSerializer(DynamicModelSerializer):
    mapItemTemplates = DynamicRelationField('web.serializers.MapItemTemplateSerializer',many=True, source='mapitemtemplate_set')
    owner = DynamicRelationField('web.serializers.UserSerializer', read_only=True, default=CurrentUserDefault())

    def create(self, validated_data):
        reliefMap = ReliefMap.objects.create(**validated_data)

        user = self.context['request'].user
        Membership.objects.create(type='admin', memberable=reliefMap, user=user)

        return reliefMap

    class Meta:
        model = ReliefMap
        name = 'reliefMap'
        fields = ('id', 'name', 'description', 'mapItemTemplates', 'public', 'owner', 'createdAt', 'updatedAt')
