from django.db import models

# Create your models here.

class city(models.Model):
    city_name = models.CharField(max_length=2048)
    describtion = models.TextField