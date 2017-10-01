from dynamic_rest.viewsets import DynamicModelViewSet

from web.models import MapItemTemplate
from web.serializers import MapItemTemplateSerializer
from web.permissions import ObjectReliefMapPermission

class MapItemTemplateViewSet(DynamicModelViewSet):
    queryset = MapItemTemplate.objects.all()
    serializer_class = MapItemTemplateSerializer
    permission_classes = (ObjectReliefMapPermission,)
