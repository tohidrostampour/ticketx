from rest_framework.permissions import BasePermission


class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.customer.user == request.user:
            return True
        return False
