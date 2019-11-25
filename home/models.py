from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    showPhone = models.BooleanField()
    email = models.CharField(max_length=200)
    showEmail = models.BooleanField()

class About(models.Model):
    shortDescription = models.CharField(max_length=500)
    longDescription = models.TextField()

class SocialNetwork(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)