from django.db import models

# Create your models here.

class Power(models.Model):
    name = models.CharField(max_length=255)