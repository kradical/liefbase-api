from web.serializers import MapItemTemplateSerializer

from web.models import ReliefMap

from rest_framework import serializers


class ReliefMapSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
    mapitemtemplate_set = MapItemTemplateSerializer(read_only=True, many=True)

    class Meta:
        model = ReliefMap
        fields = ('id', 'name', 'description', 'owner', 'mapitemtemplate_set')
