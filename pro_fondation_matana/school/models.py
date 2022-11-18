from django.db import models
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Ecole(models.Model):
    nom = models.CharField(max_length=100)
    slug= models.SlugField(null=True, blank=True)
    date_creation = models.DateField(max_length=25, blank=False, null=True)
    email = models.EmailField(max_length=25, blank=False, null=True)
    phone_number = PhoneNumberField(max_length=25, blank=False, null=True),
    logo=models.ImageField(upload_to='ecole', blank=True)
    nombre_programmes = models.PositiveSmallIntegerField()
    nom_responsable = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug= slugify(self.nom)
        super().save(*args, **kwargs) 

    
    class Meta :
        db_table = 'ecole'
