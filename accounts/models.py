from enum import unique
from django.db import models

# Create your models here.

class BlogUser(models.Model):
    first_name = models.CharField(max_length=50 , blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)