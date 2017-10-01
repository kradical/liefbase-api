from rest_framework import permissions
from rest_framework.exceptions import NotFound

from web.models import ReliefMap, Membership, Memberable, MapItemTemplate

def is_admin_of(pk, user):
    try:
        memberable = Memberable.objects.get(pk=pk)
    except Memberable.DoesNotExist:
        raise NotFound()

    isAdmin = Membership.objects.filter(user=user, memberable=memberable, type='admin').exists()
    return isAdmin

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        return obj == request.user

class IsAdminOfPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        isAdmin = Membership.objects.filter(user=request.user, memberable=obj, type='admin').exists()

        return isAdmin

class ObjectReliefMapPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        try:
            pk = request.data['reliefMap']
            reliefMap = ReliefMap.objects.get(id=pk)
        except ReliefMap.DoesNotExist:
            raise NotFound()
        except KeyError:
            return request.user.is_authenticated()

        # has any sort of membership to the relief map
        isMemberOrAdmin = Membership.objects.filter(user=request.user, memberable=reliefMap).exists()
        return isMemberOrAdmin

    def has_object_permission(self, request, view, obj):
        isMemberOrAdmin = Membership.objects.filter(user=request.user, memberable=obj.reliefMap).exists()
        return isMemberOrAdmin

class ItemReliefMapPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != 'POST':
            return request.user.is_authenticated()

        try:
            pk = request.data['properties']['mapItemTemplate']
            mapItemTemplate = MapItemTemplate.objects.get(id=pk)
        except (MapItemTemplate.DoesNotExist, KeyError):
            raise NotFound()

        # has any sort of membership to the relief map
        isMemberOrAdmin = Membership.objects.filter(user=request.user, memberable=mapItemTemplate.reliefMap).exists()
        return isMemberOrAdmin

    def has_object_permission(self, request, view, obj):
        isMemberOrAdmin = Membership.objects.filter(user=request.user, memberable=obj.mapItemTemplate.reliefMap).exists()
        return isMemberOrAdmin


class MembershipPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        try:
            pk = request.data['memberable']
        except KeyError:
            raise request.user.is_authenticated()

        return is_admin_of(pk, request.user)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        # must be an admin of the "targeted" organization
        if request.data and 'memberable' in request.data:
            memberable = Memberable.objects.get(id=request.data['memberable'])
        else:
            memberable = obj.memberable

        isAdmin = Membership.objects.filter(user=request.user, memberable=memberable, type='admin').exists()
        isRemove = request.method == 'DELETE' or memberable != obj.memberable
        isLastAdmin = Membership.objects.filter(type='admin', memberable=memberable).count() == 1

        return isAdmin and (not isRemove or not isLastAdmin)
