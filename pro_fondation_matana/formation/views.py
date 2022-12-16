from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from formation.serializers import *



# Create your views here.

class Programme_viewset(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class= Programme_serializer



class Periode_viewset(viewsets.ModelViewSet):
    queryset = Periode.objects.all()
    serializer_class= Periode_serializer


class Programme_periode_viewset(viewsets.ModelViewSet):
    queryset = Programme_periode.objects.all()
    serializer_class= Programme_periode_serializer


class Niveau_viewset(viewsets.ModelViewSet):
    queryset = Niveau.objects.all()
    serializer_class= Niveau_serializer


class Programme_periode_niveau_viewset(viewsets.ModelViewSet):
    queryset = Programme_periode_niveau.objects.all()
    serializer_class= Programme_periode_niveau_serializer


class Classe_viewset(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class= Classe_serializer


class Matiere_viewset(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class= Matiere_serializer


class Matiere_programme_periode_viewset(viewsets.ModelViewSet):
    queryset = Matiere_programme_periode.objects.all()
    serializer_class= Matiere_programme_periode_serializer



class Cours_viewset(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class= Cours_serializer


class Lecon_viewset(viewsets.ModelViewSet):
    queryset = Lecon.objects.all()
    serializer_class= Lecon_serializer