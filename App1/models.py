from django.db import models

# Create your models here.

class Personales(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return self.nombre +" "+ str(self.edad) + " " + str(self.mail)   

class Pronosticos(models.Model):
    campeon = models.CharField(max_length=50)
    subcampeon = models.CharField(max_length=50)
    goleador = models.CharField(max_length=50)

    def __str__(self):
        return self.campeon +" "+ self.subcampeon + " " + self.goleador   

class Apuestas(models.Model):
    mediopago = models.CharField(max_length=50)
    monto = models.IntegerField()
    

    def __str__(self):
        return self.mediopago +" "+ str(self.monto)    
