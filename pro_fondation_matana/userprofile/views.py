from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView

from .serializers import *

# Create your views here.

class Super_admin_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Super_admin_serializer



class Admin_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Admin_serializer



class Teacher_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Teacher_serializer



class Student_viewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Student_serializer


class Update_student_view(UpdateAPIView):

    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = Update_student_serializer