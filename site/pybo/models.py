from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class world(models.Model):
    CONTINENT = models.CharField(max_length=100)
    COUNTRY = models.CharField(max_length=100)
    p1 = models.CharField(max_length=500, null=True)
    p2 = models.CharField(max_length=500, null=True)
    p3 = models.CharField(max_length=500, null=True)
    p4 = models.CharField(max_length=500, null=True)
    p5 = models.CharField(max_length=500, null=True)
    p6 = models.CharField(max_length=500, null=True)
    p7 = models.CharField(max_length=500, null=True)
    p8 = models.CharField(max_length=500, null=True)

    
