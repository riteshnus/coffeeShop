from django.db import models

# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price_tall = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_grande = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_venti = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    orderId = models.IntegerField
    type = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    volume = models.IntegerField
    size = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

