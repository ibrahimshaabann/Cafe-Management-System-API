from rest_framework import permissions
from authentication.models import User


class AdminOnly(permissions.BasePermission):
    """
    Only admin has access to do any operations on
    Salray deduction or Employees
    
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.method in ('POST', 'GET', 'PATCH', 'PUT', 'DELETE'):
            return request.user.role in [User.Roles.ADMIN]
        
        else: # if request.user is a normal user
            return False
        

class IsUserPOST(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Allow POST only for user requests
        if request.method in ('POST'):
            return True

        # Check if the user has the admin or superuser role
        if request.user.role in [User.Roles.ADMIN]:
            return True

        return False