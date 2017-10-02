from dynamic_rest.viewsets import DynamicModelViewSet

from web.models import MapItem
from web.serializers import MapItemSerializer
from web.permissions import ItemReliefMapPermission

class MapItemViewSet(DynamicModelViewSet):
    queryset = MapItem.objects.all()
    serializer_class = MapItemSerializer
    permission_classes = (ItemReliefMapPermission,)
