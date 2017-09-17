from web.models import MapItem
from web.serializers import MapItemSerializer
from web.permissions import ItemReliefMapPermission

from rest_framework import viewsets
from rest_framework.response import Response

class MapItemViewSet(viewsets.ModelViewSet):
    queryset = MapItem.objects.all()
    serializer_class = MapItemSerializer
    permission_classes = (ItemReliefMapPermission,)
