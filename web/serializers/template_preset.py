from web.models import TemplatePreset

from rest_framework import serializers

class TemplatePresetSerializer(serializers.ModelSerializer):
    rawTemplates = serializers.JSONField(source='raw_templates')

    def create(self, validated_data):
        user = self.context['request'].user
        return TemplatePreset.objects.create(owner=user, **validated_data)

    class Meta:
        model = TemplatePreset
        fields = ('id', 'name', 'rawTemplates')
