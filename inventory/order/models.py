import imp
from django.db import models
from customer.models import Customer

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_of_order = models.DateField()