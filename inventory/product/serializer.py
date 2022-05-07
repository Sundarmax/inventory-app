import imp
from itertools import product
from rest_framework import serializers
from product.models import * 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ('id','product_name','product_price')
