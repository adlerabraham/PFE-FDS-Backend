from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy 
from school.models import Ecole




# Create your models here.


class User(AbstractUser):

    
    class Sexe (models.TextChoices):
        homme = "Homme"
        femme = "Femme"
        non_binaire = "Non binaire"


    class Groupe_Sanguin(models.TextChoices):
        Inconnu = 'Inconnu'
        O_plus = 'O+', gettext_lazy('O+')
        O_moins = 'O-', gettext_lazy('O-')
        B_plus = 'B+', gettext_lazy('B+')
        B_moins = 'B-', gettext_lazy('B-')
        A_plus = 'A+', gettext_lazy('A+')
        A_moins = 'A-', gettext_lazy('A-')
        AB_plus = 'AB+', gettext_lazy('AB+')
        AB_moins = 'AB-', gettext_lazy('AB-')


    date_naissance = models.DateField(max_length=25, blank=False, null=True)
    adresse = models.CharField(max_length=250, blank=False, null=True)
    numero_telephone = PhoneNumberField(max_length=25, blank=False, null=True),
    sexe = models.CharField(max_length=25, choices=Sexe.choices, blank=False, null=True)
    groupe_sanguin = models.CharField(max_length=25, choices=Groupe_Sanguin.choices, blank=False, null=True)
    photo_profil=models.ImageField(upload_to='user', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    initial_password = models.CharField(max_length=250, blank=False, null=True, verbose_name= 'password2')



    class Meta :
        db_table = 'utilisateur'


