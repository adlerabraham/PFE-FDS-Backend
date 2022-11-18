from rest_framework import serializers
from school.models import *

class Ecole_serializer(serializers.ModelSerializer):
    class Meta:
        model= Ecole
        fields = '__all__'
