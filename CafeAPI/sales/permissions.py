from rest_framework import permissions
from authentication.models import User
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, LIST, and PATCH requests for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is authenticated and is an admin or superuser
        if request.user.is_authenticated and request.user.role in [User.Roles.ADMIN, User.Roles.SUPERUSER]:
            return True

        if not request.user.is_authenticated:
            raise PermissionDenied("Authentication required.")

        # If the user is authenticated but doesn't have the required role
        raise PermissionDenied("Permission denied.")

