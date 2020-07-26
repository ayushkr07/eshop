from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

from .models.product import Product
from .models.cateogory import Cateogory
from .models.customer import Customer
from .models.orders import Order


class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if remove:
                if quantity <= 1:
                    cart.pop(product)
                else:
                    cart[product] =quantity - 1
            else:
                if quantity:
                    cart[product] = quantity + 1
                else:
                    cart[product] = 1
        else:
            cart ={}
            cart[product] = 1
        request.session['cart']=cart
        print(request.session['cart'])
        return redirect('index')

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        cateogories = Cateogory.get_all_cateogories()
        cateogoryID = request.GET.get('cateogory')
        if cateogoryID:
            products = Product.get_all_products_by_cateogory_id(cateogoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['cateogories'] = cateogories

        return render(request, 'index.html', data)

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        values = {
            'first_name': f_name,
            'last_name': l_name,
            'phone': phone,
            'email': email
        }
        customer = Customer(first_name=f_name,
                            last_name=l_name,
                            phone=phone,
                            email=email,
                            password=password)
        # Validation
        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'value': values
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
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


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        # get customer by email
        try:
            customer = Customer.objects.get(email=email)
        except:
            customer = False

        # error_message = None

        if customer:
            if check_password(password, customer.password):

                request.session['customer'] = customer.id
                return redirect('index')
            else:
                error_message = 'Incorrect email or password'
        else:
            error_message = 'Incorrect email or password'

        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_ids(ids)
        # print(products)
        return render(request, 'cart.html',{'products' : products})

class Checkout(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_ids(list(cart.keys()))
        print(address,phone,customer,cart,products)

        for product in products:
            order = OrderView(product=product,
                              customer=Customer(id=customer),
                              quantity=cart.get(str(product.id)),
                              price=product.price,
                              address=address,
                              phone=phone)
            order.place_order()
            request.session['cart']={}
        return redirect('cart')

class OrderView(View):
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_order_by_customer(customer)
        return render(request,'order.html',{'orders' : orders})

