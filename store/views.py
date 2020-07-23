from django.shortcuts import render,HttpResponse,redirect
from .models.product import Product
from django.contrib.auth.hashers import make_password,check_password
from .models.cateogory import Cateogory
from .models.customer import Customer


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

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        values = {
            'first_name':f_name,
            'last_name':l_name,
            'phone':phone,
            'email':email
        }
        customer = Customer(first_name=f_name,
                            last_name=l_name,
                            phone=phone,
                            email=email,
                            password=password)
        # Validation
        error_message = None
        if not f_name:
            error_message = 'First name required'
        elif len(f_name) < 4:
            error_message = 'First name must have atleast four characters'
        elif not l_name:
            error_message = 'Last name required'
        elif len(l_name) < 4:
            error_message = 'Last name must have atleast four characters'
        elif not phone:
            error_message = 'Phone Number required'
        elif len(phone)<10:
            error_message = 'Phone Number must have atleast ten characters'
        elif not password:
            error_message = 'Password required'
        elif len(password)<6:
            error_message = 'Password must have atleast six characters'
        elif not email:
            error_message = 'Email required'
        elif len(email)<5:
            error_message = 'Email must have atleast five characters'
        elif customer.isExists():
            error_message = 'Email already exists'

        if not error_message:
            customer.password=make_password(customer.password)
            customer.save()
            return redirect('index')
        else:
            data={
                'error':error_message,
                'value':values
            }
            return render(request,'signup.html',data)
