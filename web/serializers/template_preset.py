from web.models import TemplatePreset

from rest_framework import serializers


class TemplatePresetSerializer(serializers.ModelSerializer):

    class Meta:
        model = TemplatePreset
        fields = ('id', 'name', 'raw_templates')
