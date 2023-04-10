from rest_framework import permissions


class HasAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj in request.user.get_real_estates()


class IsAdmin(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.is_anonymous or request.user.role is None:
            return False
        return request.user.role.admin
