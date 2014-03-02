from django.db import models

# Create your models here.

class Car(models.Model):
    year = models.PositiveSmallIntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    horsepower = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=100)

    def __unicode__(self):
        return self.make
