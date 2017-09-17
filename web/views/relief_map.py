from web.models import ReliefMap, Membership
from web.serializers import ReliefMapSerializer
from web.permissions import IsAdminOfPermission

from rest_framework import viewsets

from django.core.exceptions import ObjectDoesNotExist

class ReliefMapViewSet(viewsets.ModelViewSet):
    serializer_class = ReliefMapSerializer
    permission_classes = (IsAdminOfPermission,)

    def get_queryset(self):
        user = self.request.user
        memberships = Membership.objects.filter(user=user)

        memberables = (x.memberable.cast() for x in memberships)
        relief_maps = [x for x in memberables if x.get_instance_name() == 'reliefmap']
        ids = (x.id for x in relief_maps)

        public_maps = ReliefMap.objects.filter(public=True).exclude(id__in=ids)

        return relief_maps + list(public_maps)
