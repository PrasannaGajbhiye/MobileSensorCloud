from __future__ import unicode_literals
from django.db import models

# Create your models here.

class SensorDetails(models.Model):
    station = models.CharField(max_length=400)
    station_desc = models.CharField(max_length=800)
    sensor_type = models.CharField(max_length=100)
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    url = models.CharField(max_length=800)
    active=models.IntegerField
    sensorOwner=models.CharField(max_length=200)

    def __str__(self):
        return self.station+''


