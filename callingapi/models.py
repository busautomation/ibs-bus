from django.db import models

# Create your models here.
class CallingList(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    callingstatus = models.CharField(max_length=200, default='Not Called')
    def __str__(self):
        return self.name
        