from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
  neighbourhood_name = models.CharField(max_length=25)
  general_location = models.CharField(max_length=25)
  
  def __str__(self):
    return self.neighbourhood_name