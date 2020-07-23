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

def validateCustomer(customer):
    error_message = None
    if not customer.first_name:
        error_message = 'First name required'
    elif len(customer.first_name) < 4:
        error_message = 'First name must have atleast four characters'
    elif not customer.last_name:
        error_message = 'Last name required'
    elif len(customer.last_name) < 4:
        error_message = 'Last name must have atleast four characters'
    elif not customer.phone:
        error_message = 'Phone Number required'
    elif len(customer.phone) < 10:
        error_message = 'Phone Number must have atleast ten characters'
    elif not customer.password:
        error_message = 'Password required'
    elif len(customer.password) < 6:
        error_message = 'Password must have atleast six characters'
    elif not customer.email:
        error_message = 'Email required'
    elif len(customer.email) < 5:
        error_message = 'Email must have atleast five characters'
    elif customer.isExists():
        error_message = 'Email already exists'

    return error_message

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
        error_message = validateCustomer(customer)
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

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        #get customer by email
        try:
            customer = Customer.objects.get(email=email)
        except:
            customer = False

        # error_message = None

        if customer:
            if check_password(password,customer.password):
                return redirect('index')
            else:
                error_message = 'Incorrect email or password'
        else:
            error_message = 'Incorrect email or password'

        return render(request,'login.html',{'error' : error_message})
