from rest_framework.serializers import CurrentUserDefault
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from dynamic_rest.serializers import DynamicRelationField, WithDynamicModelSerializerMixin

from web.models import MapItem

class MapItemSerializer(GeoFeatureModelSerializer):
    pass

class DynamicMapItemSerializer(WithDynamicModelSerializerMixin, MapItemSerializer):
    mapItemTemplate = DynamicRelationField('web.serializers.MapItemTemplateSerializer')
    owner = DynamicRelationField('web.serializers.UserSerializer', read_only=True, default=CurrentUserDefault())

    class Meta:
        model = MapItem
        name = 'mapItem'
        geo_field = "point"
        fields = ('id', 'quantity', 'mapItemTemplate', 'owner', 'createdAt', 'updatedAt')
