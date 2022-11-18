from rest_framework import serializers
from formation.models import *

class Programme_serializer(serializers.ModelSerializer):
    class Meta:
        model= Programme
        fields = '__all__'


class Periode_serializer(serializers.ModelSerializer):
    class Meta:
        model= Periode
        fields = '__all__'


class Programme_periode_serializer(serializers.ModelSerializer):
    class Meta:
        model= Programme_periode
        fields = '__all__'


class Niveau_serializer(serializers.ModelSerializer):
    class Meta:
        model= Niveau
        fields = '__all__'


class Programme_periode_niveau_serializer(serializers.ModelSerializer):
    class Meta:
        model= Programme_periode_niveau
        fields = '__all__'


class Classe_serializer(serializers.ModelSerializer):
    class Meta:
        model= Classe
        fields = '__all__'



class Matiere_serializer(serializers.ModelSerializer):
    class Meta:
        model= Matiere
        fields = '__all__'


class Matiere_programme_periode_serializer(serializers.ModelSerializer):
    class Meta:
        model= Matiere_programme_periode
        fields = '__all__'



class Cours_serializer(serializers.ModelSerializer):
    class Meta:
        model= Cours
        fields = '__all__'


class Lecon_serializer(serializers.ModelSerializer):
    class Meta:
        model= Lecon
        fields = '__all__'