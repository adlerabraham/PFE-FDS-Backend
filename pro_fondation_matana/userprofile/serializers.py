from rest_framework.serializers import ModelSerializer, Serializer, ValidationError, CharField, EmailField
from .models import *




class Super_admin_serializer(ModelSerializer):

    class Meta :
        model = Super_admin
        fields= '__all__'


class Admin_serializer(ModelSerializer):

    class Meta :
        model = Admin
        fields= '__all__'


class Teacher_serializer(ModelSerializer):

    class Meta :
        model = Teacher
        fields= '__all__'

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.updated_at = timezone.now()
        instance.updated_by = self._context['request'].user.username
        instance.save()
        return instance


class Student_serializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ['responsible_person', 
                  'relationship',
                  'phone_number',
                  ] #'__all__'

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.updated_at = timezone.now()
        instance.updated_by = self._context['request'].user.username
        instance.save()
        return instance



# class Update_student_serializer(ModelSerializer):

#     class Meta:
#         model = Student
#         fields = '__all__'

        
#     def update(self, instance, validated_data):
#         user = self.context['request'].user

#         if user.pk != instance.pk:
#             raise ValidationError({"authorize": "You dont have permission for this user."})

#         instance.personne_responsable = validated_data["personne_responsable"],
#         instance.lien = validated_data["lien"],
#         instance.numero_telephone = validated_data["numero_telephone"],
       
#         instance.save()

#         return instance
