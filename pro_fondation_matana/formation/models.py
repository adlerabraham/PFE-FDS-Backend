from django.db import models
from django.template.defaultfilters import slugify
from school.models import Ecole

# Create your models here.


class Programme(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE, related_name='ecole')
    logo=models.ImageField(upload_to='programme', blank=True)
    description = models.TextField(max_length = 100)
    nom_responsable = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug= slugify(self.nom)
        super().save(*args, **kwargs) 

    class Meta :
        db_table = 'programme'




class Periode(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    date_debut = models.DateField(max_length=25, blank=False, null=True)
    date_fin = models.DateField(max_length=25, blank=False, null=True)
    coefficient = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug= slugify(self.nom)
        super().save(*args, **kwargs) 

    
    class Meta :
        db_table = 'periode'
    



class Programme_periode(models.Model):

    class Unite_duree (models.TextChoices):
        mois = "mois"
        annee = "annee"
        
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    periode = models.ForeignKey(Periode, on_delete=models.CASCADE)
    duree = models.PositiveSmallIntegerField()
    unite_duree = models.CharField(max_length=25, choices=Unite_duree.choices, blank=False, null=True)
    nombre_etudiant = models.IntegerField()
    nombre_professeur = models.IntegerField()


    
    class Meta :
        db_table = 'programme_periode'



class Niveau(models.Model):
    models.SmallIntegerField()

    
    class Meta :
        db_table = 'niveau'



class Programme_periode_niveau(models.Model):    
    programme_periode = models.ForeignKey(Programme_periode, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)

    
    class Meta :
        db_table = 'programme_periode_niveau'



class Classe(models.Model):
    Programme_periode_niveau = models.ForeignKey(Programme_periode_niveau, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    abbreviation = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug= slugify(self.nom)
        super().save(*args, **kwargs) 
    

    class Meta :
        db_table = 'classe'




class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.CharField(max_length=500)

     
    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug= slugify(self.nom)
        super().save(*args, **kwargs) 


    class Meta :
        db_table = 'matiere'




class Matiere_programme_periode(models.Model):
    Programme_periode = models.ForeignKey(Programme_periode, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    

    class Meta :
        db_table = 'matiere_programme_periode'




class Cours(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    coefficient = models.PositiveSmallIntegerField()
    logo=models.ImageField(upload_to='cours', blank=True)
    #professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)

       
    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug= slugify(self.nom)
        super().save(*args, **kwargs) 


    class Meta :
        db_table = 'cours'




class Lecon(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    chapitre = models.IntegerField()
    description = models.CharField(max_length=100)
    


    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug= slugify(self.nom)
        super().save(*args, **kwargs) 


    class Meta :
        db_table = 'lecon'