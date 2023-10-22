from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsAdminOrAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        return bool(user.is_staff or (user == obj.created_by and not obj.is_published) or user.is_superuser)


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_superuser or user.is_staff)

    def has_object_permission(self, request, view, obj):
        user = request.user
        return bool(user.is_superuser or user.is_staff)


class IsCommentAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        user = request.user
        return bool(user.is_staff or user == obj.student or user.is_superuser)