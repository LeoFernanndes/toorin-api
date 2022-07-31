from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == "create":
            return True
        if view.action in ["update", "partial_update", "retrieve"] and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        return False