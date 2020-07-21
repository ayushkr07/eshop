from django.contrib import admin
from .models.product import Product
from .models.cateogory import Cateogory

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','cateogory']

class AdminCateogory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product,AdminProduct)
admin.site.register(Cateogory,AdminCateogory)