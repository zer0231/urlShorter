from django.db import models

# Create your models here.

class Url(models.Model): #Defining the model for our url object
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)

