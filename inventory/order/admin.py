from django.contrib import admin
from .models import Order,order_detail

admin.site.register(Order)
admin.site.register(order_detail)