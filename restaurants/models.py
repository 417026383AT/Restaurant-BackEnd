from django.db import models

# Create your models here.


class Direction(models.Model):
    city = models.CharField(max_length=30)
    pc = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    int_number = models.CharField(max_length=30, null=True)
    ext_number = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    location = models.CharField(max_length=20)


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    schedule_open = models.TimeField(auto_now=False, auto_now_add=False)
    schedule_close = models.TimeField(auto_now=False, auto_now_add=False)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    restaurant_type = models.CharField(max_length=20)

    def __str__(self):
        return self.name
