from dynamic_rest.viewsets import DynamicModelViewSet

from web.models import MapItem
from web.serializers import DynamicMapItemSerializer
from web.permissions import ItemReliefMapPermission

class MapItemViewSet(DynamicModelViewSet):
    queryset = MapItem.objects.all()
    serializer_class = DynamicMapItemSerializer
    permission_classes = (ItemReliefMapPermission,)
