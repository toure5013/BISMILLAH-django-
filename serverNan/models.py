from django.db import models

# Create your models here.
# User table.
class User(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    nbr_joueur = models.EmailField(max_length=100)
    password = models.EmailField(max_length=200, null=False, blank=False)
    




class userPari(models.Model):
    namePari = models.CharField(max_length=120)
    nameUser = models.CharField(max_length=200, null=False, blank=False)
    montantParier = models.CharField(max_length=200, null=False, blank=False)
    idPari = models.CharField(max_length=200, null=False, blank=False)





class pariListe(models.Model):
    namePari = models.CharField(max_length=120)
    montantMin = models.CharField(max_length=200, null=False, blank=False)
    montantMax = models.CharField(max_length=200, null=False, blank=False)
    pourcentage = models.CharField(max_length=200, null=False, blank=False)
    dateDebut = models.CharField(max_length=200, null=False, blank=False)
    dateFin = models.CharField(max_length=200, null=False, blank=False)
    nbreEquipeMin = models.CharField(max_length=200, null=False, blank=False)
    nbreEquipeMax = models.CharField(max_length=200, null=False, blank=False)

