from django.urls import path

from customer.views import addCustomer
from customer.signals import *

urlpatterns = [
    path('customer',addCustomer,name="add-customer"),
]