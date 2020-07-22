from django.db import models
from .cateogory import Cateogory

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    cateogory=models.ForeignKey(Cateogory,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='upload/product/')


    @staticmethod
    def get_all_products():
        return Product.objects.all()