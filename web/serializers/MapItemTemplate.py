from rest_framework.serializers import CurrentUserDefault
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from web.models import MapItemTemplate

class MapItemTemplateSerializer(DynamicModelSerializer):
    mapItems = DynamicRelationField('web.serializers.MapItemSerializer', many=True, source='mapitem_set')
    reliefMap = DynamicRelationField('web.serializers.ReliefMapSerializer')
    owner = DynamicRelationField('web.serializers.UserSerializer', read_only=True, default=CurrentUserDefault())

    class Meta:
        model = MapItemTemplate
        name = 'mapItemTemplate'
        fields = ('id', 'name', 'category', 'subCategory', 'reliefMap', 'mapItems', 'owner', 'createdAt', 'updatedAt')
