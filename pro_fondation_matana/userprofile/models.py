from django.db import models
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from school.models import Ecole
from user.models import User

# Create your models here.

class Super_admin(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta :
        db_table = 'super_admin'

class Admin(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    ecole= models.ForeignKey(Ecole, on_delete=models.CASCADE)
    
    class Meta :
        db_table = 'admin'


class Student(models.Model):
    personne_responsable = models.CharField(max_length=250, blank=False, null=True)
    lien = models.CharField(max_length=250, blank=False, null=True)
    numero_telephone =PhoneNumberField(help_text='Ex:+509XXXXXXXX',blank=True,max_length=15, null=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta :
        db_table = 'etudiant'


class Teacher(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)


    class Meta :
        db_table = 'professeur'