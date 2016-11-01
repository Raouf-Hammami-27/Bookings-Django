from django.db import models

'''classe de gestion des hotes '''
class Hotel(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    etoiles = models.PositiveIntegerField(default=4)
    chambres = models.PositiveIntegerField(default=100)
    ville = models.CharField(max_length=255, null=True)
    note= models.DecimalField(decimal_places=1, max_digits=2, default=5)
    date_creation= models.DateField(null = True)
    actif = models.BooleanField(default=True)
    clients = models.ManyToManyField('Client',through='Reservation')

    def __str__(self):
        return self.nom

    ''' classe de gestion des chambres'''
class Chambre(models.Model):
    numero = models.CharField(max_length=5)
    diponibilite = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotel)

    def __str__(self):
        return self.numero


class Client(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Reservation(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    date_reservation = models.DateField()
