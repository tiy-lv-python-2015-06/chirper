from rest_framework import permissions

class IsOwnerReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # Only return True if the chirp is the same as the user
        return obj.author == request.user