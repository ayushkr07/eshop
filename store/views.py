from django.shortcuts import render
from .models.product import Product
from .models.cateogory import Cateogory

def index(request):
    cateogories=Cateogory.get_all_cateogories()
    cateogoryID = request.GET.get('cateogory')
    if cateogoryID:
        products = Product.get_all_products_by_cateogory_id(cateogoryID)
    else:
        products = Product.get_all_products()
    data={}
    data['products']=products
    data['cateogories']=cateogories
    return render(request,'index.html',data)
