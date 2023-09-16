from rest_framework import permissions
from .models import User

# class IsAdminOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to allow read-only access to all users
#     but full access to admins.
#     """

#     def has_permission(self, request, view):
#         if request.user.is_staff:
#             # Admins have full access (GET, POST, PATCH, PUT, DELETE)
#             return True
#         return request.method in permissions.SAFE_METHODS

#     def has_object_permission(self, request, view, obj):
#         if request.user.is_staff:
#             # Admins have full access to any object
#             return True
#         return request.method in permissions.SAFE_METHODS


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow read-only access to all users
    but full access to admins.
    """

    def has_permission(self, request, view):
        # Check if the user has 'admin' role and is_staff = True
        return request.user.role == User.Roles.ADMIN and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Admins have full access to any object
        return request.user.is_staff

class IsUserOwner(permissions.BasePermission):
    """
    Custom permission to allow access to the user object only if
    the user making the request is the owner and has the 'user' role.
    """

    def has_object_permission(self, request, view, obj):
        # Users with the 'user' role can only access their own user object
        return obj == request.user and obj.role == 'user'

    def has_permission(self, request, view):
        # Users with the 'user' role can only access their own user object
        if view.action == 'retrieve':
            return True
        return False