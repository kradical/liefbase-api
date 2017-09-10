from web.serializers import UserSerializer, OrganizationSerializer, TeamSerializer, MembershipSerializer
from web.permissions import UserPermission, OrganizationPermission, MembershipPermission
from web.models import User, Organization, Team, Membership

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (OrganizationPermission,)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (OrganizationPermission,)

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = (MembershipPermission,)
