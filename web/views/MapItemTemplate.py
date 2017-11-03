from dynamic_rest.viewsets import DynamicModelViewSet

from web.models import MapItemTemplate, DataLayer
from web.serializers import MapItemTemplateSerializer, DataLayerSerializer
from web.permissions import ObjectReliefMapPermission

class MapItemTemplateViewSet(DynamicModelViewSet):
    queryset = MapItemTemplate.objects.all()
    serializer_class = MapItemTemplateSerializer
    permission_classes = (ObjectReliefMapPermission,)

class DataLayerViewSet(DynamicModelViewSet):
    queryset = DataLayer.objects.all()
    serializer_class = DataLayerSerializer
    permission_classes = (ObjectReliefMapPermission,)
