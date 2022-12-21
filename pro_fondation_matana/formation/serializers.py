from rest_framework import serializers
from formation.models import *

class Program_serializer(serializers.ModelSerializer):
    class Meta:
        model= Program
        fields = '__all__'


class Period_serializer(serializers.ModelSerializer):
    class Meta:
        model= Period
        fields = '__all__'


class Program_period_serializer(serializers.ModelSerializer):
    class Meta:
        model= Program_period
        fields = '__all__'


class Level_serializer(serializers.ModelSerializer):
    class Meta:
        model= Level
        fields = '__all__'


class Program_period_level_serializer(serializers.ModelSerializer):
    class Meta:
        model= Program_period_level
        fields = '__all__'


class Classroom_serializer(serializers.ModelSerializer):
    class Meta:
        model= Classroom
        fields = '__all__'



class Subject_serializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields = '__all__'


class Subject_program_period_serializer(serializers.ModelSerializer):
    class Meta:
        model= Subject_program_period
        fields = '__all__'



class Course_serializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields = '__all__'


class Lesson_serializer(serializers.ModelSerializer):
    class Meta:
        model= Lesson
        fields = '__all__'