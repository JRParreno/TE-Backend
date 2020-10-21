# from rest_framework import permissions
# from authentication.models import User


# class IsProfessor(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         user = User.objects.get(username=request.user.username)
#         if user.is_professor == True:
#             return True
#         return False
