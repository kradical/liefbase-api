from web.models import Membership, Memberable

from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj == request.user

class OrganizationPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        admin_memberships = Membership.objects.filter(user=request.user, memberable=obj, type='admin')
        is_admin = len(admin_memberships) > 0
        
        return is_admin

class MembershipPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != 'POST':
            return True

        has_memberable = request.data and 'memberable' in request.data

        if not has_memberable:
            return False

        try:
            memberable = Memberable.objects.get(id=request.data['memberable'])
        except Memberable.DoesNotExist:
            return False
        
        is_admin = Membership.objects.filter(user=request.user, memberable=memberable, type='admin').exists()
        return is_admin

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # must be an admin of the "targeted" organization
        if request.data and 'memberable' in request.data:
            memberable = Memberable.objects.get(id=request.data['memberable'])
        else:
            memberable = obj.memberable
        
        is_admin = Membership.objects.filter(user=request.user, memberable=memberable, type='admin').exists()
        is_remove = request.method == 'DELETE' or memberable != obj.memberable
        is_last_admin = Membership.objects.filter(type='admin', memberable=memberable).count() == 1

        return is_admin and (not is_remove or not is_last_admin)
