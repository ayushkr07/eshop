from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
]
