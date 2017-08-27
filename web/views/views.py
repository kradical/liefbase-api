from web.models import ReliefMap
from web.serializers import ReliefMapSerializer, UserSerializer
from web.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from django.contrib.auth.models import User


class ReliefMapViewSet(viewsets.ModelViewSet):
    queryset = ReliefMap.objects.all()
    serializer_class = ReliefMapSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
