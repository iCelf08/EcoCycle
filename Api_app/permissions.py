from rest_framework import permissions
from .models import User

class IsEnterprise(permissions.BasePermission):
    message = 'Access Enterprise profile not allowed'
    def has_permission(self, request, view):
        user : User = request.user
        return user.is_enterprise