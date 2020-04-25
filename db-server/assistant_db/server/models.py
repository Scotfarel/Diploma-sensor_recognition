from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    weight = models.FloatField()
    material = models.TextField()

    def __str__(self):
        return f'{self.material} {self.name}'
