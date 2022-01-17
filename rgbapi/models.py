from django.db import models

# Create your models here.
class RGB(models.Model):
    device_name = models.CharField(max_length=100)
    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()

    def __str__(self):
        return self.device_name
class Dimmer(models.Model):
    device_name = models.CharField(max_length=100)
    brigtness = models.IntegerField()

    def __str__(self):
        return self.device_name
