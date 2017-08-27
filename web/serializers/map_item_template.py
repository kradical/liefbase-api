from web.models import MapItemTemplate

from rest_framework import serializers


class MapItemTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapItemTemplate
        fields = ('id', 'name', 'category', 'sub_category')
