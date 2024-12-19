from django.db import models

class Korisnik(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    mjesto = models.CharField(max_length=100)
    dob = models.IntegerField()
    vip = models.BooleanField()

class Oglas(models.Model):
    prodavatelj = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    predmet = models.CharField(max_length=100)
    mjesto = models.CharField(max_length=100)
    cijena = models.IntegerField()
    razmjena = models.BooleanField()
    

