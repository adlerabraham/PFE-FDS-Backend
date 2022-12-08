from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.


class Archives(models.Model):
    nom =  models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    type = models.CharField(max_length=30, blank=False)
    lien = models.URLField(max_length=200, blank= False)
    
    def __str__(self):
        return self.nom