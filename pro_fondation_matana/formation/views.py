from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from formation.serializers import *



# Create your views here.

class Program_viewset(viewsets.ModelViewSet):
    queryset = Program.undeleted_objects.all()
    serializer_class= Program_serializer



class Period_viewset(viewsets.ModelViewSet):
    queryset = Period.undeleted_objects.all()
    serializer_class= Period_serializer


class Program_period_viewset(viewsets.ModelViewSet):
    queryset = Program_period.undeleted_objects.all()
    serializer_class= Program_period_serializer


class Level_viewset(viewsets.ModelViewSet):
    queryset = Level.undeleted_objects.all()
    serializer_class= Level_serializer


class Program_period_level_viewset(viewsets.ModelViewSet):
    queryset = Program_period_level.undeleted_objects.all()
    serializer_class= Program_period_level_serializer


class Classe_viewset(viewsets.ModelViewSet):
    queryset = Classroom.undeleted_objects.all()
    serializer_class= Classroom_serializer


class Subject_viewset(viewsets.ModelViewSet):
    queryset = Subject.undeleted_objects.all()
    serializer_class= Subject_serializer


class Subject_program_period_viewset(viewsets.ModelViewSet):
    queryset = Subject_program_period.undeleted_objects.all()
    serializer_class= Subject_program_period_serializer



class Course_viewset(viewsets.ModelViewSet):
    queryset = Course.undeleted_objects.all()
    serializer_class= Course_serializer


class Lesson_viewset(viewsets.ModelViewSet):
    queryset = Lesson.undeleted_objects.all()
    serializer_class= Lesson_serializer