from rest_framework.serializers import CurrentUserDefault
from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField

from web.models import TemplatePreset

class TemplatePresetSerializer(DynamicModelSerializer):
    owner = DynamicRelationField('web.serializers.UserSerializer', read_only=True, default=CurrentUserDefault())

    class Meta:
        model = TemplatePreset
        name = 'templatePreset'
        fields = ('id', 'name', 'rawTemplates', 'owner', 'createdAt', 'updatedAt')
