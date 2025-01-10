from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.userrole.role.name == 'Admin'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.userrole.role.name == 'Manager'

class IsPremiumOrCorporate(BasePermission):
    def has_permission(self, request, view):
        user_group = request.user.usergroup.group.name
        return user_group == 'Premium' or request.user.user_type == 'corporate'
