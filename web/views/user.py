from web.serializers import UserSerializer
from web.permissions import IsOwnerOrReadOnly

from rest_framework import permissions
from rest_framework import viewsets

from django.contrib.auth.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
