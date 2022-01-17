from django.db import models

# Create your models here.
class LocationData(models.Model):
    device_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return self.device_name
