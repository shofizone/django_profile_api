from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user  to edit there own profile only"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to edit there won profile"""
        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
