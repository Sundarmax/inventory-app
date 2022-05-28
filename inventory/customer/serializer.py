from pyexpat import model

from attr import field, fields
from customer.models import Customer
from rest_framework import serializers



class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id','first_name','address','phone','email')
