from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    email = models.EmailField(max_length=60)
    dp = models.ImageField(upload_to = 'teams')