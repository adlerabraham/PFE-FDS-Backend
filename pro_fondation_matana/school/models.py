from django.db import models
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from pro_fondation_matana.mixins import *


# Create your models here.
class Institution(AuditMixin, models.Model):
    name = models.CharField(max_length=100)
    slug= models.SlugField(null=True, blank=True)
    creation_date = models.DateField(max_length=25, blank=False, null=True)
    email = models.EmailField(max_length=25, blank=False, null=True)
    address= models.CharField(max_length=100)
    phone_number = PhoneNumberField(max_length=25, blank=False, null=True),
    logo=models.ImageField(upload_to='ecole', blank=True)
    number_program = models.PositiveSmallIntegerField()
    responsible = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug= slugify(self.nom)
        super().save(*args, **kwargs) 

    
    class Meta :
        db_table = 'institution'
