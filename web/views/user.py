from web.serializers import UserSerializer, OrganizationSerializer, TeamSerializer, MembershipSerializer
from web.permissions import UserPermission, OrganizationPermission, MembershipPermission, AddMemberPermission
from web.models import User, Organization, Team, Membership, Memberable

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, MethodNotAllowed, APIException
from rest_framework import status

from django.db.utils import IntegrityError

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

class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission,)

    def list(self, request, memberable_pk):
        try:
            admins = (x.user for x in Membership.objects.filter(type='admin', memberable_id=memberable_pk))
        except Membership.DoesNotExist:
            raise NotFound()

        serializer = UserSerializer(admins, many=True)
        return Response(serializer.data)

    def create(self, request, memberable_pk):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)
            user = User.objects.get(id=request.data['user'])
        except (Memberable.DoesNotExist, User.DoesNotExist):
            raise NotFound()

        membership, created = Membership.objects.get_or_create(type='admin', user=user, memberable=memberable)
        
        serializer = MembershipSerializer(membership)
        s = status.HTTP_201_CREATED if created else status.HTTP_409_CONFLICT

        return Response(serializer.data, status=s)

    def retrieve(self, request, memberable_pk, pk=None):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)
            user = User.objects.get(id=pk)
            membership = Membership.objects.get(type='admin', user=user, memberable=memberable)
        except (Memberable.DoesNotExist, User.DoesNotExist, Membership.DoesNotExist):
            raise NotFound()

        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    def update(self, request, memberable_pk, pk=None):
        return self.partial_update(request, memberable_pk, pk)

    def partial_update(self, request, memberable_pk, pk=None):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)
            user = User.objects.get(id=pk)
            membership = Membership.objects.get(type='admin', user=user, memberable=memberable)
        except (Memberable.DoesNotExist, User.DoesNotExist, Membership.DoesNotExist):
            raise NotFound()

        try:
            membership_type = request.data['type']
        except KeyError:
            return Response({ 'detail': 'type is a required field'}, status=status.HTTP_400_BAD_REQUEST)
        
        membership.type = membership_type

        try:
            membership.save()
        except IntegrityError:
            membership.delete()
            membership = Membership.objects.get(type=membership_type, user=user, memberable=memberable)

        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    def destroy(self, request, memberable_pk, pk=None):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)
            user = User.objects.get(id=pk)
            
            # add them back as a member if they aren't already
            Membership.objects.get(type='admin', user=user, memberable=memberable).delete()
            Membership.objects.get_or_create(type='member', user=user, memberable=memberable)
        except (Memberable.DoesNotExist, User.DoesNotExist, Membership.DoesNotExist):
            raise NotFound()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission,)

    def list(self, request, memberable_pk):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)    
        except Memberable.DoesNotExist:
            raise NotFound()

        members = (x.user for x in Membership.objects.filter(type='member', memberable=memberable))
        
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)

    def create(self, request, memberable_pk):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)
            user = User.objects.get(id=request.data['user'])
        except (Memberable.DoesNotExist, User.DoesNotExist):
            raise NotFound()

        membership, created = Membership.objects.get_or_create(type='member', user=user, memberable=memberable)
        
        serializer = MembershipSerializer(membership)
        s = status.HTTP_201_CREATED if created else status.HTTP_409_CONFLICT

        return Response(serializer.data, status=s)

    def retrieve(self, request, memberable_pk, pk=None):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)
            user = User.objects.get(id=pk)
            membership = Membership.objects.get(type='member', user=user, memberable=memberable)
        except (Memberable.DoesNotExist, User.DoesNotExist, Membership.DoesNotExist):
            raise NotFound()

        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    def update(self, request, memberable_pk, pk=None):
        return self.partial_update(request, memberable_pk, pk)

    def partial_update(self, request, memberable_pk, pk=None):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)
            user = User.objects.get(id=pk)
            membership = Membership.objects.get(type='member', user=user, memberable=memberable)
        except (Memberable.DoesNotExist, User.DoesNotExist, Membership.DoesNotExist):
            raise NotFound()

        try:
            membership_type = request.data['type']
        except KeyError:
            return Response({ 'detail': 'type is a required field'}, status=status.HTTP_400_BAD_REQUEST)
        
        membership.type = membership_type

        try:
            membership.save()
        except IntegrityError:
            membership.delete()
            membership = Membership.objects.get(type=membership_type, user=user, memberable=memberable)

        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    def destroy(self, request, memberable_pk, pk=None):
        try:
            memberable = Memberable.objects.get(pk=memberable_pk)
            user = User.objects.get(id=pk)
            Membership.objects.get(type='member', user=user, memberable=memberable).delete()
        except (Memberable.DoesNotExist, User.DoesNotExist, Membership.DoesNotExist):
            raise NotFound()

        return Response(status=status.HTTP_204_NO_CONTENT)
