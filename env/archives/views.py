from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from archives.serializers import ArchivesSerializers
from archives.models import Archives

# Create your views here
class ArchivesViewSet(ModelViewSet):
    serializer_class=ArchivesSerializers
    def get_queryset(self):
        return Archives.objects.all()