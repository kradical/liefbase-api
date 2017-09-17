from web.models import FilterPreset
from web.serializers import FilterPresetSerializer
from web.permissions import ObjectReliefMapPermission

from rest_framework import viewsets

class FilterPresetViewSet(viewsets.ModelViewSet):
    queryset = FilterPreset.objects.all()
    serializer_class = FilterPresetSerializer
    permission_classes = (ObjectReliefMapPermission,)
