from web.models import Membership

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
