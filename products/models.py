from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
