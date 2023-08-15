# posts/permissions.py
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any reqest
        # permissions.SAFE_METHOD = ('GET', 'OPTIONS', 'HEAD')
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        # All owner to make any type of HTTP request
        return obj.author == request.user
