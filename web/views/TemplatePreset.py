from rest_framework import viewsets

from web.models import TemplatePreset
from web.serializers import TemplatePresetSerializer

class TemplatePresetViewSet(viewsets.ModelViewSet):
    queryset = TemplatePreset.objects.all()
    serializer_class = TemplatePresetSerializer
