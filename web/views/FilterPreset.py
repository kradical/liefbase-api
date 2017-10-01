from rest_framework import viewsets

from web.models import FilterPreset
from web.serializers import FilterPresetSerializer
from web.permissions import ObjectReliefMapPermission

class FilterPresetViewSet(viewsets.ModelViewSet):
    queryset = FilterPreset.objects.all()
    serializer_class = FilterPresetSerializer
    permission_classes = (ObjectReliefMapPermission,)
