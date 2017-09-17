from web.models import MapItemTemplate
from web.serializers import MapItemTemplateSerializer
from web.permissions import ObjectReliefMapPermission

from rest_framework import viewsets
from rest_framework.response import Response

class MapItemTemplateViewSet(viewsets.ModelViewSet):
    queryset = MapItemTemplate.objects.all()
    serializer_class = MapItemTemplateSerializer
    permission_classes = (ObjectReliefMapPermission,)
