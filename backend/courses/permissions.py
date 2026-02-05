from rest_framework.permissions import BasePermission

class IsCreator(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == 'creator'
        )
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'creator'):
            return obj.creator == request.user
        elif hasattr(obj, 'course'):
            return obj.course.creator == request.user
        elif hasattr(obj, 'section'):
            return obj.section.course.creator == request.user
        return False