from web.models import MapItem
from web.serializers import MapItemSerializer

from rest_framework import viewsets


class MapItemViewSet(viewsets.ModelViewSet):
    queryset = MapItem.objects.all()
    serializer_class = MapItemSerializer
