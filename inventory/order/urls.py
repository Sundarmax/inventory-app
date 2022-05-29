
from django.urls import path
from order.models import Order,order_detail
from order.views import addNewOrder\

urlpatterns = [
    path('order/add',addNewOrder.as_view())
]
