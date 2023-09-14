from rest_framework import permissions
from .models import User

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.Roles.ADMIN and request.user.is_staff
    

    
    def has_object_permission(self, request, view, obj):

        """
        this method is getting executed when there is an Object or ID passed in the URL 
        u have to get through has_permission method first
        """
        if obj.role == User.Roles.USER:
            return True

        else:

            return request.user == obj and request.user.is_staff and request.user.role == User.Roles.ADMIN
        
 

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow read-only access to all users
    but full access to the owner of the object.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the HTTP method is one of the safe methods (GET, HEAD, OPTIONS).
        if request.method in permissions.SAFE_METHODS:
            # If it's a safe method, allow access (read-only).
            return True

        # For other methods (e.g., POST, PUT, DELETE), check if the user making the request
        # is the owner of the object they are trying to access.
        return request.user == obj