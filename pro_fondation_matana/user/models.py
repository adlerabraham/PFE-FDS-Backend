from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy 
from school.models import *
from pro_fondation_matana.mixins import *





# Create your models here.


class User(AbstractUser, AuditMixin, SoftDeleteModel):

    
    class Sex (models.TextChoices):
        male="Male", gettext_lazy('male')
        female="Female", gettext_lazy('female')
        non_binary="Non Binary", gettext_lazy('binary')


    class Blood_type(models.TextChoices):
        Inconnu = 'Inconnu'
        O_plus = 'O+', gettext_lazy('O+')
        O_moins = 'O-', gettext_lazy('O-')
        B_plus = 'B+', gettext_lazy('B+')
        B_moins = 'B-', gettext_lazy('B-')
        A_plus = 'A+', gettext_lazy('A+')
        A_moins = 'A-', gettext_lazy('A-')
        AB_plus = 'AB+', gettext_lazy('AB+')
        AB_moins = 'AB-', gettext_lazy('AB-')


    birth_date= models.DateField(max_length=50, blank=False, null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    phone_number =PhoneNumberField(help_text='Ex:+509XXXXXXXX',blank=True,max_length=15, null=True)
    sex = models.CharField(max_length=25,choices=Sex.choices,blank=False, null=True)
    blood_type =  models.CharField(max_length=25,choices=Blood_type.choices,blank=True, null=True)
    profile_picture=models.ImageField(upload_to='user', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    initial_password = models.CharField(max_length=250, blank=False, null=True, verbose_name= 'password2')



    class Meta :
        db_table = 'user'


