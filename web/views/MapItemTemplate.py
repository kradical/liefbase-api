from rest_framework import viewsets
from rest_framework.response import Response

from web.models import MapItemTemplate
from web.serializers import MapItemTemplateSerializer
from web.permissions import ObjectReliefMapPermission

class MapItemTemplateViewSet(viewsets.ModelViewSet):
    queryset = MapItemTemplate.objects.all()
    serializer_class = MapItemTemplateSerializer
    permission_classes = (ObjectReliefMapPermission,)
