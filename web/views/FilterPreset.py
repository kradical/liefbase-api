from dynamic_rest.viewsets import DynamicModelViewSet

from web.models import FilterPreset
from web.serializers import FilterPresetSerializer
from web.permissions import ObjectReliefMapPermission

class FilterPresetViewSet(DynamicModelViewSet):
    queryset = FilterPreset.objects.all()
    serializer_class = FilterPresetSerializer
    permission_classes = (ObjectReliefMapPermission,)
