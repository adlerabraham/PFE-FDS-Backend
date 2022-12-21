from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from school.serializers import *
from userprofile.permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView




# Create your views here.
class Ecole_view(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'put',]
    serializer_class = Institution_serializer

    def get(self, request, pk):
        institution = Ecole.undeleted_objects.get(pk=pk)
        serializer = self.serializer_class(institution)
        return Response(serializer.data, status=status.HTTP_200_OK)    

    def post(self, request):
        self.permission_classes = (IsAdminUser,)
        self.check_permissions(request)
        serializer = Institution_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        self.permission_classes = (IsAdminUser,)
        self.check_permissions(request)
        institution = Ecole.objects.get(pk=pk)
        institution.updated_by = request.user.username
        serializer = self.serializer_class(institution, data=request.data, partial=True,context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

