from pyexpat import model
from rest_framework.serializers import ModelSerializer
from order.models import *

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("customer","date_of_order")