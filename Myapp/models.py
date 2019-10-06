from django.db import models
from jsonfield import JSONField

# Create your models here.

class FibonanciMethod(models.Model):
    number = models.IntegerField()
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    totalTime = models.IntegerField()
    FiboniciList = JSONField()
    Fibonaci_output = models.IntegerField()
