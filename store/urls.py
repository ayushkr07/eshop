from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='checkout'),
    path('order', OrderView.as_view(), name='order'),
    path('logout',logout,name='logout'),
]
