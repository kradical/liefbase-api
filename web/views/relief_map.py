from web.models import ReliefMap
from web.serializers import ReliefMapSerializer
from web.permissions import IsOwner

from rest_framework import permissions
from rest_framework import viewsets


class ReliefMapViewSet(viewsets.ModelViewSet):
    serializer_class = ReliefMapSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return ReliefMap.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
