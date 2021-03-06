from django.db import models
from datetime import datetime

from .product import Product
from .customer import Customer

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=100,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)


    def place_order(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer):
        return Order.objects.filter(customer=customer).order_by('-date')