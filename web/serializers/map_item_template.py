from web.models import MapItemTemplate, ReliefMap

from rest_framework import serializers


class MapItemTemplateSerializer(serializers.ModelSerializer):
    relief_map = serializers.PrimaryKeyRelatedField(queryset=ReliefMap.objects.all())

    class Meta:
        model = MapItemTemplate
        fields = ('id', 'name', 'category', 'sub_category', 'relief_map')
