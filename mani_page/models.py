from __future__ import unicode_literals

from django.db import models

# Create your models here.
class skillset(models.Model):
    first = models.CharField(max_length=400)
    second = models.CharField(max_length=400)
    third = models.CharField(max_length=400)
