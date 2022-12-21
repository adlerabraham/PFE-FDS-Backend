from django.db import models
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from school.models import *
from user.models import User
from pro_fondation_matana.mixins import *


# Create your models here.

class Super_admin(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta :
        db_table = 'super_admin'

class Admin(AuditMixin, models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    institution= models.ForeignKey(Institution, on_delete=models.CASCADE)
    
    class Meta :
        db_table = 'admin'


class Student(AuditMixin, models.Model):
    responsible_person = models.CharField(max_length=250, blank=False, null=True)
    relationship = models.CharField(max_length=250, blank=False, null=True)
    phone_number =PhoneNumberField(help_text='Ex:+509XXXXXXXX',blank=True,max_length=15, null=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta :
        db_table = 'student'


class Teacher(AuditMixin, models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)


    class Meta :
        db_table = 'teacher'