from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('cart',Cart.as_view(),name='cart'),
    path('logout',logout,name='logout'),
]
