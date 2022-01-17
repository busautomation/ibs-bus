from django.db import models

# Create your models here.
class BusSatusData(models.Model):
    BusNo = models.CharField(max_length=10)
    DriverName = models.CharField(max_length=50)
    ConductorName = models.CharField(max_length=50)
    DepartureTime = models.CharField(max_length=50)
    ArrivalTime = models.CharField(max_length=50)
    LastService= models.CharField(max_length=50)
    PUC=models.DateTimeField()
    Insurance=models.DateTimeField()
    DriverContactNo=models.CharField(max_length=50)
    ConductorContactNo=models.CharField(max_length=50)
    def __str__(self):
        return self.BusNo

class SensorData(models.Model):
    FuelDataPercentage = models.FloatField()
    FuelDataLitre = models.FloatField()
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    FireHydrantPercentage = models.FloatField()
    FireHydrantKg = models.FloatField()

class BusContact(models.Model):
    BusContactNo = models.CharField(max_length=10)
    def __str__(self):
        return  self.BusContactNo




    


