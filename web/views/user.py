from web.serializers import UserSerializer
from web.permissions import IsStaffOrCreate

from rest_framework import viewsets

from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsStaffOrCreate,)
