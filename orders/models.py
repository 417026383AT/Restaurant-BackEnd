from django.db import models

from restaurants.models import Restaurant
from users.models import User
from products.models import Products

# Create your models here.


class Status(models.Model):
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=300)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='OrderProducts')


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
