from web.models import ReliefMap, Membership, Memberable, MapItemTemplate

from rest_framework import permissions
from rest_framework.exceptions import NotFound

def is_admin_of(pk, user):
    try:
        memberable = Memberable.objects.get(pk=pk)
    except Memberable.DoesNotExist:
        raise NotFound()

    is_admin = Membership.objects.filter(user=user, memberable=memberable, type='admin').exists()
    return is_admin

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

        is_admin = Membership.objects.filter(user=request.user, memberable=obj, type='admin').exists()

        return is_admin

class ObjectReliefMapPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        try:
            relief_map_id = request.data['relief_map']
            relief_map = ReliefMap.objects.get(id=relief_map_id)
        except ReliefMap.DoesNotExist:
            raise NotFound()
        except KeyError:
            return request.user.is_authenticated()

        # has any sort of membership to the relief map
        is_member_or_admin = Membership.objects.filter(user=request.user, memberable=relief_map).exists()
        return is_member_or_admin

    def has_object_permission(self, request, view, obj):
        is_member_or_admin = Membership.objects.filter(user=request.user, memberable=obj.relief_map).exists()
        return is_member_or_admin

class ItemReliefMapPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != 'POST':
            return request.user.is_authenticated()

        try:
            template_id = request.data['properties']['template']
            template = MapItemTemplate.objects.get(id=template_id)
        except (MapItemTemplate.DoesNotExist, KeyError):
            raise NotFound()

        # has any sort of membership to the relief map
        is_member_or_admin = Membership.objects.filter(user=request.user, memberable=template.relief_map).exists()
        return is_member_or_admin

    def has_object_permission(self, request, view, obj):
        is_member_or_admin = Membership.objects.filter(user=request.user, memberable=obj.template.relief_map).exists()
        return is_member_or_admin


class MembershipPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        try:
            memberable_id = request.data['memberable']
        except KeyError:
            raise request.user.is_authenticated()

        return is_admin_of(memberable_id, request.user)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated()

        # must be an admin of the "targeted" organization
        if request.data and 'memberable' in request.data:
            memberable = Memberable.objects.get(id=request.data['memberable'])
        else:
            memberable = obj.memberable

        is_admin = Membership.objects.filter(user=request.user, memberable=memberable, type='admin').exists()
        is_remove = request.method == 'DELETE' or memberable != obj.memberable
        is_last_admin = Membership.objects.filter(type='admin', memberable=memberable).count() == 1

        return is_admin and (not is_remove or not is_last_admin)
