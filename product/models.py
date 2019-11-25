from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Category(models.Model):
    text = models.CharField(max_length=200)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    price = models.FloatField(default=0.0)
    visit_number = models.IntegerField(default=0)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    link = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)