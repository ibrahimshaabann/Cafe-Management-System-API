from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from authentication.models import User


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Allow GET, LIST, and PATCH requests
        if request.method in ('GET', 'LIST', 'PATCH'):
            return True

        # Check if the user has the admin or superuser role
        if request.user.role in [User.Roles.ADMIN, User.Roles.SUPERUSER]:
            return True

        return False


class IsAdminDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Allow GET, POST, and PATCH requests
        if request.method in ('GET', 'POST', 'PATCH'):
            return True

        # Check if the user has the admin or superuser role
        if request.user.role in [User.Roles.ADMIN, User.Roles.SUPERUSER]:
            return True

        return False