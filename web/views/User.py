from dynamic_rest.viewsets import DynamicModelViewSet

from web.serializers import UserSerializer, MembershipSerializer, OrganizationSerializer, TeamSerializer
from web.permissions import UserPermission, MembershipPermission, IsAdminOfPermission
from web.models import User, Membership, Organization, Team

class UserViewSet(DynamicModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    def get_object(self):
        if self.kwargs.get('pk', None) == 'me':
            self.kwargs['pk'] = self.request.user.pk

        return super(UserViewSet, self).get_object()

class OrganizationViewSet(DynamicModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAdminOfPermission,)

class TeamViewSet(DynamicModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAdminOfPermission,)

class MembershipViewSet(DynamicModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = (MembershipPermission,)
