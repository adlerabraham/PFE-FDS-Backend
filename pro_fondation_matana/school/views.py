from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from school.serializers import *


# Create your views here.
class Ecole_viewset(viewsets.ModelViewSet):
    queryset = Ecole.objects.all()
    serializer_class= Ecole_serializer