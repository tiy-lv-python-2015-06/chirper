from rest_framework import permissions


class IsOwnerReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow access to owner of chirp
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # Only return true if the chirp author is the same as the user
        return obj.author == request.user
