from rest_framework import serializers
from school.models import *

class Institution_serializer(ModelSerializer):

    class Meta:
        model = Institution
        fields = ['id', 
                  'name', 
                  'type', 
                  'creation_date', 
                  'address', 
                  'email', 
                  'phone_number', 
                  'logo',
                  'responsible',
                  'number_program'
                  ]
    
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.created_at = timezone.now()
        instance.created_by = self._context['request'].user.username
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.updated_at = timezone.now()
        instance.updated_by = self._context['request'].user.username
        instance.save()
        return instance
