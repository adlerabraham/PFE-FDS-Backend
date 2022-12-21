from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.generics import UpdateAPIView
from rest_framework.exceptions import PermissionDenied


# Create your views here.

class Super_admin_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Super_admin_serializer



class Admin_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Admin_serializer



class Teacher_update_view(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = Teacher_serializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        teacher = get_object_or_404(Teacher, User__id=user_id)
        if teacher.User.id != self.request.user.id and "admin" not in self.request.user.groups.values_list("name", flat=True):
            raise PermissionDenied
        return teacher



class Student_update_view(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = Student_serializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        student = get_object_or_404(Student, User__id=user_id)
        if student.User.id != self.request.user.id and "admin" not in self.request.user.groups.values_list("name", flat=True):
            raise PermissionDenied
        return student


# class Update_student_view(UpdateAPIView):

#     queryset = User.objects.all()
#     #permission_classes = (IsAuthenticated,)
#     serializer_class = Update_student_serializer