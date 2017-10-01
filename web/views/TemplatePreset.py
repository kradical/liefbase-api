from dynamic_rest.viewsets import DynamicModelViewSet

from web.models import TemplatePreset
from web.serializers import TemplatePresetSerializer

class TemplatePresetViewSet(DynamicModelViewSet):
    queryset = TemplatePreset.objects.all()
    serializer_class = TemplatePresetSerializer
