from web.models import TemplatePreset
from web.serializers import TemplatePresetSerializer

from rest_framework import permissions
from rest_framework import viewsets


class TemplatePresetViewSet(viewsets.ModelViewSet):
    queryset = TemplatePreset.objects.all()
    serializer_class = TemplatePresetSerializer
    permission_classes = (permissions.IsAuthenticated,)
