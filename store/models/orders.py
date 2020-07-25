from django.db import models
from datetime import datetime

from .product import Product
from .customer import Customer

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default=datetime.today)