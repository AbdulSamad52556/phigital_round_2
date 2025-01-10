from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'userrole') and request.user.userrole.role.name == 'Admin'

class IsManagerWithRestrictedAccess(BasePermission):
    def has_permission(self, request, view):
        if not hasattr(request.user, 'userrole'):
            return False
        if request.user.userrole.role.name == 'Manager':
            if request.user.usergroup.group.name == 'Non-Premium' and request.user.user_type == 'normal':
                return False
            return True
        return False
