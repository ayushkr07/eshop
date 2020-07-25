from django.db import models
from .cateogory import Cateogory

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    cateogory=models.ForeignKey(Cateogory,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='upload/product/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products_by_cateogory_id(cateogory_id):
        if cateogory_id:
            return Product.objects.filter(cateogory=cateogory_id)
        return Product.objects.all()