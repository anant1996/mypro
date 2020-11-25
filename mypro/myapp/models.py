from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="parenty")

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ManyToManyField(Category,related_name="category")