from web.serializers import UserSerializer, OrganizationSerializer
from web.permissions import IsStaffOrCreate
from web.models import User, Group

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsStaffOrCreate,)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.filter(type='organization')
    serializer_class = OrganizationSerializer

