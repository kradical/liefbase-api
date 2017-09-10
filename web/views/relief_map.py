from web.models import ReliefMap
from web.serializers import ReliefMapSerializer

from rest_framework import permissions
from rest_framework import viewsets


class ReliefMapViewSet(viewsets.ModelViewSet):
    queryset = ReliefMap.objects.all()
    serializer_class = ReliefMapSerializer
    permission_classes = (permissions.IsAuthenticated,)
