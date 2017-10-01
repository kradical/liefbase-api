from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets

from web.models import ReliefMap, Membership
from web.serializers import ReliefMapSerializer
from web.permissions import IsAdminOfPermission

class ReliefMapViewSet(viewsets.ModelViewSet):
    serializer_class = ReliefMapSerializer
    permission_classes = (IsAdminOfPermission,)

    def get_queryset(self):
        user = self.request.user

        ids = []
        if user.is_authenticated():
            memberships = Membership.objects.filter(user=user)

            memberables = (x.memberable.cast() for x in memberships)
            ids = (x.id for x in memberables if x.get_instance_name() == 'reliefmap')

        return ReliefMap.objects.filter(Q(public=True) | Q(id__in=ids))
