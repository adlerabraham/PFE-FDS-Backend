from rest_framework.permissions import BasePermission

# class AdminPermission(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user or not request.user.is_authenticated:
#             return False
#         group_name = view.kwargs.get('admin')
#         if not group_name:
#             return False
#         return request.user.groups.filter(name=group_name).exists()




class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.groups.filter(name='admin').exists()

