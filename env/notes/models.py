from unittest.util import _MAX_LENGTH
from django.db import models

    # Create your models here.

class Annee_aca(models.Model):
    nom = models.CharField(max_length=30, blank=True, null=True)
    date_debut = models.DateField(auto_now=True)
    date_fin = models.DateField
    
class Periode( models.Model):
    class statut(models.TextChoices):
        achevé = 'Achevée'
        en_cours = 'En cours'
        
    nom_periode = models.CharField(max_length=20, null=True)
    coefficient = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    coefficient = models.PositiveIntegerField()
    annee_aca = models.ForeignKey(Annee_aca, on_delete=models.CASCADE)
    statut = models.CharField(choices=statut.choices)
    def __str__(self):
        return f"{self.nom_periode}"
    
class Filiere (models.Model):
    nom_filiere= models.CharField(max_length=50,null=True,blank=False)
    description= models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nom_filiere}"
    
class Niveaux(models.Model):
    nom= models.CharField(max_length=20,null=True)
    def __str__(self):
        return f"{self.nom}"

class Classe(models.Model):
    nom = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=10)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    niveaux = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}"
    
class Filiere_periode(models.Model):
    duree=models.IntegerField()
    nomb_etudiant=models.IntegerField()
    nomb_prof=models.IntegerField()
    periode=models.ForeignKey(Periode, on_delete=models.DO_NOTHING)
    filieres=models.ForeignKey(Filiere, on_delete=models.DO_NOTHING)

class Matiere(models.Model):
    matiere= models.CharField(max_length=20,null=True)
    nombre_heure= models.IntegerField()
    coefficient=models.IntegerField()
    note_passage=models.IntegerField()
    def __str__(self):
        return f"{self.matiere}"



class Matiere_niveaux(models.Model):
    Titre="Matiere"
    nom_prof=models.CharField(max_length=50,null=True)
    niveau=models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    matiere=models.ForeignKey(Matiere, on_delete=models.CASCADE)

class Lecon(models.Model):
    titre =  models.CharField(max_length=50, null=True)
    description=models.TextField(null=True)
    chapitre=models.CharField(max_length=30)
    # lecon=models.FileField(upload_to=None)
    matiere_niveau=models.ForeignKey(Matiere_niveaux,on_delete=models.CASCADE)

class Etudiant(models.Model):
    class sex(models.TextChoices):
        masculin='M'
        feminin='F'
    nom=models.CharField(max_length=30,null=True)
    prenom=models.CharField(max_length=30,null=True)
    email=models.EmailField()
    date_naissance=models.DateField()
    sexe=models.CharField(max_length=1, choices=sex.choices)
    filiere_etudiant= models.ForeignKey(Filiere, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Notes (models.Model):
    note_obtenue=models.IntegerField()
    note_etudiant=models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    
    
class Evaluation (models.Model):
    heure_debut= models.DateTimeField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    heure_fin = models.DateTimeField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)

class Class_courant (models.Model):
    classe = models.ForeignKey( Classe, verbose_name=_(""), on_delete=models.CASCADE)



