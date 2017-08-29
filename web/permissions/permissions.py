from rest_framework import permissions

class IsStaffOrCreate(permissions.BasePermission):
    """
    Custom permission for user creation when not authenticated.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method == 'POST':
            return True

        return request.user.is_staff