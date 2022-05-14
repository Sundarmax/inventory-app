import imp
from django.db import models
from customer.models import Customer
from product.models import Product
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_of_order = models.DateField()


class order_detail(models.Model):
    order_id    = models.ForeignKey(Order,on_delete=models.CASCADE)
    product     = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    date        = models.DateField()
    unit_price  = models.IntegerField()
    total       = models.FloatField()

    class Meta:
        ordering = ['-id']
