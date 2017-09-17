from web.models import FilterPreset, MapItemTemplate, ReliefMap
from web.serializers import FilterPresetSerializer
from web.permissions import ObjectReliefMapPermission

from rest_framework import viewsets
from rest_framework.response import Response

class FilterPresetViewSet(viewsets.ModelViewSet):
    queryset = FilterPreset.objects.all()
    serializer_class = FilterPresetSerializer
    permission_classes = (ObjectReliefMapPermission,)
