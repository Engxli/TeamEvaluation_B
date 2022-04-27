from rest_framework import permissions

class LockedProject(permissions.BasePermission):

        
    def has_object_permission(self, request, view, obj):
        return not obj.isLock