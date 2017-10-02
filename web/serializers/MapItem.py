from rest_framework.serializers import CurrentUserDefault
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from dynamic_rest.serializers import DynamicRelationField, DynamicModelSerializer

from web.models import MapItem

"""
Roll our own geojson serializer because dynamic_rest doesn't play nicely with drf's
"""
class MapItemSerializer(DynamicModelSerializer):
    mapItemTemplate = DynamicRelationField('web.serializers.MapItemTemplateSerializer')
    owner = DynamicRelationField('web.serializers.UserSerializer', read_only=True, default=CurrentUserDefault())

    def to_representation(self, instance):
        data = super(MapItemSerializer, self).to_representation(instance)

        if self.id_only():
            return data

        properties = {}

        # add everything to properties so client can find it where expected.
        for key in data:
            if key not in ('id', self.Meta.geo_field):
                properties[key] = data[key]

        for key in properties:
            # keep dynamic related fields at the top level so dynamic_rest can extract them properly
            if key in ('owner', 'mapItemTemplate'):
                # nest id only
                try:
                    properties[key] = int(properties[key])
                except:
                    properties[key] = properties[key]['id']
            else:
                data.pop(key)

        data['properties'] = properties
        data['geometry'] = data[self.Meta.geo_field]
        data['type'] = 'Feature'

        data.pop(self.Meta.geo_field)

        return data

    def to_internal_value(self, data):
        # add all the properties to the top level object so dynamic_rest picks them up
        attrs = data
        if 'properties' in data:
            attrs = data["properties"]

            if 'geometry' in data:
                attrs[self.Meta.geo_field] = data['geometry']


        return super(MapItemSerializer, self).to_internal_value(attrs)

    class Meta:
        model = MapItem
        name = 'mapItem'
        geo_field = 'point'
        fields = ('id', 'quantity', 'mapItemTemplate', 'point', 'owner', 'createdAt', 'updatedAt')
