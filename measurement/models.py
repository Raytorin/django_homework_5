from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    picture = models.ImageField(default=None, null=True)
