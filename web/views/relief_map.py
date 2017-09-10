from web.models import ReliefMap
from web.serializers import ReliefMapSerializer
from web.views import MemberableViewSet

from rest_framework import permissions
from rest_framework import viewsets


class ReliefMapViewSet(MemberableViewSet):
    queryset = ReliefMap.objects.all()
    serializer_class = ReliefMapSerializer
    permission_classes = (permissions.IsAuthenticated,)
