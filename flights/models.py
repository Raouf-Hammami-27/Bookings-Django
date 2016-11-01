from django.db import models

'''classe de gestion des Vols '''
class Vol(models.Model):
    numero = models.CharField(max_length=255)
    depart = models.DateField()
    arrivee = models.DateField()
    origine = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    modele = models.CharField(max_length=255)


def __str__(self):
    return self.numero
