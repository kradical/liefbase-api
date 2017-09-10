from web.serializers import UserSerializer, OrganizationSerializer, TeamSerializer, MembershipSerializer
from web.permissions import UserPermission, OrganizationPermission, MembershipPermission, AddMemberPermission
from web.models import User, Organization, Team, Membership, Memberable

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

class MemberableViewSet(viewsets.ModelViewSet):
    def get_member_of_type(self, type, pk):
        try:
            memberable = Memberable.objects.get(pk=pk)
        except Memberable.DoesNotExist:
            raise NotFound()

        memberships = Membership.objects.filter(type=type, memberable=memberable)
        members = (x.user for x in memberships)
        
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)

    def create_member_of_type(self, type, pk, request):
        try:
            memberable = Memberable.objects.get(pk=pk)
            user = User.objects.get(id=request.data['user'])
        except (Memberable.DoesNotExist, User.DoesNotExist):
            raise NotFound()

        membership, created = Membership.objects.get_or_create(type=type, user=user, memberable=memberable)
        
        serializer = MembershipSerializer(membership)
        s = status.HTTP_201_CREATED if created else status.HTTP_409_CONFLICT

        return Response(serializer.data, status=s)

    @detail_route(methods=['get', 'post'], permission_classes=[AddMemberPermission], url_path='admins')
    def get_admins(self, request, pk=None):
        if request.method == 'POST':
            return self.create_member_of_type('admin', pk, request)
        elif request.method == 'GET':
            return self.get_member_of_type('admin', pk)

    @detail_route(methods=['get', 'post'], permission_classes=[AddMemberPermission], url_path='members')
    def get_members(self, request, pk=None):
        if request.method == 'POST':
            return self.create_member_of_type('member', pk, request)
        elif request.method == 'GET':
            return self.get_member_of_type('member', pk)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

class OrganizationViewSet(MemberableViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (OrganizationPermission,) 

class TeamViewSet(MemberableViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (OrganizationPermission,)

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = (MembershipPermission,)
