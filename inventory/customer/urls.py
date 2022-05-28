from django.urls import path

from customer.views import addCustomer

urlpatterns = [
    path('customer',addCustomer,name="add-customer"),
]
