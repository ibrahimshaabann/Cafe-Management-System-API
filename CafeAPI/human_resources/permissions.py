from rest_framework import permissions
from authentication.models import User

"""
IsAuthenticated
The IsAuthenticated permission class will deny permission to any unauthenticated user, and allow permission otherwise.

This permission is suitable if you want your API to only be accessible to registered users.

IsAdminUser
The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed.

This permission is suitable if you want your API to only be accessible to a subset of trusted administrators.

IsAuthenticatedOrReadOnly
The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request. Requests for unauthorised users will only be permitted if the request method is one of the "safe" methods; GET, HEAD or OPTIONS.

This permission is suitable if you want to your API to allow read permissions to anonymous users, and only allow write permissions to authenticated users.


"""


class CustomerAccessPermission(permissions.BasePermission):
    """
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in ('POST', 'GET', 'PATCH', 'PUT'):
            return request.user.role in [User.Roles.USER, User.Roles.ADMIN]
        else: #Delete
            return request.user.role == User.Roles.ADMIN
        

class SalOrEmpAccessPermission(permissions.BasePermission):
    """
    Only admin has access to do any operations on
    Salray deduction or Employees
    
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.method in ('POST', 'GET', 'PATCH', 'PUT', 'DELETE'):
            return request.user.role == User.Roles.ADMIN
        
        else: # if request.user is a normal user
            return False
        

class ShiftOrAttendencePermission(permissions.BasePermission):

    def has_permission(self, request, view):

        # Users, admins and superusers are allowed to perform POST, PATCH or GET
        if request.method in ('POST', 'PATCH','GET'):
            return True
        
        # Only admins and superusers are allowed to perform PUT or DELETE
        if request.method in ('DELETE', 'PUT'):
            return request.user.role == User.Roles.ADMIN
        

