from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.email == request.user.email


class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_authenticated and IsAdminUser
        )
