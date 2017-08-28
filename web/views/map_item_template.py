from web.models import MapItemTemplate
from web.serializers import MapItemTemplateSerializer

from rest_framework import viewsets


class MapItemTemplateViewSet(viewsets.ModelViewSet):
    queryset = MapItemTemplate.objects.all()
    serializer_class = MapItemTemplateSerializer
